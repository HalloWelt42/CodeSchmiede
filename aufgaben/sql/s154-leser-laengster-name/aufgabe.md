---
schema_version: 1
id: s154-leser-laengster-name
revision: 1
titel: "Leser mit längstem Namen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [subquery, length, max]
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
  - ["Greta Hoffmann"]
  - ["Jonas Schaefer"]
  - ["Olivia Krueger"]
hints:
  - kosten: 0
    text: |
      Subquery liefert MAX(LENGTH(name)).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Längster Lesername

Leser mit dem längsten Namen (kann mehrere geben).
