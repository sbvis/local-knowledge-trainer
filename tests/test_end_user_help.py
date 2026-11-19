"""Regressions against inventing developer instructions for end-user tasks."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.analysis import analyze_chunks
from local_knowledge_trainer.demo import run_question
from local_knowledge_trainer.index import create_index, is_ui_instruction_question
from local_knowledge_trainer.prepare import Chunk, generated_examples
from local_knowledge_trainer.ui_help import answer_ui_question

REPO = 'https://github.com/example/Scatterplot'


def samples(include_guide=False):
    code = '''Plot::Plot() : _plotGroup(this, "Point"), _sizeAction(this, "Point size") {
    _plotGroup.addSubAction(&_sizeAction);
    connect(&_sizeAction, &gui::DecimalAction::valueChanged, this, [this](float value) {
        renderer.setPointSize(value);
    });
}'''
    chunks = [Chunk(REPO, 'src/PointPlotAction.cpp', 'code', code, 1, 5),
              Chunk(REPO, 'README.md', 'document', '# Scatterplot\nShows point data visually.', 1, 2)]
    if include_guide:
        chunks.append(Chunk(REPO, 'docs/user-guide.md', 'document',
                            '# Point size\nOpen the Point settings panel and adjust the Point size control.', 1, 2))
    return chunks


class EndUserTests(unittest.TestCase):
    def test_existing_control_named_and_grouped_without_code_advice(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'knowledge.db'
            chunks = samples()
            create_index(chunks, db, facts=analyze_chunks(chunks))
            response = answer_ui_question(db, 'How to increase point size in Scatterplot?')
            self.assertEqual(response.level, 'control')
            self.assertIn('**Point size**', response.answer)
            self.assertIn('**Point**', response.answer)
            self.assertNotIn('modify the code', response.answer)
            self.assertNotIn('getContextMenu()', response.answer)
            self.assertIn('src/PointPlotAction.cpp', response.answer)

    def test_documented_navigation_preferred_over_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'knowledge.db'
            chunks = samples(include_guide=True)
            create_index(chunks, db, facts=analyze_chunks(chunks))
            response = answer_ui_question(db, 'How to change point size in Scatterplot?')
            self.assertEqual(response.level, 'documented')
            self.assertIn('Open the Point settings panel', response.answer)
            self.assertNotIn('renderer.setPointSize', response.answer)

    def test_absent_evidence_abstains(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'knowledge.db'
            chunks = samples()
            create_index(chunks, db, facts=analyze_chunks(chunks))
            response = answer_ui_question(db, 'How to change unknown XYZZY?')
            self.assertEqual(response.level, 'insufficient')
            self.assertIn('cannot verify', response.answer)

    def test_ui_query_does_not_launch_llm_even_when_model_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            release = Path(tmp) / 'release'
            release.mkdir()
            (release / 'assistant.gguf').write_bytes(b'GGUF fake')
            chunks = samples()
            create_index(chunks, release / 'knowledge.db', facts=analyze_chunks(chunks))
            with patch('local_knowledge_trainer.demo.locate_llama_cli', side_effect=AssertionError('not needed')):
                n = run_question(release, 'How to change point size in Scatterplot?')
            self.assertGreater(n, 0)

    def test_user_questions_default_to_user_help(self):
        self.assertTrue(is_ui_instruction_question('How to change point size'))
        self.assertTrue(is_ui_instruction_question('How do I select a dataset?'))
        self.assertFalse(is_ui_instruction_question('How do I implement point size in C++?'))
        self.assertFalse(is_ui_instruction_question('What is PCA?'))


    def test_unrelated_tutorial_does_not_override_real_ui_control(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'knowledge.db'
            chunks = samples() + [Chunk('https://github.com/example/website',
                '_tutorials/unrelated.md', 'document',
                '# Tutorial\nIncrease size. The point color legend is available.\n', 1, 3)]
            create_index(chunks, db, facts=analyze_chunks(chunks))
            response = answer_ui_question(db, 'How to change point size?')
            self.assertEqual(response.level, 'control')
            self.assertIn('**Point size**', response.answer)
            self.assertNotIn('website', response.answer)

    def test_ui_help_can_run_using_index_without_gguf(self):
        with tempfile.TemporaryDirectory() as tmp:
            release = Path(tmp) / 'release'
            release.mkdir()
            chunks = samples()
            create_index(chunks, release / 'knowledge.db', facts=analyze_chunks(chunks))
            with patch('local_knowledge_trainer.demo.locate_model', side_effect=AssertionError('not needed')):
                n = run_question(release, 'How to change point size?')
            self.assertGreater(n, 0)

    def test_version_output_identifies_source_checkout(self):
        import subprocess
        import sys
        project = Path(__file__).resolve().parents[1]
        proc = subprocess.run([sys.executable, str(project / 'bootstrap.py'), '--version'],
                              capture_output=True, text=True, check=True)
        self.assertIn('v0.4.5', proc.stdout)
        self.assertIn(str(project), proc.stdout)

    def test_training_examples_default_to_user_not_developer(self):
        chunks = samples()
        facts = analyze_chunks(chunks)
        examples = generated_examples(chunks, facts=facts)
        answers = '\n'.join(r['messages'][1]['content'] for r in examples)
        self.assertIn('locate the Point → Point size control', answers)
        self.assertIn('Adjust the numeric value', answers)
        self.assertNotIn('Source code registers the control through', answers)
        self.assertFalse(any(r.get('_evidence_type') == 'cross_repository' for r in examples))
        developer = generated_examples(chunks, facts=facts, audience='developer')
        self.assertTrue(any('Source code registers the control through' in r['messages'][1]['content']
                            for r in developer))


if __name__ == '__main__':
    unittest.main()
