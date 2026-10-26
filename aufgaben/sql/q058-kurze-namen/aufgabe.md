---
schema_version: 1
id: q058-kurze-namen
revision: 1
titel: Große Schilder für kurze Namen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- like
- textfunktionen
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 5
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
- schild
- laenge
sortierung_egal: false
erwartetes_ergebnis:
- - PIA
  - 3
- - PAUL
  - 4
- - PINA
  - 4
hints:
- kosten: 0
  text: LIKE und LENGTH in WHERE, mit AND verbunden.
- kosten: 2
  text: '`WHERE name LIKE ''%a%'' AND LENGTH(name) <= 4`'
starter_code: ''
---

Für kurze Namen gibt es große Schilder. Hole für alle Pinguine mit einem a im Namen und höchstens vier Zeichen den Namen in Großbuchstaben (Spalte `schild`) und die Länge des Namens (Spalte `laenge`).
