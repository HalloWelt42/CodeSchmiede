---
schema_version: 1
id: q023-wie-alt
revision: 1
titel: Wie alt?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 2
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
- - Pit
  - 7
- - Pia
  - 6
- - Paul
  - 9
- - Pina
  - 4
- - Pepe
  - 8
- - Polly
  - 7
- - Pablo
  - 5
- - Pünktchen
  - 3
hints:
- kosten: 0
  text: '`2026 - geburtsjahr AS jahre`.'
starter_code: ''
---

Hole für jeden Pinguin den Namen und sein Alter im Jahr 2026 als Spalte `jahre` (2026 minus Geburtsjahr).
