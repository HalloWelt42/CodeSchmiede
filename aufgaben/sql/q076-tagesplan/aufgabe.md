---
schema_version: 1
id: q076-tagesplan
revision: 1
titel: Der Tagesplan
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- order_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 7
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
- tag
- pinguin_id
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - 3
  - 8
- - '2026-10-20'
  - 1
  - 6
- - '2026-10-20'
  - 5
  - 5
- - '2026-10-20'
  - 2
  - 4
- - '2026-10-21'
  - 6
  - 6
- - '2026-10-21'
  - 1
  - 5
- - '2026-10-21'
  - 7
  - 4
- - '2026-10-21'
  - 4
  - 3
- - '2026-10-22'
  - 3
  - 7
- - '2026-10-22'
  - 2
  - 5
- - '2026-10-22'
  - 1
  - 3
- - '2026-10-22'
  - 8
  - 2
hints:
- kosten: 0
  text: Zwei Spalten hinter ORDER BY; DESC gilt nur für die davor.
starter_code: ''
---

Hole Tag, `pinguin_id` und Menge aller Fütterungen, sortiert nach Tag und innerhalb eines Tages die größte Menge zuerst.
