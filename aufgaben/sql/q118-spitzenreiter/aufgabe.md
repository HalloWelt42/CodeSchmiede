---
schema_version: 1
id: q118-spitzenreiter
revision: 1
titel: Die Spitzenreiter
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- unterabfrage
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 11
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
- - Paul
  - 5.1
hints:
- kosten: 0
  text: Zwei Unterabfragen, mit AND verbunden.
- kosten: 2
  text: '`AND id IN (SELECT pinguin_id FROM fuetterungen WHERE fisch = ''Hering'')`'
starter_code: ''
---

Hole Name und Gewicht aller Pinguine, die schwerer sind als der Durchschnitt aller Pinguine und schon einmal Hering bekommen haben.
