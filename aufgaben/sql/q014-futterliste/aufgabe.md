---
schema_version: 1
id: q014-futterliste
revision: 1
titel: Die Futterliste
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- select
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 1
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
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - Hering
  - 6
- - Lachs
  - 4
- - Hering
  - 8
- - Makrele
  - 5
- - Hering
  - 5
- - Sardine
  - 3
- - Lachs
  - 6
- - Hering
  - 4
- - Makrele
  - 7
- - Sardine
  - 2
- - Lachs
  - 5
- - Sardine
  - 3
hints:
- kosten: 0
  text: 'Andere Tabelle, gleiche Form: `SELECT ... FROM fuetterungen;`'
starter_code: ''
---

In der Tabelle `fuetterungen` steht jede Fütterung. Hole für jede den Fisch und die Menge.
