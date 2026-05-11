---
schema_version: 1
id: s102-rcte-fibonacci
revision: 1
titel: "Recursive CTE: Fibonacci bis Index 10"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [recursive-cte, fibonacci]
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
erwartete_spalten: ["i", "wert"]
sortierung_egal: false
erwartetes_ergebnis:
  - [0, 0]
  - [1, 1]
  - [2, 1]
  - [3, 2]
  - [4, 3]
  - [5, 5]
  - [6, 8]
  - [7, 13]
  - [8, 21]
  - [9, 34]
  - [10, 55]
hints:
  - kosten: 0
    text: |
      Recursive CTE mit zwei akkumulierten Spalten a, b. Tausche pro Schritt.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Fibonacci-Folge

Index 0..10 + Fibonacci-Wert.
