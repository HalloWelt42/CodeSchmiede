---
schema_version: 1
id: q074-die-juengsten
revision: 1
titel: Die zwei Jüngsten
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- order_by
- limit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 7
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
- geburtsjahr
sortierung_egal: false
erwartetes_ergebnis:
- - Pünktchen
  - 2023
- - Pina
  - 2022
hints:
- kosten: 0
  text: Die jüngsten haben das späteste Geburtsjahr.
- kosten: 1
  text: Erst ORDER BY ... DESC, dann LIMIT 2.
starter_code: ''
---

Hole Name und Geburtsjahr der zwei jüngsten Pinguine, den jüngsten zuerst.
