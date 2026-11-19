import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.sharding import parse_shard_size, discover_shards, shard_model


class ShardingTests(unittest.TestCase):
    def test_parse_size(self):
        self.assertEqual(parse_shard_size('250m'), '250M')
        for size in ('0M', '9M', '100', '-1G', '6K'):
            with self.assertRaises(ValueError):
                parse_shard_size(size)

    def test_complete_shards(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            for i in range(1, 3):
                (folder / f'assistant-{i:05d}-of-00002.gguf').write_bytes(b'GGUF' + b'0' * 10)
            self.assertEqual(len(discover_shards(folder)), 2)
            (folder / 'assistant-00002-of-00002.gguf').unlink()
            with self.assertRaises(ValueError):
                discover_shards(folder)

    def test_sharding_invokes_tensor_aware_splitter(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            model = root / 'model.gguf'
            model.write_bytes(b'GGUF' + b'x' * 10)
            splitter = root / 'splitter'
            splitter.write_text('fake binary')
            def fake_run(cmd, check):
                self.assertIn('--split-max-size', cmd)
                self.assertIn('250M', cmd)
                (root / 'shards' / 'assistant-00001-of-00001.gguf').write_bytes(b'GGUF' + b'x')
            with patch('local_knowledge_trainer.sharding.subprocess.run', side_effect=fake_run):
                shards = shard_model(model, splitter, root / 'shards', '250M')
            self.assertEqual(len(shards), 1)
