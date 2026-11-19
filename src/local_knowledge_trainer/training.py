"""Native MLX training and portable llama.cpp conversion utilities."""
import os
import hashlib
import json
import venv
import shutil
import subprocess
import sys
from pathlib import Path

from .common import info, run

LLAMA_CPP_COMMIT = '2cbfc3cf34f94c8ada67eb8766efe7374a3d2db6'


def tool_cache_directory(cache_dir):
    """Keep Windows build and package paths short, with one cache per run."""
    cache_dir = Path(cache_dir)
    if sys.platform != 'win32':
        return cache_dir
    identity = hashlib.sha256(str(cache_dir.resolve()).encode()).hexdigest()[:12]
    base = Path(os.environ.get('LOCALAPPDATA', str(Path.home() / '.cache')))
    return base / 'LocalKnowledgeTrainer' / identity


def llama_cpp_root(cache_dir):
    legacy = Path(cache_dir) / 'llama.cpp'
    return legacy if legacy.exists() else tool_cache_directory(cache_dir) / 'llama.cpp'


def download_model(preset, backend="mlx"):
    from huggingface_hub import snapshot_download
    repo = preset.mlx_repo if backend == "mlx" else preset.hf_repo
    info(f"Downloading / loading pretrained model: {repo}")
    # Serial acquisition avoids a symlink-capability probe race on Windows
    # accounts without permission to create symbolic links.
    return Path(snapshot_download(repo_id=repo, max_workers=1 if os.name == 'nt' else 8))


def train(model_path, data_dir, adapter_dir, preset, mode):
    from .training_plan import make_training_plan
    plan = make_training_plan(data_dir, preset, mode)
    iterations = plan.iterations
    info(f"Training plan: {plan.examples} examples, {iterations} updates "
         f"(~{plan.effective_passes} passes), context {plan.max_sequence_length}")
    command = [sys.executable, "-m", "mlx_lm", "lora", "--train",
               "--model", model_path, "--data", data_dir, "--adapter-path", adapter_dir,
               "--fine-tune-type", "lora", "--mask-prompt", "--grad-checkpoint",
               "--batch-size", "1", "--num-layers", str(preset.layers),
               "--iters", str(iterations), "--max-seq-length", str(plan.max_sequence_length),
               "--learning-rate", str(plan.learning_rate), "--steps-per-report", "10",
               "--steps-per-eval", str(plan.validation_interval),
               "--save-every", str(min(200, iterations)),
               "--val-batches", str(plan.validation_batches)]
    info("Fine-tuning locally with MLX LoRA (no API calls)")
    run(command)
    from .common import dump_json
    dump_json(Path(adapter_dir) / "training_plan.json", plan.as_dict())
    if not (Path(adapter_dir) / "adapters.safetensors").is_file():
        raise RuntimeError("MLX did not produce adapter weights. Check training logs.")
    return iterations


def fuse(model_path, adapter_dir, fused_dir):
    info("Merging trained adapter into model weights (dequantizing)")
    run([sys.executable, "-m", "mlx_lm", "fuse",
         "--model", model_path, "--adapter-path", adapter_dir,
         "--save-path", fused_dir, "--dequantize"])
    if not any(Path(fused_dir).glob("*.safetensors")):
        raise RuntimeError("No fused safetensors found")


def tool_binary(build: Path, name: str) -> Path:
    """Locate built binaries on Unix, MSVC and multi-config CMake builds."""
    exe = name + (".exe" if os.name == "nt" else "")
    for candidate in (build / "bin" / exe, build / "bin" / "Release" / exe,
                      build / "Release" / exe):
        if candidate.is_file():
            return candidate
    return build / "bin" / exe


