---
schema_version: 1
id: k094-gerade-bis
revision: 1
titel: Nur die geraden
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- for
- range
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: range(2, n + 1, 2) beginnt bei 2 und springt in Zweierschritten.
tests_sichtbar:
- input:
  - '9'
  expected: '2

    4

    6

    8

    '
tests_versteckt:
- input:
  - '10'
  expected: '2

    4

    6

    8

    10

    '
- input:
  - '1'
  expected: ''
starter_code: ''
---

Lies eine Zahl n ein und gib alle geraden Zahlen von 2 bis n aus, mit range und Schrittweite. Bei `9`:

```
2
4
6
8
```
