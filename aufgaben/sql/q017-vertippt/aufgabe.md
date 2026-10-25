---
schema_version: 1
id: q017-vertippt
revision: 1
titel: Vertippt
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- select
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 1
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
- gewicht_kg
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 4.2
- - Pia
  - 3.8
- - Paul
  - 5.1
- - Pina
  - 3.5
- - Pepe
  - 4.9
- - Polly
  - 4.6
- - Pablo
  - 4.0
- - Pünktchen
  - 2.9
hints:
- kosten: 0
  text: Zwei Namen stimmen nicht; die richtigen zeigt die Vorschau des Datensatzes.
- kosten: 1
  text: '`gewicht_kg` und `pinguine`.'
starter_code: 'SELECT name, gewicht

  FROM pinguin;'
---

Diese Abfrage soll Name und Gewicht aller Pinguine holen, meldet aber Fehler. Repariere sie.
