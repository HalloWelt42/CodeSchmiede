---
schema_version: 1
id: q153-ohne-sardinen
revision: 1
titel: Ohne Sardinen
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- delete
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 15
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
kontrolle: SELECT * FROM fuetterungen ORDER BY id
erwartete_spalten:
- id
- pinguin_id
- tag
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - 1
  - '2026-10-20'
  - Hering
  - 6
- - 2
  - 2
  - '2026-10-20'
  - Lachs
  - 4
- - 3
  - 3
  - '2026-10-20'
  - Hering
  - 8
- - 4
  - 5
  - '2026-10-20'
  - Makrele
  - 5
- - 5
  - 1
  - '2026-10-21'
  - Hering
  - 5
- - 7
  - 6
  - '2026-10-21'
  - Lachs
  - 6
- - 8
  - 7
  - '2026-10-21'
  - Hering
  - 4
- - 9
  - 3
  - '2026-10-22'
  - Makrele
  - 7
- - 11
  - 2
  - '2026-10-22'
  - Lachs
  - 5
hints:
- kosten: 0
  text: '`WHERE fisch = ''Sardine''`'
starter_code: ''
---

Lösche alle Fütterungen mit Sardinen.
