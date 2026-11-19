# Training quality, data leakage and model evaluation (v0.4.5)

## The previous failure

The user's v0.4.4 training log showed **772 train / 80 validation** rows, with
**29 documented-workflow rows and 523 static-action rows**. MLX fine-tuning
stopped after **100 optimizer updates**, about **8,500 processed tokens**.
A small train loss simply indicated that a tiny model had become good at
predicting these particular synthetic replies. It was not a benchmark of
whether people could navigate ManiVault Studio.

## What the new training stage does

1. Reconstruct Markdown tutorial sections across overlapping source chunks.
   Keep only explicit, attributable user actions, including single actionable
   steps. Do not invent missing UI controls or menu paths.
2. Keep plain question/answer examples so the assistant can retain common user
   vocabulary. Also train on **real source excerpts** with exactly the
   `Reference excerpts` and `Question` boundary used during inference.
3. Down-weight noisy source-label explanations. UI examples must have a
   meaningful visible label and a verified action type. Generic "Point" and
   "Settings" symbols are not user instructions.
4. Include very small numbers of abstention examples. Too many refusals can
   make small models overly hesitant.
5. Make optional two-source comparison examples only when **two original
   documents** have overlapping, informative topics. Those examples say what
   each document states, not that the repositories integrate at runtime.
6. Hold out source **files**, not randomized copies of the same task. Any
   multi-source QA touching a validation file is dropped before training.
7. Cover the dataset approximately once in quick training and three times
   in standard training, with a maximum of 1800 MLX optimizer updates. PyTorch
   uses four accumulated microbatches per update and budgets accordingly.

## Dry run and inspect before training

```sh
./start.command --sources-file sources.txt --model 2 --mode standard --yes --dry-run
./start.command inspect-training runs/RUN_ID --model 2 --mode standard
```

Inspect `runs/RUN_ID/training_quality.json` for `unique_workflows`,
`retrieval_conditioned_count`, `known_bad_phrases` and example types.
`evaluation.json` contains a **retrieval diagnostic**, not a model score.
`data/train.jsonl` and `data/valid.jsonl` are actual model input examples.
`training_plans.json` shows projected MLX budgets for each preset.

The pipeline still cannot create a verified user workflow when neither the
repository code nor documents establish one. More epochs do not repair
missing evidence, retrieval failures or a poor base model. A strong model is
not guaranteed even if every new automated test passes.

## Human-review model benchmark

```sh
./start.command evaluate runs/RUN_ID/release \
  examples/benchmarks/evoviewer-model-qa.jsonl \
  model-evaluation.json
```

This actually executes your model (unlike `evaluate-ui`, which only evaluates
the source-anchored answerer). Review each output for correctness, practical
steps, exact source support, unanswered requests and invented menu locations.
Run the same held-out questions against the **unmodified base model** with
identical retrieved excerpts if you want a defensible measurement of how
much fine-tuning helped. A model smoke test using `Hello` is only a load test.

For a comparison across 0.5B and 1.5B, use the same sources, prepared data,
question set and inference settings. Source licenses, provenance, and
privacy restrictions apply to each exported model and training dataset.

## Environment limitations

Automated Python tests were executed here on local synthetic repositories and
bundled, source-attributed tutorial text. The user's online GitHub repository
cache, actual Qwen GGUF, and Apple Silicon MLX GPU are not available in the
current runtime, so no real-model correctness score can be claimed.

## Two distinct UI answer modes

`ask` remains conservative: it returns verified source-grounded instructions
without generating potentially fabricated click paths. `ask-model` runs the
GGUF on the retrieved UI evidence when a corresponding documented task or
control is found. It is for testing whether fine-tuning actually improved the
model's answers. Review its output; generated instructions can still be wrong.

```sh
./start.command ask-model runs/RUN_ID/release \
  "How do I find marker genes in EvoViewer?"
```
