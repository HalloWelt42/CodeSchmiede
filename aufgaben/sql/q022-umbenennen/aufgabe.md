---
schema_version: 1
id: q022-umbenennen
revision: 1
titel: Ein neues Schild
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- alias
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 2
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
- wo
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
- - Süd
  - Felsenküste
- - Ost
  - Sandstrand
- - West
  - Eishöhle
hints:
- kosten: 0
  text: Ein neuer Name kommt mit `AS`.
starter_code: 'SELECT name, lage ___ wo

  FROM kolonien;'
---

Ergänze die Lücke `___`, damit die Spalte `lage` im Ergebnis `wo` heißt.
