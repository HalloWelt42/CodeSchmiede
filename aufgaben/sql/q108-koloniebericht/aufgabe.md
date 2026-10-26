---
schema_version: 1
id: q108-koloniebericht
revision: 1
titel: Der Koloniebericht
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- left_join
- group_by
- kurztest
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
- kolonie
- lage
- pinguine
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
  - 4
- - Ost
  - Sandstrand
  - 2
- - Süd
  - Felsenküste
  - 2
- - West
  - Eishöhle
  - 0
hints:
- kosten: 0
  text: LEFT JOIN von kolonien aus, damit West bleibt.
- kosten: 1
  text: COUNT(*) würde für West 1 zählen.
- kosten: 2
  text: '`COUNT(p.id) AS pinguine ... ORDER BY pinguine DESC, k.name`'
starter_code: ''
---

Hole für jede der vier Kolonien ihren Namen (Spalte `kolonie`), ihre Lage und die Zahl ihrer Pinguine (Spalte `pinguine`), auch für Kolonien ohne Pinguine. Die größte Kolonie zuerst, bei Gleichstand nach dem Namen.
