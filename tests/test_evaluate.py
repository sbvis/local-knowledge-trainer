import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace
from local_knowledge_trainer.evaluate import load_cases, evaluate
from local_knowledge_trainer.index import create_index
from local_knowledge_trainer.prepare import Chunk


class EvaluationTests(unittest.TestCase):
    def test_read_and_validate_cases(self):
        with tempfile.TemporaryDirectory() as tmp:
            cases = Path(tmp) / 'cases.jsonl'
            cases.write_text('{"question":"Where is the parser?","reference":"src/parser.cpp"}\n')
            self.assertEqual(load_cases(cases)[0]['question'], 'Where is the parser?')
            cases.write_text('{"reference":"no question"}\n')
            with self.assertRaises(ValueError):
                load_cases(cases)

    def test_evaluate_writes_reviewable_answers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            release = root / 'release'
            release.mkdir()
            (release / 'assistant.gguf').write_bytes(b'GGUF' + b'0')
            create_index([Chunk('repo', 'src/parser.cpp', 'code', 'Parser::load() reads config files', 1, 3)],
                         release / 'knowledge.db')
            cases = root / 'cases.jsonl'
            cases.write_text('{"question":"What does Parser::load do?", "reference":"Loads config files"}\n')
            binary = root / 'llama-cli'
            binary.write_text('placeholder')
            output = root / 'review.json'
            with patch('local_knowledge_trainer.demo.supported_llama_flags', return_value=frozenset({'--single-turn', '--offline'})), \
                 patch('local_knowledge_trainer.evaluate.subprocess.run',
                       return_value=SimpleNamespace(stdout='It loads config files.')) as run:
                results = evaluate(release, cases, output, cli_path=str(binary))
            self.assertEqual(len(results), 1)
            self.assertIn('loads config', results[0]['response'])
            self.assertTrue(results[0]['sources'])
            self.assertIsNone(results[0]['human_review'])
            self.assertIn('manual', json.loads(output.read_text())['notice'])
            self.assertIn('--offline', run.call_args.args[0])
