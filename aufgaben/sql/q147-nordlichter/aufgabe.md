---
schema_version: 1
id: q147-nordlichter
revision: 1
titel: Mehr für die Nordlichter
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- update
- unterabfrage
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 14
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
kontrolle: SELECT id, pinguin_id, menge FROM fuetterungen ORDER BY id
erwartete_spalten:
- id
- pinguin_id
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - 1
  - 7
- - 2
  - 2
  - 4
- - 3
  - 3
  - 9
- - 4
  - 5
  - 5
- - 5
  - 1
  - 6
- - 6
  - 4
  - 4
- - 7
  - 6
  - 7
- - 8
  - 7
  - 4
- - 9
  - 3
  - 8
- - 10
  - 8
  - 2
- - 11
  - 2
  - 5
- - 12
  - 1
  - 4
hints:
- kosten: 0
  text: '`WHERE pinguin_id IN (SELECT id FROM pinguine WHERE ...)`'
starter_code: ''
---

Alle Fütterungen von Pinguinen der Nordkolonie bekommen einen Fisch mehr. In fuetterungen steht nur die Nummer des Pinguins; wähle die Zeilen mit einer Unterabfrage aus.
