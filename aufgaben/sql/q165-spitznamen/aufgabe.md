---
schema_version: 1
id: q165-spitznamen
revision: 1
titel: Spitznamen
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- create_table
- update
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
kontrolle: SELECT name, spitzname FROM pinguine ORDER BY id
erwartete_spalten:
- name
- spitzname
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - null
- - Pia
  - null
- - Paul
  - null
- - Pina
  - null
- - Pepe
  - null
- - Polly
  - null
- - Pablo
  - null
- - Pünktchen
  - Pünkti
hints:
- kosten: 0
  text: Erst ALTER TABLE ... ADD COLUMN, dann UPDATE.
starter_code: ''
---

Die Pinguine bekommen eine neue Spalte spitzname (TEXT). Pünktchen heißt ab jetzt bei allen Pünkti.
