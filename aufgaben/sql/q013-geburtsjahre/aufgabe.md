---
schema_version: 1
id: q013-geburtsjahre
revision: 1
titel: Wer ist wie alt?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
- geburtsjahr
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 2019
- - Pia
  - 2020
- - Paul
  - 2017
- - Pina
  - 2022
- - Pepe
  - 2018
- - Polly
  - 2019
- - Pablo
  - 2021
- - Pünktchen
  - 2023
hints:
- kosten: 0
  text: Zwei Spalten hinter SELECT, mit Komma getrennt.
starter_code: ''
---

Hole Name und Geburtsjahr aller Pinguine, in dieser Reihenfolge.
