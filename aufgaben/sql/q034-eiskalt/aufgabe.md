---
schema_version: 1
id: q034-eiskalt
revision: 1
titel: Eiskaltes Wasser
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
- lage
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
- - West
  - Eishöhle
hints:
- kosten: 0
  text: Tabelle `kolonien`, Spalte `wassertemperatur`.
starter_code: ''
---

Hole Name und Lage aller Kolonien, deren Wasser kälter als null Grad ist.
