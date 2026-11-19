"""Loading many source URLs from one file should be predictable and safe."""
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from local_knowledge_trainer.cli import build, load_sources_file


class SourceFileTests(unittest.TestCase):
    def test_sources_file_comments_duplicates_and_local_relative_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "notes").mkdir()
            sources = root / "list.txt"
            sources.write_text("\ufeff# Repositories\n\nhttps://github.com/psf/requests\n"
                               "https://github.com/psf/requests\n./notes\n", encoding="utf-8")
            self.assertEqual(load_sources_file(sources),
                             ["https://github.com/psf/requests", str((root / 'notes').resolve())])

    def test_invalid_source_list_line_has_location(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_file = Path(tmp) / 'sources.txt'
            source_file.write_text('https://github.com/psf/requests\nhttp://insecure.test/file.pdf\n')
            with self.assertRaisesRegex(ValueError, r'sources.txt:2'):
                load_sources_file(source_file)
            source_file.write_text('# only a comment\n')
            with self.assertRaisesRegex(ValueError, 'No sources'):
                load_sources_file(source_file)

    def test_dry_run_with_source_list_without_wizard_or_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'sample'
            folder.mkdir()
            (folder / 'guide.md').write_text('# Tutorial\n' + 'Configuration and data loading.\n' * 30)
            (folder / 'guide2.md').write_text('# API Guide\n' + 'Setup and loading parameters.\n' * 30)
            sources = root / 'sources.txt'
            sources.write_text('./sample\n')
            args = SimpleNamespace(dry_run=True, model=1, sources=[], sources_file=[sources],
                                   qa=None, mode='quick', yes=True, run_name='file-run',
                                   output=str(root / 'runs'))
            build(args)
            self.assertTrue((root / 'runs/file-run/release/knowledge.db').is_file())
