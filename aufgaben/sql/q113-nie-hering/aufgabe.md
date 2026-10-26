---
schema_version: 1
id: q113-nie-hering
revision: 1
titel: Nie Hering bekommen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
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
sortierung_egal: false
erwartetes_ergebnis:
- - Pia
- - Pina
- - Pepe
- - Polly
- - Pünktchen
hints:
- kosten: 0
  text: Die Unterabfrage liefert die Nummern der Heringsesser.
- kosten: 2
  text: '`WHERE id NOT IN (SELECT pinguin_id ...)`'
starter_code: ''
---

Hole die Namen aller Pinguine, die noch nie Hering gefüttert bekommen haben.
