---
schema_version: 1
id: q068-raetselliste
revision: 1
titel: Die Rätselliste
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- null_werte
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 6
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
- fisch
sortierung_egal: false
erwartetes_ergebnis:
- - Pia
  - Lachs
- - Pina
  - unbekannt
- - Pepe
  - Makrele
- - Polly
  - Lachs
- - Pünktchen
  - unbekannt
hints:
- kosten: 0
  text: 'Das Filtern und das Füllen sind zwei verschiedene Dinge: WHERE und COALESCE.'
- kosten: 2
  text: '`WHERE lieblingsfisch <> ''Hering'' OR lieblingsfisch IS NULL`'
starter_code: ''
---

Für das Fischrätsel am Wochenende: hole Name und Lieblingsfisch (Spalte `fisch`) aller Pinguine, die nicht Hering am liebsten mögen, auch die mit unbekanntem Lieblingsfisch. Statt NULL soll `'unbekannt'` dastehen.