def prepare_llama_cpp(cache_dir):
    """Build local GGUF quantizer, splitter and model-test CLI. No server required."""
    root = llama_cpp_root(cache_dir)
    if not (root / "convert_hf_to_gguf.py").is_file():
        info("Cloning llama.cpp converter/quantizer")
        root.parent.mkdir(parents=True, exist_ok=True)
        run(["git", "init", root])
        run(["git", "-C", root, "remote", "add", "origin", "https://github.com/ggml-org/llama.cpp.git"])
        run(["git", "-C", root, "fetch", "--depth", "1", "origin", LLAMA_CPP_COMMIT])
        run(["git", "-C", root, "checkout", "--detach", "FETCH_HEAD"])
    build = root / "build"
    quantizer = tool_binary(build, "llama-quantize")
    cli = tool_binary(build, "llama-cli")
    splitter = tool_binary(build, "llama-gguf-split")
    completion = tool_binary(build, "llama-completion")
    if not quantizer.is_file() or not cli.is_file() or not splitter.is_file() or not completion.is_file():
        info("Building llama.cpp quantizer and offline model-check executable")
        # llama.cpp currently creates llama-cli only with LLAMA_BUILD_SERVER=ON:
        # its CLI links server components, even though no server is started here.
        # Explicitly disable the web UI and its downloadable assets.
        run(["cmake", "-S", root, "-B", build, "-DCMAKE_BUILD_TYPE=Release",
             "-DGGML_METAL=ON" if sys.platform == "darwin" else "-DGGML_METAL=OFF",
             "-DLLAMA_BUILD_COMMON=ON", "-DLLAMA_BUILD_TOOLS=ON",
             "-DLLAMA_BUILD_TESTS=OFF", "-DLLAMA_BUILD_EXAMPLES=OFF",
             "-DLLAMA_BUILD_SERVER=ON", "-DLLAMA_BUILD_UI=OFF",
             "-DLLAMA_USE_PREBUILT_UI=OFF", "-DLLAMA_BUILD_APP=OFF"])
        run(["cmake", "--build", build, "--config", "Release", "--target",
             "llama-quantize", "llama-cli", "llama-completion", "llama-gguf-split", "--parallel", "2"])
    quantizer = tool_binary(build, "llama-quantize")
    cli = tool_binary(build, "llama-cli")
    splitter = tool_binary(build, "llama-gguf-split")
    completion = tool_binary(build, "llama-completion")
    if not quantizer.is_file() or not cli.is_file() or not splitter.is_file() or not completion.is_file():
        raise RuntimeError("llama.cpp build completed but required executable not found")
    return root, quantizer, cli, splitter


def _converter_python(cache_dir: Path, requirements: Path) -> Path:
    """Keep converter packages isolated from MLX/PyTorch fine-tuning dependencies."""
    env_dir = tool_cache_directory(cache_dir) / "converter-venv"
    interpreter = env_dir / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    stamp = env_dir / "requirements.sha256"
    checksum = hashlib.sha256(requirements.read_bytes()).hexdigest()
    if not interpreter.is_file():
        info("Creating isolated GGUF converter Python environment")
        env_dir.parent.mkdir(parents=True, exist_ok=True)
        venv.EnvBuilder(with_pip=True).create(env_dir)
    if not stamp.is_file() or stamp.read_text(encoding="ascii").strip() != checksum:
        info("Installing GGUF conversion dependencies into isolated environment")
        run([interpreter, "-m", "pip", "install", "--disable-pip-version-check", "-r", requirements])
        stamp.write_text(checksum + "\n", encoding="ascii")
    return interpreter


def normalize_tokenizer_config(fused_dir):
    """Adapt Transformers 5 tokenizer metadata to llama.cpp's Transformers 4 converter.

    MLX-LM may save ``extra_special_tokens`` as a list (Transformers 5 schema),
    while llama.cpp's isolated converter currently installs Transformers 4,
    which expects a dictionary for that key. Transformers 4 supports
    ``additional_special_tokens`` as a list; migrate rather than discard tokens.

    Fused weights and vocabulary files are unchanged. Save a one-time backup
    of the original metadata so a completed training run is recoverable.
    """
    config_path = Path(fused_dir) / "tokenizer_config.json"
    if not config_path.is_file():
        raise FileNotFoundError(f"Fused model is missing tokenizer metadata: {config_path}")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ValueError(f"Invalid tokenizer metadata (expected JSON object): {config_path}")
    extras = config.get("extra_special_tokens")
    if not isinstance(extras, list):
        return False

    existing = config.get("additional_special_tokens") or []
    if not isinstance(existing, list):
        raise ValueError("additional_special_tokens is not a list; cannot safely migrate metadata")
    for token in extras:
        if not isinstance(token, (str, dict)):
            raise ValueError("Unexpected special token entry; refusing to change tokenizer metadata")
    merged = existing.copy()
    for token in extras:
        if token not in merged:
            merged.append(token)
    config.pop("extra_special_tokens")
    config["additional_special_tokens"] = merged

    backup = config_path.with_name("tokenizer_config.transformers5.backup.json")
    if not backup.exists():
        shutil.copy2(config_path, backup)
    temp_path = config_path.with_name("tokenizer_config.json.tmp")
    try:
        temp_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temp_path.replace(config_path)
    finally:
        temp_path.unlink(missing_ok=True)
    info(f"Converted Transformers 5 tokenizer metadata to 4.x format; original saved at {backup.name}")
    return True


