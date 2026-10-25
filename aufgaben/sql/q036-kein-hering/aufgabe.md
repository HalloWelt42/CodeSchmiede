---
schema_version: 1
id: q036-kein-hering
revision: 1
titel: Bloß kein Hering
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- where
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 3
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
- - Pia
  - Lachs
- - Pepe
  - Makrele
- - Polly
  - Lachs
hints:
- kosten: 0
  text: Ungleich heißt in SQL `<>`.
starter_code: ''
---

Hole Name und Lieblingsfisch aller Pinguine, deren Lieblingsfisch nicht Hering ist. Pinguine, deren Lieblingsfisch noch niemand kennt, fallen dabei von selbst heraus; warum, klärt ein späteres Kapitel.
