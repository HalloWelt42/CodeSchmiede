---
schema_version: 1
id: s006-leser-orte
revision: 1
titel: "Distinct Orte der Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [select, distinct, order-by]
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
  - ["Berlin"]
  - ["Dresden"]
  - ["Frankfurt"]
  - ["Hamburg"]
  - ["Köln"]
  - ["Leipzig"]
  - ["München"]
  - ["Stuttgart"]
hints:
  - kosten: 0
    text: |
      `DISTINCT` entfernt Duplikate. `ORDER BY ort` sortiert alphabetisch.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Distinct Orte der Leser

Liefere jede Stadt nur einmal, alphabetisch sortiert.
