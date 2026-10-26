---
schema_version: 1
id: q144-nachschlag
revision: 1
titel: Nachschlag am 21.
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- update
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
kontrolle: SELECT id, tag, menge FROM fuetterungen ORDER BY id
erwartete_spalten:
- id
- tag
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - '2026-10-20'
  - 6
- - 2
  - '2026-10-20'
  - 4
- - 3
  - '2026-10-20'
  - 8
- - 4
  - '2026-10-20'
  - 5
- - 5
  - '2026-10-21'
  - 7
- - 6
  - '2026-10-21'
  - 5
- - 7
  - '2026-10-21'
  - 8
- - 8
  - '2026-10-21'
  - 6
- - 9
  - '2026-10-22'
  - 7
- - 10
  - '2026-10-22'
  - 2
- - 11
  - '2026-10-22'
  - 5
- - 12
  - '2026-10-22'
  - 3
hints:
- kosten: 0
  text: '`SET menge = menge + 2`'
starter_code: ''
---

Alle Fütterungen vom 21. Oktober 2026 bekommen nachträglich zwei Fische mehr.
