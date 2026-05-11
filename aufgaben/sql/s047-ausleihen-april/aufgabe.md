---
schema_version: 1
id: s047-ausleihen-april
revision: 1
titel: "Ausleihen im April 2025"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [date, between]
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
  - [7, 3, 17, "2025-04-01"]
  - [26, 14, 6, "2025-04-01"]
  - [23, 12, 12, "2025-04-05"]
  - [13, 7, 9, "2025-04-12"]
  - [14, 7, 18, "2025-04-12"]
  - [18, 9, 14, "2025-04-15"]
hints:
  - kosten: 0
    text: |
      Im ISO-Format reicht ein BETWEEN auf Strings.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Ausleihen im April 2025

Alle Ausleihen, die im April 2025 begonnen wurden.