def _valid_gguf(path: Path) -> bool:
    """Conservative guard against reusing files from interrupted conversions."""
    if not path.is_file() or path.stat().st_size < 10_000_000:
        return False
    with path.open("rb") as handle:
        return handle.read(4) == b"GGUF"


def export_gguf(fused_dir, cache_dir, release_dir):
    """Convert fused weights to Q4_K_M GGUF, retaining all trained artifacts."""
    fused_dir = Path(fused_dir)
    release_dir = Path(release_dir)
    release_dir.mkdir(parents=True, exist_ok=True)
    root, quantizer, cli, splitter = prepare_llama_cpp(cache_dir)
    final = release_dir / "assistant.gguf"
    if final.is_file():
        if not _valid_gguf(final):
            raise RuntimeError(f"Existing GGUF is incomplete/invalid: {final}. Preserve it for inspection before retrying.")
        info("Reusing previously exported GGUF model")
        run([cli, "--model", final, "--prompt", "Hello", "--n-predict", "8", "--temp", "0", "--single-turn", "--offline"])
        return final

    requirements = root / "requirements" / "requirements-convert_hf_to_gguf.txt"
    if not requirements.is_file():
        raise RuntimeError(f"llama.cpp converter requirements not found: {requirements}")
    converter_py = _converter_python(Path(cache_dir), requirements)
    intermediate = fused_dir.parent / "assistant-f16.gguf"
    if not _valid_gguf(intermediate):
        # An interrupted export may leave a partial GGUF at either filename.
        # Keep original fused weights and tokenizer backup; intermediate is disposable.
        if intermediate.exists():
            info("Discarding incomplete intermediate GGUF before retry")
            intermediate.unlink()
        normalize_tokenizer_config(fused_dir)
        info("Checking tokenizer compatibility before GGUF conversion")
        run([converter_py, "-c", "from transformers import AutoTokenizer; import sys; "
             "t=AutoTokenizer.from_pretrained(sys.argv[1], local_files_only=True); "
             "assert len(t.get_vocab()) > 0, 'Empty tokenizer vocabulary'", fused_dir])
        info("Converting fused model to GGUF")
        temporary = intermediate.with_name("assistant-f16.gguf.partial")
        temporary.unlink(missing_ok=True)
        try:
            run([converter_py, root / "convert_hf_to_gguf.py", fused_dir,
                 "--outfile", temporary, "--outtype", "f16"])
            if not _valid_gguf(temporary):
                raise RuntimeError("GGUF converter returned without producing a complete-looking model file")
            temporary.replace(intermediate)
        finally:
            temporary.unlink(missing_ok=True)
    else:
        info("Reusing previously converted intermediate GGUF")

    info("Quantizing model to Q4_K_M")
    temporary_final = release_dir / "assistant.gguf.partial"
    temporary_final.unlink(missing_ok=True)
    try:
        run([quantizer, intermediate, temporary_final, "Q4_K_M"])
        if not _valid_gguf(temporary_final):
            raise RuntimeError("Quantization did not produce a complete-looking GGUF file")
        # Confirm model loads before publishing final assistant.gguf.
        info("Smoke testing quantized GGUF with llama.cpp")
        run([cli, "--model", temporary_final, "--prompt", "Hello", "--n-predict", "8", "--temp", "0", "--single-turn", "--offline"])
        temporary_final.replace(final)
    finally:
        temporary_final.unlink(missing_ok=True)
    intermediate.unlink(missing_ok=True)
    return final
