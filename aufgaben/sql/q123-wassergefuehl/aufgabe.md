---
schema_version: 1
id: q123-wassergefuehl
revision: 1
titel: Wie fühlt sich das Wasser an?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- case
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 12
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
- gefuehl
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - -1.5
  - eisig
- - Süd
  - 4.0
  - frisch
- - Ost
  - 9.5
  - mild
- - West
  - -0.5
  - eisig
hints:
- kosten: 0
  text: Die strengste Bedingung zuerst.
- kosten: 2
  text: '`CASE WHEN wassertemperatur < 0 THEN ''eisig'' WHEN ...`'
starter_code: ''
---

Hole Name und Wassertemperatur jeder Kolonie und eine Spalte `gefuehl`: unter null Grad `'eisig'`, unter fünf Grad `'frisch'`, sonst `'mild'`.
