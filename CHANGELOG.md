## 0.4.5 — Better supervised data and meaningful training budgets

- Replace static 100-iteration LoRA training with data-size-aware quick/standard
  coverage budgets (MLX and PyTorch, accounting for gradient accumulation).
- Use original source excerpts in retrieval-conditioned SFT examples instead
  of synthetic answers embedded as evidence; add source-aware deduplication.
- Keep only actionable, identifiable UI controls in the training mix and
  cap weak document summaries and repetitive refusals.
- Add coverage-balanced documented workflows and include explicit one-action
  workflows that were previously discarded.
- Add carefully qualified, multi-document cross-repository Q&A using two
  citations; prohibit validation leakage for multi-source examples.
- Preserve training-file groups and avoid putting the only documented task
  group entirely in validation.
- Repair retrieval diagnostics to use workflow retrieval for workflow questions
  and code-relationship search for UI questions; include breakdown by type.
- Write `training_quality.json` and `training_plans.json`; add
  `inspect-training` and a separate, real-model human-review benchmark.
- Add new end-to-end and budget tests.

## 0.4.4 — Adjacent tutorial retrieval and user-task detection

- Resolve end-user tasks without requiring "UI", "menu" or "GUI" in the question.
  Captures cell abundance, marker-gene workflows, cell-type selection and point opacity.
- Reconstruct adjoining source documentation lines across short FTS excerpts;
  rank tightly matching task headings and avoid unrelated instructions.
- Clean Jekyll/HTML markup, accept steps with short contextual prefixes,
  normalize plurals and the common "celltypes" spelling.
- Include a source-attributed, optional EvoViewer guide from the published tutorial;
  `add-guide` updates an existing release without retraining or altering its GGUF.
- Extend the offline acceptance suite to 94 tests, including EvoViewer workflow
  extraction, paraphrases, unsupported actions and point-opacity guidance.
- Generate task-specific supervised fine-tuning examples directly from documented
  multi-step tutorial sections and keep their train/validation groups together.
- Report documented-workflow and static-control sample counts before training;
  warn if the corpus is not sufficient to establish navigation skills.
- Keep synthetic graph relationship strings out of general overview prompts,
  and use natural-language facts for technical cross-repository questions.
