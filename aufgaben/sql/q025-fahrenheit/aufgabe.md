---
schema_version: 1
id: q025-fahrenheit
revision: 1
titel: Grad Fahrenheit
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 2
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
- fahrenheit
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - 29.3
- - Süd
  - 39.2
- - Ost
  - 49.1
- - West
  - 31.1
hints:
- kosten: 0
  text: 'Rechnung: `wassertemperatur * 9 / 5 + 32`.'
- kosten: 2
  text: Gerundet mit `ROUND(..., 1)`.
starter_code: ''
---

Für Besuch aus Übersee: gib je Kolonie den Namen und die Wassertemperatur in Grad Fahrenheit aus, auf eine Stelle gerundet, als Spalte `fahrenheit`. Die Formel: Grad Celsius mal 9, geteilt durch 5, plus 32.
