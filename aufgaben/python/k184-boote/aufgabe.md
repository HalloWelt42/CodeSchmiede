---
schema_version: 1
id: k184-boote
revision: 1
titel: Genug Boote
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- modul
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Aufrunden mit `math.ceil`.
tests_sichtbar:
- input:
  - '10'
  expected: 'Boote: 3

    '
tests_versteckt:
- input:
  - '8'
  expected: 'Boote: 2

    '
- input:
  - '1'
  expected: 'Boote: 1

    '
- input:
  - '0'
  expected: 'Boote: 0

    '
starter_code: ''
---

In jedes Boot passen 4 Pinguine. Lies die Zahl der Pinguine ein und gib aus, wie viele Boote gebraucht werden; ein angefangenes Boot zählt ganz. Bei `10`:

```
Boote: 3
```
