---
schema_version: 1
id: s032-leser-ohne-ausleihe
revision: 1
titel: "Leser ohne Ausleihen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [left-join, anti-join, is-null]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  []
hints:
  - kosten: 0
    text: |
      LEFT JOIN + WHERE Joined-Spalte IS NULL = Anti-Join.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser ohne Ausleihen

Leser, die noch nie etwas ausgeliehen haben.
