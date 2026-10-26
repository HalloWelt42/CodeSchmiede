---
schema_version: 1
id: q095-beliebte-fische
revision: 1
titel: Die Renner
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- group_by
- having
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 9
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
- fisch
- fische
sortierung_egal: true
erwartetes_ergebnis:
- - Hering
  - 23
- - Lachs
  - 15
- - Makrele
  - 12
hints:
- kosten: 0
  text: Die Bedingung betrifft die Summe einer Gruppe.
- kosten: 2
  text: '`HAVING SUM(menge) > 10`'
starter_code: ''
---

Hole jede Fischsorte, von der insgesamt mehr als zehn Stück verfüttert wurden, mit der Summe als Spalte `fische`.
