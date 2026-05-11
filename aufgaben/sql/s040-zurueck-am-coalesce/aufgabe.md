---
schema_version: 1
id: s040-zurueck-am-coalesce
revision: 1
titel: "Rückgabe-Datum oder 'offen'"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [coalesce, null-handling]
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
erwartete_spalten: ["id", "zurueck"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, "2025-01-19"]
  - [2, "2025-03-02"]
  - [3, "2025-02-04"]
  - [4, "offen"]
  - [5, "2025-03-04"]
  - [6, "2025-03-22"]
  - [7, "offen"]
  - [8, "2025-02-15"]
  - [9, "2024-12-24"]
  - [10, "2025-02-12"]
  - [11, "2025-04-05"]
  - [12, "2025-03-08"]
  - [13, "offen"]
  - [14, "offen"]
  - [15, "2024-12-01"]
  - [16, "2025-02-28"]
  - [17, "2025-04-10"]
  - [18, "offen"]
  - [19, "2025-02-20"]
  - [20, "2025-03-25"]
  - [21, "2025-03-05"]
  - [22, "2025-04-01"]
  - [23, "offen"]
  - [24, "2025-02-10"]
  - [25, "2025-04-08"]
  - [26, "offen"]
  - [27, "offen"]
hints:
  - kosten: 0
    text: |
      `COALESCE(a, b)` liefert `a`, oder `b` wenn `a` NULL ist.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Rückgabe-Datum oder offen

Für jede Ausleihe ID + Rückgabe-Datum oder 'offen' wenn NULL.
