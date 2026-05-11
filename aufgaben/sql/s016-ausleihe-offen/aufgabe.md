---
schema_version: 1
id: s016-ausleihe-offen
revision: 1
titel: "Offene Ausleihen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [where, is-null]
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
erwartete_spalten: ["id", "leser_id", "buch_id"]
sortierung_egal: false
erwartetes_ergebnis:
  - [4, 2, 8]
  - [7, 3, 17]
  - [13, 7, 9]
  - [14, 7, 18]
  - [18, 9, 14]
  - [23, 12, 12]
  - [26, 14, 6]
  - [27, 15, 8]
hints:
  - kosten: 0
    text: |
      `IS NULL` -- nicht `= NULL`!
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Offene Ausleihen

IDs, Leser-ID und Buch-ID aller noch nicht zurueckgegebenen Ausleihen.
