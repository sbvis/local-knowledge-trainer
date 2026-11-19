"""Regression tests against the v0.4.4 failure: sparse tasks, 100 steps, bad text."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.models import PRESETS
from local_knowledge_trainer.prepare import Chunk, _chunks_for_text, generated_examples, write_training_data
from local_knowledge_trainer.sft_quality import assemble_user_examples, quality_metrics
from local_knowledge_trainer.training_plan import make_training_plan
from local_knowledge_trainer.training import train
from local_knowledge_trainer.multisource_training import extract_multisource_examples
from local_knowledge_trainer.workflow_training import extract_workflow_examples


SRC = 'https://github.com/example/user-guide'


def make_dataset(root, n, val=4):
    d = root / 'data'
    d.mkdir()
    for kind, count in (('train', n), ('valid', val)):
        with (d / f'{kind}.jsonl').open('w') as stream:
            for i in range(count):
                stream.write(json.dumps({'messages': [
                    {'role': 'user', 'content': f'How do I select a cell type {i}?'},
                    {'role': 'assistant', 'content': f'Click the cell-type rectangle {i}.'},
                ]}) + '\n')
    return d


class TrainingQualityTests(unittest.TestCase):
    def test_budget_adapts_to_full_corpus(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = make_dataset(Path(tmp), 400)
            normal = make_training_plan(d, PRESETS[0], 'standard')
            quick = make_training_plan(d, PRESETS[0], 'quick')
            other = make_training_plan(d, PRESETS[1], 'standard')
            torch = make_training_plan(d, PRESETS[0], 'standard', backend='torch')
            self.assertEqual(normal.iterations, 1200)
            self.assertEqual(normal.effective_passes, 3)
            self.assertEqual(quick.iterations, 400)
            self.assertEqual(other.learning_rate, 2e-5)
            self.assertEqual(normal.learning_rate, 3e-5)
            self.assertEqual(torch.iterations, 300)
            self.assertEqual(torch.effective_passes, 3)
            self.assertEqual(normal.max_sequence_length, 1024)

    def test_bad_dataset_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = make_dataset(Path(tmp), 4)
            (d / 'train.jsonl').write_text('this is not JSON\n')
            with self.assertRaises(ValueError):
                make_training_plan(d, PRESETS[0], 'standard')

    def test_mlxlm_command_uses_real_budget_and_copies_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = make_dataset(root, 75)
            adapters = root / 'adapters'
            def fake_run(command):
                self.assertEqual(command[command.index('--iters') + 1], '225')
                self.assertEqual(command[command.index('--max-seq-length') + 1], '1024')
                self.assertEqual(command[command.index('--learning-rate') + 1], '3e-05')
                adapters.mkdir()
                (adapters / 'adapters.safetensors').write_bytes(b'test')
            with patch('local_knowledge_trainer.training.run', side_effect=fake_run):
                self.assertEqual(train('model', str(d), str(adapters), PRESETS[0], 'standard'), 225)
            self.assertEqual(json.loads((adapters / 'training_plan.json').read_text())['examples'], 75)

    def test_single_explicit_documented_action_is_trainable(self):
        text = ('# User guide\n\n## Identifying marker genes\n'
                'Click Species Appearance to rank genes by cross-species relevance.\n'
                '\n## Background\nClick Continue to read the background.\n')
        chunks = [Chunk(SRC, 'tutorial.md', 'document', txt, start, end)
                  for start, end, txt in _chunks_for_text(text, chunk_lines=5, overlap=1)]
        rows = extract_workflow_examples(chunks)
        self.assertEqual(len(rows), 1)
        self.assertIn('identify marker genes', rows[0]['messages'][0]['content'])
        self.assertIn('Species Appearance', rows[0]['messages'][1]['content'])

    def test_workflow_question_does_not_repeat_application_name(self):
        text = ('# User guide\n\n## Select cell types in EvoViewer\n'
                'Click a cell-type rectangle in the hierarchy.\n'
                'Hold Shift and click another rectangle.\n')
        rows = extract_workflow_examples([Chunk(SRC, '_tutorials/cytosplore-evoviewer.md',
                                                'document', text, 1, 6)])
        self.assertTrue(rows)
        self.assertEqual(rows[0]['messages'][0]['content'], 'How do I select cell types in EvoViewer?')

    def test_retrieval_training_uses_actual_source_not_answer_as_excerpt(self):
        text = ('# User guide\n\n## Identify marker genes\n'
                'Select a cell-type rectangle to select that cell type.\n'
                'Click Update to compute characteristics.\n'
                'Click Species Appearance to sort interesting genes.\n')
        chunks = [Chunk(SRC, 'README.md', 'document', text, 1, len(text.splitlines()))]
        rows = generated_examples(chunks, limit=50)
        contextual = [r for r in rows if r.get('_training_style') == 'retrieval_conditioned'
                      and r.get('_evidence_type') == 'documented_workflow']
        self.assertTrue(contextual)
        prompt = contextual[0]['messages'][0]['content']
        self.assertIn('Click Update to compute characteristics.', prompt)
        self.assertNotIn('Follow these documented steps:', prompt)
        self.assertIn('Question: How do I identify marker genes', prompt)
        self.assertNotIn('[references_class]', str(rows))
        self.assertGreaterEqual(quality_metrics(rows)['unique_workflows'], 1)

    def test_single_workflow_group_cannot_all_be_held_out(self):
        workflow = {
            'messages': [{'role': 'user', 'content': 'How to select a cell type?'},
                         {'role': 'assistant', 'content': 'Click the cell type rectangle in the hierarchy.'}],
            '_source': 'repoA::doc.md', '_split_group': 'repoA::doc.md',
            '_location': 'doc.md:L2-L2', '_evidence_type': 'documented_workflow',
        }
        generic = {'messages': [{'role': 'user', 'content': 'What is repo B?'},
                                {'role': 'assistant', 'content': 'Repo B contains other documentation.'}],
                   '_source': 'repoB::readme.md', '_location': 'readme.md:L1-L1'}
        with tempfile.TemporaryDirectory() as tmp:
            write_training_data([workflow, generic], Path(tmp))
            train_rows = [json.loads(line) for line in (Path(tmp) / 'train.jsonl').read_text().splitlines()]
            self.assertIn('How to select a cell type?', [r['messages'][0]['content'] for r in train_rows])

    def test_multi_repo_examples_have_two_citations_and_no_false_integration(self):
        a = Chunk('https://github.com/example/scatter', 'README.md', 'document',
                  '# Scatterplot controls\nScatterplot point size and opacity controls help users adjust the point size and point opacity within the active visualization view.', 1, 2)
        b = Chunk('https://github.com/example/legend', 'README.md', 'document',
                  '# Legend controls\nThe legend shows point size and point opacity choices for scatterplot elements, allowing users to compare visual values across selections.', 1, 2)
        rows = extract_multisource_examples([a, b])
        self.assertTrue(rows)
        self.assertIn('[1] Source:', rows[0]['messages'][0]['content'])
        self.assertIn('[2] Source:', rows[0]['messages'][0]['content'])
        self.assertIn('do not by themselves establish', rows[0]['messages'][1]['content'])
        self.assertEqual(len(rows[0]['_referenced_groups']), 2)

    def test_only_typed_ui_control_group_kept_for_training_when_possible(self):
        rows = []
        for name, kind in [('guide', 'documented_workflow'), ('actions', 'static_ui'),
                           ('other', 'general_document_or_safety'), ('extra', 'general_document_or_safety')]:
            rows.append({
                'messages': [{'role': 'user', 'content': f'How to use {name}?'},
                             {'role': 'assistant', 'content': f'User-facing documentation for {name}.'}],
                '_source': f'{name}::README.md', '_location': 'README.md:L1-L1',
                '_evidence_type': kind,
            })
        with tempfile.TemporaryDirectory() as tmp:
            write_training_data(rows, Path(tmp))
            items = [json.loads(line) for line in (Path(tmp) / 'train.jsonl').read_text().splitlines()]
            questions = [r['messages'][0]['content'] for r in items]
            self.assertIn('How to use guide?', questions)
            self.assertIn('How to use actions?', questions)

    def test_multi_repo_training_cannot_leak_validation_file(self):
        ordinary = []
        for repo in ('A', 'B', 'C', 'D'):
            ordinary.append({
                'messages': [{'role': 'user', 'content': f'Question from repo {repo}?'},
                             {'role': 'assistant', 'content': f'Answer from repo {repo}.'}],
                '_source': f'repo{repo}::README.md', '_location': 'README.md:L1-L1',
            })
        cross = {
            'messages': [{'role': 'user', 'content': 'Compare A and B?'},
                         {'role': 'assistant', 'content': 'A reports one fact. B reports another fact.'}],
            '_source': 'multi::repoA::repoB', '_split_group': 'repoA::README.md',
            '_referenced_groups': ['repoA::README.md', 'repoB::README.md'],
            '_training_only': True, '_location': 'README.md:L1-L1',
        }
        with tempfile.TemporaryDirectory() as tmp:
            _, heldout = write_training_data(ordinary + [cross], Path(tmp))
            heldout_sources = {r['_source'] for r in heldout}
            train_rows = [json.loads(line) for line in (Path(tmp) / 'train.jsonl').read_text().splitlines()]
            if any(r['messages'][0]['content'] == 'Compare A and B?' for r in train_rows):
                self.assertFalse({'repoA::README.md', 'repoB::README.md'} & heldout_sources)


if __name__ == '__main__':
    unittest.main()
