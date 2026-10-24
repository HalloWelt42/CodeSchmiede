#!/usr/bin/env bash
# Plattform-Setup: prueft Voraussetzungen, baut die Sandbox-Images,
# legt das Backend-venv an und installiert Frontend-Pakete.
# Ausfuehren einmalig nach dem Klonen oder bei groesseren Updates.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Codeschmiede-Setup ==="
echo

echo "Pruefe Voraussetzungen ..."
fehlt=0
for tool in docker uv npm; do
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
echo "Baue Sandbox-Images ..."
"$SCRIPT_DIR/build-sandbox.sh"

echo
echo "Backend-venv anlegen + Pakete installieren ..."
cd "$ROOT_DIR/backend"
# genau nach der Sperrdatei (uv.lock); uv holt die passende Python-Fassung
uv sync --frozen --extra dev --quiet
echo "  OK"

echo
echo "Frontend-Pakete installieren ..."
cd "$ROOT_DIR/frontend"
npm install --no-fund --no-audit --silent
echo "  OK"

echo
echo "=== Fertig ==="
echo
echo "Starten (Sandbox-Dienst, Backend und Frontend im Hintergrund):"
echo "  $SCRIPT_DIR/start.sh"
echo
echo "Stoppen:"
echo "  $SCRIPT_DIR/stop.sh"
echo
echo "Oder vollstaendig dockerisiert:"
echo "  cd $ROOT_DIR && docker compose up -d  # Browser dann auf http://localhost:8201"
echo
echo "Lokale Entwicklung -- Browser: http://localhost:5184"
