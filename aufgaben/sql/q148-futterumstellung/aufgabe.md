---
schema_version: 1
id: q148-futterumstellung
revision: 1
titel: Die Futterumstellung
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- update
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 14
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
kontrolle: 'SELECT f.id, f.fisch, f.menge, p.lieblingsfisch

  FROM fuetterungen f JOIN pinguine p ON p.id = f.pinguin_id

  ORDER BY f.id'
erwartete_spalten:
- id
- fisch
- menge
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Hering
  - 6
  - Hering
- - 2
  - Lachs
  - 4
  - Lachs
- - 3
  - Hering
  - 8
  - Hering
- - 4
  - Makrele
  - 5
  - Makrele
- - 5
  - Hering
  - 5
  - Hering
- - 6
  - Hering
  - 4
  - Hering
- - 7
  - Lachs
  - 6
  - Lachs
- - 8
  - Hering
  - 4
  - Hering
- - 9
  - Makrele
  - 7
  - Hering
- - 10
  - Hering
  - 3
  - Hering
- - 11
  - Lachs
  - 5
  - Lachs
- - 12
  - Hering
  - 4
  - Hering
hints:
- kosten: 0
  text: Zwei UPDATE, eins je Tabelle.
- kosten: 2
  text: Das zweite braucht `WHERE lieblingsfisch IS NULL`.
starter_code: ''
---

Sardinen sind ausverkauft. Jede Sardinen-Fütterung wird zu einer Hering-Fütterung mit einem Fisch mehr. Und wer noch keinen Lieblingsfisch hat, bekommt Hering eingetragen.
