---
schema_version: 1
id: s042-orte-gross
revision: 1
titel: "Leserorte in Großbuchstaben"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [string, upper, distinct]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: bibliothek
schema_hinweis: |
  autoren(id, name, geburtsjahr, land)
  buecher(id, titel, autor_id, jahr, seiten, kategorie, exemplare)
  leser(id, name, ort, alter_jahre, mitglied_seit)
  ausleihen(id, leser_id, buch_id, ausgeliehen_am, zurueck_am)
erwartete_spalten: ["ort"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["BERLIN"]
  - ["DRESDEN"]
  - ["FRANKFURT"]
  - ["HAMBURG"]
  - ["KOELN"]
  - ["LEIPZIG"]
  - ["MUENCHEN"]
  - ["STUTTGART"]
hints:
  - kosten: 0
    text: |
      `UPPER(ort)` macht Großbuchstaben.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leserorte in Großbuchstaben

Alle distinkten Orte als UPPERCASE, sortiert.
