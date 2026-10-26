---
schema_version: 1
id: q137-heringe-fuer-den-osten
revision: 1
titel: Heringe für den Osten
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- insert
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 13
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
kontrolle: SELECT pinguin_id, tag, fisch, menge FROM fuetterungen WHERE tag = '2026-10-23' ORDER BY pinguin_id
erwartete_spalten:
- pinguin_id
- tag
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - 7
  - '2026-10-23'
  - Hering
  - 3
- - 8
  - '2026-10-23'
  - Hering
  - 3
hints:
- kosten: 0
  text: INSERT INTO ... SELECT statt VALUES.
- kosten: 2
  text: '`SELECT id, ''2026-10-23'', ''Hering'', 3 FROM pinguine WHERE kolonie = ''Ost''`'
starter_code: ''
---

Jeder Pinguin der Ostkolonie bekommt am 23. Oktober 2026 drei Heringe. Schreib es als eine Anweisung, die ihre Zeilen aus einer Abfrage holt.
