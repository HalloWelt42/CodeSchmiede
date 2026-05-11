---
schema_version: 1
id: s153-ausleihen-letzten-30-tage
revision: 1
titel: "Ausleihen der letzten 30 Tage"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [date, julianday, where]
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
erwartete_spalten: ["id", "leser_id", "buch_id", "ausgeliehen_am"]
sortierung_egal: false
erwartetes_ergebnis:
  - [18, 9, 14, "2025-04-15"]
  - [13, 7, 9, "2025-04-12"]
  - [14, 7, 18, "2025-04-12"]
  - [23, 12, 12, "2025-04-05"]
  - [7, 3, 17, "2025-04-01"]
  - [26, 14, 6, "2025-04-01"]
hints:
  - kosten: 0
    text: |
      Stichtag 2025-05-01, julianday-Diff <= 30.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Letzte 30 Tage

Ausleihen, die in den 30 Tagen vor dem 2025-05-01 begonnen wurden, jüngste zuerst.
