---
schema_version: 1
id: q125-schwere-je-kolonie
revision: 1
titel: Schwergewichte je Kolonie
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- case
- group_by
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
- kolonie
- schwere
- alle
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - 3
  - 4
- - Ost
  - 0
  - 2
- - Süd
  - 1
  - 2
hints:
- kosten: 0
  text: Jeder schwere Pinguin trägt 1 bei, die anderen 0.
- kosten: 2
  text: '`SUM(CASE WHEN gewicht_kg > 4 THEN 1 ELSE 0 END)`'
starter_code: ''
---

Hole für jede Kolonie, wie viele ihrer Pinguine mehr als vier Kilo wiegen (Spalte `schwere`) und wie viele sie insgesamt hat (Spalte `alle`), sortiert nach Kolonie.
