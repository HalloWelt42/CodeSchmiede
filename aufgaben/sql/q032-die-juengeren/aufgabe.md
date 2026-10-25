---
schema_version: 1
id: q032-die-juengeren
revision: 1
titel: Die Jüngeren
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- where
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 3
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
- geburtsjahr
sortierung_egal: false
erwartetes_ergebnis:
- - Pina
  - 2022
- - Pablo
  - 2021
- - Pünktchen
  - 2023
hints:
- kosten: 0
  text: 'Nach 2020 heißt: größer als 2020.'
starter_code: 'SELECT name, geburtsjahr

  FROM pinguine

  WHERE geburtsjahr ___ 2020;'
---

Ergänze die Lücke `___`, damit alle Pinguine kommen, die nach 2020 geboren sind.
