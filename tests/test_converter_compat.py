"""Regression tests for MLX/Transformers 5 -> llama.cpp/Transformers 4 export."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.training import (
    normalize_tokenizer_config, export_gguf, _valid_gguf,
    tool_cache_directory, llama_cpp_root,
)


class TokenizerConversionTests(unittest.TestCase):
    def test_windows_tools_avoid_deep_run_paths_and_preserve_legacy_checkouts(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            run_cache = base / ('nested-' * 30) / 'tools'
            with patch('local_knowledge_trainer.training.sys.platform', 'win32'), \
                 patch.dict('os.environ', {'LOCALAPPDATA': str(base)}):
                short = tool_cache_directory(run_cache)
                self.assertLess(len(str(short)), len(str(run_cache)))
                self.assertEqual(short, tool_cache_directory(run_cache))
                self.assertNotEqual(short, tool_cache_directory(base / 'another-run'))
                self.assertEqual(llama_cpp_root(run_cache), short / 'llama.cpp')
                legacy = base / 'old-tools' / 'llama.cpp'
                legacy.mkdir(parents=True)
                self.assertEqual(llama_cpp_root(legacy.parent), legacy)

    def _prepare_fused(self, root: Path, config: dict) -> Path:
        fused = root / "fused"
        fused.mkdir()
        (fused / "tokenizer_config.json").write_text(json.dumps(config), encoding="utf-8")
        return fused

    def test_transforms_v5_list_without_losing_special_tokens(self):
        with tempfile.TemporaryDirectory() as folder:
            fused = self._prepare_fused(Path(folder), {
                "tokenizer_class": "Qwen2TokenizerFast",
                "extra_special_tokens": ["<|im_start|>", "<|im_end|>", "<|fim_prefix|>"],
                "additional_special_tokens": ["<|im_start|>"],
                "chat_template": "{{ messages }}",
            })
            self.assertTrue(normalize_tokenizer_config(fused))
            updated = json.loads((fused / "tokenizer_config.json").read_text())
            original = json.loads((fused / "tokenizer_config.transformers5.backup.json").read_text())
            self.assertNotIn("extra_special_tokens", updated)
            self.assertEqual(updated["additional_special_tokens"],
                             ["<|im_start|>", "<|im_end|>", "<|fim_prefix|>"])
            self.assertEqual(updated["chat_template"], "{{ messages }}")
            self.assertEqual(original["extra_special_tokens"],
                             ["<|im_start|>", "<|im_end|>", "<|fim_prefix|>"])
            self.assertFalse(normalize_tokenizer_config(fused))

    def test_legacy_dict_stays_untouched_and_no_backup_is_written(self):
        with tempfile.TemporaryDirectory() as folder:
            fused = self._prepare_fused(Path(folder), {
                "extra_special_tokens": {"my_token": "<|token|>"},
            })
            before = (fused / "tokenizer_config.json").read_bytes()
            self.assertFalse(normalize_tokenizer_config(fused))
            self.assertEqual((fused / "tokenizer_config.json").read_bytes(), before)
            self.assertFalse((fused / "tokenizer_config.transformers5.backup.json").exists())

    def test_invalid_extra_token_does_not_change_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            fused = self._prepare_fused(Path(folder), {"extra_special_tokens": [123]})
            with self.assertRaises(ValueError):
                normalize_tokenizer_config(fused)
            self.assertEqual(json.loads((fused / "tokenizer_config.json").read_text()),
                             {"extra_special_tokens": [123]})

    def test_missing_tokenizer_metadata_fails_clearly(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                normalize_tokenizer_config(Path(folder))

    def test_resume_export_rebuilds_invalid_partial_and_reuses_valid_final(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            fused = self._prepare_fused(root, {
                "extra_special_tokens": ["<|im_start|>", "<|im_end|>"],
            })
            (root / "assistant-f16.gguf").write_bytes(b"GGUFpartial")
            converter = root / "fake-converter"
            converter.write_bytes(b"x")
            root_cpp = root / "llama.cpp"
            (root_cpp / "requirements").mkdir(parents=True)
            (root_cpp / "requirements" / "requirements-convert_hf_to_gguf.txt").write_text("mock")
            quantizer, cli, splitter = (root / name for name in ("quantize", "llama-cli", "splitter"))
            cmds = []

            def write_gguf(file):
                with Path(file).open("wb") as out:
                    out.write(b"GGUF")
                    out.truncate(10_000_100)

            def fake_run(command):
                args = [str(x) for x in command]
                cmds.append(args)
                if "convert_hf_to_gguf.py" in args[1]:
                    config = json.loads((fused / "tokenizer_config.json").read_text())
                    self.assertNotIn("extra_special_tokens", config)
                    self.assertEqual(config["additional_special_tokens"],
                                     ["<|im_start|>", "<|im_end|>"])
                    write_gguf(args[args.index("--outfile") + 1])
                elif args[0] == str(quantizer):
                    write_gguf(args[2])

            release = root / "release"
            with patch('local_knowledge_trainer.training.prepare_llama_cpp',
                       return_value=(root_cpp, quantizer, cli, splitter)), \
                 patch('local_knowledge_trainer.training._converter_python', return_value=converter), \
                 patch('local_knowledge_trainer.training.run', side_effect=fake_run):
                final = export_gguf(fused, root, release)
                self.assertTrue(_valid_gguf(final))
                self.assertFalse((root / "assistant-f16.gguf.partial").exists())
                self.assertFalse((root / "assistant-f16.gguf").exists())
                self.assertFalse((release / "assistant.gguf.partial").exists())
                self.assertTrue(any("convert_hf_to_gguf.py" in c[1] for c in cmds))
                self.assertTrue(any(c[:2] == [str(converter), '-c'] for c in cmds))
                count = len(cmds)
                export_gguf(fused, root, release)
                self.assertEqual(len(cmds), count + 1)  # final GGUF smoke test only

    def test_file_with_header_only_is_not_a_valid_intermediate(self):
        with tempfile.TemporaryDirectory() as folder:
            f = Path(folder) / "assistant.gguf"
            f.write_bytes(b"GGUF" + b"x" * 32)
            self.assertFalse(_valid_gguf(f))


if __name__ == '__main__':
    unittest.main()
