---
schema_version: 1
id: s109-ueberfaellig
revision: 1
titel: "Überfaellige Bücher (> 30 Tage offen)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
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
  - [27, 15, 8, "2025-02-25"]
  - [4, 2, 8, "2025-03-01"]
  - [7, 3, 17, "2025-04-01"]
  - [26, 14, 6, "2025-04-01"]
  - [23, 12, 12, "2025-04-05"]
  - [13, 7, 9, "2025-04-12"]
  - [14, 7, 18, "2025-04-12"]
  - [18, 9, 14, "2025-04-15"]
hints:
  - kosten: 0
    text: |
      Heutiges Datum hardcoden. julianday-Diff > 30.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Überfaellige Bücher

Ausleihen, die noch offen sind und vor mehr als 30 Tagen (Stichtag 2026-05-11) begonnen wurden.
