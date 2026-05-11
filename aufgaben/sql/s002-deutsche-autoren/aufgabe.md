---
schema_version: 1
id: s002-deutsche-autoren
revision: 1
titel: "Deutsche Autoren alphabetisch"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [select, where, order-by]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- WHERE + ORDER BY.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: bibliothek
schema_hinweis: |
  autoren(id, name, geburtsjahr, land)
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Cornelia Funke"]
  - ["Hermann Hesse"]
  - ["Thomas Mann"]
hints:
  - kosten: 0
    text: |
      `WHERE` filtert Zeilen, `ORDER BY` sortiert. Filtere `land = 'Deutschland'`
      und sortiere nach `name`.
  - kosten: 3
    text: |
      `SELECT name FROM autoren WHERE land = 'Deutschland' ORDER BY name;`
starter_code: |
  SELECT name FROM autoren WHERE ___ ORDER BY ___;
---

# Deutsche Autoren alphabetisch

Liste die `name`-Spalte aller Autoren aus **Deutschland**, sortiert
alphabetisch.

3 Zeilen werden erwartet.
