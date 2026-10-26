---
schema_version: 1
id: q167-ein-komma-zu-viel
revision: 1
titel: Ein Komma zu viel
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
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

  FROM pragma_table_info(''notizen'')

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
- - text
  - TEXT
  - 1
  - 0
hints:
- kosten: 0
  text: Nach der letzten Spalte kommt kein Komma.
starter_code: "CREATE TABLE notizen (\n  id INTEGER PRIMARY KEY,\n  text TEXT NOT NULL,\n);"
---

Das Skript soll die Tabelle notizen anlegen, meldet aber einen Fehler. Repariere es. Die Kontrolle liest den Aufbau der Tabelle aus: je Spalte Name, Datentyp, ob sie Pflicht ist (NOT NULL) und ob sie der Schlüssel ist (PRIMARY KEY).
