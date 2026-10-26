---
schema_version: 1
id: q139-umzug-ankunft
revision: 1
titel: 'Umzug in den Westen: die Ankunft'
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
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
kontrolle: SELECT * FROM pinguine WHERE kolonie = 'West' ORDER BY id
erwartete_spalten:
- id
- name
- kolonie
- gewicht_kg
- geburtsjahr
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - 9
  - Pelle
  - West
  - 3.1
  - 2025
  - null
- - 10
  - Pippa
  - West
  - 3.6
  - 2024
  - Hering
hints:
- kosten: 0
  text: Zwei Klammern hinter VALUES.
- kosten: 1
  text: NULL ohne Hochkommas.
starter_code: ''
---

**Kapitelprojekt Umzug in den Westen, Stück 1.** Die Westkolonie war bisher leer, jetzt ziehen zwei Pinguine ein: Pelle (Nummer 9, 3,1 Kilo, geboren 2025, Lieblingsfisch unbekannt) und Pippa (Nummer 10, 3,6 Kilo, geboren 2024, mag Hering). Trage beide mit einer Anweisung ein; schreib alle sechs Spalten aus und setze für Pelles Lieblingsfisch NULL.