- Include a seven-case EvoViewer guide acceptance benchmark (passed locally,
  not a measurement of GGUF accuracy on the user's Mac).
- Do not claim GGUF reasoning or accuracy on an unshared real knowledge database.

## 0.4.3 — Evidence-first user tasks and executable accuracy checks

- Change strategy for end-user UI questions: infer an interaction affordance
  from uniquely evidenced ManiVault Qt action types and visible labels, not from
  a free-form 0.5B model response.
- Resolve action declarations from other files in the same repository, and
  typed signal/slot references where declarations were not indexed.
- Match everyday language (e.g. "dots bigger") to an existing Point size
  control; avoid speculative menu positions and source editing suggestions.
- Create task-oriented UI training examples with observed grouping/action type
  rather than repetitive symbol-location drills; reserve additional sample
  capacity for these examples.
- Add `evaluate-ui RELEASE benchmark.jsonl` with pass/fail assertions,
  source checks, JSON reporting and CI-friendly nonzero exit status.
- Verify against an independent synthetic three-repository multi-file fixture,
  and compare exactly the same checks against v0.4.2 (1/4 versus 4/4).
- No GGUF or live ManiVault GUI was available for a physical runtime test.

## 0.4.2 — Runtime provenance and focused UI help

- Display the actual checkout path and version with `./start.command --version`.
- Warn when a project is running from a Trash directory, where trained models are at risk of deletion.
- Show explicitly when UI questions take the deterministic evidence-based path instead of model generation.
- Run UI evidence answers from an existing knowledge.db even if no GGUF is present.
- Reject unrelated tutorial snippets that only contain topic terms in distant parts of a document.
- Regression coverage for mistakenly mixed release versions and irrelevant document hits.

## 0.4.1 — End-user navigation first

- Fixed the documented failure where a UI question caused the small model to suggest editing C++ source files.
- Added dependency-free extractive UI guidance from documentation, control labels, and explicit registration groups.
- Changed default generated training examples to prioritize user-facing information rather than code declarations.
- Preserved opt-in developer-oriented training examples in the Python API.
- Added cross-platform tests for unsupported operations, verified documentation, and code-only UI controls.
- Existing GGUF releases work with the updated CLI without retraining.

# Changelog

## 0.4.0 — Cross-repository source reasoning and grounded UI analysis

- Add conservative, dependency-free cross-repository source graph from unique C/C++ header/class references, Qt control labels, signals and observable setter callbacks.
- Improve source coverage with round-robin chunk collection instead of exhausting the global cap on early repositories.
- Generate additional fact-grounded UI and cross-repo fine-tuning examples without fabricating GUI paths or executable behavior.
- Hybrid source/relationship retrieval now supplements docs with Qt action evidence and uniquely resolved cross-repository target excerpts.
- Introduce `upgrade-index` for previously exported releases (backs up SQLite, preserves GGUF) and `inspect-symbol` for transparent source-fact inspection.
- Publish `analysis_summary.json`, training/evaluation limitations, and separate architecture/verification documentation.
- Add end-to-end regression tests for multi-repo linking, ambiguous resolution, UI signal/setter patterns, corpus fairness and legacy-index upgrade.

## 0.3.6 — User-facing guidance and inference compatibility

- Separate UI-help retrieval from developer code lookup, with honest abstention
  when no actionable user documentation is indexed.
- Avoid double-applying ChatML to llama-cli prompts; prefer the raw
  llama-completion tool where available. Preserve one-shot invocation.
- Add `add-guide` to update a completed release with locally verified UI manuals
  without retraining or changing GGUF weights; update manifest and checksums.
- Improve default generated code examples so declarations are not presented as
  operating instructions; expand grounded answer length and regression tests.
- Document user-guide authoring, accuracy checks and missing-evidence behavior.

## 0.3.5 — Training environment recovery

- Diagnose and repair missing/corrupt NumPy compiled extensions before any costly source ingestion.
- Add `doctor` launcher command and clear MLX/PyTorch import checks.
- Reuse installed dependencies when requirements have not changed.
- Extend `resume` to continue prepared-but-not-trained runs without re-cloning repositories.
- Persist the training mode in new run metadata and require explicit `--mode` on older incomplete runs.
- Add focused tests for environment recovery and pre-training resume.


## v0.3.4

- Skip and report individually failed URLs, repositories and local paths instead of aborting a viable build; keep strict fail-fast mode with `--strict-sources`.
- Retry transient HTTP/network failures, detect invalid PDF downloads, and prevent partial files from entering the cache.
- Share successful Git/document acquisitions across runs in `runs/.source-cache` (configurable timeout/retries; `--no-source-cache` opt-out).
- Publish `source_failures.json` with every new release and include it in the manifest and checksums.
- Add mocked timeout, PDF error, clone retry, cache reuse and ingestion recovery regression tests.


## v0.3.3

- Fixed `ask`, `chat` and `evaluate` compatibility with llama.cpp versions that reject the removed `--no-conversation` CLI flag. Optional flags are now detected from the local executable's help output.
- Prioritize explicitly named GitHub repositories and relevant README content when searching the offline knowledge index.
- Added batch source URL/path import from UTF-8 `.txt` files using `--sources-file` and the interactive wizard; supports comments, deduplication and file-relative paths.
- Added source-list, retrieval-ranking and model-command regression tests, including a fake offline CLI smoke test.
- Fixed classification of Windows drive-letter paths as local sources.

## v0.3.2

- Tokenizer conversion compatibility for Transformers 4/5 and improved export resume.
