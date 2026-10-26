---
schema_version: 1
id: q093-mahlzeiten
revision: 1
titel: Mahlzeiten je Pinguin
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
- pinguin_id
- mahlzeiten
sortierung_egal: true
erwartetes_ergebnis:
- - 1
  - 3
- - 2
  - 2
- - 3
  - 2
- - 4
  - 1
- - 5
  - 1
- - 6
  - 1
- - 7
  - 1
- - 8
  - 1
hints:
- kosten: 0
  text: '`GROUP BY pinguin_id` und `COUNT(*)`.'
starter_code: ''
---

Hole für jede `pinguin_id` aus `fuetterungen`, wie oft dieser Pinguin gefüttert wurde (Spalte `mahlzeiten`).
