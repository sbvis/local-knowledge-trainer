import tempfile
import unittest
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace
from local_knowledge_trainer.cli import build


class CliTests(unittest.TestCase):
    def test_installed_cli_prepares_unrelated_unicode_documents(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            materials = root / 'materials'
            materials.mkdir()
            for name, task in [('résumé.md', 'Import documents'), ('export.md', 'Export results')]:
                (materials / name).write_text(
                    f'# {task}\n\nUse the documented workflow for local documents.\n'
                    '1. Open the workspace menu.\n2. Select the relevant operation.\n', encoding='utf-8')
            env = os.environ.copy()
            env['PYTHONPATH'] = str(Path(__file__).resolve().parents[1] / 'src')
            result = subprocess.run(
                [sys.executable, '-m', 'local_knowledge_trainer', '--source', str(materials),
                 '--output', str(root / 'runs'), '--run-name', 'check', '--model', '1',
                 '--mode', 'quick', '--yes', '--strict-sources', '--dry-run'],
                env=env, capture_output=True, text=True, encoding='utf-8', timeout=60)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((root / 'runs/check/release/knowledge.db').is_file())
            self.assertFalse((root / 'runs/check/release/assistant.gguf').exists())

    def test_dry_run_without_model_download(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "repo"
            source.mkdir()
            (source / "README.md").write_text("# Alpha\n\nThis is a tutorial about Alpha settings.\n" * 22)
            (source / "core.cpp").write_text("class CoreAlpha {};\nvoid CoreAlpha::initialize() {}\n" * 10)
            args = SimpleNamespace(dry_run=True, model=1, sources=[str(source)], qa=None,
                                   mode="quick", yes=True, run_name="test-run", output=str(root / "output"))
            build(args)
            self.assertTrue((root / "output" / "test-run" / "release" / "knowledge.db").is_file())
            self.assertFalse((root / "output" / "test-run" / "release" / "assistant.gguf").exists())
