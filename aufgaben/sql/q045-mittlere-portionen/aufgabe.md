---
schema_version: 1
id: q045-mittlere-portionen
revision: 1
titel: Mittlere Portionen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
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
- tag
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - Hering
  - 6
- - '2026-10-20'
  - Lachs
  - 4
- - '2026-10-20'
  - Makrele
  - 5
- - '2026-10-21'
  - Hering
  - 5
- - '2026-10-21'
  - Lachs
  - 6
- - '2026-10-21'
  - Hering
  - 4
- - '2026-10-22'
  - Lachs
  - 5
hints:
- kosten: 0
  text: Für einen Bereich gibt es BETWEEN.
starter_code: ''
---

Hole Tag, Fisch und Menge aller Fütterungen mit vier bis sechs Fischen (beide Grenzen gehören dazu).
