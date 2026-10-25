---
schema_version: 1
id: q018-pflegerliste
revision: 1
titel: Die Pflegerliste
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- select
- kurztest
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
  - Greta
- - Süd
  - Hannes
- - Ost
  - Ida
- - null
  - Jonas
hints:
- kosten: 0
  text: Tabelle `pfleger`, zwei Spalten in eigener Reihenfolge.
starter_code: ''
---

Für den Aushang am Eingang: hole von allen Pflegern zuerst die Kolonie und dann den Namen.
