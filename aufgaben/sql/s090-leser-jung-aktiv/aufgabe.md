---
schema_version: 1
id: s090-leser-jung-aktiv
revision: 1
titel: "Junge aktive Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [left-join, group-by, having, where]
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
erwartete_spalten: ["name", "alter_jahre", "ausleihen"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Clara Weber", 28, 3]
  - ["Anna Schmidt", 34, 2]
  - ["Greta Hoffmann", 25, 2]
  - ["Jonas Schaefer", 30, 2]
  - ["Lukas Richter", 22, 2]
  - ["David Fischer", 19, 1]
  - ["Niklas Wolf", 27, 1]
  - ["Olivia Krueger", 33, 1]
hints:
  - kosten: 0
    text: |
      WHERE auf Leser-Alter, HAVING auf Ausleih-Anzahl.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Junge aktive Leser

Leser unter 35 mit mindestens einer Ausleihe -- Name, Alter, Anzahl Ausleihen.
