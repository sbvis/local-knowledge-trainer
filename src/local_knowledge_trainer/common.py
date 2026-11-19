"""Shared file and command helpers. No third-party dependencies."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def info(message):
    print(f"\n▸ {message}", flush=True)


def run(command, *, cwd=None):
    printable = " ".join(str(c) for c in command)
    print(f"  $ {printable}", flush=True)
    subprocess.run([str(c) for c in command], cwd=cwd, check=True)


def dump_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path):
    checksum = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def now_utc():
    return datetime.now(timezone.utc).isoformat()
