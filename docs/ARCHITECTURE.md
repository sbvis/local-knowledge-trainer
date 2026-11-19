# Architecture and design decisions

## Pipeline

1. **Acquisition:** Accept local paths, GitHub repository homepages and direct HTTPS document URLs. Clone GitHub repositories at a recorded commit. Do not execute downloaded code. Cache successful acquisitions between runs and skip/report individual failures by default; strict mode aborts on any failure.
2. **Extraction:** Parse supported plain text, programming files, HTML, DOCX and PDF text, with file-size limits and exclusion of build/vendor directories.
3. **Indexing and relationship extraction:** Round-robin bounded source chunks across repositories in SQLite FTS5; derive source-observed class/include and Qt control/connection facts into a backward-compatible SQLite table. No embedding model or external inference dependency.
4. **Instruction data:** Create source-evidence examples for documented text, observable Qt UI controls and uniquely resolved cross-repo relationships; use careful uncertainty wording. Allow manually reviewed user Q&A to teach behavior and workflow knowledge. Split examples by source group to reduce train/validation leakage.
5. **Fine-tuning:** Select a model preset and either MLX LoRA (Apple Silicon) or PyTorch/PEFT LoRA (CUDA or CPU). The base model remains available in its pretrained state outside the release.
6. **Export:** Merge the adapter into the base weights, convert Hugging Face-compatible weights to FP16 GGUF with llama.cpp, then quantize to Q4_K_M and run a GGUF-load smoke test.
7. **Packaging:** Copy the SQLite index, provenance, manifest and checksums. Optionally tensor-shard the GGUF and test loading the first shard.
8. **Answering:** Retrieve relevant excerpts, UI documentation and source relationship facts (including uniquely resolved target snippets), build a bounded prompt with file citations and confidence limits, and generate locally with llama.cpp. The terminal chat is stateless and starts a new CLI process per question.
9. **Evaluation:** Run offline held-out question cases to produce source-cited answers for independent human grading; do not label loss or lexical retrieval scores as factual accuracy.

## Why hybrid fine-tuning + source search?

Fine-tuning is valuable for learning style, terminology and recurring tasks. It does **not** provide robust line-perfect factual recall from dozens of changing repositories. A small lexical SQLite index is easy to deploy and provides traceable factual context, although it struggles with synonyms, semantic matching and complex cross-file relationships. Future enhancements might add semantic retrieval and symbol-aware parsing as optional features without affecting the portable release contract.

## Portability

The data-preparation API and index/query path use Python's standard library except for PDF text extraction (`pypdf`). Training backends are imported only on demand; they are not a runtime dependency of exported models. Compilation of llama.cpp uses platform-specific CMake configurations and a local C++ compiler. Windows, macOS and Linux produce the same GGUF/SQLite format.

## Current limits

- The relationship table is a conservative source-level graph, **not** a complete compiler-verified semantic or call graph; macros, templates and runtime plugin wiring remain hard.
- Automatic instruction generation extracts and links evidence but cannot verify every end-user workflow or on-screen UI position.
- Training is not a model knowledge memorization guarantee; always evaluate with independent, human-reviewed questions.
- Direct links to JavaScript-rendered web apps and scanned PDFs are not crawled/OCR'd.
- The build process accesses external URLs to acquire sources, models and tools; release inference does not.
- OS/platform compatibility tests cannot substitute for successful device-specific model export and human QA evaluation.
