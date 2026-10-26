---
schema_version: 1
id: q105-warmes-wasser
revision: 1
titel: Nichts für Frostbeulen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- join
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 10
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
- wassertemperatur
sortierung_egal: true
erwartetes_ergebnis:
- - Pia
  - 4.0
- - Pepe
  - 4.0
- - Pablo
  - 9.5
- - Pünktchen
  - 9.5
hints:
- kosten: 0
  text: Erst verbinden, dann mit WHERE sieben.
starter_code: ''
---

Hole Name und Wassertemperatur aller Pinguine, deren Kolonie Wasser über null Grad hat.
