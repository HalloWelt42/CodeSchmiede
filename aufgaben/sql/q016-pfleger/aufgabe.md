---
schema_version: 1
id: q016-pfleger
revision: 1
titel: Das Pflegeteam
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
- id
- name
- kolonie
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Greta
  - Nord
- - 2
  - Hannes
  - Süd
- - 3
  - Ida
  - Ost
- - 4
  - Jonas
  - null
hints:
- kosten: 0
  text: '`*` heißt alle Spalten.'
starter_code: ''
---

Hole alle Spalten der Tabelle `pfleger`. Bei einem Pfleger steht in der Kolonie NULL: er springt überall ein.
