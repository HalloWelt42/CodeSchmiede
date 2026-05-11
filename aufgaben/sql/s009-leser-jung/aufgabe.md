---
schema_version: 1
id: s009-leser-jung
revision: 1
titel: "Junge Leser unter 25"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [where, vergleich]
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
erwartete_spalten: ["name", "alter_jahre"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["David Fischer", 19]
  - ["Lukas Richter", 22]
hints:
  - kosten: 0
    text: |
      `WHERE alter_jahre < 25`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Junge Leser unter 25

Name und Alter aller Leser unter 25, jung-zuerst.
