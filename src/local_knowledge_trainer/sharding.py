"""Portable GGUF tensor-aware sharding: avoids corrupt byte slicing."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from .common import sha256_file

_SIZE_RE = re.compile(r"^[1-9][0-9]{0,4}[MG]$")
_SHARD_RE = re.compile(r"-([0-9]{5})-of-([0-9]{5})\.gguf$")


def parse_shard_size(size: str) -> str:
    """GGUF splitter supports decimal M or G suffix (e.g. '250M')."""
    normalized = size.upper().strip()
    if not _SIZE_RE.fullmatch(normalized):
        raise ValueError("Shard size must be a positive integer followed by M or G, e.g. 250M or 1G")
    if int(normalized[:-1]) < 10 and normalized.endswith("M"):
        raise ValueError("Minimum shard size is 10M")
    return normalized


def discover_shards(folder: Path, prefix: str = "assistant") -> list[Path]:
    """Ensure complete, consecutively numbered llama.cpp GGUF shards."""
    items = sorted(folder.glob(f"{prefix}-*-of-*.gguf"))
    if not items:
        raise FileNotFoundError(f"No GGUF shards found in {folder}")
    parsed = [_SHARD_RE.search(path.name) for path in items]
    if any(match is None for match in parsed):
        raise ValueError("Unrecognized shard filename")
    totals = {int(match.group(2)) for match in parsed}
    if len(totals) != 1 or len(items) != next(iter(totals)):
        raise ValueError("Incomplete GGUF shard set")
    sequence = [int(match.group(1)) for match in parsed]
    if sequence != list(range(1, len(items) + 1)):
        raise ValueError("Shard sequence is incomplete or duplicated")
    for path in items:
        with path.open("rb") as stream:
            if stream.read(4) != b"GGUF":
                raise ValueError(f"Invalid GGUF shard: {path}")
    return items


def shard_model(model: Path, splitter: Path, output_dir: Path, size: str) -> list[Path]:
    model, splitter, output_dir = Path(model), Path(splitter), Path(output_dir)
    size = parse_shard_size(size)
    if not model.is_file():
        raise FileNotFoundError(f"Model does not exist: {model}")
    if not splitter.is_file():
        raise FileNotFoundError(f"llama-gguf-split not found: {splitter}")
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f"Refusing to overwrite existing output directory: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([str(splitter), "--split-max-size", size, str(model),
                    str(output_dir / "assistant")], check=True)
    return discover_shards(output_dir)


def merge_model(shard_dir: Path, splitter: Path, destination: Path) -> Path:
    paths = discover_shards(Path(shard_dir))
    destination, splitter = Path(destination), Path(splitter)
    if not splitter.is_file():
        raise FileNotFoundError(f"llama-gguf-split not found: {splitter}")
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([str(splitter), "--merge", str(paths[0]), str(destination)], check=True)
    with destination.open("rb") as stream:
        if stream.read(4) != b"GGUF":
            raise RuntimeError("Merged model has invalid GGUF header")
    return destination


def shard_metadata(paths: list[Path], release: Path) -> list[dict]:
    return [{"path": str(path.relative_to(release)), "bytes": path.stat().st_size,
             "sha256": sha256_file(path)} for path in paths]
