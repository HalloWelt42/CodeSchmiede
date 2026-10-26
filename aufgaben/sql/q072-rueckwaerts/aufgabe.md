---
schema_version: 1
id: q072-rueckwaerts
revision: 1
titel: Das Alphabet rückwärts
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- order_by
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
sortierung_egal: false
erwartetes_ergebnis:
- - Pünktchen
- - Polly
- - Pit
- - Pina
- - Pia
- - Pepe
- - Paul
- - Pablo
hints:
- kosten: 0
  text: Absteigend heißt DESC.
starter_code: 'SELECT name

  FROM pinguine

  ORDER BY name ___;'
---

Ergänze die Lücke `___`, damit die Namen rückwärts nach dem Alphabet kommen.
