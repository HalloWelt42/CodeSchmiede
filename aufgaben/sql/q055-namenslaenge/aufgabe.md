---
schema_version: 1
id: q055-namenslaenge
revision: 1
titel: Wie lang ist der Name?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- textfunktionen
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
- name
- laenge
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 3
- - Pia
  - 3
- - Paul
  - 4
- - Pina
  - 4
- - Pepe
  - 4
- - Polly
  - 5
- - Pablo
  - 5
- - Pünktchen
  - 9
hints:
- kosten: 0
  text: '`LENGTH(name)`'
starter_code: ''
---

Hole für alle Pinguine den Namen und die Zahl seiner Zeichen als Spalte `laenge`.
