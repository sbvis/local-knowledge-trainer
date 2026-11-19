import json
import tempfile
import unittest
from pathlib import Path
from local_knowledge_trainer.prepare import Chunk, collect_chunks, generated_examples, load_curated, write_training_data, extract_text
from local_knowledge_trainer.sources import Source


class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_local_cpp_and_markdown(self):
        (self.root / "README.md").write_text("# Loading data\n\nUse documented steps to load supported files.\n" * 12)
        (self.root / "solver.cpp").write_text("class MatrixSolver {};\nvoid MatrixSolver::solve(int n) {}\n" * 15)
        chunks = collect_chunks([Source("local", "fixture", self.root)])
        self.assertGreaterEqual(len(chunks), 2)
        self.assertTrue(any(c.kind == "code" for c in chunks))
        examples = generated_examples(chunks, audience="developer")
        self.assertTrue(any("MatrixSolver" in str(e) for e in examples))
        user_examples = generated_examples(chunks)
        self.assertFalse(any("add `void" in str(e) for e in user_examples))
        stats, validation = write_training_data(examples, self.root / "data")
        self.assertGreater(stats["train_examples"], 0)
        self.assertGreater(stats["validation_examples"], 0)
        self.assertGreater(len(validation), 0)
        self.assertTrue((self.root / "data" / "train.jsonl").is_file())

    def test_no_data_leak_between_groups(self):
        rows = []
        for group in "abcdefghijkl":
            for number in range(2):
                rows.append({"messages": [{"role": "user", "content": f"Question {number}"},
                                          {"role": "assistant", "content": f"Answer {number}"}],
                             "_source": group, "_location": group})
        stats, valid = write_training_data(rows, self.root / "data")
        self.assertEqual(stats["train_examples"] + stats["validation_examples"], 24)
        self.assertEqual(len({v["_source"] for v in valid}), 1)

    def test_manual_qa_validation(self):
        data = self.root / "qa.jsonl"
        data.write_text(json.dumps({"messages": [
            {"role": "user", "content": "Where?"}, {"role": "assistant", "content": "Here."}]}) + "\n")
        self.assertEqual(len(load_curated(data)), 1)
        data.write_text('{"messages": [{"role":"user", "content":"Question"}]}\n')
        with self.assertRaises(ValueError):
            load_curated(data)

    def test_docx_stdlib_extraction(self):
        import zipfile
        docx = self.root / "test.docx"
        with zipfile.ZipFile(docx, "w") as archive:
            archive.writestr("word/document.xml", '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Testing DOCX</w:t></w:r></w:p></w:body></w:document>')
        self.assertIn("Testing DOCX", extract_text(docx))
