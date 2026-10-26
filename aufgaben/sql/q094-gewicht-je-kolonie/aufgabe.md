---
schema_version: 1
id: q094-gewicht-je-kolonie
revision: 1
titel: Gewicht je Kolonie
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- group_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
dataset: pinguinzoo
schema_hinweis: 'kolonien(name, lage, wassertemperatur)

  pinguine(id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)

  pfleger(id, name, kolonie)

  fuetterungen(id, pinguin_id, tag, fisch, menge)

  '
erwartete_spalten:
- kolonie
- schnitt
sortierung_egal: true
erwartetes_ergebnis:
- - Nord
  - 4.35
- - Ost
  - 3.45
- - Süd
  - 4.35
hints:
- kosten: 0
  text: '`ROUND(AVG(gewicht_kg), 2)` je Kolonie.'
starter_code: ''
---

Hole für jede Kolonie das Durchschnittsgewicht ihrer Pinguine, auf zwei Stellen gerundet (Spalte `schnitt`).
