---
schema_version: 1
id: q012-namen
revision: 1
titel: Nur die Namen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- select
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 1
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
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
- - Pia
- - Paul
- - Pina
- - Pepe
- - Polly
- - Pablo
- - Pünktchen
hints:
- kosten: 0
  text: Die Spalte heißt `name`.
starter_code: 'SELECT ___

  FROM pinguine;'
---

Ergänze die Lücke `___`, damit nur die Namen aller Pinguine kommen.
