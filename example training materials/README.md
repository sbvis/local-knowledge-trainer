# Example training materials

Edit `sources.txt` to replace the training corpus. It accepts one HTTPS repository, GitHub tree directory, document URL, or local file/folder path per line. Local paths are relative to this file. A leading `#` disables an entry.

The active example contains every supported file in the ManiVault `_tutorials` folder and all 568 pages from `papers/MANIVAULT_ALL_DOCUMENTATION.txt`, split into individual Markdown files under `papers/documentation/` so the trainer can ingest each page within its file-size limit. The other repositories and URLs remain commented out. Edit `sources.txt` to train on another project.

Activate your Python environment, then run from the trainer repository root. Git, CMake, and a C++ toolchain are required for GGUF export. On Windows, a short checkout path helps avoid package installation path limits.

```powershell
python -m pip install -e . -r requirements-base.txt -r requirements-torch.txt cmake
python -X utf8 -m local_knowledge_trainer --backend torch --sources-file 'example training materials/sources.txt' --model 4 --mode standard --max-chunks 0 --max-files-per-source 0 --strict-sources --yes --run-name my-assistant
```

Preset 4 uses Qwen2.5 1.5B Instruct. Preset 1 uses the smaller Qwen2.5-Coder 0.5B Instruct. The zero limits include all supported source files and passages. Both presets export a quantized GGUF model and a SQLite knowledge index.

Training prepares source-backed examples and reserves source files for validation. The PyTorch backend selects the adapter with the lowest validation loss. Inspect the generated examples and test real questions after export. Retrieval diagnostics and training loss measure different parts of the pipeline from answer correctness.

`evaluation-questions.jsonl` contains example questions and expected facts for this corpus. Replace these questions and references when using different materials. They are used for answer review after training.

```powershell
python -X utf8 -m local_knowledge_trainer evaluate runs/my-assistant/release 'example training materials/evaluation-questions.jsonl' runs/my-assistant/answer-review.json --max-tokens 160
```
ZIP the completed run's entire `release` directory.

```powershell
Compress-Archive -LiteralPath runs/my-assistant/release -DestinationPath runs/my-assistant.zip
Get-FileHash runs/my-assistant.zip -Algorithm SHA256
```

Upload the ZIP to a direct HTTPS download location. Keep the model, knowledge index, manifest, checksums, and release reports together. Configure ChatAssistantPlugin with the ZIP URL and its SHA-256 digest.

```cmake
-DASSISTANT_PACKAGE_URL="https://your-host/my-assistant.zip"
-DASSISTANT_PACKAGE_SHA256="<ZIP SHA-256>"
```
