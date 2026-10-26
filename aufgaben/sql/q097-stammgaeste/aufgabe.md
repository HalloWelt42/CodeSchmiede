---
schema_version: 1
id: q097-stammgaeste
revision: 1
titel: Stammgäste
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
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
- pinguin_id
- mahlzeiten
sortierung_egal: true
erwartetes_ergebnis:
- - 1
  - 3
- - 2
  - 2
- - 3
  - 2
hints:
- kosten: 0
  text: WHERE kennt noch keine Gruppen.
- kosten: 2
  text: HAVING nach GROUP BY.
starter_code: 'SELECT pinguin_id, COUNT(*) AS mahlzeiten

  FROM fuetterungen

  WHERE COUNT(*) > 1

  GROUP BY pinguin_id;'
---

Die Abfrage soll alle Pinguine finden, die mehr als einmal gefüttert wurden, meldet aber einen Fehler. Repariere sie.
