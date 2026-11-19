"""Offline batch question runner for human review; does not invent accuracy scores."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from .demo import locate_llama_cli, locate_model, infer_command, _raw_completion, supported_llama_flags
from .index import search_evidence, is_ui_instruction_question
from .workflow_search import search_workflows
from .common import dump_json, now_utc


def load_cases(path: Path) -> list[dict]:
    cases = []
    with Path(path).open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            if not isinstance(row, dict) or not isinstance(row.get("question"), str) or not row["question"].strip():
                raise ValueError(f"Invalid question at {path}:{number}")
            if "reference" in row and not isinstance(row["reference"], str):
                raise ValueError(f"Invalid reference at {path}:{number}")
            cases.append({"question": row["question"], "reference": row.get("reference", "")})
    if not cases:
        raise ValueError("Question file is empty")
    return cases


def evaluate(release: Path, cases: Path, output: Path, *, cli_path: str | None = None,
             max_tokens: int = 256, limit: int = 50) -> list[dict]:
    """Save raw answers and context for reproducible manual correctness review."""
    if output.exists():
        raise FileExistsError(f"Output already exists: {output}")
    if not 1 <= max_tokens <= 2048 or not 1 <= limit <= 1000:
        raise ValueError("max_tokens must be 1..2048 and limit must be 1..1000")
    release = Path(release).expanduser().resolve()
    db = release / "knowledge.db"
    if not db.is_file():
        raise FileNotFoundError(f"Knowledge database missing: {db}")
    model, binary = locate_model(release), locate_llama_cli(release, cli_path)
    results = []
    for index, case in enumerate(load_cases(cases)[:limit], 1):
        user_help = is_ui_instruction_question(case["question"])
        if user_help:
            # Exact same task-oriented documents users see with `ask`. Build
            # model evaluation prompts from their published steps rather than
            # from unconnected code symbols or the old keyword-only snippets.
            workflows = search_workflows(db, case['question'], limit=4)
            hits = [
                {'source': flow.source, 'location': flow.location,
                 'content': '\n'.join((flow.title, *flow.details, *flow.steps))}
                for flow in workflows
            ]
            if not hits:
                hits = search_evidence(db, case['question'], limit=4, ui=True)
        else:
            hits = search_evidence(db, case['question'], limit=4, ui=False)
        if user_help and not hits:
            results.append({"question": case["question"], "reference": case["reference"],
                            "response": "Cannot verify the UI procedure from indexed user documentation.",
                            "sources": [], "human_review": None})
            continue
        command = infer_command(binary, model, case["question"], hits, max_tokens, user_help=user_help)
        completed = subprocess.run(command, text=True, capture_output=True, check=True)
        results.append({"question": case["question"], "reference": case["reference"],
                        "response": completed.stdout.strip(),
                        "note": "Raw model output; inspect for llama.cpp diagnostic lines and unsupported steps.",
                        "sources": [{"source": hit["source"], "location": hit["location"]} for hit in hits],
                        "human_review": None})
        print(f"[{index}] Answer saved: {case['question'][:70]}")
    dump_json(output, {
        "created_at_utc": now_utc(), "source_release": str(release),
        "model": str(model.name), "cases": results,
        "notice": "No automatic accuracy score: grade each answer manually for correctness, citations and abstention."
    })
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run an offline human-review QA benchmark")
    parser.add_argument("release", type=Path)
    parser.add_argument("cases", type=Path, help="JSONL with question and optional reference fields")
    parser.add_argument("output", type=Path, help="New JSON result file")
    parser.add_argument("--llama-cli", type=str)
    parser.add_argument("--max-tokens", type=int, default=256)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args(argv)
    try:
        results = evaluate(args.release, args.cases, args.output, cli_path=args.llama_cli,
                           max_tokens=args.max_tokens, limit=args.limit)
        print(f"Saved {len(results)} responses to {args.output}. Human verification is required.")
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
