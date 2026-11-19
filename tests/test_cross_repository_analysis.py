"""End-to-end behavioral checks for the source-fact graph and hybrid retrieval."""
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from local_knowledge_trainer.analysis import analyze_chunks, graph_summary, ui_controls
from local_knowledge_trainer.api import prepare_knowledge
from local_knowledge_trainer.index import create_index, search_evidence, related_facts
from local_knowledge_trainer.prepare import Chunk, generated_examples
from local_knowledge_trainer.upgrade_index import upgrade_release


RENDERER = 'https://github.com/acme/RenderApp'
COMMON = 'https://github.com/acme/CommonTypes'


def sample_chunks():
    return [
        Chunk(RENDERER, 'src/Render.cpp', 'code', '''#include "SharedModel.h"
Render::Render() : _pointSizeAction(this, "Point size") {
  connect(&_pointSizeAction, &mv::gui::DecimalAction::valueChanged,
    this, [this](float size) {
       _renderer.setPointSize(size);
    });
}
''', 1, 7),
        Chunk(COMMON, 'include/SharedModel.h', 'code',
              'class SharedModel {\n public: void load();\n};', 1, 3),
        Chunk(RENDERER, 'README.md', 'document',
              '# RenderApp\nThis application displays points on a scatterplot canvas.', 1, 2),
    ]


