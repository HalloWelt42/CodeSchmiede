---
schema_version: 1
id: s101-rcte-zahlen-1-10
revision: 1
titel: "Recursive CTE: Zahlen 1 bis 10"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [recursive-cte, with]
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
erwartete_spalten: ["n"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1]
  - [2]
  - [3]
  - [4]
  - [5]
  - [6]
  - [7]
  - [8]
  - [9]
  - [10]
hints:
  - kosten: 0
    text: |
      `WITH RECURSIVE name(spalte) AS (Basisfall UNION ALL Rekursionsschritt)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Recursive CTE: 1 bis 10

Generiere die Zahlen 1 bis 10 per recursive CTE.
