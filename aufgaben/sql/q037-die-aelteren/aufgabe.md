---
schema_version: 1
id: q037-die-aelteren
revision: 1
titel: Die Älteren
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- where
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 3
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
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 7
- - Pia
  - 6
- - Paul
  - 9
- - Pepe
  - 8
- - Polly
  - 7
hints:
- kosten: 0
  text: Auch in WHERE darf gerechnet werden.
- kosten: 2
  text: '`WHERE 2026 - geburtsjahr > 5`; der Name jahre gilt in WHERE noch nicht, denn WHERE arbeitet vor SELECT.'
starter_code: ''
---

Hole Name und Alter im Jahr 2026 (Spalte `jahre`) aller Pinguine, die 2026 älter als fünf Jahre sind.
