"""Regression tests: timeouts, retries, source cache and failure reporting."""
import json
import subprocess
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.api import prepare_knowledge
from local_knowledge_trainer.sources import acquire, get_document


class FakeResponse:
    url = "https://example.org/manual.pdf"

    def __init__(self, body):
        self.body = body
        self.headers = {"Content-Length": str(len(body))}

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None

    def read(self, _count):
        return self.body


class RecoveryTests(unittest.TestCase):
    def test_cli_dry_run_with_missing_document_completes(self):
        from types import SimpleNamespace
        from local_knowledge_trainer.cli import build
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local = root / 'source'
            local.mkdir()
            (local / 'guide.md').write_text('# Guide\n' + 'Repeatable instructions for users.\n' * 45)
            (local / 'api.md').write_text('# API\n' + 'Reference for application functions.\n' * 45)
            urls = root / 'sources.txt'
            urls.write_text('./source\nhttps://example.org/slow.pdf\n')
            opts = SimpleNamespace(dry_run=True, model=1, sources=[], sources_file=[urls],
                                   qa=None, mode='quick', yes=True, run_name='mixed-run',
                                   output=str(root / 'runs'), download_timeout=5,
                                   download_retries=0, strict_sources=False,
                                   no_source_cache=False)
            with patch('local_knowledge_trainer.sources.get_document',
                       side_effect=RuntimeError('timed out')):
                build(opts)
            release = root / 'runs/mixed-run/release'
            self.assertTrue((release / 'knowledge.db').is_file())
            self.assertEqual(len(json.loads((release / 'source_failures.json').read_text())['failed']), 1)
            self.assertTrue((root / 'runs/.source-cache').is_dir())

    def test_report_saved_even_when_all_sources_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / 'bad-run'
            with patch('local_knowledge_trainer.sources.get_document',
                       side_effect=RuntimeError('unavailable')):
                with self.assertRaisesRegex(RuntimeError, 'No usable sources'):
                    prepare_knowledge(['https://example.org/bad.pdf'], workspace)
            report = json.loads((workspace / 'source_failures.json').read_text())
            self.assertEqual(len(report['failed']), 1)

    def test_pdf_retries_then_saves_atomically(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'manual.pdf'
            with patch('local_knowledge_trainer.sources.urllib.request.urlopen', side_effect=[
                urllib.error.URLError('timed out'), FakeResponse(b'%PDF-1.7\nexample')
            ]) as opener, patch('local_knowledge_trainer.sources.time.sleep'):
                self.assertEqual(get_document('https://example.org/manual.pdf', target,
                                              timeout=5, retries=1), target)
                self.assertEqual(opener.call_count, 2)
                self.assertEqual(target.read_bytes(), b'%PDF-1.7\nexample')
                self.assertFalse(target.with_name('manual.pdf.part').exists())

    def test_failure_leaves_no_partial_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'manual.pdf'
            with patch('local_knowledge_trainer.sources.urllib.request.urlopen',
                       side_effect=urllib.error.URLError('timed out')), \
                 patch('local_knowledge_trainer.sources.time.sleep'):
                with self.assertRaisesRegex(RuntimeError, 'timed out'):
                    get_document('https://example.org/manual.pdf', target,
                                 timeout=5, retries=1)
            self.assertFalse(target.exists())
            self.assertFalse(target.with_name('manual.pdf.part').exists())

    def test_404_is_not_retried(self):
        with tempfile.TemporaryDirectory() as tmp:
            err = urllib.error.HTTPError('https://example.org/missing.pdf', 404, 'not found', {}, None)
            with patch('local_knowledge_trainer.sources.urllib.request.urlopen', side_effect=err) as opener:
                with self.assertRaisesRegex(RuntimeError, 'HTTP 404'):
                    get_document('https://example.org/missing.pdf', Path(tmp) / 'missing.pdf', retries=3)
                self.assertEqual(opener.call_count, 1)

    def test_truncated_document_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'manual.pdf'
            response = FakeResponse(b'%PDF-1.7\npartial')
            response.headers['Content-Length'] = str(len(response.body) + 100)
            with patch('local_knowledge_trainer.sources.urllib.request.urlopen', return_value=response):
                with self.assertRaisesRegex(ValueError, 'truncated'):
                    get_document('https://example.org/manual.pdf', target)
            self.assertFalse(target.exists())

    def test_corrupted_cached_pdf_is_reacquired(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            url = 'https://example.org/manual.pdf'
            def fake_download(_url, target, **_kwargs):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b'%PDF-1.7\ncorrected')
                return target
            with patch('local_knowledge_trainer.sources.get_document', side_effect=fake_download) as download:
                original = acquire([url], root)[0]
                original.path.write_bytes(b'<html>bad cache</html>')
                reacquired = acquire([url], root)[0]
                self.assertEqual(download.call_count, 2)
                self.assertEqual(reacquired.path.read_bytes(), b'%PDF-1.7\ncorrected')

    def test_html_masquerading_as_pdf_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'manual.pdf'
            with patch('local_knowledge_trainer.sources.urllib.request.urlopen',
                       return_value=FakeResponse(b'<html>Login required</html>')):
                with self.assertRaisesRegex(ValueError, 'Expected PDF'):
                    get_document('https://example.org/manual.pdf', target)
            self.assertFalse(target.exists())

    def test_failed_url_skipped_and_cached_local_source_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            local = root / 'source'
            local.mkdir()
            (local / 'README.md').write_text('# Local guide\n' + 'Local document text for indexing.\n' * 40)
            (local / 'usage.md').write_text('# Usage guide\n' + 'Additional instructions about local usage.\n' * 40)
            url = 'https://example.org/slow.pdf'
            with patch('local_knowledge_trainer.sources.get_document',
                       side_effect=RuntimeError('timed out')) as download:
                result = prepare_knowledge([url, str(local)], root / 'first',
                                           source_cache=root / 'cached')
            self.assertEqual(download.call_count, 1)
            self.assertEqual(len(result.failed_sources), 1)
            self.assertEqual(len(result.sources), 1)
            self.assertTrue(result.database.is_file())
            report = json.loads((root / 'first/release/source_failures.json').read_text())
            self.assertEqual(report['successful'], 1)
            self.assertEqual(report['failed'][0]['origin'], url)
            self.assertIn('timed out', report['failed'][0]['reason'])

    def test_successful_download_reused_between_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cache = root / 'cached'
            url = 'https://example.org/doc.txt'
            def fake_download(_url, target, **kwargs):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text('Documentation to reuse')
                return target
            with patch('local_knowledge_trainer.sources.get_document', side_effect=fake_download) as download:
                first = acquire([url], cache)
                second = acquire([url], cache)
            self.assertEqual(download.call_count, 1)
            self.assertEqual(first[0].path, second[0].path)

    def test_strict_mode_raises_and_records_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            failures = []
            with patch('local_knowledge_trainer.sources.get_document',
                       side_effect=RuntimeError('timed out')):
                with self.assertRaisesRegex(RuntimeError, 'timed out'):
                    acquire(['https://example.org/doc.pdf'], tmp, failures=failures, strict=True)
            self.assertEqual(len(failures), 1)

    def test_all_failed_sources_stop_with_helpful_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            failures = []
            with patch('local_knowledge_trainer.sources.get_document',
                       side_effect=RuntimeError('timed out')):
                with self.assertRaisesRegex(RuntimeError, 'No usable sources'):
                    acquire(['https://example.org/doc.pdf'], tmp, failures=failures)
            self.assertEqual(len(failures), 1)

    def test_failed_git_clone_cleaned_and_not_cached(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = 'https://github.com/example/repo'
            calls = []
            def fake_run(args):
                target = Path(args[-1])
                target.mkdir(parents=True)
                calls.append(target)
                if len(calls) == 1:
                    raise subprocess.CalledProcessError(1, args)
                (target / '.git').mkdir()
            with patch('local_knowledge_trainer.sources.run', side_effect=fake_run), \
                 patch('local_knowledge_trainer.sources.subprocess.check_output', return_value='a' * 40 + '\n'), \
                 patch('local_knowledge_trainer.sources.time.sleep'):
                first = acquire([repo], root, retries=1)
                second = acquire([repo], root, retries=1)
            self.assertEqual(len(calls), 2)
            self.assertEqual(first[0].commit, second[0].commit)
            self.assertEqual(first[0].path, second[0].path)


if __name__ == '__main__':
    unittest.main()
