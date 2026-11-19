# Multi-repository evidence and source-code understanding

## Scope

Local Knowledge Trainer v0.4.0 builds a small source-relationship layer into its
existing SQLite FTS5 knowledge database. It does not call an external model to
make up descriptions of code. Data collection, analysis, search and Q&A
preparation can run with the Python standard library (PDF extraction optionally
uses `pypdf`). Local LLM fine-tuning is a separate, heavier phase.

This feature improves **grounding** and organization. It does not by itself
make a 0.5B model into a reliable cross-repository reasoning engine.

## How evidence is linked

1. Source collection is interleaved across repositories to prevent one huge
   repository from consuming every available chunk slot.
2. Each indexed excerpt carries its source URL, file path and line range.
3. C/C++ declarations and references are extracted from those excerpts.
4. A cross-repository `#include` relationship is recorded only when the
   referenced filename uniquely matches an indexed file. Class references
   are linked only to a unique defining file and are labeled as references,
   **not** function calls or runtime dependencies.
5. Qt-style action labels, tooltips, widget registrations and supported
   `connect` forms are recorded as source facts. A connected setter may be
   reported if the connection's source text contains it.
6. Source facts are held in the same `knowledge.db` as the full-text chunks.
   `ask` and `chat` retrieve lexical evidence plus selected fact relationships,
   including a short excerpt from a linked target file.
7. Training examples generated from these facts are explicit about limits:
   an include establishes a source-level reference; a label/connection
   establishes a control relation, but **not** a verified visual click path.

## Index tables

- `chunks`: original SQLite FTS5 full-text source excerpts (backward-compatible).
- `facts`: observed symbol/UI relations with source and target evidence; absent
  in releases created before v0.4.0.
- `metadata`: existing schema version remains `1` for compatibility with the
  simple deployed SQLite clients. The optional `facts` table is feature-detected.

The release additionally contains `analysis_summary.json` describing observed
counts. This is a coverage diagnostic, not a truth or performance score.

## Example questions

- **What controls point size?** The retriever searches user instructions and,
  if indexed, reports UI action labels, callbacks, and setter references. It
  must not invent the on-screen location of the control.
- **How does library A connect to application B?** The retriever can show
  unique cross-repository include/reference edges and evidence from each side.
  It must not call the include evidence a runtime call chain.
- **What does a specific class do?** The retriever searches its definition,
  comments and referencing files. The model should separate confirmed behavior
  from interpretation and cite source files/lines.

## Commands

```bash
# Before model training; this downloads URLs but no LLM weights:
./start.command --sources-file sources.txt --model 2 --dry-run --yes

# A new local training run using those same sources:
./start.command --sources-file sources.txt --model 2 --mode standard --yes

# Already have a v0.3.x model? Enrich its index without changing GGUF weights:
./start.command upgrade-index runs/OLD_RUN/release

# Review grounded relationships:
./start.command inspect-symbol runs/NEW_RUN/release/knowledge.db _pointSizeAction
./start.command search runs/NEW_RUN/release/knowledge.db \
  "How does RendererApp depend on SharedLibrary?"
```

## What requires caution

- **Not a compiler:** Preprocessor macros, templates, overloaded method calls,
  generated source, plugins loaded dynamically, and indirect UI wiring can be
  misunderstood or missed. There is no automatic build/test of the sources.
- **Limited corpus:** Source caps and exclusions trade completeness for local
  resource use. Inspect the source list and counts to confirm coverage.
- **No fabricated UI operations:** A `DecimalAction` and `valueChanged` handler
  may prove a setting exists and changes a renderer value, but not which panel
  hosts it when the UI is constructed elsewhere or at runtime.
- **No autonomous truth checking:** Source snippets are evidence, not ground
  truth for user-facing behavior. Human-reviewed questions remain essential.
- **No guarantee from LoRA:** A short fine-tuning run can teach answer style and
  vocabulary, while detailed facts still require search and citations.
- **Historical releases:** Upgrading an older DB can only analyze snippets
  actually present in it. A fresh run may yield additional relations.

## Evaluation checklist

Before releasing the package, write at least 20 independent questions not
created from the same training excerpts. Include cross-repo dependencies, exact
class references, UI settings, missing/ambiguous information and ordinary
general knowledge. Verify source citations, answer correctness, uncertainty
handling, and qualitative difference against the unmodified base model.
Metrics such as training loss and source-hit@5 do **not** measure factual QA
accuracy. A high-recall lexical search can still yield an incorrect answer if
source linking or synthesis is wrong.
