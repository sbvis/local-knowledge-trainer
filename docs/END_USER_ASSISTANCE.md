# End-user assistance and evidence quality

This project targets people who want to operate an existing application: what
can it do, which features to choose, where to find controls, and what happens
when they change a setting. An implementation question is a different task.

## How a navigation question is answered

- The CLI classifies explicitly user-facing operational questions.
- It first checks documentation for relevant, actionable lines.
- If documentation lacks a procedure, it checks statically observed GUI labels,
  tooltips and registrations in the SQLite `facts` table.
- If the code explicitly registers one labeled action with another labeled
  group in the same file, that grouping can be reported, with provenance.
- It never treats a renderer setter as evidence for the location of a UI
  slider, nor creates new source code for someone asking how to use software.
- If neither documentation nor a matching control exists, it reports that
  the procedure is unverified.

This is a deliberate deterministic protection for small models. Source-anchored
navigation is more useful than hallucinated instructions, but it is not a
substitute for verifying a real application session.

## Knowledge extraction and fine-tuning

`generated_examples(..., audience="end_user")` is the default and avoids
training on low-value C++ symbol-occurrence answers. The **developer** audience
is still accessible through the Python API for users who want a coding model.
LoRA training is not a guarantee of memorizing repositories or producing
accurate UX instructions. Existing models do not need retraining to benefit
from the new end-user question route.

## How to validate before distribution

Create a separate benchmark with at least 20 end-user tasks. Each task should
have the correct UI actions, applicable version and workspace configuration,
and a supporting source or screenshot. Check whether the answer is correct,
whether a visible UI control is actionable, and whether any invented steps are
introduced. Keep a baseline model and index, and report accuracy separately
for documented tasks, code-inferred controls, and unanswerable questions.

## Known limitations

C++/Qt source analysis here is a conservative pattern matcher, not a compiler,
UI automation agent, or runtime inspector. Actions may be conditionally hidden,
renamed, placed in more than one context, or controlled by runtime layout.
The current path will accurately describe a source-level label while sometimes
being unable to say precisely which panel or toolbar shows it. Do not turn that
uncertainty into a fabricated click path.

## Complete workflows in v0.4.4

`workflow_search.search_workflows` reconstructs lines from overlapping indexed
Markdown/text chunks before looking for documented steps. It ranks **complete,
compact task passages**, with topic words occurring in a heading or sentence,
instead of matching incidental words in separate source snippets. It accepts
steps introduced by a panel phrase ("In the gene table, select ...") and
normalizes variants such as "celltypes". Plain HTML tags and Jekyll decorations
are removed from displayed instructions. A source location accompanies each
answer.

The included EvoViewer guide is a checked, compact transcription of a *published*
user tutorial, not a set of automatically inferred actions from C++. For an
existing model package, add it once via `add-guide` and ask again. When the
code is the only available evidence, the reply describes a control with the
exact available label, but does not invent its on-screen position.

Tests include exact user-reported questions (marker genes, abundance, point
opacity and cell-type selection). They verify the Python answer system, not
actual interactive clicking in ManiVault or GGUF fine-tuning quality.
