#!/bin/sh
# macOS: double-click in Finder or run from Terminal.
set -eu
cd "$(dirname "$0")"
exec python3 bootstrap.py "$@"
