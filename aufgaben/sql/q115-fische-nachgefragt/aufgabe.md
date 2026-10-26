---
schema_version: 1
id: q115-fische-nachgefragt
revision: 1
titel: Fische, nachgefragt
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- unterabfrage
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 11
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
- fische
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 14
- - Pia
  - 9
- - Paul
  - 15
- - Pina
  - 3
- - Pepe
  - 5
- - Polly
  - 6
- - Pablo
  - 4
- - Pünktchen
  - 2
hints:
- kosten: 0
  text: Die Unterabfrage braucht den Bezug auf die äußere Zeile.
- kosten: 2
  text: '`WHERE f.pinguin_id = p.id`'
starter_code: ''
---

Hole für jeden Pinguin den Namen und, über eine Unterabfrage im SELECT, wie viele Fische er insgesamt bekommen hat (Spalte `fische`).
