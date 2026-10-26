---
schema_version: 1
id: q102-wassertemperatur
revision: 1
titel: Wie warm ist mein Wasser?
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
- name
- wassertemperatur
sortierung_egal: true
erwartetes_ergebnis:
- - Pit
  - -1.5
- - Pia
  - 4.0
- - Paul
  - -1.5
- - Pina
  - -1.5
- - Pepe
  - 4.0
- - Polly
  - -1.5
- - Pablo
  - 9.5
- - Pünktchen
  - 9.5
hints:
- kosten: 0
  text: Der Name der Kolonie soll zur Kolonie des Pinguins passen.
- kosten: 1
  text: '`p.kolonie`'
starter_code: 'SELECT p.name, k.wassertemperatur

  FROM pinguine p

  JOIN kolonien k ON k.name = ___;'
---

Ergänze die Lücke `___`, damit zu jedem Pinguin die Wassertemperatur seiner Kolonie kommt.
