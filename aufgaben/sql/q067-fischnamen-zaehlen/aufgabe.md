---
schema_version: 1
id: q067-fischnamen-zaehlen
revision: 1
titel: Lange Fischnamen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- null_werte
- textfunktionen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 6
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
  - 6
- - Pia
  - 5
- - Paul
  - 6
- - Pina
  - 0
- - Pepe
  - 7
- - Polly
  - 5
- - Pablo
  - 6
- - Pünktchen
  - 0
hints:
- kosten: 0
  text: LENGTH von NULL ist NULL.
- kosten: 2
  text: '`COALESCE(LENGTH(lieblingsfisch), 0)`'
starter_code: ''
---

Hole für alle Pinguine den Namen und die Zahl der Zeichen ihres Lieblingsfischs als Spalte `laenge`. Ist der Fisch unbekannt, soll dort 0 stehen.
