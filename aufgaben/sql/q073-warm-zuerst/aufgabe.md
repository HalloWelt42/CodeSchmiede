---
schema_version: 1
id: q073-warm-zuerst
revision: 1
titel: Warm zuerst
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- order_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 7
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
sortierung_egal: false
erwartetes_ergebnis:
- - Ost
  - 9.5
- - Süd
  - 4.0
- - West
  - -0.5
- - Nord
  - -1.5
hints:
- kosten: 0
  text: '`ORDER BY wassertemperatur DESC`'
starter_code: ''
---

Hole Name und Wassertemperatur aller Kolonien, die wärmste zuerst.
