---
schema_version: 1
id: k056-zwei-zahlen
revision: 1
titel: Zwei Zahlen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- eingabe
- umwandeln
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei input, jedes gleich umwandeln.
tests_sichtbar:
- input:
  - '3'
  - '4'
  expected: '7

    '
tests_versteckt:
- input:
  - '10'
  - '-2'
  expected: '8

    '
- input:
  - '100'
  - '1'
  expected: '101

    '
starter_code: ''
---

Lies zwei ganze Zahlen ein, jede mit eigenem `input()`, und gib ihre Summe aus. Bei `3` und `4`:

```
7
```
