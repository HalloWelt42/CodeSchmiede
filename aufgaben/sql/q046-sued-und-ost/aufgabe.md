---
schema_version: 1
id: q046-sued-und-ost
revision: 1
titel: Wählerisch im Süden und Osten
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- logik
- in_between
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 4
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
- kolonie
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - Pia
  - Süd
  - Lachs
- - Pablo
  - Ost
  - Hering
hints:
- kosten: 0
  text: Zwei Listen, mit AND verbunden.
- kosten: 2
  text: '`WHERE kolonie IN (''Süd'', ''Ost'') AND lieblingsfisch IN (''Hering'', ''Lachs'')`'
starter_code: ''
---

Hole Name, Kolonie und Lieblingsfisch aller Pinguine aus Süd oder Ost, die Hering oder Lachs am liebsten mögen.
