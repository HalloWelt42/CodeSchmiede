---
schema_version: 1
id: k083-bis-n
revision: 1
titel: Bis wohin du willst
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- while
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Zähler i, der bei 1 beginnt und bis n wächst.
tests_sichtbar:
- input:
  - '3'
  expected: '1

    2

    3

    '
tests_versteckt:
- input:
  - '5'
  expected: '1

    2

    3

    4

    5

    '
- input:
  - '0'
  expected: ''
starter_code: ''
---

Lies eine Zahl n ein und gib alle Zahlen von 1 bis n aus, jede in ihrer Zeile. Bei `3`:

```
1
2
3
```
