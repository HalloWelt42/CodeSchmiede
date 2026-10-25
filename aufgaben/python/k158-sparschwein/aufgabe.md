---
schema_version: 1
id: k158-sparschwein
revision: 1
titel: Das Sparschwein
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- funktion
- rueckgabe
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Neuer Betrag: `betrag * (1 + prozent / 100)`, gerundet mit `round(..., 2)`.'
- kosten: 3
  text: In der Schleife das Ergebnis der Funktion wieder in betrag speichern.
tests_sichtbar:
- input:
  - '100'
  - '5'
  - '3'
  expected: 'Jahr 1: 105.0

    Jahr 2: 110.25

    Jahr 3: 115.76

    '
tests_versteckt:
- input:
  - '50'
  - '10'
  - '1'
  expected: 'Jahr 1: 55.0

    '
- input:
  - '10'
  - '0'
  - '2'
  expected: 'Jahr 1: 10.0

    Jahr 2: 10.0

    '
starter_code: ''
---

Schreibe eine Funktion `zinsen(betrag, prozent)`, die den Betrag nach einem Jahr mit Zinsen zurückgibt, auf zwei Stellen gerundet. Lies Startbetrag (ganze Zahl), Zinssatz in Prozent (ganze Zahl) und Anzahl der Jahre ein und gib den Stand nach jedem Jahr aus. Bei `100`, `5`, `3`:

```
Jahr 1: 105.0
Jahr 2: 110.25
Jahr 3: 115.76
```
