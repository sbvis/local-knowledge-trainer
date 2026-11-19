import tempfile
import unittest
from pathlib import Path
from local_knowledge_trainer.sources import classify, repository_coordinates, repository_tree, normalize_document_url, get_document


class SourceParsingTests(unittest.TestCase):
    def test_github_tree_directory_is_a_repository_source(self):
        url = 'https://github.com/acme/alpha/tree/main/docs/tutorials'
        self.assertEqual(classify(url), 'repo')
        self.assertEqual(repository_tree(url), ('https://github.com/acme/alpha', 'main', 'docs/tutorials'))
        with self.assertRaises(ValueError):
            repository_tree('https://github.com/acme/alpha/tree/main/%2E%2E/private')

    def test_github_homepages(self):
        self.assertEqual(repository_coordinates("https://github.com/acme/alpha.git"), ("acme", "alpha"))
        self.assertIsNone(repository_coordinates("https://other.example/acme/alpha"))
        self.assertIsNone(repository_coordinates("https://github.com/acme/alpha/tree/main"))

    def test_classifies_files_and_urls(self):
        self.assertEqual(classify("https://github.com/acme/alpha"), "repo")
        self.assertEqual(classify("https://example.org/manual.pdf"), "url")
        self.assertEqual(classify("~/docs/guide.md"), "local")
        self.assertEqual(classify(r"C:\Users\public\guide.md"), "local")
        with self.assertRaises(ValueError):
            classify("http://example.org/test.pdf")

    def test_github_blob_raw(self):
        self.assertEqual(normalize_document_url("https://github.com/a/b/blob/main/docs/Guide.md"),
                         "https://raw.githubusercontent.com/a/b/main/docs/Guide.md")
