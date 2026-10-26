---
schema_version: 1
id: q096-schwerste-je-kolonie
revision: 1
titel: Die Schwersten der Erwachsenen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- group_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 9
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
- schwerster
sortierung_egal: true
erwartetes_ergebnis:
- - Nord
  - 5.1
- - Ost
  - 4.0
- - Süd
  - 4.9
hints:
- kosten: 0
  text: Die Bedingung betrifft einzelne Pinguine, also WHERE vor GROUP BY.
starter_code: ''
---

Hole für jede Kolonie das größte Gewicht (Spalte `schwerster`), zähle dabei aber nur Pinguine, die vor 2022 geboren sind.
