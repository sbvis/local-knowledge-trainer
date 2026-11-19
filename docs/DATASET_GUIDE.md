> **v0.4.5 update:** The active end-user dataset builder now favors grounded
> tutorial workflows and retrieval-conditioned examples, not generic code symbol
> Q&A. See [Training-quality audit](TRAINING_QUALITY.md) for the current split
> and optimization rules. The sections below describe additional curated data.

# Data engineering and evaluation guide

## What can be learned?

LoRA can adapt answer style, system terminology and frequently repeated behavior, but it cannot guarantee perfect recall of hundreds of repositories. A standalone 4-bit GGUF file is not a reliable encyclopedia of arbitrary Git commits. Retrieval with `knowledge.db` is therefore essential.

### Automatically generated rows

The builder creates conservative question/answer pairs about document sections and C++ class/member locations using exact excerpts and symbol names. The generated rows are **not synthetic functional explanations** and should not be presented as such. They teach grounded answer phrasing and common vocabulary; quality depends heavily on documentation quality.

### Recommended expert dataset

For each supported task, supply several verified user-facing examples:

- Prerequisites and expected dataset type
- Step-by-step UI instructions from the current application version
- Relevant module and supported inputs
- Common failure modes and corrections
- C++ method names with citations only when verified
- Unanswerable/unsupported questions (model should acknowledge absence of evidence)

JSONL: one object per line, in the MLX conversational `messages` structure. The final message must be from `assistant`. Add this to the wizard as a curated QA file. An illustrative template is included in `examples/curated_qa.example.jsonl`; replace it with your actual verified answers.

### Validation

The generated rows are split by **source file/group** between training and validation. This reduces, but cannot eliminate, overlap: two files may reproduce the same text. Manually curated rows have independent groups.

`evaluation.json` reports the number of rows and `source_hit_at_k`, which tests whether the **expected repository and source file** was found in FTS5 top-k results for held-out generated questions. This is a retrieval diagnostic only. There are no unearned model accuracy percentages in the output.

**For a credible portfolio:** manually construct 30–50 end-user questions with expected source references, reserve them *entirely* from training, test baseline and fine-tuned models with identical context/retrieval and decoding settings, and publish example outcomes plus failures. Include function-level and workflow questions, multi-file cases and unknown-answer checks. Report exact machine specs, model revisions and token budgets.

### Privacy and security

Source files can contain secrets; upload neither datasets nor checkpoints. A trained model may reveal memorized content. See [SECURITY.md](SECURITY.md). Publish only models and databases whose source licenses and confidentiality permit it.

### Large source lists

Use `--sources-file` or the guided file prompt to import repository and document paths from a UTF-8 text file (one per line). This is separate from the curated Q&A JSONL file: a source list specifies *what to read*, while Q&A examples specify *what to teach the model*. Paths that are relative to a list file resolve against the list file's parent directory.
