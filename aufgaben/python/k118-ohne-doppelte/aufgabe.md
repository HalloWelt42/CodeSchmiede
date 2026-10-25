---
schema_version: 1
id: k118-ohne-doppelte
revision: 1
titel: Ohne Doppelte
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- listenmethoden
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Nur anhängen, wenn die Zahl noch nicht in der Liste ist (`not in`).
tests_sichtbar:
- input:
  - '3'
  - '1'
  - '3'
  - '2'
  - '1'
  - '0'
  expected: '[3, 1, 2]

    [1, 2, 3]

    '
tests_versteckt:
- input:
  - '5'
  - '5'
  - '5'
  - '0'
  expected: '[5]

    [5]

    '
- input:
  - '9'
  - '4'
  - '7'
  - '0'
  expected: '[9, 4, 7]

    [4, 7, 9]

    '
starter_code: ''
---

Lies Zahlen ein, bis `0` kommt, und gib die Liste ohne Doppelte in der Reihenfolge des ersten Auftretens aus, danach sortiert. Bei `3`, `1`, `3`, `2`, `1`, `0`:

```
[3, 1, 2]
[1, 2, 3]
```
