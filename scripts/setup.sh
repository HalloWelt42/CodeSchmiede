#!/usr/bin/env bash
# Plattform-Setup: prueft Voraussetzungen, baut das Sandbox-Image,
# legt das Backend-venv an und installiert Frontend-Pakete.
# Ausfuehren einmalig nach dem Klonen oder bei groesseren Updates.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Codeschmiede-Setup ==="
echo

echo "Pruefe Voraussetzungen ..."
fehlt=0
for tool in docker python3.11 npm; do
  if command -v "$tool" >/dev/null 2>&1; then
    echo "  OK: $tool ($(command -v "$tool"))"
  else
    echo "  FEHLT: $tool"
    fehlt=1
  fi
done
if [ "$fehlt" -ne 0 ]; then
  echo
  echo "Bitte fehlende Werkzeuge installieren und das Skript erneut starten."
  exit 1
fi

echo
echo "Baue Sandbox-Image ..."
"$SCRIPT_DIR/build-sandbox.sh"

echo
echo "Backend-venv anlegen + Pakete installieren ..."
cd "$ROOT_DIR/backend"
python3.11 -m venv .venv
.venv/bin/pip install --quiet --upgrade pip
.venv/bin/pip install --quiet -e ".[dev]"
echo "  OK"

echo
echo "Frontend-Pakete installieren ..."
cd "$ROOT_DIR/frontend"
npm install --no-fund --no-audit --silent
echo "  OK"

echo
echo "=== Fertig ==="
echo
echo "Backend starten:"
echo "  cd backend && .venv/bin/python -m codeschmiede.main"
echo
echo "Frontend starten (in einem zweiten Terminal):"
echo "  cd frontend && npm run dev"
echo
echo "Browser: http://localhost:5184"
