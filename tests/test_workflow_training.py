"""Workflow-quality tests: train on documented steps, not symbol fragments."""
import tempfile
import unittest
from pathlib import Path

from local_knowledge_trainer.prepare import Chunk, _chunks_for_text, generated_examples, write_training_data
from local_knowledge_trainer.workflow_training import extract_workflow_examples

DOC = 'https://github.com/ManiVaultStudio/manivaultstudio.github.io'
TEXT = '''# Cytosplore EvoViewer

## Selecting cell types
A cell-type hierarchy allows visual comparisons.
1. Click a cell-type rectangle to select cells.
2. Hold Shift and click other rectangles to select additional types.

## Identify marker genes
Marker genes are listed by species relevance.
1. Click Update to calculate characteristics of the selected population.
2. Select Species Appearance to sort genes by species relevance.
3. Adjust Top N to change the threshold.

## Building the C++ application
1. Run cmake to configure the build directory.
2. Run make to build executable.

## Background information
Gene data provides useful biological context.
It is not a procedure.
'''


class WorkflowTrainingTests(unittest.TestCase):
    def test_only_documented_user_tasks_become_examples(self):
        chunks = [Chunk(DOC, '_tutorials/cytosplore-evoviewer.md', 'document', text, lo, hi)
                  for lo, hi, text in _chunks_for_text(TEXT, chunk_lines=8, overlap=3)]
        rows = extract_workflow_examples(chunks)
        prompts = [r['messages'][0]['content'] for r in rows]
        self.assertTrue(any('select cell types' in q for q in prompts), prompts)
        self.assertTrue(any('identify marker genes' in q for q in prompts), prompts)
        self.assertFalse(any('C++' in q or 'Background' in q for q in prompts), prompts)
        self.assertGreaterEqual(len(rows), 2)
        for row in rows:
            self.assertIn('_tutorials/cytosplore-evoviewer.md:L', row['messages'][1]['content'])
            self.assertNotIn('[references_class]', row['messages'][1]['content'])
            self.assertNotIn('edit the source', row['messages'][1]['content'])

    def test_user_training_prefers_steps_and_avoids_validation_leak(self):
        chunks = [Chunk(DOC, '_tutorials/cytosplore-evoviewer.md', 'document', t, l, h)
                  for l, h, t in _chunks_for_text(TEXT, chunk_lines=8, overlap=3)]
        chunks.append(Chunk('local-other', 'README.md', 'document',
                            '# Loading data\nOpen the application, select the data file, confirm the dataset and check the results before continuing.\n', 1, 2))
        rows = generated_examples(chunks, limit=60)
        self.assertTrue(any(r.get('_evidence_type') == 'documented_workflow' for r in rows))
        with tempfile.TemporaryDirectory() as tmp:
            stats, valid = write_training_data(rows, Path(tmp))
            self.assertGreater(stats['train_examples'], 0)
            self.assertGreater(stats['validation_examples'], 0)
            self.assertEqual(len({r['_source'].split('::', 1)[0] for r in rows}), 2)
            doc_train = {r['_source'] for r in rows if r['_source'].startswith(DOC)}
            self.assertEqual(len(doc_train), 1)

    def test_makes_no_claim_from_code_only(self):
        rows = extract_workflow_examples([
            Chunk('local', 'PointPlotAction.cpp', 'code',
                  'void Plot::setOpacity(double value) {}', 1, 1)])
        self.assertEqual(rows, [])


if __name__ == '__main__':
    unittest.main()
