---
schema_version: 1
id: s114-leser-kohorten
revision: 1
titel: "Leser-Kohorten (Beitrittsjahr)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [date, group-by, avg]
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
erwartete_spalten: ["kohorte", "anzahl", "schnitt_alter"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2008", 1, 61.0]
  - ["2010", 1, 56.0]
  - ["2012", 1, 52.0]
  - ["2014", 1, 45.0]
  - ["2015", 1, 42.0]
  - ["2016", 1, 39.0]
  - ["2017", 1, 37.0]
  - ["2018", 2, 33.5]
  - ["2019", 1, 30.0]
  - ["2020", 2, 27.5]
  - ["2021", 1, 25.0]
  - ["2022", 1, 19.0]
  - ["2023", 1, 22.0]
hints:
  - kosten: 0
    text: |
      GROUP BY Beitrittsjahr, dazu Average-Alter.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser-Kohorten

Kohorte (Beitrittsjahr) + Anzahl Leser + Durchschnittsalter, chronologisch.
