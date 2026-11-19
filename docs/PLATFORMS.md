# Platform setup

## Cross-platform requirements

Install Python 3.10 or newer, Git, a C++ compiler and CMake. Initial bootstrap installs CMake inside the project's `.venv` when training. The project can ingest local files, prepare training data and search the index without any GPU.

The project launcher `python bootstrap.py` picks the training backend automatically: MLX for macOS Apple Silicon, PyTorch for all other systems. To override, pass `--backend mlx` or `--backend torch`.

### macOS Apple Silicon (recommended for an ordinary M1)

1. Install Apple's command-line tools with `xcode-select --install` and Python 3.10+.
2. Run `./start.command` or `python3 bootstrap.py`.
3. Choose the 0.5B preset for 8 GB unified memory. Use a small dataset first.
4. MLX LoRA trains on Apple Silicon. Temporary full precision files require considerably more storage/memory than the final quantized model.

### Linux with NVIDIA GPU

1. Install Python 3.10+, Git, `cmake`, a C++ compiler, and NVIDIA drivers compatible with PyTorch.
2. Run `./start.sh` or `python3 bootstrap.py --backend torch`.
3. Check in the created environment with `python -c 'import torch; print(torch.cuda.is_available())'` (use `.venv/bin/python`).
4. If CUDA is unavailable, training falls back to CPU, often extremely slowly. If PyTorch's default wheel does not support your CUDA setup, install the proper torch wheel from the [official selector](https://pytorch.org/get-started/locally/) before restarting.

### Windows 10/11

1. Install Python 3.10+ (with `py` launcher), Git and **Visual Studio Build Tools** with the C++ workload.
2. Run `start.bat` or `py -3 bootstrap.py --backend torch` from Command Prompt/PowerShell.
3. NVIDIA CUDA training uses the installed PyTorch build when a compatible driver/GPU is detected. CPU fallback works but can be slow.
4. CMake Visual Studio multi-config builds are supported by the native executable locator. Verify that your compiler and CMake are on PATH.

### Intel Mac, machines without GPUs

`--backend torch` uses CPU if CUDA is unavailable. Start with the 0.5B model. Training speed is not guaranteed, and some machines may not have sufficient RAM for the FP32 merge stage. Training is not a requirement for **data preparation, search and terminal inference**.

## Minimal/manual installation

```sh
python -m venv .venv
# Activate the environment (platform-specific) or use .venv/bin/python / .venv\\Scripts\\python.exe
python -m pip install -e . -r requirements-base.txt
# For actual training, install ONLY the matching backend requirements:
python -m pip install -r requirements-mlx.txt  # Apple Silicon
# OR
python -m pip install -r requirements-torch.txt # Linux/Windows/CPU
```

In virtual environments, install CMake if missing: `python -m pip install cmake`.

Model files are GGUF/SQLite and do not depend on the operating system. Native inference binaries must be built for the intended OS and CPU architecture, separately from the model weights.

## Resuming export after an interrupted build

Run `./start.command resume runs/YOUR_RUN --model 1` on macOS,
`./start.sh resume runs/YOUR_RUN --model 1` on Linux, or
`start.bat resume runs/YOUR_RUN --model 1` on Windows for old v0.3.0 runs.
The original model number is needed for metadata, not to download or train it
again. New runs save `build_state.json` and can omit `--model`.
The converter has an isolated Python environment to preserve the training environment.
New Windows tool and converter caches live under `%LOCALAPPDATA%/LocalKnowledgeTrainer`
with a short directory name derived from the run path. Other platforms use the run's
`tools/` directory. Existing run-local llama.cpp checkouts remain supported.

### Repairing a damaged training environment

Run `./start.command doctor` on macOS/Linux (or `start.bat doctor` on Windows) before retrying a failed training job. The command verifies NumPy native extensions and imports the active backend. A corrupted NumPy wheel is reinstalled automatically; no source repositories are touched. Use `./start.command resume runs/<run-id> --mode standard` if the earlier run had already prepared the training dataset but had not completed LoRA training.
