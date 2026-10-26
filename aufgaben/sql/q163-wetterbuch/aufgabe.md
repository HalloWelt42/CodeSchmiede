---
schema_version: 1
id: q163-wetterbuch
revision: 1
titel: Das Wetterbuch
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- create_table
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
kontrolle: 'SELECT name, upper(type) AS typ, "notnull" AS pflicht, pk AS schluessel

  FROM pragma_table_info(''wetter'')

  ORDER BY cid'
erwartete_spalten:
- name
- typ
- pflicht
- schluessel
sortierung_egal: false
erwartetes_ergebnis:
- - tag
  - TEXT
  - 0
  - 1
- - grad
  - REAL
  - 1
  - 0
- - notiz
  - TEXT
  - 0
  - 0
hints:
- kosten: 0
  text: Drei Spalten in Klammern, durch Kommas getrennt.
- kosten: 2
  text: '`tag TEXT PRIMARY KEY, grad REAL NOT NULL, notiz TEXT`'
starter_code: ''
---

Lege die Tabelle wetter an: die Spalte tag als TEXT und Schlüssel (PRIMARY KEY), die Spalte grad als REAL und Pflicht (NOT NULL), die Spalte notiz als TEXT ohne Regel. Die Kontrolle liest den Aufbau der Tabelle aus: je Spalte Name, Datentyp, ob sie Pflicht ist (NOT NULL) und ob sie der Schlüssel ist (PRIMARY KEY).
