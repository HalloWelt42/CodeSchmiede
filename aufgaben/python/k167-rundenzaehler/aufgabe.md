---
schema_version: 1
id: k167-rundenzaehler
revision: 1
titel: Der Rundenzähler
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- sichtbarkeit
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Mehrere Namen in einer Zeile: `global runden, bestzeit`.'
- kosten: 2
  text: Die erste Runde ist immer die bisher beste.
tests_sichtbar:
- input:
  - '52'
  - '48'
  - '50'
  - '0'
  expected: 'Runden: 3

    Bestzeit: 48

    '
tests_versteckt:
- input:
  - '61'
  - '0'
  expected: 'Runden: 1

    Bestzeit: 61

    '
- input:
  - '5'
  - '4'
  - '3'
  - '0'
  expected: 'Runden: 3

    Bestzeit: 3

    '
starter_code: 'runden = 0

  bestzeit = 0

  '
---

Schreibe eine Funktion `runde(zeit)`, die bei jedem Aufruf den Zähler `runden` draußen erhöht und die beste (kleinste) Zeit in `bestzeit` draußen merkt. Lies Rundenzeiten ein, bis `0` kommt. Bei `52`, `48`, `50`, `0`:

```
Runden: 3
Bestzeit: 48
```
