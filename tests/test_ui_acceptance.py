"""Independent acceptance tests with a multi-file, multi-repository Qt corpus.

This is an offline static-analysis fixture, not ManiVault execution and not
an end-to-end test of the user's GGUF model.
"""
import json
import tempfile
import unittest
from pathlib import Path

from local_knowledge_trainer.api import prepare_knowledge
from local_knowledge_trainer.index import is_ui_instruction_question
from local_knowledge_trainer.ui_benchmark import evaluate_ui
from local_knowledge_trainer.ui_help import answer_ui_question


def populate(tmp):
    base = Path(tmp)
    scatter = base / 'Scatterplot'
    core = base / 'core'
    tutorial = base / 'website'
    for path in [scatter / 'src', core / 'include', tutorial / '_tutorials']:
        path.mkdir(parents=True)
    (scatter / 'src' / 'PointPlotAction.h').write_text('''#pragma once
#include "DecimalAction.h"
class PointPlotAction {
    mv::gui::DecimalAction _pointSizeAction;
    mv::gui::DecimalAction _pointOpacityAction;
    mv::gui::GroupAction _pointGroup;
};
''')
    (scatter / 'src' / 'PointPlotAction.cpp').write_text('''#include "PointPlotAction.h"
PointPlotAction::PointPlotAction() : _pointGroup(this, "Point"),
    _pointSizeAction(this, "Point size"),
    _pointOpacityAction(this, "Point opacity") {
    _pointGroup.addSubAction(&_pointSizeAction);
    _pointGroup.addSubAction(&_pointOpacityAction);
    connect(&_pointSizeAction, &mv::gui::DecimalAction::valueChanged,
            this, [this](float size) { _renderer.setPointSize(size); });
    connect(&_pointOpacityAction, &mv::gui::DecimalAction::valueChanged,
            this, [this](float opacity) { _renderer.setOpacity(opacity); });
}
''')
    (scatter / 'README.md').write_text('# Scatterplot\nA visualization of high-dimensional data as points in a plot.\n')
    (core / 'include' / 'DecimalAction.h').write_text('''#pragma once
class DecimalAction { // generic numeric action
   public: void setValue(double value);
};
''')
    (core / 'README.md').write_text('# ManiVault core\nReusable numeric controls and layouts.\n')
    (tutorial / '_tutorials' / 'unrelated.md').write_text('''# Point exploration
Increase the view size to show the whole canvas.
The point color can be configured separately.
This is about a different plugin and does not describe point size controls.
''')
    (tutorial / 'README.md').write_text('# Website\nGeneral app tutorials.\n')
    return [str(scatter), str(core), str(tutorial)]


class UIAcceptanceTests(unittest.TestCase):
    def test_multi_file_multi_repo_dry_run_and_judged_answers(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            sources = populate(tmp)
            prepared = prepare_knowledge(sources, base / 'run')
            self.assertGreater(prepared.analysis_summary['facts'], 0)
            self.assertGreaterEqual(prepared.analysis_summary['cross_repository_pairs'], 1)
            index = prepared.database
            checks = [
                dict(question='How to increase point size in Scatterplot?', expected_level='control',
                     must_include=['Point', 'Point size', 'Increase the value'],
                     must_not_include=['modify the code', 'source files', 'getContextMenu'],
                     expected_source='Scatterplot'),
                dict(question='How do I make dots bigger in Scatterplot?', expected_level='control',
                     must_include=['Point size', 'Increase the value'],
                     must_not_include=['website']),
                dict(question='how to change point opacity?', expected_level='control',
                     must_include=['Point opacity', 'Adjust the numeric value'],
                     must_not_include=['PointPlotAction class', 'references_class']),
                dict(question='How to decrease point opacity in Scatterplot?', expected_level='control',
                     must_include=['Point opacity', 'Decrease the value'],
                     must_not_include=['modify source']),
                dict(question='How to change unknown XYZZY setting?', expected_level='insufficient',
                     must_include=['cannot verify'], must_not_include=['setPointSize']),
            ]
            benchmark = base / 'acceptance.jsonl'
            benchmark.write_text(''.join(json.dumps(c) + '\n' for c in checks))
            result = evaluate_ui(index, benchmark)
            self.assertEqual((result['passed'], result['tested']), (5, 5), result)
            self.assertEqual(result['scope'], 'evidence-first offline UI guidance; not GGUF model accuracy')
            self.assertFalse(is_ui_instruction_question('How is setPointSize implemented in C++?'))
            # The trained model is not needed for these checked UI questions.
            self.assertTrue((prepared.workspace / 'data' / 'train.jsonl').is_file())

    def test_benchmark_detects_wrong_answer_and_missing_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            prepared = prepare_knowledge(populate(tmp), base / 'run')
            benchmark = base / 'bad.jsonl'
            benchmark.write_text(json.dumps(dict(question='How to increase point size in Scatterplot?',
                 expected_level='documented', must_include=['click hidden menu'],
                 expected_source='not-present-repository'))+'\n')
            outcome = evaluate_ui(prepared.database, benchmark)
            self.assertEqual(outcome['failed'], 1)
            self.assertGreaterEqual(len(outcome['cases'][0]['failures']), 2)


if __name__ == '__main__':
    unittest.main()
