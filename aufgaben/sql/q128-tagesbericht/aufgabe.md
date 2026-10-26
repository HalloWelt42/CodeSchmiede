---
schema_version: 1
id: q128-tagesbericht
revision: 1
titel: Der Tagesbericht
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- case
- group_by
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 12
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
- grosse
- lachs
- alle
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - 2
  - 4
  - 23
- - '2026-10-21'
  - 1
  - 6
  - 18
- - '2026-10-22'
  - 1
  - 5
  - 17
hints:
- kosten: 0
  text: 'Zwei SUM mit CASE: einmal Einsen zählen, einmal Mengen summieren.'
- kosten: 2
  text: '`SUM(CASE WHEN fisch = ''Lachs'' THEN menge ELSE 0 END) AS lachs`'
starter_code: ''
---

Hole für jeden Tag, sortiert nach Tag: wie viele große Portionen mit mindestens sechs Fischen es gab (Spalte `grosse`), wie viele Lachse verfüttert wurden (Spalte `lachs`) und wie viele Fische insgesamt (Spalte `alle`).
