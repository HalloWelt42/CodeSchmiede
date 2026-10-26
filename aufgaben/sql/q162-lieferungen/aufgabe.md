---
schema_version: 1
id: q162-lieferungen
revision: 1
titel: Fischlieferungen
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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

  FROM pragma_table_info(''lieferungen'')

  ORDER BY cid'
erwartete_spalten:
- name
- typ
- pflicht
- schluessel
sortierung_egal: false
erwartetes_ergebnis:
- - id
  - INTEGER
  - 0
  - 1
- - fisch
  - TEXT
  - 1
  - 0
- - kilo
  - REAL
  - 0
  - 0
hints:
- kosten: 0
  text: Nicht leer ...
starter_code: "CREATE TABLE lieferungen (\n  id INTEGER PRIMARY KEY,\n  fisch TEXT ___ NULL,\n  kilo REAL\n);"
---

Ergänze die Lücke `___`, damit jede Lieferung einen Fisch haben muss. Die Kontrolle liest den Aufbau der Tabelle aus: je Spalte Name, Datentyp, ob sie Pflicht ist (NOT NULL) und ob sie der Schlüssel ist (PRIMARY KEY).
