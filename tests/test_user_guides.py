"""Regression tests: user UI guidance must be based on instructions, not code."""
import json
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.demo import (compose_prompt, infer_command, run_question,
                                         supported_llama_flags)
from local_knowledge_trainer.guides import add_guide
from local_knowledge_trainer.index import (create_index, is_ui_instruction_question,
                                           search_ui_guides)
from local_knowledge_trainer.prepare import Chunk


class UserGuideTests(unittest.TestCase):
    def test_ui_vs_developer_intents(self):
        self.assertTrue(is_ui_instruction_question('How to increase the point size in the scatterplot plugin?'))
        self.assertTrue(is_ui_instruction_question('Where can I change opacity in the UI?'))
        self.assertFalse(is_ui_instruction_question('How do I implement a point size slider in C++?'))
        self.assertFalse(is_ui_instruction_question('What is the purpose of Scatterplot?'))

    def test_code_does_not_count_as_ui_instructions(self):
        with tempfile.TemporaryDirectory() as temp:
            db = Path(temp) / 'knowledge.db'
            create_index([
                Chunk('https://github.com/example/Scatterplot', 'src/PointAction.cpp', 'code',
                      'setPointSize() makes the marker larger when clicked', 1, 15),
                Chunk('https://github.com/example/Scatterplot', 'README.md', 'document',
                      'Scatterplot displays a high-performance point cloud.', 1, 15),
            ], db)
            self.assertEqual(search_ui_guides(db, 'How to increase point size in Scatterplot?'), [])

    def test_guide_addition_and_replacement_preserve_release(self):
        with tempfile.TemporaryDirectory() as temp:
            release = Path(temp) / 'release'
            release.mkdir()
            (release / 'assistant.gguf').write_bytes(b'GGUF' + b'0' * 16)
            (release / 'manifest.json').write_text(json.dumps({
                'knowledge_index': {'chunk_count': 1}, 'fine_tuning': {'iterations': 100}}))
            (release / 'SHA256SUMS.txt').write_text('oldhash  knowledge.db\noldhash  manifest.json\n')
            source = 'https://github.com/example/Scatterplot'
            create_index([Chunk(source, 'src/main.cpp', 'code',
                                'void pointSize();', 1, 10)], release / 'knowledge.db')
            guide = Path(temp) / 'scatterplot-guide.md'
            guide.write_text('# Scatterplot UI guide\n\n'
                             'To increase point size, open Point settings and adjust the Point size slider.\n'
                             'This is a synthetic test guide, not a real application manual.\n')
            self.assertEqual(add_guide(release, guide, source), 1)
            hits = search_ui_guides(release / 'knowledge.db',
                                    'How to increase point size in Scatterplot?')
            self.assertTrue(hits)
            self.assertIn('slider', hits[0]['content'])
            self.assertEqual(hits[0]['kind'], 'document')
            self.assertEqual(add_guide(release, guide, source), 1)
            import sqlite3
            with closing(sqlite3.connect(release / 'knowledge.db')) as db:
                self.assertEqual(db.execute('SELECT COUNT(*) FROM chunks').fetchone()[0], 2)
            manifest = json.loads((release / 'manifest.json').read_text())
            self.assertEqual(manifest['fine_tuning']['iterations'], 100)
            self.assertEqual(manifest['knowledge_index']['chunk_count'], 2)
            from local_knowledge_trainer.common import sha256_file
            sums = (release / 'SHA256SUMS.txt').read_text()
            self.assertIn(f"{sha256_file(release / 'knowledge.db')}  knowledge.db", sums)
            self.assertIn(f"{sha256_file(release / 'manifest.json')}  manifest.json", sums)

    def test_missing_guides_abstain_before_llm_launch(self):
        with tempfile.TemporaryDirectory() as temp:
            release = Path(temp) / 'release'
            release.mkdir()
            (release / 'assistant.gguf').write_bytes(b'GGUFmock')
            create_index([Chunk('https://github.com/example/Scatterplot', 'src/Plot.cpp',
                                'code', 'setPointSize called from the widget', 1, 10)],
                         release / 'knowledge.db')
            with patch('local_knowledge_trainer.demo.locate_llama_cli') as locate:
                self.assertEqual(run_question(release, 'How to increase point size in Scatterplot?'), 0)
                locate.assert_not_called()

    def test_plain_llama_cli_prompt_does_not_contain_chatml(self):
        with patch('local_knowledge_trainer.demo.supported_llama_flags',
                   return_value=frozenset({'--single-turn', '--offline'})):
            command = infer_command('/bin/llama-cli', Path('assistant.gguf'), 'Question?', [], 120)
            self.assertIn('--single-turn', command)
            self.assertNotIn('<|im_start|>', command[command.index('--prompt') + 1])
            self.assertIn('Question?', command[command.index('--prompt') + 1])

    def test_raw_completion_passes_chatml_and_disables_conversation(self):
        with patch('local_knowledge_trainer.demo.supported_llama_flags',
                   return_value=frozenset({'--single-turn', '--offline', '--no-conversation'})):
            command = infer_command('/bin/llama-completion', Path('assistant.gguf'), 'Question?', [], 120)
            self.assertIn('--no-conversation', command)
            self.assertIn('<|im_start|>', command[command.index('--prompt') + 1])


if __name__ == '__main__':
    unittest.main()
