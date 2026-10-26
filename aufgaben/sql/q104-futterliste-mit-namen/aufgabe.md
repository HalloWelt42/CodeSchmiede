---
schema_version: 1
id: q104-futterliste-mit-namen
revision: 1
titel: Die Futterliste mit Namen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- join
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 10
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
- pinguin
- fisch
- menge
sortierung_egal: true
erwartetes_ergebnis:
- - Pit
  - Hering
  - 5
- - Pina
  - Sardine
  - 3
- - Polly
  - Lachs
  - 6
- - Pablo
  - Hering
  - 4
hints:
- kosten: 0
  text: In `fuetterungen` steht die Nummer, in `pinguine` heißt sie `id`.
- kosten: 2
  text: '`JOIN pinguine p ON p.id = f.pinguin_id`'
starter_code: ''
---

Hole für alle Fütterungen vom 21. Oktober 2026 den Namen des Pinguins (Spalte `pinguin`), den Fisch und die Menge.
