---
schema_version: 1
id: s128-leser-ohne-letztes-jahr
revision: 1
titel: "Inaktive Leser (keine Ausleihe in 2025)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [subquery, not-in, date]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  []
hints:
  - kosten: 0
    text: |
      NOT IN mit Subquery, Date-Filter via strftime.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Inaktive Leser

Leser, die in 2025 keine Ausleihe getaetigt haben.
