---
schema_version: 1
id: q119-steckbrief-mahlzeiten
revision: 1
titel: 'Steckbrief: die Mahlzeiten'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- projekt
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
- kuerzel
- kolonie
- lage
- lieblingsfisch
- jahre
- mahlzeiten
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - Pau
  - Nord
  - Packeis
  - Hering
  - 9
  - 2
- - Pit
  - Pit
  - Nord
  - Packeis
  - Hering
  - 7
  - 3
- - Polly
  - Pol
  - Nord
  - Packeis
  - Lachs
  - 7
  - 1
- - Pablo
  - Pab
  - Ost
  - Sandstrand
  - Hering
  - 5
  - 1
- - Pina
  - Pin
  - Nord
  - Packeis
  - unbekannt
  - 4
  - 1
- - Pünktchen
  - Pün
  - Ost
  - Sandstrand
  - unbekannt
  - 3
  - 1
hints:
- kosten: 0
  text: Eine Unterabfrage im SELECT mit Bezug auf p.id.
- kosten: 2
  text: '`(SELECT COUNT(*) FROM fuetterungen f WHERE f.pinguin_id = p.id) AS mahlzeiten`'
starter_code: "SELECT p.name, SUBSTR(p.name, 1, 3) AS kuerzel, p.kolonie, k.lage, COALESCE(p.lieblingsfisch, 'unbekannt')\
  \ AS lieblingsfisch,\n       2026 - p.geburtsjahr AS jahre\nFROM pinguine p\nJOIN kolonien k ON k.name = p.kolonie\nWHERE\
  \ p.kolonie IN ('Nord', 'Ost')\nORDER BY jahre DESC, p.name;"
---

**Kapitelprojekt Pinguinsteckbrief, Stück 11.** Deine Abfrage aus Stück 10 steht schon da. Hinter `jahre` kommt eine Spalte `mahlzeiten`: wie oft der Pinguin gefüttert wurde.
