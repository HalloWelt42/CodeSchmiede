#!/usr/bin/env bash
# Baut das Sandbox-Image fuer die Python-Aufgaben.
# Idempotent. Ausfuehren bei jedem Update am Sandbox-Dockerfile.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
SANDBOX_DIR="$ROOT_DIR/aufgaben/sandbox"

cd "$SANDBOX_DIR"

echo "Baue codeschmiede-sandbox:python aus $SANDBOX_DIR ..."
docker build --tag codeschmiede-sandbox:python .

echo ""
echo "Image fertig:"
docker images codeschmiede-sandbox:python
