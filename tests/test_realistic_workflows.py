"""Task-based end-user checks, not merely symbol-detection tests."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from local_knowledge_trainer.analysis import analyze_chunks
from local_knowledge_trainer.demo import run_question
from local_knowledge_trainer.index import create_index, is_ui_instruction_question
from local_knowledge_trainer.prepare import Chunk, _chunks_for_text
from local_knowledge_trainer.ui_help import answer_ui_question
from local_knowledge_trainer.workflow_search import query_topics, search_workflows

SITE = 'https://github.com/ManiVaultStudio/manivaultstudio.github.io'
PLUGIN = 'https://github.com/ManiVaultStudio/XSCGeneDetectPlugin'
OTHER = 'https://github.com/ManiVaultStudio/HDF5Loader'


def fixture():
    # Intentionally contains sections spanning the trainer's normal 36-line
    # overlapping chunk boundaries and a Jekyll-style Markdown tutorial.
    filler = '\n'.join(f'Study notes concerning general visualization {n}.' for n in range(34))
    guide = ('---\nlayout: tutorial\n---\n# Cytosplore EvoViewer\n' + filler + '\n'
             '## Marker genes\n'
             'Marker genes identify expression signatures across cell populations.\n'
             '1. Open the gene detection panel.\n'
             '2. Select the population of interest.\n'
             '3. Click Detect marker genes to list candidate markers.\n'
             '<img src="some-image.png" />\n'
             '\n## Cell abundance\n'
             'The Cell abundance view shows relative population frequencies.\n'
             '1. Open the Cell abundance view.\n'
             '2. Select a sample in the comparison dropdown.\n'
             '3. Click <strong>Show abundance</strong> to display the summary.\n')
    chunks = [Chunk(SITE, '_tutorials/cytosplore-evoviewer.md', 'document', s, a, b)
              for a, b, s in _chunks_for_text(guide)]
    chunks.extend([
        Chunk(PLUGIN, 'src/SettingsAction.cpp', 'code',
              'SettingsAction::SettingsAction(): markerGenes(this, "Detect marker genes") {}', 1, 1),
        Chunk(OTHER, 'docs/other.md', 'document',
              '# Cell abundance statistics\nThis has a cell in a box.\n'
              'Lots of other details. No procedure about abundance.\n', 1, 3),
    ])
    return chunks


class RealisticWorkflowTests(unittest.TestCase):
    def test_unrelated_corpus_scopes_application_and_explicit_documents(self):
        from local_knowledge_trainer.index import search
        origin = 'https://github.com/acme/manuals/tree/main/guides'
        chunks = [
            Chunk(origin, 'acme-atlasviewer.md', 'document',
                  '## Point size\nSelect the Point size slider to adjust the point size.', 1, 2),
            Chunk(origin, 'acme-terraviewer.md', 'document',
                  '## Point size\nSelect a different Point size setting.', 1, 2),
            Chunk('local:reference', 'reference.pdf', 'document',
                  'The instrument measures pressure in pascals.', 1, 1),
            Chunk('local:unrelated', 'other.pdf', 'document',
                  'Pressure pressure pressure is described differently here.', 1, 1),
        ]
        create_index(chunks, self.release / 'knowledge.db')
        hits = search_workflows(self.release / 'knowledge.db',
                                'How do I adjust point size in AtlasViewer?')
        self.assertTrue(hits)
        self.assertTrue(all('atlasviewer.md:' in hit.location for hit in hits))
        hits = search(self.release / 'knowledge.db', 'What pressure units does reference.pdf specify?')
        self.assertTrue(hits)
        self.assertTrue(all(hit['location'].startswith('reference.pdf:') for hit in hits))

    def test_html_summary_sections_supply_training_and_retrieval_steps(self):
        from local_knowledge_trainer.workflow_training import extract_workflow_examples
        text = ('<summary class="section-header">\n'
                '<span class="arrow"></span>Zooming the hierarchy\n</summary>\n\n'
                '<i class="icon"></i> Press Ctrl and click a cell type rectangle to zoom in.<br/>\n'
                '<i class="icon"></i> Press Ctrl and click a parent rectangle to zoom out.<br/>\n')
        chunks = [Chunk(SITE, '_tutorials/another-viewer.md', 'document', text, 1, 6)]
        examples = extract_workflow_examples(chunks)
        self.assertTrue(examples)
        self.assertIn('Press Ctrl', examples[0]['messages'][-1]['content'])
        create_index(chunks, self.release / 'knowledge.db')
        result = search_workflows(self.release / 'knowledge.db',
                                  'How can I zoom in on a branch of the cell-type hierarchy?')
        self.assertTrue(result)
        self.assertIn('Press Ctrl', result[0].steps[0])

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.release = Path(self.tmp.name) / 'release'
        self.release.mkdir()
        chunks = fixture()
        create_index(chunks, self.release / 'knowledge.db', facts=analyze_chunks(chunks))

    def test_normal_task_intents_have_no_ui_keyword_requirement(self):
        for question in ('How can I find cell abundance',
                         'How can I find marker genes in the EvoViewer UI?',
                         'How do I create a subset?',
                         'Identify marker genes'):
            with self.subTest(question=question):
                self.assertTrue(is_ui_instruction_question(question))
        self.assertFalse(is_ui_instruction_question('How do I implement gene detection in C++?'))
        self.assertFalse(is_ui_instruction_question('What is differential expression?'))

    def test_marker_gene_steps_from_tutorial_instead_of_cpp(self):
        response = answer_ui_question(self.release / 'knowledge.db',
                                      'How can I find marker genes in the EvoViewer UI?')
        self.assertEqual(response.level, 'documented', response.answer)
        self.assertIn('gene detection panel', response.answer)
        self.assertIn('Detect marker genes', response.answer)
        self.assertIn('cytosplore-evoviewer.md', response.answer)
        self.assertNotIn('SettingsAction::', response.answer)
        self.assertNotIn('<img', response.answer)

    def test_cell_abundance_without_named_app(self):
        response = answer_ui_question(self.release / 'knowledge.db',
                                      'How can I find cell abundance?')
        self.assertEqual(response.level, 'documented', response.answer)
        self.assertIn('Cell abundance view', response.answer)
        self.assertIn('Show abundance', response.answer)
        self.assertNotIn('other.md', response.answer)
        self.assertNotIn('<strong>', response.answer)

    def test_real_ui_question_never_invokes_llm(self):
        with patch('local_knowledge_trainer.demo.locate_llama_cli',
                   side_effect=AssertionError('should use tutorial')):
            references = run_question(self.release, 'How can I find cell abundance?')
        self.assertGreater(references, 0)

    def test_nonexistent_setting_must_not_use_nearby_unrelated_steps(self):
        response = answer_ui_question(self.release / 'knowledge.db',
                                      'How do I configure spaceship polarity?')
        self.assertEqual(response.level, 'insufficient', response.answer)

    def test_topic_normalizes_plural_and_tracks_app_separately(self):
        self.assertEqual(query_topics('How to find marker genes in EvoViewer UI?'),
                         (('marker', 'gene'), ('evoviewer',)))
        self.assertEqual(query_topics('How to select celltypes in AnotherViewer'),
                         (('cell', 'type'), ('anotherviewer',)))

    def test_bundled_verified_evo_tutorial_in_existing_release(self):
        from local_knowledge_trainer.guides import add_guide
        guide = Path(__file__).resolve().parents[1] / 'examples' / 'verified' / 'cytosplore-evoviewer-ui.md'
        add_guide(self.release, guide, source='https://viewer.cytosplore.org/documentation/evoviewer')
        cases = {
            'How do I identify marker genes in EvoViewer?': ('Species Appearance', 'Top N'),
            'How can I find cell abundance?': ('Absolute', 'Relative'),
            'How do I explore gene expression across species?': ('left-hand gene table', 'Revert'),
            'How to select celltypes in the EvoViewer?': ('cell-type rectangle', 'Shift'),
        }
        for question, checks in cases.items():
            with self.subTest(question=question):
                result = answer_ui_question(self.release / 'knowledge.db', question)
                self.assertEqual(result.level, 'documented', result.answer)
                for check in checks:
                    self.assertIn(check, result.answer)
                self.assertIn('viewer.cytosplore.org', result.answer)
                self.assertNotIn('SettingsAction.cpp', result.answer)

    def test_workflow_sources_and_line_numbers_preserved(self):
        hits = search_workflows(self.release / 'knowledge.db',
                                'How can I find marker genes in EvoViewer?')
        self.assertTrue(hits)
        self.assertTrue(hits[0].location.startswith('_tutorials/cytosplore-evoviewer.md:L'))
        self.assertGreater(len(hits[0].steps), 0)


if __name__ == '__main__':
    unittest.main()
