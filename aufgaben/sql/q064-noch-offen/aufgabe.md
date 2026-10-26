---
schema_version: 1
id: q064-noch-offen
revision: 1
titel: Noch offen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- null_werte
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 6
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
- fisch
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Hering
- - Pia
  - Lachs
- - Paul
  - Hering
- - Pina
  - noch offen
- - Pepe
  - Makrele
- - Polly
  - Lachs
- - Pablo
  - Hering
- - Pünktchen
  - noch offen
hints:
- kosten: 0
  text: '`COALESCE(wert, ersatz)`'
starter_code: ''
---

Hole für alle Pinguine den Namen und den Lieblingsfisch als Spalte `fisch`; wo er unbekannt ist, soll `'noch offen'` stehen.
