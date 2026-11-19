"""Interrupted export recovery and toolchain configuration regression tests."""
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from local_knowledge_trainer.cli import _recover_prior_state, resume
from local_knowledge_trainer.index import create_index
from local_knowledge_trainer.prepare import Chunk
from local_knowledge_trainer.training import prepare_llama_cpp


class ResumeTests(unittest.TestCase):
    def test_recovers_v030_training_metadata_without_retraining(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "release").mkdir()
            (workspace / "adapters").mkdir()
            (workspace / "fused").mkdir()
            (workspace / "adapters" / "0000100_adapters.safetensors").write_bytes(b"adapter")
            (workspace / "fused" / "model.safetensors").write_bytes(b"fused")
            source = "https://github.com/example/project"
            create_index([Chunk(source, "src/core.cpp", "code", "class Sample { public: void run(); };", 1, 1, "a" * 40)],
                         workspace / "release" / "knowledge.db")
            (workspace / "evaluation.json").write_text(json.dumps({
                "training": {"train_examples": 10, "validation_examples": 2},
                "retrieval": {"top_k": 5, "tested": 2, "source_hit_at_k": 0.5},
            }))
            state = _recover_prior_state(workspace, 1, "mlx")
            self.assertEqual(state["steps"], 100)
            self.assertEqual(state["preset_id"], 1)
            self.assertEqual(state["indexed"], 1)
            self.assertEqual(state["source_provenance"][0]["commit"], "a" * 40)
            with patch('local_knowledge_trainer.cli.finalize_release') as finalize:
                resume(SimpleNamespace(workspace=workspace, model=1, backend="mlx",
                                       shard_size=None, shards_only=False))
                self.assertEqual(finalize.call_count, 1)
                self.assertEqual(finalize.call_args.args[3], 100)
            with self.assertRaises(ValueError):
                _recover_prior_state(workspace, None, "mlx")


    def test_resume_prepared_run_trains_without_reingestion(self):
        from local_knowledge_trainer.models import PRESETS
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            (workspace / "release").mkdir()
            (workspace / "release" / "knowledge.db").write_bytes(b"sqlite")
            (workspace / "data").mkdir()
            (workspace / "data" / "train.jsonl").write_text('\n')
            state = {
                "preset_id": 1, "backend": "mlx", "steps": None,
                "model_revision": "abc", "source_provenance": [],
                "indexed": 10, "counts": {}, "retrieval": {}
            }
            (workspace / "build_state.json").write_text(json.dumps(state))
            options = SimpleNamespace(workspace=workspace, model=None, backend="auto",
                                      mode="standard", shard_size=None, shards_only=False)
            with patch('local_knowledge_trainer.training.download_model', return_value=workspace / "cached-model") as download, \
                 patch('local_knowledge_trainer.training.train', return_value=100) as train, \
                 patch('local_knowledge_trainer.training.fuse') as fuse, \
                 patch('local_knowledge_trainer.cli.finalize_release') as finalize:
                resume(options)
            download.assert_called_once_with(PRESETS[0], "mlx")
            train.assert_called_once()
            self.assertEqual(train.call_args.args[-1], "standard")
            fuse.assert_called_once()
            finalize.assert_called_once()
            self.assertEqual(json.loads((workspace / "build_state.json").read_text())["steps"], 100)
            with self.assertRaisesRegex(ValueError, "Specify --mode"):
                (workspace / "build_state.json").write_text(json.dumps(state))
                resume(SimpleNamespace(workspace=workspace, model=None, backend="auto",
                                       mode=None, shard_size=None, shards_only=False))

    def test_resume_reuses_completed_training_for_fusion(self):
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            (workspace / "release").mkdir()
            (workspace / "release" / "knowledge.db").write_bytes(b"sqlite")
            (workspace / "data").mkdir()
            (workspace / "data" / "train.jsonl").write_text('\n')
            state = {"preset_id": 1, "backend": "mlx", "steps": 100,
                     "model_revision": "abc", "source_provenance": [],
                     "indexed": 10, "counts": {}, "retrieval": {}}
            (workspace / "build_state.json").write_text(json.dumps(state))
            options = SimpleNamespace(workspace=workspace, model=None, backend="auto",
                                      mode="standard", shard_size=None, shards_only=False)
            with patch('local_knowledge_trainer.training.download_model', return_value=workspace / "cached-model"), \
                 patch('local_knowledge_trainer.training.train') as train, \
                 patch('local_knowledge_trainer.training.fuse') as fuse, \
                 patch('local_knowledge_trainer.cli.finalize_release') as finalize:
                resume(options)
            train.assert_not_called()
            fuse.assert_called_once()
            finalize.assert_called_once()

    def test_finalize_release_packages_existing_weights(self):
        from local_knowledge_trainer.cli import finalize_release
        from local_knowledge_trainer.models import PRESETS
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "fused").mkdir()
            (workspace / "release").mkdir()
            (workspace / "tools" / "llama.cpp").mkdir(parents=True)
            (workspace / "evaluation.json").write_text('{"retrieval": {}}')
            (workspace / "release" / "knowledge.db").write_bytes(b"knowledge")
            (workspace / "release" / "source_failures.json").write_text(json.dumps({
                "requested": 2, "successful": 1,
                "failed": [{"origin": "https://example.org/unavailable.pdf", "kind": "url",
                            "reason": "timed out"}],
            }))
            def fake_export(_fused, _tools, release):
                result = Path(release) / "assistant.gguf"
                result.write_bytes(b"GGUF" + b"M" * 20)
                return result
            with patch('local_knowledge_trainer.training.export_gguf', side_effect=fake_export), \
                 patch('local_knowledge_trainer.cli.subprocess.check_output', return_value='examplecommit\n'), \
                 patch('importlib.metadata.version', return_value='0.32.2'):
                finalize_release(workspace, PRESETS[0], "mlx", 100, "unrecorded",
                                 [{"origin": "https://github.com/example/project", "kind": "repo", "commit": "a" * 40}],
                                 17, {"train_examples": 10, "validation_examples": 2},
                                 {"source_hit_at_k": 0.5})
            manifest = json.loads((workspace / "release" / "manifest.json").read_text())
            self.assertEqual(manifest["fine_tuning"]["iterations"], 100)
            self.assertEqual(manifest["knowledge_index"]["chunk_count"], 17)
            self.assertTrue((workspace / "release" / "SHA256SUMS.txt").exists())
            self.assertEqual(len(manifest["source_acquisition"]["failed"]), 1)
            self.assertIn("source_failures.json", (workspace / "release" / "SHA256SUMS.txt").read_text())

    def test_llama_cli_target_is_enabled_with_server_components(self):
        with tempfile.TemporaryDirectory() as tmp:
            tool_root = Path(tmp) / "llama.cpp"
            tool_root.mkdir()
            (tool_root / "convert_hf_to_gguf.py").write_text("# mock converter")
            seen = []
            def fake_run(command):
                seen.append([str(part) for part in command])
                if "--build" in command:
                    binary_dir = tool_root / "build" / "bin"
                    binary_dir.mkdir(parents=True)
                    for name in ("llama-cli", "llama-completion", "llama-quantize", "llama-gguf-split"):
                        (binary_dir / (name + ('.exe' if os.name == 'nt' else ''))).write_bytes(b"program")
            with patch('local_knowledge_trainer.training.run', side_effect=fake_run):
                _, quantizer, cli, splitter = prepare_llama_cpp(tmp)
            self.assertTrue(quantizer.exists() and cli.exists() and splitter.exists())
            flags = [x for x in seen[0] if x.startswith("-D")]
            self.assertIn("-DLLAMA_BUILD_SERVER=ON", flags)
            self.assertIn("-DLLAMA_BUILD_UI=OFF", flags)
            self.assertIn("-DLLAMA_BUILD_TOOLS=ON", flags)
            self.assertIn("llama-cli", seen[1])


if __name__ == '__main__':
    unittest.main()
