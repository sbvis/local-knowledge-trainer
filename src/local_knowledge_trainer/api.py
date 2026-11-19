"""Reusable, dependency-light source preparation API.

This API can be used on Python 3.10+ without Apple Silicon or MLX for
source collection, deterministic training-data preparation and local search.
Fine-tuning uses MLX on Apple Silicon and PyTorch on other systems.
"""
from dataclasses import dataclass
from collections import Counter
from pathlib import Path
from typing import Optional, Sequence

from .common import dump_json
from .index import create_index, source_hit_rate
from .analysis import analyze_chunks, graph_summary
from .prepare import collect_chunks, generated_examples, load_curated, write_training_data
from .sources import Source, SourceFailure, acquire


@dataclass(frozen=True)
class PreparationResult:
    """Paths and provenance of a completed ingestion/index/data preparation run."""
    workspace: Path
    database: Path
    sources: tuple[Source, ...]
    indexed_chunks: int
    example_count: int
    data_summary: dict
    retrieval_diagnostic: dict
    failed_sources: tuple[SourceFailure, ...]
    analysis_summary: dict | None = None


def prepare_knowledge(
    source_inputs: Sequence[str],
    workspace: Path | str,
    *,
    curated_qa: Optional[Path | str] = None,
    source_cache: Optional[Path | str] = None,
    strict_sources: bool = False,
    download_timeout: int = 20,
    download_retries: int = 1,
    max_chunks: int = 12000,
    max_files_per_source: int = 2000,
) -> PreparationResult:
    """Prepare local source materials and training examples, without downloading any LLM.

    Inputs may be GitHub repository URLs, direct HTTPS document URLs, or local
    paths. Source retrieval needs network access for URLs; local paths do not.
    This function does not run training. It creates `data/train.jsonl`,
    `data/valid.jsonl`, `release/knowledge.db` and `evaluation.json`.

    Output is kept in `workspace`, which must be new to avoid accidental
    replacement of existing model training artifacts. When `source_cache` is
    specified, successful remote downloads are shared between runs. Failures
    are recorded but do not stop the build if any useful source remains; use
    `strict_sources=True` to abort on the first failure.
    """
    if not source_inputs:
        raise ValueError("At least one source URL or local path is required")
    workspace = Path(workspace).expanduser().resolve()
    if workspace.exists():
        raise FileExistsError(f"Workspace already exists: {workspace}")
    workspace.mkdir(parents=True)

    failures: list[SourceFailure] = []
    cache_root = Path(source_cache).expanduser().resolve() if source_cache else workspace / "sources"
    try:
        sources = acquire(list(dict.fromkeys(source_inputs)), cache_root,
                          failures=failures, strict=strict_sources,
                          timeout=download_timeout, retries=download_retries)
    finally:
        dump_json(workspace / "source_failures.json", {
            "requested": len(list(dict.fromkeys(source_inputs))),
            "failed": [failure.as_dict() for failure in failures],
        })
    if failures:
        print(f"\n  Source acquisition summary: {len(sources)} succeeded; "
              f"{len(failures)} skipped. Details: {workspace / 'source_failures.json'}", flush=True)
    if max_chunks < 0 or max_files_per_source < 0:
        raise ValueError("Source limits must be nonnegative; use 0 for unlimited")
    chunks = collect_chunks(sources, max_chunks=max_chunks, max_files_per_source=max_files_per_source)
    if not chunks:
        raise ValueError("No readable content found. Provide supported code, text or document files")

    release = workspace / "release"
    release.mkdir()
    database = release / "knowledge.db"
    dump_json(release / "source_failures.json", {
        "requested": len(list(dict.fromkeys(source_inputs))),
        "successful": len(sources),
        "failed": [failure.as_dict() for failure in failures],
    })
    facts = analyze_chunks(chunks)
    analysis_summary = graph_summary(facts)
    indexed = create_index(chunks, database, facts=facts)
    dump_json(release / 'analysis_summary.json', analysis_summary)
    print(f"  Source analysis: {analysis_summary['facts']} facts, "
          f"{analysis_summary['cross_repository_pairs']} cross-repository pairs, "
          f"{analysis_summary['ui_controls_with_labels']} labeled UI controls", flush=True)
    examples = generated_examples(chunks, facts=facts)
    if curated_qa:
        examples.extend(load_curated(Path(curated_qa).expanduser()))
    counts, validation = write_training_data(examples, workspace / "data")
    quality = dict(Counter(row.get('_evidence_type', 'general_document_or_safety')
                           for row in examples))
    retrieval_rows = [r for r in validation
                      if not r['_source'].startswith('curated::')
                      and (not r['_source'].startswith('relation::')
                           or r.get('_evidence_type') == 'static_ui')]
    retrieval = source_hit_rate(database, retrieval_rows, top_k=5)
    from .sft_quality import quality_metrics
    from .training_plan import make_training_plan
    quality_audit = quality_metrics(examples)
    quality_audit['planned_training_examples'] = counts['train_examples']
    quality_audit['planned_validation_examples'] = counts['validation_examples']
    # This is a plan only: the model is downloaded/trained by the CLI later.
    from .models import PRESETS
    planned = {str(i): make_training_plan(workspace / 'data', preset, 'standard').as_dict()
               for i, preset in enumerate(PRESETS, 1)}
    dump_json(workspace / 'training_quality.json', quality_audit)
    dump_json(workspace / 'training_plans.json', planned)
    dump_json(workspace / "evaluation.json", {
        "retrieval": retrieval,
        "explanation": "Source-hit@k measures retrieval of expected sources, NOT generated-answer accuracy.",
        "training": counts,
        "training_example_types": quality,
        "training_quality": quality_audit,
        "training_plans": planned,
        "static_analysis": analysis_summary,
        "limitations": ["Model quality has not been benchmarked on verified real user tasks.",
                        "Static source relationships are not verified user-interface behavior.",
                        "Automatically generated answers are extraction exercises, not independent ground truth."],
    })
    return PreparationResult(
        workspace=workspace,
        database=database,
        sources=tuple(sources),
        indexed_chunks=indexed,
        example_count=len(examples),
        data_summary=counts,
        retrieval_diagnostic=retrieval,
        failed_sources=tuple(failures),
        analysis_summary=analysis_summary,
    )
