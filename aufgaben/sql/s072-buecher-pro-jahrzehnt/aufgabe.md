---
schema_version: 1
id: s072-buecher-pro-jahrzehnt
revision: 1
titel: "Buecher pro Jahrzehnt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, expression, math]
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
erwartete_spalten: ["jahrzehnt", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1810, 2]
  - [1900, 1]
  - [1910, 1]
  - [1920, 4]
  - [1940, 5]
  - [1950, 1]
  - [1960, 2]
  - [1980, 1]
  - [1990, 1]
  - [2000, 2]
hints:
  - kosten: 0
    text: |
      `(jahr / 10) * 10` rundet auf 1900, 1910, 1920 ab (Integer-Division).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buecher pro Jahrzehnt

Jahrzehnt + Anzahl Buecher. 1903 -> 1900, 1949 -> 1940 etc.
