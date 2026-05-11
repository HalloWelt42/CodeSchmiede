---
schema_version: 1
id: s046-mitglieder-pro-jahr
revision: 1
titel: "Neue Mitglieder pro Jahr"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [date, group-by, count]
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
erwartete_spalten: ["jahr", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2008", 1]
  - ["2010", 1]
  - ["2012", 1]
  - ["2014", 1]
  - ["2015", 1]
  - ["2016", 1]
  - ["2017", 1]
  - ["2018", 2]
  - ["2019", 1]
  - ["2020", 2]
  - ["2021", 1]
  - ["2022", 1]
  - ["2023", 1]
hints:
  - kosten: 0
    text: |
      GROUP BY auf strftime-Ausdruck.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Neue Mitglieder pro Jahr

Jahr + Anzahl der Beitritte, chronologisch.
