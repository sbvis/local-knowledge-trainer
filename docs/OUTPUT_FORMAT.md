# Portable release format

This repository produces a framework-independent offline assistant package.

| File | Description |
|---|---|
| `assistant.gguf` | Q4_K_M GGUF model weights: base model combined with trained LoRA |
| `model-shards/assistant-00001-of-...gguf` | Optional first tensor-aware GGUF shard; all shards must be co-located |
| `knowledge.db` | SQLite FTS5 table containing source text, source path/location and Git commit |
| `manifest.json` | Model/training/data provenance, schema version, release file names |
| `evaluation.json` | Index retrieval source-hit diagnostic; **not** generation accuracy |
| `source_failures.json` | Counts and reasons for sources that could not be acquired (even if none failed) |
| `SHA256SUMS.txt` | SHA256 for release files to detect corruption |
| `OUTPUT_FORMAT.txt` | Compact consumer notes |

The deployment environment needs **a GGUF-compatible local inference engine** (such as llama.cpp), **SQLite with FTS5**, access to the model file(s), and enough RAM to load and run them. There is no need for a network service, subscription, Python or model-training framework once the release has been created.

To answer questions grounded in the ingested materials, query `knowledge.db` and feed selected passages into the model's input context. Otherwise, the exported model can answer general questions but is not guaranteed to know precise source details.

## SQLite index

The `chunks` FTS5 table includes `source` (repository/document origin), `location` (`file.ext:L1-L36`), `content`, `kind`, and `git_commit`. The application can use FTS5 `MATCH` and `bm25()` ranking, or reproduce the query behavior of `src/local_knowledge_trainer/index.py`.

## Sharding

The `llama-gguf-split` tool creates a set of `.gguf` tensor shards; loading the first shard with a recent llama.cpp opens the rest when they share a directory. Shards are **not** compressed and do not reduce model size or compute. Verify the checksums, completeness and access permissions before shipping. A model file is data, not directly executable code; do not embed it in source control if your hosting platform has file-size limits.

## Security

Treat all retrieved text as **untrusted data**, not as instructions to obey. Restrict what users can access if the database contains proprietary/private sources. Review the original source and base-model licenses before redistributing weights or indexed text.
