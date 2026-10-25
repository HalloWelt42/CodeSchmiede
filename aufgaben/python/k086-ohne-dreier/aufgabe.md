---
schema_version: 1
id: k086-ohne-dreier
revision: 1
titel: Ohne Dreier
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- while
- abbruch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst hochzählen, dann prüfen, ob continue greift, dann ausgeben.
tests_sichtbar:
- input: []
  expected: '1

    2

    4

    5

    7

    8

    10

    '
starter_code: ''
---

Gib die Zahlen von 1 bis 10 aus, aber lass alle aus, die durch 3 teilbar sind. Benutze `continue`.

```
1
2
4
5
7
8
10
```
