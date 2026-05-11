---
schema_version: 1
id: s029-autoren-pro-land
revision: 1
titel: "Autoren pro Land"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [group-by, count]
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
erwartete_spalten: ["land", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Deutschland", 3]
  - ["Großbritannien", 2]
  - ["Japan", 1]
  - ["Schweden", 1]
  - ["Tschechien", 1]
  - ["USA", 1]
  - ["Österreich", 1]
hints:
  - kosten: 0
    text: |
      `GROUP BY land`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autoren pro Land

Land + Anzahl Autoren, hauefigstes Land zuerst.
