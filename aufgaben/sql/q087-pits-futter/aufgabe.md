---
schema_version: 1
id: q087-pits-futter
revision: 1
titel: Pits Futterbilanz
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- aggregat
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 8
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
- mahlzeiten
- fische
sortierung_egal: false
erwartetes_ergebnis:
- - 3
  - 14
hints:
- kosten: 0
  text: In `fuetterungen` steht Pit als `pinguin_id = 1`.
starter_code: ''
---

Pit hat die Nummer 1. Wie oft wurde er gefüttert (Spalte `mahlzeiten`) und wie viele Fische hat er dabei bekommen (Spalte `fische`)?
