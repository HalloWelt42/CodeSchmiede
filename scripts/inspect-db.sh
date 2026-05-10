#!/usr/bin/env bash
# Schnellinspektion der DB: Tabellen-Counts, letzte Submissions, Streak.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
DB="$ROOT_DIR/data/codeschmiede.db"

if [ ! -f "$DB" ]; then
  echo "Keine DB unter $DB. Backend einmal gestartet?"
  exit 1
fi

echo "Datei: $DB ($(du -h "$DB" | cut -f1))"
echo

echo "Tabellen-Counts:"
for tabelle in aufgaben aufgaben_versionen pfade submissions progress kv_state schema_version; do
  n=$(sqlite3 "$DB" "SELECT COUNT(*) FROM $tabelle" 2>/dev/null || echo "?")
  printf "  %-22s %s\n" "$tabelle" "$n"
done

echo
echo "Letzte 5 Submissions:"
sqlite3 -column -header "$DB" \
  "SELECT id, aufgabe_id, bestanden, ROUND(laufzeit_ms,0) AS ms, datetime(zeitstempel) AS zeit
   FROM submissions ORDER BY id DESC LIMIT 5" 2>/dev/null || echo "  (keine)"

echo
echo "Streak:"
sqlite3 -column -header "$DB" \
  "SELECT key, value FROM kv_state WHERE key LIKE 'streak.%'" 2>/dev/null || echo "  (kein Eintrag)"

echo
echo "Faellige Wiederholungen heute:"
sqlite3 -column -header "$DB" \
  "SELECT aufgabe_id, faellig_am, intervall_tage, ease
   FROM progress
   WHERE faellig_am IS NOT NULL AND faellig_am <= date('now') AND status = 'geloest'" \
  2>/dev/null || echo "  (keine)"
