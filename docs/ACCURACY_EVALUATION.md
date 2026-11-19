# How to measure whether the assistant helps users

This project is designed for **end users navigating existing software**. Its
main success criterion is whether a person can perform a real task without
modifying source code, not a low language-model training loss.

## What has actually been tested

The standard automated suite tests parsing, acquisition, indexing, export
orchestration and the UI answerer. The v0.4.3 acceptance fixture is a small,
**synthetic** three-repository project with a Scatterplot-like action, a
separate type header, an associated Core action class, and an unrelated
website tutorial. The independently written questions require it to identify
Point → Point size, suggest increasing/decreasing a numeric value, reject
irrelevant sources, and admit when the setting does not exist. The test runs
full local source preparation into SQLite and checks real answer text.

This is a regression test, not proof the GGUF model understands ManiVault. A
real task evaluation requires the actual source revisions, model, knowledge.db,
application UI version and an independently checked set of correct actions.

## Evaluate your *existing* release (no retraining)

```
./start.command --version
./start.command evaluate-ui runs/EXISTING_RUN/release \
  examples/ui-benchmark.example.jsonl \
  --output ui-results.json --min-pass-rate 0.5
```

A JSONL case looks like this:

```
{"question":"How do I make dots bigger in Scatterplot?","must_include":["Point size","increase"],"must_not_include":["edit source","C++"],"expected_source":"Scatterplot"}
```

`expected_level` is optional and takes `documented`, `control` or
`insufficient`. A case can test positive evidence and/or a negative
hallucination. A benchmark score depends on the **quality of the independently
verified expectations**, so the example file is only a starter. Cases should
cover normal tasks, paraphrases, similar-named controls in different plugins,
wrong assumptions, missing evidence and multiple-workspace layouts.

## Release gate for a real user-facing application

Create at least 20 *held-out* tasks per software version. Verify every
expected procedure in the actual GUI (screen recording or annotated screenshot
is useful), and record the source revision. Run the benchmark and manually
check each response for a misleading claim, false screen location, or omitted
required step. Distinguish:

- **Documented / verified:** Every action is supported by a guide or a tested UI.
- **Code-observed:** The control and its type/group are supported by source,
  but placement in the running UI is not independently confirmed.
- **Insufficient:** The system cannot substantiate the requested operation.

Measure action correctness, step completeness, unsupported-claim rate and
abstention appropriateness **separately**. Model validation loss,
retrieval source-hit@5, and unit-test counts cannot replace these checks.

## Why this version changes the strategy

The old fine-tuning pipeline generated many generic documentation explanations
and trained the 0.5B model for only 100 iterations. That is not adequate to
teach broad multi-repository operational reasoning. v0.4.3 instead performs
source-grounded control detection and a bounded answer assembly for UI
questions, with the model reserved for questions it can usefully synthesize.
The rule-based approach is intentionally narrow: it is safer and more
measurable, not a claim of complete UI understanding. To expand beyond simple
controls, build a verified workflow graph from public user guides and live UI
observations, then evaluate against held-out tasks before further fine-tuning.

## v0.4.4: actual documented-workflow checks

The shipped `examples/verified/cytosplore-evoviewer-ui.md` is a concise,
source-attributed guide based on
https://viewer.cytosplore.org/documentation/evoviewer (checked 2026-11-15).
`examples/verified/evoviewer-benchmark.jsonl` includes six end-user questions
and one unsupported setting. The local offline, evidence-first answer system
passed **7/7** after the guide was inserted into a freshly created SQLite
index. This verifies extractive answering **when this guide is indexed**;
it is not an independent measurement of model inference, nor a test of the
user's actual `knowledge.db` or GUI version.

The generated LoRA training data now includes explicit documented-workflow Q&A
where tutorials contain two or more source-backed interaction steps. Summaries
from random document fragments are capped when such examples exist. Check the
`training_example_types` field in `evaluation.json`: a low number of
`documented_workflow` examples means the model's task-answer training remains
weak even when overall training loss falls.

General purpose questions no longer get irrelevant `[references_class]`
relationship strings injected into their evidence prompt. Technical architecture
questions still retrieve uniquely resolved cross-repository code links.
