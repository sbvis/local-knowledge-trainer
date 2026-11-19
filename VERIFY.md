# Verification

Checked on 18 November 2026 using Windows and Python 3.12.13.

## Automated tests

```sh
python -m pip install -e .
python -X utf8 -m unittest discover -s tests -v
```

The local suite ran 116 tests with 115 passing and one skipped. Coverage includes source lists, GitHub tree paths, document extraction, independent source groups, retrieval, training plans, export recovery, Windows executable discovery, Unicode CLI input, and unrelated application/document fixtures.

The GitHub Actions matrix runs Python 3.10 and 3.12 on Windows, macOS, and Linux. CI results are available on the repository's Actions page.

## Fresh environment

An isolated copy of the staged source was tested in a new virtual environment. The launcher installed its base dependencies and prepared a knowledge index from two unrelated local Markdown documents. Training inspection and index search were exercised through the launcher.

## Model and source checks

Windows CUDA runs fine-tuned the 0.5B code model and the 1.5B general model, merged their adapters, exported quantized GGUF models, and loaded the exported models with llama.cpp.

The example corpus contains 18 tutorial files and three papers comprising 24 pages. All were indexed. A source-based review checked 34 questions covering all tutorial files, paper facts, and unsupported requests. It recorded 33 correct core answers and one partial paper explanation. Some responses contained unnecessary detail or imprecise wording. Detailed review reports accompany the separately generated model package.

Training and export require a compatible backend, compiler, and enough memory and storage. Source coverage, retrieval diagnostics, validation loss, and reviewed answers should all be checked when replacing the example corpus.

A fresh Windows tool cache fetched the pinned llama.cpp revision, built all four required tools using the default Visual Studio generator, installed the isolated converter dependencies, and loaded the trained GGUF successfully. This check used the new short-cache paths without a drive alias or manual Ninja rebuild.
