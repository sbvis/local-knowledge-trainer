"""Cross-platform launcher: guided training, recovery, and offline utilities.

The training environment is checked before ingestion to avoid wasting time on
sources when NumPy/MLX has been damaged by an interrupted installation.
"""
from __future__ import annotations

import hashlib
import os
import platform
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _running_from_trash(root: Path = ROOT) -> bool:
    """Recognize macOS Finder Trash and freedesktop trash locations."""
    parts = root.expanduser().resolve().parts
    return '.Trash' in parts or any(p.lower() in ('trash', 'files')
                                     and i and parts[i-1] in ('.local', 'Trash')
                                     for i, p in enumerate(parts))


VENV = ROOT / ".venv"


def _venv_python() -> Path:
    return VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def _backend(args: list[str]) -> str:
    default = "mlx" if platform.system() == "Darwin" and platform.machine() == "arm64" else "torch"
    if "--backend" not in args:
        return default
    index = args.index("--backend")
    if index + 1 >= len(args):
        raise ValueError("--backend requires mlx, torch or auto")
    backend = args[index + 1]
    if backend == "auto":
        return default
    if backend not in ("mlx", "torch"):
        raise ValueError("--backend must be auto, mlx or torch")
    if backend == "mlx" and default != "mlx":
        raise ValueError("MLX backend requires Apple Silicon. Use --backend torch.")
    return backend


def _import_check(python: Path, code: str, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(python), "-c", code], cwd=ROOT, env=env,
                          capture_output=True, text=True, check=False)


def verify_training_environment(python: Path, backend: str, env: dict[str, str]) -> None:
    """Check imports and repair an unusable NumPy wheel once, before ingestion.

    A successful `pip install` is insufficient: an existing NumPy dist-info can
    claim success even when its native _multiarray_umath extension is missing.
    """
    numpy_probe = "import numpy as np; assert int(np.arange(3).sum()) == 3; print('NumPy', np.__version__, 'OK')"
    result = _import_check(python, numpy_probe, env)
    if result.returncode:
        print("NumPy's compiled extension is unavailable. Repairing the existing environment...")
        print("Previous error:", result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "import failed")
        subprocess.run([str(python), "-m", "pip", "install", "--disable-pip-version-check",
                        "--no-cache-dir", "--force-reinstall", "--no-deps", "numpy>=1.26,<3"],
                       cwd=ROOT, env=env, check=True)
        result = _import_check(python, numpy_probe, env)
        if result.returncode:
            raise RuntimeError("NumPy repair did not succeed. See the import error below:\n"
                               + result.stderr.strip())
        print("NumPy repaired successfully.")
    else:
        print(result.stdout.strip())
    import_code = "import mlx_lm; import mlx.core; print('MLX backend OK')" if backend == "mlx" else \
                  "import torch; print('PyTorch backend OK')"
    result = _import_check(python, import_code, env)
    if result.returncode:
        raise RuntimeError(f"The {backend} backend cannot load:\n{result.stderr.strip()}\n"
                           "Re-run the launcher to reinstall its backend requirements.")
    print(result.stdout.strip())


