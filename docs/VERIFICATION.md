# v0.4.3 verification record

The tests below were run in a Linux/Python environment using the shipped
repository, without model weights or access to the user's local Mac files.
No live ManiVault GUI or GGUF-generation session was tested here.

## Baseline comparison on an identical independent fixture

A locally created three-repository corpus has Qt Point and Point size/Point
opacity actions in separate header/source files, an included Core action
header and an irrelevant website tutorial. We independently specified four
expectations: increase Point size, make dots bigger (paraphrase), decrease
Point opacity, and abstain on an unavailable control.

- v0.4.2: 1 / 4 passed
- v0.4.3: 4 / 4 passed

Comparison uses the same generated SQLite index and same acceptance cases for
both source versions. It does NOT establish performance on the user's GitHub
clone data, user GGUF, or the running graphical interface.

## Full test suite

`PYTHONPATH=src python -m unittest discover -s tests -q` — 83 tests passed
before the ZIP was created. A separate post-extraction pass is required for
release acceptance.

## Actual environment still needing testing

The user should run `./start.command --version` then `./start.command
 evaluate-ui runs/<RUN_ID>/release examples/ui-benchmark.example.jsonl` on
the exact `knowledge.db` used for their release, inspect the answers, then
manually verify at least 20 UI tasks against the installed ManiVault version.
The example benchmark is an illustrative starting point, not accepted ground
truth for arbitrary versions or workspace layouts.
