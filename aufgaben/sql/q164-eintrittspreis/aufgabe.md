---
schema_version: 1
id: q164-eintrittspreis
revision: 1
titel: Der Eintrittspreis
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- create_table
- insert
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 16
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
kontrolle: SELECT besucher, preis FROM eintritt ORDER BY id
erwartete_spalten:
- besucher
- preis
sortierung_egal: false
erwartetes_ergebnis:
- - Mia
  - 12.5
hints:
- kosten: 0
  text: '`preis REAL NOT NULL DEFAULT 12.5`'
- kosten: 1
  text: Beim INSERT nur die Spalte besucher nennen.
starter_code: ''
---

Lege die Tabelle eintritt an mit id (INTEGER PRIMARY KEY), besucher (TEXT, Pflicht) und preis (REAL, Pflicht, Vorgabewert 12,5). Trage dann Mia ein, ohne einen Preis anzugeben.
