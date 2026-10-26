---
schema_version: 1
id: q156-nur-pina
revision: 1
titel: Nur Pinas Fütterungen
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- delete
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 15
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
kontrolle: SELECT * FROM fuetterungen ORDER BY id
erwartete_spalten:
- id
- pinguin_id
- tag
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - 1
  - '2026-10-20'
  - Hering
  - 6
- - 2
  - 2
  - '2026-10-20'
  - Lachs
  - 4
- - 3
  - 3
  - '2026-10-20'
  - Hering
  - 8
- - 4
  - 5
  - '2026-10-20'
  - Makrele
  - 5
- - 5
  - 1
  - '2026-10-21'
  - Hering
  - 5
- - 7
  - 6
  - '2026-10-21'
  - Lachs
  - 6
- - 8
  - 7
  - '2026-10-21'
  - Hering
  - 4
- - 9
  - 3
  - '2026-10-22'
  - Makrele
  - 7
- - 10
  - 8
  - '2026-10-22'
  - Sardine
  - 2
- - 11
  - 2
  - '2026-10-22'
  - Lachs
  - 5
- - 12
  - 1
  - '2026-10-22'
  - Sardine
  - 3
hints:
- kosten: 0
  text: Dem DELETE fehlt sein WHERE.
starter_code: DELETE FROM fuetterungen;
---

Das Skript soll nur die Fütterungen von Pina (Nummer 4) löschen, löscht aber alle. Repariere es.
