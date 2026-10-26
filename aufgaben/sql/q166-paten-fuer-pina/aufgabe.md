---
schema_version: 1
id: q166-paten-fuer-pina
revision: 1
titel: Paten für Pina
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
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
kontrolle: 'SELECT pa.name AS pate, p.name AS pinguin

  FROM paten pa JOIN pinguine p ON p.id = pa.pinguin_id

  ORDER BY pa.name'
erwartete_spalten:
- pate
- pinguin
sortierung_egal: false
erwartetes_ergebnis:
- - Familie Kim
  - Pina
- - Klasse 5b
  - Pina
hints:
- kosten: 0
  text: '`pinguin_id INTEGER NOT NULL REFERENCES pinguine(id)`'
- kosten: 1
  text: Zwei Klammern hinter VALUES.
starter_code: ''
---

Lege die Tabelle paten an mit id (INTEGER PRIMARY KEY), name (TEXT, Pflicht) und pinguin_id (INTEGER, Pflicht, zeigt auf pinguine(id)). Trage die Familie Kim und die Klasse 5b als Paten von Pina (Nummer 4) ein.
