---
schema_version: 1
id: q044-pfleger-nord-ost
revision: 1
titel: Pfleger im Norden und Osten
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- in_between
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
sortierung_egal: false
erwartetes_ergebnis:
- - Greta
- - Ida
hints:
- kosten: 0
  text: '`kolonie IN (''Nord'', ''Ost'')`.'
starter_code: ''
---

Hole die Namen der Pfleger, die für die Kolonie Nord oder Ost zuständig sind. Schreib es mit IN.
