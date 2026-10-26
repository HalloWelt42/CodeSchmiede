---
schema_version: 1
id: q155-west-wird-abgerissen
revision: 1
titel: Die leere Kolonie
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- delete
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 15
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
kontrolle: SELECT * FROM kolonien ORDER BY name
erwartete_spalten:
- name
- lage
- wassertemperatur
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
  - -1.5
- - Ost
  - Sandstrand
  - 9.5
- - Süd
  - Felsenküste
  - 4.0
hints:
- kosten: 0
  text: Die Spalte heißt name.
starter_code: ''
---

Die Westkolonie hat keine Pinguine und soll weg. Lösche sie aus der Tabelle kolonien.
