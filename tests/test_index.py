import tempfile
import unittest
from pathlib import Path
from local_knowledge_trainer.index import create_index, search, source_hit_rate
from local_knowledge_trainer.prepare import Chunk


class IndexTests(unittest.TestCase):
    def test_named_repo_overrides_incidental_mentions(self):
        with tempfile.TemporaryDirectory() as temp:
            db = Path(temp) / 'knowledge.db'
            chunks = [
                Chunk('https://github.com/example/Scatterplot', 'README.md', 'document',
                      '# Plot module\nA charting library for interactive data exploration.', 1, 2),
                Chunk('https://github.com/example/OtherRepo', 'README.md', 'document',
                      'Scatterplot Scatterplot Scatterplot is described in this unrelated repository.', 1, 2),
                Chunk('https://github.com/example/OtherRepo', 'src/plot.cpp', 'code',
                      'Scatterplot references and more Scatterplot calls in OtherRepo.', 3, 5),
            ]
            create_index(chunks, db)
            hits = search(db, 'What is the purpose of the Scatterplot repository?', limit=4)
            self.assertTrue(hits)
            self.assertTrue(all(hit['source'].endswith('/Scatterplot') for hit in hits))
            self.assertEqual(hits[0]['location'], 'README.md:L1-L2')

    def test_search_and_grounded_recall(self):
        with tempfile.TemporaryDirectory() as temp:
            db = Path(temp) / "knowledge.db"
            chunks = [
                Chunk("repo-a", "src/parser.cpp", "code", "class DataLoader constructs a dataset.\nSupports PointType input.", 1, 2, "abc123"),
                Chunk("repo-b", "docs/tutorial.md", "document", "# Visualizing points\nSelect plot and assign an axis.", 3, 4, "def456"),
            ]
            self.assertEqual(create_index(chunks, db), 2)
            hits = search(db, "DataLoader PointType")
            self.assertTrue(hits)
            self.assertEqual(hits[0]["location"], "src/parser.cpp:L1-L2")
            self.assertEqual(hits[0]["git_commit"], "abc123")
            self.assertEqual(search(db, "?"), [])
            rows = [{"messages": [{"role": "user", "content": "DataLoader PointType"}],
                     "_location": "src/parser.cpp:L1-L2"}]
            result = source_hit_rate(db, rows, top_k=1)
            self.assertEqual(result["source_hit_at_k"], 1.0)
