---
schema_version: 1
id: q052-am-strand
revision: 1
titel: Am Strand
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- like
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 5
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
- lage
sortierung_egal: false
erwartetes_ergebnis:
- - Ost
  - Sandstrand
hints:
- kosten: 0
  text: Vor und hinter strand darf etwas stehen.
- kosten: 2
  text: '`''%strand%''`'
starter_code: 'SELECT name, lage

  FROM kolonien

  WHERE lage LIKE ___;'
---

Ergänze das Muster `___`, damit alle Kolonien kommen, in deren Lage das Wort strand vorkommt.
