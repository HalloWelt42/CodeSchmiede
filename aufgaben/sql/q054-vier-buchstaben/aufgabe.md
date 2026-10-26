---
schema_version: 1
id: q054-vier-buchstaben
revision: 1
titel: Genau vier Buchstaben
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
- - Pina
- - Pepe
hints:
- kosten: 0
  text: Ein Unterstrich steht für genau ein Zeichen.
starter_code: ''
---

Hole die Namen aller Pinguine, die genau vier Buchstaben lang sind. Benutze LIKE.
