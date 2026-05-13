#!/usr/bin/env bash
# Beendet Backend + Frontend anhand der gespeicherten PIDs aus
# data/codeschmiede.pids. Wenn die Datei fehlt oder die Prozesse
# nicht mehr existieren, wird das stillschweigend uebergangen.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PID_FILE="$ROOT_DIR/data/codeschmiede.pids"

if [ ! -f "$PID_FILE" ]; then
  echo "Keine PID-Datei gefunden ($PID_FILE) -- nichts zu beenden."
  exit 0
fi

while IFS=' ' read -r name pid; do
  if [ -z "${pid:-}" ]; then
    continue
  fi
  if kill -0 "$pid" 2>/dev/null; then
    echo "Beende $name (PID $pid) ..."
    kill "$pid" 2>/dev/null || true
    # bis zu 5 Sekunden auf sauberen Exit warten
    for i in 1 2 3 4 5; do
      if ! kill -0 "$pid" 2>/dev/null; then
        break
      fi
      sleep 1
    done
    if kill -0 "$pid" 2>/dev/null; then
      echo "  reagiert nicht, erzwinge mit -9"
      kill -9 "$pid" 2>/dev/null || true
    fi
  else
    echo "$name (PID $pid) lief nicht mehr."
  fi
done < "$PID_FILE"

rm -f "$PID_FILE"
echo "Codeschmiede beendet."
