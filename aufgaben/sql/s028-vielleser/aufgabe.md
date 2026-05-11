---
schema_version: 1
id: s028-vielleser
revision: 1
titel: "Viel-Leser (3+ Ausleihen)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 7
tags: [join, group-by, having]
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
erwartete_spalten: ["name", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Clara Weber", 3]
  - ["Eva Schulz", 3]
hints:
  - kosten: 0
    text: |
      `HAVING` filtert nach Aggregaten -- nicht `WHERE`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Viel-Leser

Leser, die mindestens 3 Buecher ausgeliehen haben (auch zurueckgegebene zaehlen).
