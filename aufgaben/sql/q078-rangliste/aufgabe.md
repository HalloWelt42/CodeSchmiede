---
schema_version: 1
id: q078-rangliste
revision: 1
titel: Die Altersrangliste
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- order_by
- limit
- kurztest
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
- name
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - 9
- - Pepe
  - 8
- - Pit
  - 7
hints:
- kosten: 0
  text: WHERE, dann ORDER BY mit zwei Spalten, dann LIMIT.
- kosten: 2
  text: '`ORDER BY jahre DESC, name`'
starter_code: ''
---

Hole Name und Alter im Jahr 2026 (Spalte `jahre`) der drei ältesten Pinguine aus Nord und Süd. Bei gleichem Alter entscheidet der Name nach dem Alphabet.
