---
schema_version: 1
id: q103-wer-pflegt-wen
revision: 1
titel: Wer pflegt wen?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
- pinguin
- pfleger
sortierung_egal: true
erwartetes_ergebnis:
- - Pit
  - Greta
- - Pia
  - Hannes
- - Paul
  - Greta
- - Pina
  - Greta
- - Pepe
  - Hannes
- - Polly
  - Greta
- - Pablo
  - Ida
- - Pünktchen
  - Ida
hints:
- kosten: 0
  text: Beide Tabellen haben eine Spalte kolonie.
- kosten: 2
  text: '`JOIN pfleger pf ON pf.kolonie = p.kolonie`'
starter_code: ''
---

Hole zu jedem Pinguin den Pfleger seiner Kolonie, als Spalten `pinguin` und `pfleger`.
