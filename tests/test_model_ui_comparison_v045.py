"""The actual model benchmark must receive tutorial evidence, not stray code."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from local_knowledge_trainer.prepare import Chunk, _chunks_for_text
from local_knowledge_trainer.index import create_index
from local_knowledge_trainer.demo import run_question
from local_knowledge_trainer.evaluate import evaluate


class ModelUIComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.release = self.root / 'release'
        self.release.mkdir()
        guide = Path(__file__).resolve().parents[1] / 'examples/verified/cytosplore-evoviewer-ui.md'
        text = guide.read_text()
        chunks = [Chunk('https://viewer.cytosplore.org/documentation/evoviewer',
                        'cytosplore-evoviewer-ui.md', 'document', segment, start, end)
                  for start, end, segment in _chunks_for_text(text)]
        create_index(chunks, self.release / 'knowledge.db')

    def tearDown(self):
        self.temp.cleanup()

    def test_model_ui_prompt_uses_documented_evidence(self):
        invoked = []
        def capture(command, **kwargs):
            invoked.append(command)
            return SimpleNamespace(stdout='Use Species Appearance and Top N.', returncode=0)
        with patch('local_knowledge_trainer.demo.locate_model', return_value=self.root / 'assistant.gguf'), patch(
             'local_knowledge_trainer.demo.locate_llama_cli', return_value='/tmp/llama-completion'), patch(
             'local_knowledge_trainer.demo.supported_llama_flags', return_value=frozenset({'--single-turn', '--offline'})), patch(
             'local_knowledge_trainer.demo.subprocess.run', side_effect=capture):
            result = run_question(self.release, 'How can I find marker genes in EvoViewer?',
                                  force_model_ui=True)
        self.assertGreaterEqual(result, 1)
        self.assertEqual(len(invoked), 1)
        prompt = invoked[0][invoked[0].index('--prompt') + 1]
        self.assertIn('Species Appearance', prompt)
        self.assertIn('Top N', prompt)
        self.assertNotIn('PointPlotAction', prompt)

    def test_unverified_ui_question_never_reaches_model(self):
        with patch('local_knowledge_trainer.demo.locate_model', side_effect=AssertionError('do not invoke')):
            self.assertEqual(run_question(self.release,
                  'How do I activate the invisible XYZZY setting in EvoViewer?', force_model_ui=True), 0)

    def test_full_model_evaluation_includes_retrieved_workflow(self):
        cases = self.root / 'cases.jsonl'
        cases.write_text(json.dumps({'question': 'How do I find cell abundance in EvoViewer?',
                                     'reference': 'Absolute and Relative; sort species.'}) + '\n')
        captured = []
        def capture(command, **kwargs):
            captured.append(command[command.index('--prompt') + 1])
            return SimpleNamespace(stdout='Absolute and Relative abundance.', returncode=0)
        output = self.root / 'results.json'
        with patch('local_knowledge_trainer.evaluate.locate_model', return_value=self.root / 'assistant.gguf'), patch(
             'local_knowledge_trainer.evaluate.locate_llama_cli', return_value='/tmp/llama-completion'), patch(
             'local_knowledge_trainer.demo.supported_llama_flags', return_value=frozenset({'--single-turn', '--offline'})), patch(
             'local_knowledge_trainer.evaluate.subprocess.run', side_effect=capture):
            rows = evaluate(self.release, cases, output)
        self.assertEqual(len(rows), 1)
        self.assertIn('Absolute', captured[0])
        self.assertIn('Relative', captured[0])
        self.assertIn('Absolute and Relative abundance.', json.loads(output.read_text())['cases'][0]['response'])


if __name__ == '__main__':
    unittest.main()