def _requirements_signature(backend: str, dry_run: bool) -> str:
    files = [ROOT / "requirements-base.txt"]
    if not dry_run:
        files.append(ROOT / ("requirements-mlx.txt" if backend == "mlx" else "requirements-torch.txt"))
    digest = hashlib.sha256()
    digest.update((backend + ":" + str(dry_run) + ":" + sys.version.split()[0]).encode())
    for path in files:
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> int:
    os.environ['PYTHONUTF8'] = '1'
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    if sys.version_info < (3, 10):
        print("Python 3.10 or newer required", file=sys.stderr)
        return 2
    if args := (sys.argv[1:] if len(sys.argv) > 1 else []):
        if args == ["--version"]:
            sys.path.insert(0, str(ROOT / "src"))
            from local_knowledge_trainer import __version__
            print(f"Local Knowledge Trainer v{__version__}\nRunning from: {ROOT}")
            return 0
    if _running_from_trash():
        print("WARNING: The trainer is running from a Trash folder: " + str(ROOT),
              file=sys.stderr)
        print("Move the project to a permanent folder before training; files in Trash "
              "may be deleted.", file=sys.stderr)
    commands = {"ask", "ask-model", "chat", "search", "inspect-training", "inspect-symbol", "upgrade-index", "shard", "merge", "evaluate", "evaluate-ui", "add-guide"}
    args = sys.argv[1:]
    utility = bool(args and args[0] in commands) or args in (["--help"], ["-h"])
    if utility:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
        try:
            python = _venv_python() if _venv_python().is_file() else Path(sys.executable)
            return subprocess.run([str(python), "-m", "local_knowledge_trainer", *args],
                                  cwd=ROOT, env=env, check=False).returncode
        except KeyboardInterrupt:
            return 130

    try:
        backend = _backend(args)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    python = _venv_python()
    env = os.environ.copy()
    env["PATH"] = str(python.parent) + os.pathsep + env.get("PATH", "")
    env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")

    # Explicit preflight/repair without downloading sources or a model.
    if args and args[0] == "doctor":
        if not python.is_file():
            print("Training .venv not found. Run ./start.command once to install it.", file=sys.stderr)
            return 2
        try:
            verify_training_environment(python, backend, env)
            print("Training environment is healthy.")
            return 0
        except (RuntimeError, subprocess.CalledProcessError) as exc:
            print(f"Environment check failed: {exc}", file=sys.stderr)
            return 1

    # Resuming an existing run never reinstalls the whole training environment.
    # If fine-tuning wasn't completed, we do check/fix its backend first.
    if args and args[0] == "resume":
        if not python.is_file():
            print("Training .venv not found. Restore the environment before resuming.", file=sys.stderr)
            return 2
        try:
            workspace = Path(args[1]).expanduser().resolve() if len(args) > 1 else None
            if workspace and not any((workspace / "fused").glob("*.safetensors")):
                verify_training_environment(python, backend, env)
            return subprocess.run([str(python), "-m", "local_knowledge_trainer", *args],
                                  cwd=ROOT, env=env, check=False).returncode
        except (RuntimeError, subprocess.CalledProcessError) as exc:
            print(f"Environment check failed: {exc}", file=sys.stderr)
            return 1
        except KeyboardInterrupt:
            return 130

    dry_run = "--dry-run" in args
    if not python.is_file():
        print("Creating an isolated Python environment...")
        venv.EnvBuilder(with_pip=True).create(VENV)
    signature = _requirements_signature(backend, dry_run)
    stamp = VENV / ".lkt-requirements.sha256"
    install = [str(python), "-m", "pip", "install", "-e", str(ROOT),
               "-r", str(ROOT / "requirements-base.txt")]
    if not dry_run:
        install += ["-r", str(ROOT / ("requirements-mlx.txt" if backend == "mlx" else "requirements-torch.txt")),
                    "cmake>=3.22"]
    try:
        if not stamp.is_file() or stamp.read_text(encoding="ascii").strip() != signature:
            print("Installing/checking Python dependencies (internet may be needed)...")
            subprocess.run(install, cwd=ROOT, env=env, check=True)
            stamp.write_text(signature + "\n", encoding="ascii")
        else:
            print("Reusing previously installed Python dependencies.")
        if not dry_run:
            verify_training_environment(python, backend, env)
        subprocess.run([str(python), "-m", "local_knowledge_trainer", *args],
                       cwd=ROOT, env=env, check=True)
    except (subprocess.CalledProcessError, RuntimeError) as exc:
        print(f"A command failed: {exc}", file=sys.stderr)
        return (exc.returncode or 1) if isinstance(exc, subprocess.CalledProcessError) else 1
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
