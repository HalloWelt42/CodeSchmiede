---
schema_version: 1
id: k068-schaltjahr
revision: 1
titel: Schaltjahr
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- logik
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Drei Bedingungen mit `%` und `==` oder `!=`.
- kosten: 3
  text: '`jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0`'
tests_sichtbar:
- input:
  - '2024'
  expected: 'True

    '
tests_versteckt:
- input:
  - '1900'
  expected: 'False

    '
- input:
  - '2000'
  expected: 'True

    '
- input:
  - '2023'
  expected: 'False

    '
starter_code: ''
---

Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist, aber nicht durch 100; es sei denn, es ist durch 400 teilbar. Lies eine Jahreszahl ein und gib aus, ob es ein Schaltjahr ist. Bei `2024`:

```
True
```
