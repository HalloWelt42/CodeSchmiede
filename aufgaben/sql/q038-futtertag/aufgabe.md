---
schema_version: 1
id: q038-futtertag
revision: 1
titel: Der Futtertag
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- where
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 3
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
- fisch
- gramm
sortierung_egal: false
erwartetes_ergebnis:
- - Hering
  - 600
- - Sardine
  - 360
- - Lachs
  - 720
- - Hering
  - 480
hints:
- kosten: 0
  text: Der Tag steht als Text in der Spalte `tag`.
- kosten: 2
  text: '`WHERE tag = ''2026-10-21''`.'
starter_code: ''
---

Hole für den 21. Oktober 2026 (`'2026-10-21'`) jeden Fisch und das Gewicht des Futters in Gramm (ein Fisch wiegt 120 Gramm) als Spalte `gramm`.
