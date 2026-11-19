# Local Knowledge Trainer

Build a local assistant for your documentation, papers, or source code. The trainer collects sources, creates a searchable SQLite index, fine-tunes a small language model, and exports a GGUF package with provenance and checksums.

Provide your own files and URLs. The [example training materials](example%20training%20materials/README.md) contain an optional corpus with replaceable inputs and evaluation questions.

## Requirements

- Python 3.10 or newer. Python 3.12 was used for the Windows training and export checks.
- Git and internet access for dependencies, remote sources, and initial model downloads.
- For training and export, a C++ compiler and a compatible training backend. The launcher installs CMake and Python dependencies in `.venv`.

MLX runs on Apple Silicon. PyTorch runs on Windows/Linux with a supported NVIDIA GPU, or on CPU. Training and merging need more memory and disk space than the final model. CPU training can be slow. See [platform setup](docs/PLATFORMS.md).

## Clone and provide your materials

```sh
git clone https://github.com/sbvis/local-knowledge-trainer.git
cd local-knowledge-trainer
```

Create a `training materials` folder with your documents and a UTF-8 `sources.txt` file containing one source per line, for example

```text
# Paths are relative to this source list.
./documents
./manual.pdf
# https://github.com/your-organization/your-project
# https://github.com/your-organization/your-project/tree/main/docs
# https://your-organization.example/guide.html
```

Replace these entries with existing paths or reachable HTTPS URLs. Supported inputs include Markdown, text, HTML, PDF, DOCX, common source-code files, and configuration files. GitHub tree URLs select a repository directory. Encode slashes in branch names within the URL's ref component.

`training materials` is ignored by Git. The tracked `example training materials` folder provides reproducible examples. A run needs at least two source-file groups or curated Q&A groups to reserve validation material.

## Prepare and inspect

Windows PowerShell or Command Prompt

```powershell
py -3 bootstrap.py --sources-file "training materials/sources.txt" --model 1 --mode quick --strict-sources --yes --dry-run --run-name my-check
```

macOS or Linux

```sh
python3 bootstrap.py --sources-file "training materials/sources.txt" --model 1 --mode quick --strict-sources --yes --dry-run --run-name my-check
```

The launcher creates `.venv` and installs preparation dependencies automatically. A dry run collects sources and prepares the index, examples, and reports. Inspect `runs/my-check/data/` and run

```sh
python bootstrap.py inspect-training runs/my-check --model 1 --mode quick
python bootstrap.py search runs/my-check/release/knowledge.db "your question"
```

Use `py -3` on Windows or `python3` on macOS/Linux if `python` is unavailable. Utilities reuse the launcher's `.venv` when it exists.

## Train and export

Omit `--dry-run` and use a new run name.

```sh
python bootstrap.py --sources-file "training materials/sources.txt" --model 1 --mode standard --strict-sources --yes --run-name my-assistant
```

Model 1 is the smallest code-focused 0.5B preset. Model 4 is the general 1.5B instruction preset used for the bundled example. See [model choices](docs/MODELS.md). `--mode standard` increases training coverage. `--max-chunks 0 --max-files-per-source 0` includes all supported content within the extractor's file-size limits.

Continue an interrupted run with

```sh
python bootstrap.py resume runs/my-assistant
```

Run directories are preserved if they already exist, so the trainer will not overwrite a previous run. To start over with the same run name, remove that run directory first (this permanently deletes its prepared data, checkpoints, and release):

```sh
rm -rf runs/my-assistant
```

Then rerun the training command above. To keep the previous run, use a different `--run-name` instead.

The release is written to `runs/my-assistant/release/`. On Windows, new compiler and converter caches use a short path under `%LOCALAPPDATA%/LocalKnowledgeTrainer` to avoid nested build-path limits. Existing run-local tool checkouts remain usable. New exports use a pinned, tested llama.cpp revision.

## Ask questions and evaluate

```sh
python bootstrap.py ask runs/my-assistant/release "your question"
python bootstrap.py chat runs/my-assistant/release
```

Answers use the knowledge index and source citations. Documented interface procedures can be returned directly from sources. Other answers use the local model. `ask-model` lets you inspect model-generated interface answers.

Create a UTF-8 JSONL question file for your corpus, with one question and optional reference per line.

```json
{"question":"How do I configure my application?","reference":"The documented configuration steps."}
```

```sh
python bootstrap.py evaluate runs/my-assistant/release questions.jsonl runs/my-assistant/answer-review.json
```

Review answers against the sources. Training loss and retrieval scores measure different parts of the pipeline from answer correctness. Generated answers can contain mistakes or unnecessary detail. Replace example questions when using another corpus.

## Share a release

Keep the entire release together, including `assistant.gguf`, `knowledge.db`, `manifest.json`, and `SHA256SUMS.txt`. The model uses retrieved evidence for source-specific answers. See the [release format](docs/OUTPUT_FORMAT.md).

Create a ZIP in PowerShell with

```powershell
Compress-Archive -LiteralPath runs/my-assistant/release -DestinationPath runs/my-assistant.zip
Get-FileHash runs/my-assistant.zip -Algorithm SHA256
```

The [ManiVault ChatAssistantPlugin](https://github.com/ManiVaultStudio/ChatAssistantPlugin.git) accepts a release ZIP through CMake's `ASSISTANT_PACKAGE_URL` and `ASSISTANT_PACKAGE_SHA256`, or a local `ASSISTANT_PACKAGE_DIR`. Applications should validate the package and test their own retrieval and answer workflow.

## Use an existing Python environment

Activate your environment, then install the project and base dependencies.

```sh
python -m pip install -e . -r requirements-base.txt
python -m pip install -r requirements-torch.txt cmake
# Apple Silicon users can install requirements-mlx.txt instead.
```

Install a PyTorch wheel compatible with your GPU and driver before training. Run `python -m local_knowledge_trainer` with the same arguments to use the active environment. `bootstrap.py` manages the repository's own `.venv`.

## Development

```sh
python -m pip install -e .
python -X utf8 -m unittest discover -s tests -v
```

Unit tests use the standard library and mock training and network requests. GitHub Actions runs them on Windows, Linux, and macOS with Python 3.10 and 3.12. See [verification](VERIFY.md). Submit bug reports and pull requests through this repository's GitHub page.

## Privacy and license

Local files are processed on your machine. Dependencies, model acquisition, and source URLs can use the network. Completed releases run offline with a compatible inference engine. Keep private materials and model packages outside Git, and check source and base-model licenses before redistribution.

The trainer code is licensed under [MIT](LICENSE).
