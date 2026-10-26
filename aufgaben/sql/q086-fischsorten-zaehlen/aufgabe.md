---
schema_version: 1
id: q086-fischsorten-zaehlen
revision: 1
titel: Wie viele Sorten?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- aggregat
- distinct
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
- sorten
sortierung_egal: false
erwartetes_ergebnis:
- - 4
hints:
- kosten: 0
  text: Jeder Fisch soll nur einmal zählen.
- kosten: 2
  text: '`COUNT(DISTINCT fisch)`'
starter_code: ''
---

Wie viele verschiedene Fischsorten wurden verfüttert? Die Spalte heißt `sorten`.
