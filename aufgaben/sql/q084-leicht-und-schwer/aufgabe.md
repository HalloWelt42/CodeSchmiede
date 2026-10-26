---
schema_version: 1
id: q084-leicht-und-schwer
revision: 1
titel: Leicht und schwer
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- aggregat
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 8
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
- leichtester
- schwerster
sortierung_egal: false
erwartetes_ergebnis:
- - 2.9
  - 5.1
hints:
- kosten: 0
  text: MIN und MAX nebeneinander.
starter_code: ''
---

Hole das kleinste und das größte Gewicht aller Pinguine als Spalten `leichtester` und `schwerster`.
