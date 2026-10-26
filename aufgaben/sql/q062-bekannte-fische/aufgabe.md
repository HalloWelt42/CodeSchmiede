---
schema_version: 1
id: q062-bekannte-fische
revision: 1
titel: Bekannte Lieblingsfische
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- null_werte
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 6
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
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Hering
- - Pia
  - Lachs
- - Paul
  - Hering
- - Pepe
  - Makrele
- - Polly
  - Lachs
- - Pablo
  - Hering
hints:
- kosten: 0
  text: Das Gegenteil von IS NULL.
starter_code: 'SELECT name, lieblingsfisch

  FROM pinguine

  WHERE lieblingsfisch ___;'
---

Ergänze die Lücke `___`, damit nur Pinguine kommen, deren Lieblingsfisch bekannt ist.
