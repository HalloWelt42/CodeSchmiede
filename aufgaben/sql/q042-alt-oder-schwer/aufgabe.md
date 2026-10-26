---
schema_version: 1
id: q042-alt-oder-schwer
revision: 1
titel: Alt oder schwer
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
- name
- geburtsjahr
- gewicht_kg
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - 2017
  - 5.1
- - Pepe
  - 2018
  - 4.9
- - Polly
  - 2019
  - 4.6
hints:
- kosten: 0
  text: Eine der beiden Bedingungen reicht.
starter_code: 'SELECT name, geburtsjahr, gewicht_kg

  FROM pinguine

  WHERE geburtsjahr < 2019 ___ gewicht_kg > 4.5;'
---

Ergänze die Lücke `___`, damit alle Pinguine kommen, die vor 2019 geboren sind oder mehr als 4,5 Kilo wiegen.
