#!/bin/sh
# Linux / macOS quick launcher.
set -eu
cd "$(dirname "$0")"
exec python3 bootstrap.py "$@"
