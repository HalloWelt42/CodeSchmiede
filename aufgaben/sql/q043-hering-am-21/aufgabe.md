---
schema_version: 1
id: q043-hering-am-21
revision: 1
titel: Hering am 21. Oktober
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- logik
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
- pinguin_id
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - 5
- - 7
  - 4
hints:
- kosten: 0
  text: 'Beides muss stimmen: der Tag und der Fisch.'
starter_code: ''
---

Hole `pinguin_id` und `menge` aller Fütterungen vom 21. Oktober 2026 (`'2026-10-21'`), bei denen es Hering gab.
