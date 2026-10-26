---
schema_version: 1
id: q124-jung-oder-erfahren
revision: 1
titel: Jung oder erfahren
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
- stufe
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - erfahren
- - Pia
  - erfahren
- - Paul
  - erfahren
- - Pina
  - jung
- - Pepe
  - erfahren
- - Polly
  - erfahren
- - Pablo
  - jung
- - Pünktchen
  - jung
hints:
- kosten: 0
  text: '`CASE WHEN geburtsjahr >= 2021 THEN ... ELSE ... END`'
starter_code: ''
---

Hole für alle Pinguine den Namen und eine Spalte `stufe`: ab Geburtsjahr 2021 `'jung'`, sonst `'erfahren'`.
