---
schema_version: 1
id: q143-jonas-bleibt
revision: 1
titel: Jonas bleibt im Westen
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- update
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 14
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
kontrolle: SELECT * FROM pfleger ORDER BY id
erwartete_spalten:
- id
- name
- kolonie
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Greta
  - Nord
- - 2
  - Hannes
  - Süd
- - 3
  - Ida
  - Ost
- - 4
  - Jonas
  - West
hints:
- kosten: 0
  text: '`WHERE name = ''Jonas''` nicht vergessen.'
starter_code: ''
---

Jonas springt nicht mehr überall ein, er gehört ab jetzt fest zur Westkolonie.
