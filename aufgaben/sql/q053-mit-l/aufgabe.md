---
schema_version: 1
id: q053-mit-l
revision: 1
titel: Ein l im Namen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- like
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 5
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
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
- - Polly
- - Pablo
hints:
- kosten: 0
  text: 'Das l darf überall stehen: `''%l%''`.'
starter_code: ''
---

Hole die Namen aller Pinguine, in deren Namen irgendwo ein l steht.