class GraphTests(unittest.TestCase):
    def test_cross_repository_link_requires_unique_header(self):
        chunks = sample_chunks()
        facts = analyze_chunks(chunks)
        link = next(f for f in facts if f.predicate == 'imports_file')
        self.assertEqual(link.source, RENDERER)
        self.assertEqual(link.target_source, COMMON)
        self.assertEqual(link.target_location, 'include/SharedModel.h:L1-L1')
        self.assertEqual(graph_summary(facts)['cross_repository_pairs'], 1)
        duplicate = Chunk('third', 'include/SharedModel.h', 'code',
                          'class AnotherModel { void run(); };', 1, 1)
        ambiguous = analyze_chunks(chunks + [duplicate])
        self.assertFalse(any(f.predicate == 'imports_file' for f in ambiguous))

    def test_ui_signal_to_setter_and_correct_line_numbers(self):
        facts = analyze_chunks(sample_chunks())
        controls = ui_controls(facts)
        self.assertEqual(len(controls), 1)
        self.assertEqual(controls[0]['label'], 'Point size')
        self.assertIn(('_renderer.setPointSize', 'src/Render.cpp:L3-L3'),
                      controls[0]['connections'])
        self.assertFalse(any('menu' in str(f).lower() for f in facts
                             if f.predicate == 'registered_with'))

    def test_hybrid_retrieval_finds_both_repos_and_ui_connections(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'knowledge.db'
            chunks = sample_chunks()
            facts = analyze_chunks(chunks)
            create_index(chunks, db, facts)
            cross = search_evidence(db, 'How does RenderApp use CommonTypes?', limit=6)
            self.assertTrue(any('includes a header' in row['content'] for row in cross))
            self.assertTrue(any('CommonTypes' in row['content'] for row in cross))
            # General user questions must not be filled with synthetic graph
            # labels such as [references_class] or [imports_file].
            general = search_evidence(db, 'What is the purpose of RenderApp?', limit=6)
            self.assertTrue(general)
            self.assertFalse(any(r['kind'] == 'code_relation' for r in general))
            self.assertFalse(any('[references_class]' in r['content'] for r in cross))
            ui = search_evidence(db, 'How do I increase point size in RenderApp?', ui=True)
            self.assertTrue(ui)
            self.assertTrue(any('valueChanged' in r['content'] for r in ui))
            self.assertTrue(any('setPointSize' in r['content'] for r in ui))
            self.assertEqual(related_facts(db, '_pointSizeAction')[0]['source'], RENDERER)
            self.assertEqual(search_evidence(db, 'How to change unknown XYZZY setting?', ui=True), [])

    def test_ui_docs_plus_graph(self):
        chunks = sample_chunks()
        chunks.append(Chunk(RENDERER, 'docs/user-guide.md', 'document',
                            '# Adjust plot\nOpen the Point settings panel and use the Point size slider.',
                            1, 2))
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'knowledge.db'
            create_index(chunks, db, analyze_chunks(chunks))
            results = search_evidence(db, 'How do I increase point size in RenderApp?',
                                      limit=5, ui=True)
            self.assertTrue(any(r['kind'] == 'document' for r in results))
            self.assertTrue(any(r['kind'] == 'code_relation' for r in results))

    def test_better_training_examples_ground_ui_and_links(self):
        chunks = sample_chunks()
        facts = analyze_chunks(chunks)
        rows = generated_examples(chunks, facts=facts, audience="developer")
        self.assertTrue(any(r.get('_evidence_type') == 'static_ui' for r in rows))
        self.assertTrue(any(r.get('_evidence_type') == 'cross_repository' for r in rows))
        answers = [r['messages'][1]['content'] for r in rows]
        self.assertTrue(any('runtime screen position is unverified' in a for a in answers))
        self.assertTrue(any('CommonTypes' in a and 'dependency' in a for a in answers))
        self.assertFalse(any('Read the implementation to determine' in a for a in answers))

    def test_upgrade_existing_release_preserves_model_and_legacy_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            release = Path(tmp) / 'release'
            release.mkdir()
            model_bytes = b'GGUF\x00test-model'
            (release / 'assistant.gguf').write_bytes(model_bytes)
            (release / 'manifest.json').write_text(json.dumps({'knowledge_index': {'chunk_count': 3}}))
            (release / 'SHA256SUMS.txt').write_text('bad  assistant.gguf\nbad  knowledge.db\nbad  manifest.json\n')
            create_index(sample_chunks(), release / 'knowledge.db')
            self.assertEqual(search_evidence(release / 'knowledge.db',
                                              'How to increase point size?', ui=True), [])
            summary = upgrade_release(release)
            self.assertGreater(summary['facts'], 0)
            self.assertTrue((release / 'knowledge.pre-graph.db').is_file())
            self.assertEqual((release / 'assistant.gguf').read_bytes(), model_bytes)
            self.assertTrue(any(r['kind'] == 'code_relation' for r in search_evidence(
                release / 'knowledge.db', 'How to increase point size in RenderApp?', ui=True)))
            with self.assertRaises(ValueError):
                upgrade_release(release)
            self.assertIn('analysis_summary.json', (release / 'SHA256SUMS.txt').read_text())

    def test_preparation_works_across_two_local_repos_without_dependencies(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            render = root / 'RenderApp'
            common = root / 'CommonTypes'
            (render / 'src').mkdir(parents=True)
            (common / 'include').mkdir(parents=True)
            (render / 'README.md').write_text('# Rendering points\n' +
                                              'User guide: create a plot and adjust point sizes.\n' * 6)
            (render / 'src' / 'Render.cpp').write_text(sample_chunks()[0].text)
            (common / 'include' / 'SharedModel.h').write_text(sample_chunks()[1].text)
            (common / 'README.md').write_text('# Common types\n' +
                                              'Common source structures are documented here.\n' * 6)
            result = prepare_knowledge([str(render), str(common)], root / 'run')
            self.assertGreater(result.indexed_chunks, 0)
            self.assertGreater(result.analysis_summary['facts'], 0)
            self.assertEqual(result.analysis_summary['cross_repository_pairs'], 1)
            self.assertTrue((result.workspace / 'data' / 'train.jsonl').is_file())
            self.assertEqual(result.database.name, 'knowledge.db')
            self.assertEqual(len(result.failed_sources), 0)


if __name__ == '__main__':
    unittest.main()

class CorpusCoverageTests(unittest.TestCase):
    def test_global_chunk_limit_is_fair_to_many_repositories(self):
        from unittest.mock import patch
        from local_knowledge_trainer.prepare import collect_chunks
        from local_knowledge_trainer.sources import Source
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            sources = []
            for index in range(3):
                repo = base / f'repo{index}'
                repo.mkdir()
                for number in range(5):
                    (repo / f'{number}.cpp').write_text(
                        f'class LargeModule{index}_{number} {{ /* meaningful source data for indexing */ }};')
                sources.append(Source('local', f'fake-repo-{index}', repo))
            with patch('local_knowledge_trainer.prepare.MAX_CHUNKS', 6):
                chunks = collect_chunks(sources)
            self.assertEqual(len(chunks), 6)
            self.assertEqual({c.source for c in chunks}, {s.origin for s in sources})
            self.assertEqual([sum(c.source == s.origin for c in chunks) for s in sources], [2, 2, 2])
