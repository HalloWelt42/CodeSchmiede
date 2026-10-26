---
schema_version: 1
id: q112-ueberdurchschnittlich
revision: 1
titel: Überdurchschnittliche Portionen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- unterabfrage
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 11
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
- tag
- pinguin_id
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - 1
  - 6
- - '2026-10-20'
  - 3
  - 8
- - '2026-10-20'
  - 5
  - 5
- - '2026-10-21'
  - 1
  - 5
- - '2026-10-21'
  - 6
  - 6
- - '2026-10-22'
  - 3
  - 7
- - '2026-10-22'
  - 2
  - 5
hints:
- kosten: 0
  text: Gesucht ist der Durchschnitt.
starter_code: 'SELECT tag, pinguin_id, menge

  FROM fuetterungen

  WHERE menge > (SELECT ___(menge) FROM fuetterungen);'
---

Ergänze die Lücke `___`, damit alle Fütterungen kommen, bei denen es mehr Fische gab als im Durchschnitt.
