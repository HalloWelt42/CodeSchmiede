---
schema_version: 1
id: q134-sardinen-fuer-pina
revision: 1
titel: Sardinen für Pina
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
- - 4
  - '2026-10-23'
  - Sardine
  - 3
hints:
- kosten: 0
  text: Die Spalte id weglassen.
- kosten: 2
  text: '`INSERT INTO fuetterungen (pinguin_id, tag, fisch, menge) VALUES (...)`'
starter_code: ''
---

Pina (Nummer 4) bekommt am 23. Oktober 2026 drei Sardinen. Trage die Fütterung ein; die Nummer der Fütterung vergibt die Datenbank.
