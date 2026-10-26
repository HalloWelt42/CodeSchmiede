---
schema_version: 1
id: q063-raetsel-im-norden
revision: 1
titel: Das Rätsel im Norden
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
- gewicht_kg
sortierung_egal: false
erwartetes_ergebnis:
- - Pina
  - 3.5
hints:
- kosten: 0
  text: Zwei Bedingungen mit AND, die zweite mit IS NULL.
starter_code: ''
---

Hole Name und Gewicht aller Pinguine aus der Nordkolonie, deren Lieblingsfisch noch unbekannt ist.
