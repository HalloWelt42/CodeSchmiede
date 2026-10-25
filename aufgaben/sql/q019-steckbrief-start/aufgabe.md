---
schema_version: 1
id: q019-steckbrief-start
revision: 1
titel: 'Steckbrief: der Anfang'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
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
- name
- kolonie
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Nord
  - Hering
- - Pia
  - Süd
  - Lachs
- - Paul
  - Nord
  - Hering
- - Pina
  - Nord
  - null
- - Pepe
  - Süd
  - Makrele
- - Polly
  - Nord
  - Lachs
- - Pablo
  - Ost
  - Hering
- - Pünktchen
  - Ost
  - null
hints:
- kosten: 0
  text: Drei Spalten aus der Tabelle `pinguine`.
starter_code: ''
---

**Kapitelprojekt Pinguinsteckbrief, Stück 1.** Über die nächsten Kapitel wächst eine Abfrage, die für die Besuchertafel einen Steckbrief der Pinguine liefert. Zum Anfang: Name, Kolonie und Lieblingsfisch aller Pinguine.
