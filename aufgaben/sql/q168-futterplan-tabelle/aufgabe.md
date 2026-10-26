---
schema_version: 1
id: q168-futterplan-tabelle
revision: 1
titel: Der Futterplan als Tabelle
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- create_table
- insert
- kurztest
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
kontrolle: 'SELECT p.name, fp.fisch, fp.menge

  FROM futterplan fp JOIN pinguine p ON p.id = fp.pinguin_id

  ORDER BY p.id'
erwartete_spalten:
- name
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Hering
  - 2
- - Pia
  - Lachs
  - 2
- - Paul
  - Hering
  - 2
- - Pepe
  - Makrele
  - 2
- - Polly
  - Lachs
  - 2
- - Pablo
  - Hering
  - 2
hints:
- kosten: 0
  text: '`menge INTEGER NOT NULL DEFAULT 2 CHECK (menge > 0)`'
- kosten: 2
  text: INSERT INTO futterplan (pinguin_id, fisch) SELECT ...
starter_code: ''
---

Lege die Tabelle futterplan an: id (INTEGER PRIMARY KEY), pinguin_id (INTEGER, Pflicht, zeigt auf pinguine(id)), fisch (TEXT, Pflicht) und menge (INTEGER, Pflicht, Vorgabewert 2, nur Werte größer als 0). Fülle sie dann mit einer Anweisung: jeder Pinguin mit bekanntem Lieblingsfisch bekommt eine Zeile mit seinem Lieblingsfisch und der Vorgabemenge.
