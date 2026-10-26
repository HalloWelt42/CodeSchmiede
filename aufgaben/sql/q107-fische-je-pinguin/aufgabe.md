---
schema_version: 1
id: q107-fische-je-pinguin
revision: 1
titel: Die Fischrangliste
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- join
- group_by
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
- fische
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - 15
- - Pit
  - 14
- - Pia
  - 9
- - Polly
  - 6
- - Pepe
  - 5
- - Pablo
  - 4
- - Pina
  - 3
- - Pünktchen
  - 2
hints:
- kosten: 0
  text: Verbinden, je Pinguin gruppieren, summieren, sortieren.
- kosten: 2
  text: '`GROUP BY p.name ORDER BY fische DESC, pinguin`'
starter_code: ''
---

Hole für jeden Pinguin seinen Namen (Spalte `pinguin`) und wie viele Fische er insgesamt bekommen hat (Spalte `fische`), die meisten zuerst; bei Gleichstand entscheidet der Name.
