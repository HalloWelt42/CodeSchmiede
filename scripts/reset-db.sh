#!/usr/bin/env bash
# Loescht die lokale SQLite-DB. ALLE Submissions, Progress und Streaks
# sind danach weg. Aufgaben bleiben (die kommen aus dem aufgaben/-Verzeichnis).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
DB="$ROOT_DIR/data/codeschmiede.db"

if [ ! -f "$DB" ]; then
  echo "Keine DB unter $DB -- nichts zu tun."
  exit 0
fi

echo "ACHTUNG: dies loescht alle Submissions, Progress und Streaks."
echo "Datei: $DB ($(du -h "$DB" | cut -f1))"
read -r -p "Wirklich loeschen? [j/N] " antwort
if [[ "$antwort" =~ ^[JjYy]$ ]]; then
  rm -f "$DB" "$DB-journal" "$DB-wal" "$DB-shm"
  echo "DB geloescht."
else
  echo "Abgebrochen."
  exit 1
fi
