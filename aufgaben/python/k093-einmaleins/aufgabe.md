---
schema_version: 1
id: k093-einmaleins
revision: 1
titel: Die Dreierreihe
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
  text: range(1, 11) und ein f-String mit der Rechnung.
tests_sichtbar:
- input:
  - '3'
  expected: '3 x 1 = 3

    3 x 2 = 6

    3 x 3 = 9

    3 x 4 = 12

    3 x 5 = 15

    3 x 6 = 18

    3 x 7 = 21

    3 x 8 = 24

    3 x 9 = 27

    3 x 10 = 30

    '
tests_versteckt:
- input:
  - '7'
  expected: '7 x 1 = 7

    7 x 2 = 14

    7 x 3 = 21

    7 x 4 = 28

    7 x 5 = 35

    7 x 6 = 42

    7 x 7 = 49

    7 x 8 = 56

    7 x 9 = 63

    7 x 10 = 70

    '
starter_code: ''
---

Lies eine Zahl ein und gib ihre Reihe von 1 bis 10 aus. Bei `3`:

```
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
```
