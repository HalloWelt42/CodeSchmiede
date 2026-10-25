---
schema_version: 1
id: q021-in-gramm
revision: 1
titel: In Gramm
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 2
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
- gramm
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 4200.0
- - Pia
  - 3800.0
- - Paul
  - 5100.0
- - Pina
  - 3500.0
- - Pepe
  - 4900.0
- - Polly
  - 4600.0
- - Pablo
  - 4000.0
- - Pünktchen
  - 2900.0
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT name, gewicht_kg * 1000 AS gramm

  FROM pinguine;'
---

Die Abfrage steht schon da: sie rechnet das Gewicht in Gramm um und nennt die Spalte `gramm`. Prüfe sie.
