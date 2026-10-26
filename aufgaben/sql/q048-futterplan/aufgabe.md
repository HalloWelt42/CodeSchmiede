---
schema_version: 1
id: q048-futterplan
revision: 1
titel: Der Futterplan
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- logik
- in_between
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 4
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
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - 1
  - Hering
  - 6
- - '2026-10-20'
  - 3
  - Hering
  - 8
- - '2026-10-20'
  - 5
  - Makrele
  - 5
- - '2026-10-21'
  - 1
  - Hering
  - 5
hints:
- kosten: 0
  text: Drei Bedingungen, alle mit AND.
- kosten: 2
  text: '`tag BETWEEN ''2026-10-20'' AND ''2026-10-21''`'
starter_code: ''
---

Hole Tag, `pinguin_id`, Fisch und Menge aller Fütterungen vom 20. bis 21. Oktober 2026, bei denen es Hering oder Makrele gab, und zwar mindestens fünf Stück. Tage stehen als Text wie `'2026-10-20'` in der Tabelle; weil das Jahr vorn steht, lassen sie sich vergleichen wie Zahlen, auch mit BETWEEN.
