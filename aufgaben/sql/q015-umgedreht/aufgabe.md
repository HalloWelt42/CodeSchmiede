---
schema_version: 1
id: q015-umgedreht
revision: 1
titel: Kolonie zuerst
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
- kolonie
- name
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Pit
- - Süd
  - Pia
- - Nord
  - Paul
- - Nord
  - Pina
- - Süd
  - Pepe
- - Nord
  - Polly
- - Ost
  - Pablo
- - Ost
  - Pünktchen
hints:
- kosten: 0
  text: Die Reihenfolge hinter SELECT bestimmt die Reihenfolge im Ergebnis.
starter_code: ''
---

Hole für alle Pinguine erst die Kolonie, dann den Namen.
