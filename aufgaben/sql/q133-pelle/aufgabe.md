---
schema_version: 1
id: q133-pelle
revision: 1
titel: Pelle zieht ein
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
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
kontrolle: SELECT * FROM pinguine ORDER BY id
erwartete_spalten:
- id
- name
- kolonie
- gewicht_kg
- geburtsjahr
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Pit
  - Nord
  - 4.2
  - 2019
  - Hering
- - 2
  - Pia
  - Süd
  - 3.8
  - 2020
  - Lachs
- - 3
  - Paul
  - Nord
  - 5.1
  - 2017
  - Hering
- - 4
  - Pina
  - Nord
  - 3.5
  - 2022
  - null
- - 5
  - Pepe
  - Süd
  - 4.9
  - 2018
  - Makrele
- - 6
  - Polly
  - Nord
  - 4.6
  - 2019
  - Lachs
- - 7
  - Pablo
  - Ost
  - 4.0
  - 2021
  - Hering
- - 8
  - Pünktchen
  - Ost
  - 2.9
  - 2023
  - null
- - 9
  - Pelle
  - West
  - 3.1
  - 2025
  - null
hints:
- kosten: 0
  text: Fünf Spalten, fünf Werte, in derselben Reihenfolge.
- kosten: 2
  text: '`VALUES (9, ''Pelle'', ''West'', 3.1, 2025)`'
starter_code: ''
---

Trage Pelle ein: Nummer 9, Westkolonie, 3,1 Kilo, geboren 2025. Seinen Lieblingsfisch kennt noch niemand, lass die Spalte einfach weg.
