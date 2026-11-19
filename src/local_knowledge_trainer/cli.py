"""Local-first training wizard and independent offline model utilities."""
import argparse
import json
import os
import sqlite3
from contextlib import closing
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

from . import __version__
from .common import dump_json, info, now_utc, sha256_file
from .models import PRESETS
from .sources import classify
from .api import prepare_knowledge
from .sharding import shard_model, shard_metadata, discover_shards, merge_model, parse_shard_size

REPO_ROOT = Path(__file__).resolve().parents[2]


def _prompt(message, default=""):
    answer = input(message).strip()
    return answer or default


def _model_choice():
    print("\nChoose your base model (automatic free download):")
    for n, preset in enumerate(PRESETS, 1):
        print(f"  [{n}] {preset.title:19s} | {preset.size:4s} | {preset.description}")
    while True:
        response = _prompt("Model [1]: ", "1")
        if response.isdigit() and 1 <= int(response) <= len(PRESETS):
            return PRESETS[int(response) - 1]
        print("Select an option from the menu.")


def load_sources_file(file_path: str | Path) -> list[str]:
    """Read a UTF-8 list of URL/local sources; relative paths are file-relative.

    Blank lines and full-line # comments are ignored. This is intentionally
    distinct from a document .txt source, which can still be supplied normally.
    """
    path = Path(file_path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Source list file not found: {path}")
    entries: list[str] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        try:
            kind = classify(value)
            if kind == "local":
                local_path = Path(value).expanduser()
                value = str((path.parent / local_path).resolve()) if not local_path.is_absolute() else str(local_path)
            entries.append(value)
        except ValueError as exc:
            raise ValueError(f"Invalid source at {path}:{number}: {exc}") from exc
    if not entries:
        raise ValueError(f"No sources listed in {path}. Add one URL or local path per line.")
    return list(dict.fromkeys(entries))


def _source_entries():
    print("\nProvide GitHub repository URLs, document URLs, or local files/folders.")
    print("You can load them all from a UTF-8 .txt file (one source per line).")
    while True:
        path = _prompt("Source list file (blank to skip): ")
        try:
            entries = load_sources_file(path) if path else []
        except (OSError, ValueError, UnicodeError) as exc:
            print(f"  Unable to read source list: {exc}")
            continue
        break
    if entries:
        print(f"  Loaded {len(entries)} source(s) from {path}.")
    print("Optionally paste extra URLs/paths, one per line. Blank finishes.")
    while True:
        value = _prompt("Source URL/path (blank = done): ")
        if not value:
            if entries:
                return list(dict.fromkeys(entries))
            print("Please supply at least one source or a source list file.")
            continue
        try:
            classify(value)
        except ValueError as exc:
            print(f"  Invalid source: {exc}")
            continue
        entries.append(value)


def _ram_gb():
    if platform.system() != "Darwin":
        return None
    try:
        data = subprocess.check_output(["sysctl", "-n", "hw.memsize"], text=True)
        return round(int(data.strip()) / 1024**3)
    except (OSError, subprocess.SubprocessError, ValueError):
        return None


def select_backend(selected: str = "auto") -> str:
    """Native MLX for Apple Silicon; otherwise portable PyTorch LoRA."""
    if selected not in {"auto", "mlx", "torch"}:
        raise ValueError("Training backend must be auto, mlx or torch")
    backend = ("mlx" if platform.system() == "Darwin" and platform.machine() == "arm64"
               else "torch") if selected == "auto" else selected
    if backend == "mlx" and not (platform.system() == "Darwin" and platform.machine() == "arm64"):
        raise RuntimeError("MLX training runs on Apple Silicon only. Select --backend torch.")
    return backend


def _preflight(dry_run, backend="auto"):
    select_backend(backend)
    if sys.version_info < (3, 10):
        raise RuntimeError("Python 3.10 or newer required")
    if not shutil.which("git"):
        raise RuntimeError("Git is required for repository sources and converter checkout")
    if not dry_run and not shutil.which("cmake"):
        raise RuntimeError("CMake required for GGUF conversion (install CMake or use bootstrap.py)")


def build(args):
    backend = select_backend(getattr(args, "backend", "auto"))
    _preflight(args.dry_run, backend)
    print("\n" + "═" * 60)
    print(" LOCAL KNOWLEDGE TRAINER  •  portable model builder")
    print(f" Training backend: {backend}")
    print("═" * 60)
    ram = _ram_gb()
    if ram:
        print(f"Detected: {ram} GB unified memory")
    model = PRESETS[args.model - 1] if args.model else _model_choice()
    if model.size == "1.5B" and ram is not None and ram <= 8:
        print("WARNING: 1.5B fine-tuning/merging may run out of memory on an 8 GB Mac.")
        print("Consider Coder Mini instead.")
    entries = []
    for path in (getattr(args, "sources_file", None) or []):
        entries.extend(load_sources_file(path))
    entries.extend(args.sources or [])
    entries = list(dict.fromkeys(entries))
    if not entries:
        if args.yes:
            raise ValueError("Supply --sources-file PATH or at least one --source when using --yes")
        entries = _source_entries()
    curated = args.qa if args.qa is not None else ("" if args.yes else _prompt(
        "Optional curated Q&A JSONL path (blank to skip): "))
    if curated and curated.startswith("https://"):
        # Treat a document link pasted into the Q&A prompt as a source,
        # rather than aborting after the user entered many repositories.
        if args.qa is not None:
            raise ValueError("--qa expects a local .jsonl file; pass document URLs as --source")
        classify(curated)
        print("  This is a source URL, not a curated Q&A JSONL file. Adding it to sources.")
        entries = list(dict.fromkeys([*entries, curated]))
        curated = ""
    if curated and not Path(curated).expanduser().is_file():
        raise FileNotFoundError(f"Curated Q&A file not found: {curated}. Use this field for a local JSONL file only; supply document URLs as sources.")
    mode = args.mode or ("quick" if args.yes else _prompt("Training [quick/standard] (default quick): ", "quick").lower())
    if mode not in {"quick", "standard"}:
        raise ValueError("Training mode must be quick or standard")
    if not args.yes:
        print(f"\nSelected model: {model.title}\nSources: {len(entries)}\nMode: {mode}")
        if _prompt("Proceed? [y/N]: ").lower() not in {"y", "yes"}:
            print("Cancelled")
            return

    from datetime import datetime, timezone
    run_id = args.run_name or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")[:22]
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", run_id):
        raise ValueError("Run name may only contain letters, numbers, _ and -")
    workspace = (Path(args.output).expanduser() / run_id).resolve()
    if workspace.exists():
        raise FileExistsError(f"Run directory already exists: {workspace}. Use another --run-name.")
    info("Collecting sources and preparing local knowledge index")
    cache_root = (Path(args.output).expanduser().resolve() / ".source-cache"
                  if not getattr(args, "no_source_cache", False) else None)
    prepared = prepare_knowledge(
        entries, workspace, curated_qa=curated, source_cache=cache_root,
        strict_sources=getattr(args, "strict_sources", False),
        download_timeout=getattr(args, "download_timeout", 20),
        download_retries=getattr(args, "download_retries", 1),
        max_chunks=getattr(args, "max_chunks", 12000),
        max_files_per_source=getattr(args, "max_files_per_source", 2000),
    )
    release = workspace / "release"
    sources = prepared.sources
    indexed = prepared.indexed_chunks
    counts = prepared.data_summary
    retrieval = prepared.retrieval_diagnostic
    if prepared.failed_sources:
        print(f"  WARNING: {len(prepared.failed_sources)} source(s) skipped. "
              f"See {release / 'source_failures.json'}")
    if prepared.example_count < 10 and not args.dry_run:
        raise RuntimeError(f"Only {prepared.example_count} training examples found; add documents or verified Q&A (minimum 10).")
    info(f"Dataset: {counts['train_examples']} training, {counts['validation_examples']} validation examples")
    # A generated-example count is not an accuracy score. Surface the number
    # of actual documented workflows before expensive model training.
    quality = json.loads((workspace / "evaluation.json").read_text(encoding="utf-8")).get(
        "training_example_types", {})
    audit = json.loads((workspace / 'training_quality.json').read_text(encoding='utf-8'))
    print(f"  Unique documented workflows: {audit.get('unique_workflows', 0)}; "
          f"workflow Q&A examples: {quality.get('documented_workflow', 0)}; "
          f"static UI examples: {quality.get('static_ui', 0)}")
    print(f"  Retrieval-conditioned training examples: "
          f"{audit.get('retrieval_conditioned_count', 0)}")
    if audit.get('known_bad_phrases', 0):
        raise RuntimeError('Training examples contain known bad code-relation wording. '
                           'Inspect training_quality.json before proceeding.')
    if audit.get('unique_workflows', 0) < 10:
        print("  WARNING: Very few documented user workflows. Model training loss does "
              "not establish navigation accuracy; add more user guides or curated task Q&A.")
    if model.size == "0.5B":
        print("  Note: 0.5B is a lightweight model with limited cross-repository reasoning. "
              "Choose model size for the memory and compute available on the target system; verify resource use before deployment.")
    from .training_plan import make_training_plan
    plan = make_training_plan(workspace / 'data', model, mode,
                              backend=backend)
    print(f"  Training budget: {plan.iterations} updates, approximately "
          f"{plan.effective_passes} dataset passes (instead of fixed 100 steps)")
    if plan.effective_passes < plan.target_passes - 0.1:
        print('  Note: The 1800-update safety cap limits passes over this large dataset.')
    print(f"  Retrieval source-hit@5 on held-out generated examples: {retrieval['source_hit_at_k']}")
    if retrieval.get('tested', 0) and (retrieval.get('source_hit_at_k') or 0) < 0.3:
        print('  WARNING: Retrieval diagnostic is weak; answers may miss their sources. '
              'Inspect evaluation.json before relying on the release.')
    if prepared.example_count < 50:
        print("  Caution: Few examples. A trained model may show little improvement; add curated Q&A.")
    if args.dry_run:
        print(f"\nDry run complete. Data/index: {workspace}")
        return

    state = {
        "preset_id": PRESETS.index(model) + 1,
        "backend": backend,
        "steps": None,
        "training_mode": mode,
        "model_revision": "unrecorded",
        "source_provenance": [{"origin": s.origin, "kind": s.kind, "commit": s.commit} for s in sources],
        "indexed": indexed,
        "counts": counts,
        "retrieval": retrieval,
    }
    dump_json(workspace / "build_state.json", state)
    from .training import download_model, fuse, train
    model_path = download_model(model, backend)
    state["model_revision"] = model_path.name if model_path.parent.name == "snapshots" else "unrecorded"
    dump_json(workspace / "build_state.json", state)
    adapters = workspace / "adapters"
    fused = workspace / "fused"
    if backend == "mlx":
        steps = train(str(model_path), str(workspace / "data"), str(adapters), model, mode)
        state["steps"] = steps
        dump_json(workspace / "build_state.json", state)
        fuse(str(model_path), str(adapters), str(fused))
    else:
        from .torch_backend import train_torch, fuse_torch
        steps = train_torch(str(model_path), str(workspace / "data"), str(adapters), model, mode)
        state["steps"] = steps
        dump_json(workspace / "build_state.json", state)
        fuse_torch(str(model_path), str(adapters), str(fused))
    finalize_release(workspace, model, backend, steps, state["model_revision"],
                     state["source_provenance"], indexed, counts, retrieval,
                     shard_size=args.shard_size, shards_only=args.shards_only)


def finalize_release(workspace, model, backend, steps, model_revision,
                     source_provenance, indexed, counts, retrieval,
                     shard_size=None, shards_only=False):
    """Export/package previously trained and fused weights; never retrain or re-clone."""
    from .training import export_gguf, prepare_llama_cpp, llama_cpp_root
    from .common import run
    workspace = Path(workspace).resolve()
    release = workspace / "release"
    release.mkdir(exist_ok=True)
    gguf = export_gguf(str(workspace / "fused"), workspace / "tools", release)
    gguf_shards = []
    if shard_size:
        _, _, local_cli, splitter = prepare_llama_cpp(workspace / "tools")
        gguf_shards = shard_model(gguf, splitter, release / "model-shards", shard_size)
        # All shards must be colocated. Test first shard with the same inference engine.
        run([local_cli, "--model", gguf_shards[0], "--prompt", "Hello",
             "--n-predict", "8", "--single-turn", "--offline"])
        if shards_only:
            gguf.unlink()  # Delete only AFTER successfully loading the shard set.
    shutil.copy2(workspace / "evaluation.json", release / "evaluation.json")
    info("Writing portable release manifest")
    from importlib.metadata import version as installed_version
    llama_checkout = llama_cpp_root(workspace / 'tools')
    llama_revision = subprocess.check_output(
        ["git", "-C", str(llama_checkout), "rev-parse", "HEAD"], text=True).strip()
    manifest = {
        "schema_version": 1,
        "builder_version": __version__,
        "built_at_utc": now_utc(),
        "base_model": model.mlx_repo if backend == "mlx" else model.hf_repo,
        "base_model_snapshot": model_revision,
        "training_backend": backend,
        "training_framework_version": installed_version("mlx-lm" if backend == "mlx" else "torch"),
        "llama_cpp_commit": llama_revision,
        "model_size": model.size,
        "fine_tuning": {"method": "LoRA", "iterations": steps, "precision": "4-bit MLX base" if backend == "mlx" else "PyTorch fp32/fp16/bf16 LoRA", "output_quantization": "Q4_K_M"},
        "knowledge_index": {"filename": "knowledge.db", "engine": "SQLite FTS5 + optional source relationship tables", "chunk_count": indexed},
        "source_provenance": source_provenance,
        "data_summary": counts,
        "retrieval_validation": retrieval,
        "files": {"model": "model-shards/" + gguf_shards[0].name if shards_only
                  else "assistant.gguf", "knowledge": "knowledge.db"},
        "shards": shard_metadata(gguf_shards, release) if gguf_shards else [],
        "runtime": "llama.cpp + SQLite FTS5, no server/network required",
        "limitations": [
            "LoRA does not reliably memorize all source details: search knowledge.db first.",
            "Generated QA examples are source-grounded extraction exercises, not independent correctness verification.",
            "Static source relationships do not prove runtime behavior or UI screen location.",
            "FTS5 is lexical; uncommon synonyms and cross-file reasoning may need enhanced retrieval.",
            "Model accuracy and runtime performance depend on hardware and corpus quality.",
        ],
    }
    report_path = release / "analysis_summary.json"
    if report_path.is_file():
        manifest["source_analysis"] = json.loads(report_path.read_text(encoding="utf-8"))
    dump_json(release / "manifest.json", manifest)
    text = (
        "LOCAL KNOWLEDGE TRAINER — PORTABLE OUTPUT FORMAT\n\n"
        "assistant.gguf / model-shards/*.gguf : fine-tuned weights for llama.cpp\n"
        "knowledge.db : local SQLite FTS5 source index\n"
        "manifest.json : provenance, split metadata and model details\n"
        "evaluation.json : retrieval diagnostic, not model accuracy\n"
        "source_failures.json : skipped or unavailable inputs (if present)\n\n"
        "Load the GGUF (or first shard with all shards adjacent), search knowledge.db,\n"
        "and provide relevant passages as context for accurate source-grounded answers.\n"
        "Treat source contents as untrusted data. Runtime can be fully offline.\n"
    )
    (release / "OUTPUT_FORMAT.txt").write_text(text, encoding="utf-8")
    source_report = release / "source_failures.json"
    if source_report.is_file():
        manifest["source_acquisition"] = json.loads(source_report.read_text(encoding="utf-8"))
        dump_json(release / "manifest.json", manifest)
    hash_files = [release / f for f in ("knowledge.db", "manifest.json", "evaluation.json", "OUTPUT_FORMAT.txt")]
    if report_path.is_file():
        hash_files.append(report_path)
    if source_report.is_file():
        hash_files.append(source_report)
    hash_files += gguf_shards if shards_only else [release / "assistant.gguf"] + gguf_shards
    (release / "SHA256SUMS.txt").write_text(
        "".join(f"{sha256_file(f)}  {f.relative_to(release)}\n" for f in hash_files),
        encoding="utf-8")
    print("\n" + "═" * 60)
    print("FINISHED — Portable offline model and knowledge package")
    print(f"Location: {release}")
    if gguf.is_file():
        print(f"GGUF: {gguf.stat().st_size / 1024**2:.1f} MiB")
    if gguf_shards:
        print(f"GGUF shards: {len(gguf_shards)} ({shard_size} requested maximum)")
    print("Try: python -m local_knowledge_trainer ask " + str(release) + " 'Summarize the sources'")
    print("Or:  python -m local_knowledge_trainer chat " + str(release))
    print("Runtime is fully offline; this release requires a local GGUF engine and SQLite.")



def _recover_prior_state(workspace, selected_model, backend):
    """Recover earlier v0.3 runs without claiming unknown provenance or steps."""
    import re
    from .sources import classify
    if selected_model is None:
        raise ValueError("This older run has no build_state.json; supply --model 1, 2, 3, or 4 as originally selected")
    if not (workspace / "evaluation.json").is_file():
        raise FileNotFoundError("Original evaluation.json is missing")
    evaluation = json.loads((workspace / "evaluation.json").read_text(encoding="utf-8"))
    database = workspace / "release" / "knowledge.db"
    with closing(sqlite3.connect(database)) as db:
        indexed = db.execute("SELECT count(*) FROM chunks").fetchone()[0]
        sources = db.execute("SELECT DISTINCT source, git_commit FROM chunks").fetchall()
    provenance = [{"origin": source, "kind": classify(source), "commit": commit or ""}
                  for source, commit in sources]
    # Old MLX run checkpoints record iteration counts in their filenames.
    checkpoints = [int(m.group(1)) for path in (workspace / "adapters").glob("*_adapters.safetensors")
                   if (m := re.search(r"([0-9]+)_adapters\.safetensors$", path.name))]
    return {
        "preset_id": selected_model, "backend": backend,
        "steps": max(checkpoints) if checkpoints else None,
        "model_revision": "unrecorded (legacy run)",
        "source_provenance": provenance, "indexed": indexed,
        "counts": evaluation.get("training", {}),
        "retrieval": evaluation.get("retrieval", {}),
    }


def resume(args):
    """Continue from an existing run without re-cloning or rebuilding its index.

    Fused weights -> export only (original behavior).
    Prepared data -> train/fuse/export (if the training environment is healthy).
    """
    workspace = args.workspace.expanduser().resolve()
    if not workspace.is_dir():
        raise FileNotFoundError(f"Run directory does not exist: {workspace}")
    if not (workspace / "release" / "knowledge.db").is_file():
        raise FileNotFoundError("Knowledge database missing; cannot continue this run")
    state_path = workspace / "build_state.json"
    if state_path.is_file():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        if args.model is not None and args.model != state["preset_id"]:
            raise ValueError("--model conflicts with the model recorded in this run")
    else:
        inferred_backend = ("mlx" if platform.system() == "Darwin" and platform.machine() == "arm64"
                            else "torch") if args.backend == "auto" else args.backend
        state = _recover_prior_state(workspace, args.model, inferred_backend)
        info("Recovering an older run. Some training metadata was not recorded")
    if args.shards_only and not args.shard_size:
        raise ValueError("--shards-only requires --shard-size")
    preset = PRESETS[state["preset_id"] - 1]
    backend = state["backend"]
    fused = workspace / "fused"
    if not any(fused.glob("*.safetensors")):
        if not (workspace / "data" / "train.jsonl").is_file():
            raise FileNotFoundError("Neither fused weights nor prepared training data exist")
        mode = args.mode or state.get("training_mode")
        if mode not in {"quick", "standard"}:
            raise ValueError("Training mode was not recorded in this older run. "
                             "Specify --mode quick or --mode standard (original choice).")
        from .training import download_model, train, fuse
        model_path = download_model(preset, backend)
        adapters = workspace / "adapters"
        if state.get("steps") is None:
            info(f"Resuming training from prepared data: {workspace} (no repository downloads)")
            if backend == "mlx":
                steps = train(str(model_path), str(workspace / "data"), str(adapters), preset, mode)
            else:
                from .torch_backend import train_torch
                steps = train_torch(str(model_path), str(workspace / "data"), str(adapters), preset, mode)
            state["steps"] = steps
            state["training_mode"] = mode
            dump_json(state_path, state)
        else:
            info("Training already finished; merging the saved LoRA adapter")
        if backend == "mlx":
            fuse(str(model_path), str(adapters), str(fused))
        else:
            from .torch_backend import fuse_torch
            fuse_torch(str(model_path), str(adapters), str(fused))
    else:
        info(f"Resuming export only: {workspace} (no training or source downloads)")
    finalize_release(workspace, preset, backend, state["steps"], state["model_revision"],
                     state["source_provenance"], state["indexed"], state["counts"],
                     state["retrieval"], shard_size=args.shard_size,
                     shards_only=args.shards_only)


def main():
    os.environ['PYTHONUTF8'] = '1'
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    if len(sys.argv) == 2 and sys.argv[1] == '--version':
        from . import __version__
        print(f"Local Knowledge Trainer v{__version__}\nRunning from: {Path(__file__).resolve().parents[2]}")
        return
    # Subcommands stay optional to preserve the simple no-arguments wizard.
    if len(sys.argv) > 1 and sys.argv[1] == 'inspect-training':
        parser = argparse.ArgumentParser(description='Audit an already prepared run before training')
        parser.add_argument('workspace', type=Path)
        parser.add_argument('--model', type=int, choices=range(1, len(PRESETS) + 1), default=2)
        parser.add_argument('--mode', choices=['quick', 'standard'], default='standard')
        parser.add_argument('--backend', choices=['auto', 'mlx', 'torch'], default='auto')
        opts = parser.parse_args(sys.argv[2:])
        root = opts.workspace.expanduser().resolve()
        from .training_plan import make_training_plan
        quality_path = root / 'training_quality.json'
        if not quality_path.is_file():
            parser.exit(1, f'Missing {quality_path}. Prepare a run using v0.4.5 first.\n')
        report = json.loads(quality_path.read_text(encoding='utf-8'))
        counts = report.get('example_types', {})
        backend = select_backend(opts.backend)
        plan = make_training_plan(root / 'data', PRESETS[opts.model - 1], opts.mode, backend=backend)
        print(f'Run: {root}\nUnique documented workflows: {report.get("unique_workflows", 0)}')
        print(f'Training example types: {counts}')
        print(f'Retrieval-conditioned examples: {report.get("retrieval_conditioned_count", 0)}')
        print(f'Known bad example phrases: {report.get("known_bad_phrases", 0)}')
        print(f'Plan: model {opts.model}, {opts.mode}, {plan.iterations} {backend} updates '
              f'(~{plan.effective_passes} sample passes)')
        if report.get('unique_workflows', 0) < 10:
            print('WARNING: Too few verified workflows to expect broad GUI expertise.')
        if report.get('known_bad_phrases', 0):
            raise SystemExit(2)
        return
    if len(sys.argv) > 1 and sys.argv[1] == "resume":
        parser = argparse.ArgumentParser(description="Continue an interrupted training or export run using prepared data")
        parser.add_argument("workspace", type=Path, help="Existing runs/<run-id> directory")
        parser.add_argument("--model", type=int, choices=range(1, len(PRESETS) + 1),
                            help="Original model choice (required for runs created before v0.3.1)")
        parser.add_argument("--backend", choices=["auto", "mlx", "torch"], default="auto")
        parser.add_argument("--mode", choices=["quick", "standard"], help="Required for old interrupted runs without a recorded training mode")
        parser.add_argument("--shard-size", type=parse_shard_size)
        parser.add_argument("--shards-only", action="store_true")
        opts = parser.parse_args(sys.argv[2:])
        try:
            resume(opts)
        except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
            parser.exit(1, f"Resume failed (existing training files preserved): {exc}\n")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "upgrade-index":
        from .upgrade_index import upgrade_release
        parser = argparse.ArgumentParser(description="Add cross-repository relationships to an existing release without retraining")
        parser.add_argument("release", type=Path)
        opts = parser.parse_args(sys.argv[2:])
        try:
            report = upgrade_release(opts.release)
            print(f"Graph indexed: {report['facts']} facts across {report['cross_repository_pairs']} repository pairs. "
                  f"GGUF unchanged. A backup is saved as knowledge.pre-graph.db.")
        except (OSError, ValueError, sqlite3.DatabaseError) as exc:
            parser.exit(1, f"Upgrade failed (existing files preserved): {exc}\n")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "inspect-symbol":
        from .index import related_facts
        parser = argparse.ArgumentParser(description="Inspect grounded source/Qt relationships for an exact symbol")
        parser.add_argument("db", type=Path)
        parser.add_argument("symbol")
        opts = parser.parse_args(sys.argv[2:])
        for fact in related_facts(opts.db, opts.symbol):
            print(f"{fact['source']} :: {fact['location']}: "
                  f"{fact['subject']} [{fact['predicate']}] {fact['object']}")
            if fact['target_source']:
                print(f"  -> {fact['target_source']} :: {fact['target_location']}")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "add-guide":
        from .guides import add_guide
        parser = argparse.ArgumentParser(
            description="Add verified UI guide text to an existing knowledge package without retraining")
        parser.add_argument("release", type=Path)
        parser.add_argument("guide", type=Path, help="Local .md, .txt, .rst or .html user guide")
        parser.add_argument("--source", help="Optional source identifier, e.g. original GitHub repository URL")
        opts = parser.parse_args(sys.argv[2:])
        try:
            count = add_guide(opts.release, opts.guide, opts.source)
            print(f"Indexed {count} guide excerpts. Model weights unchanged; ask/chat can use them now.")
        except (OSError, ValueError, sqlite3.DatabaseError) as exc:
            parser.exit(1, f"Unable to add guide: {exc}\n")
        return
    if len(sys.argv) > 1 and sys.argv[1] == "evaluate-ui":
        from .ui_benchmark import main as benchmark_main
        raise SystemExit(benchmark_main(sys.argv[2:]))
    if len(sys.argv) > 1 and sys.argv[1] == "evaluate":
        from .evaluate import main as evaluation_main
        evaluation_main(sys.argv[2:])
        return
    if len(sys.argv) > 1 and sys.argv[1] in {"ask", "chat", "ask-model"}:
        from .demo import main as chat_main
        cmd = sys.argv[1]
        rest = sys.argv[2:]
        if cmd == "chat":
            if any(not flag.startswith("-") for flag in rest[1:2]):
                raise SystemExit("Usage: knowledge-trainer chat RELEASE [--llama-cli PATH]")
            chat_main(rest)
        else:
            chat_main(rest, force_model_ui=(cmd == 'ask-model'))
        return
    if len(sys.argv) > 1 and sys.argv[1] == "search":
        from .search_knowledge import main as search_main
        sys.argv.pop(1)
        search_main()
        return
    if len(sys.argv) > 1 and sys.argv[1] in {"shard", "merge"}:
        op = sys.argv[1]
        utility = argparse.ArgumentParser(description=f"Tensor-aware GGUF {op} utility (llama.cpp)")
        utility.add_argument("model_or_directory", type=Path)
        utility.add_argument("destination", type=Path)
        utility.add_argument("--splitter", type=Path, required=True, help="Path to llama-gguf-split executable")
        utility.add_argument("--size", default="250M", help="Size for shard: 250M, 500M, 1G")
        opts = utility.parse_args(sys.argv[2:])
        try:
            if op == "shard":
                paths = shard_model(opts.model_or_directory, opts.splitter, opts.destination, opts.size)
                print(f"Created {len(paths)} shards, first: {paths[0]}")
            else:
                model = merge_model(opts.model_or_directory, opts.splitter, opts.destination)
                print(f"Merged GGUF: {model}")
        except (OSError, ValueError, subprocess.CalledProcessError) as exc:
            utility.exit(1, f"Error: {exc}\n")
        return
    parser = argparse.ArgumentParser(description="Build a local knowledge assistant on macOS, Linux or Windows")
    parser.add_argument("--backend", choices=["auto", "mlx", "torch"], default="auto",
                        help="Training engine: auto selects MLX on Apple Silicon, else PyTorch")
    parser.add_argument("--model", type=int, choices=range(1, len(PRESETS) + 1), help="Model choice 1–4")
    parser.add_argument("--source", action="append", dest="sources", help="GitHub repo URL, document URL or file/folder; repeatable")
    parser.add_argument("--max-chunks", type=int, default=12000, help="Index passage limit; 0 includes all supported content")
    parser.add_argument("--max-files-per-source", type=int, default=2000, help="Supported file limit per source; 0 includes all files")
    parser.add_argument("--sources-file", action="append", type=Path,
                        help="UTF-8 .txt file with one URL or local path per line; repeatable")
    parser.add_argument("--qa", help="Optional manually curated Q&A JSONL")
    parser.add_argument("--mode", choices=["quick", "standard"])
    parser.add_argument("--output", default="runs", help="Output parent directory")
    parser.add_argument("--strict-sources", action="store_true",
                        help="Stop on the first failed source instead of skipping it")
    parser.add_argument("--download-timeout", type=int, default=20, metavar="SECONDS",
                        help="Timeout for each HTTPS document attempt (default: 20)")
    parser.add_argument("--download-retries", type=int, default=1, metavar="N",
                        help="Retry failed downloads/clones N times (default: 1)")
    parser.add_argument("--no-source-cache", action="store_true",
                        help="Do not reuse GitHub/document downloads from earlier runs")
    parser.add_argument("--run-name", help="Unique name for a new run (re-runs require a new name)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation")
    parser.add_argument("--dry-run", action="store_true", help="Ingest/index/data/test without training or model download")
    parser.add_argument("--shard-size", type=parse_shard_size, help="Optionally emit GGUF tensor shards, e.g. 250M")
    parser.add_argument("--shards-only", action="store_true", help="After shard smoke test, keep shards instead of full GGUF")
    args = parser.parse_args()
    if args.shards_only and not args.shard_size:
        parser.error("--shards-only requires --shard-size")
    try:
        build(args)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, KeyboardInterrupt) as exc:
        print(f"\nERROR: {exc}", file=sys.stderr)
        print("Existing files in runs/ are preserved for inspection/retry.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
