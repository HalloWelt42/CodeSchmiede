---
schema_version: 1
id: k077-groesste-zahl
revision: 1
titel: Die größte von drei
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- verzweigung
- logik
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ist a mindestens so groß wie b und c? Sonst bleibt nur noch der Vergleich von b und c.
tests_sichtbar:
- input:
  - '4'
  - '9'
  - '2'
  expected: '9

    '
tests_versteckt:
- input:
  - '7'
  - '3'
  - '1'
  expected: '7

    '
- input:
  - '1'
  - '2'
  - '8'
  expected: '8

    '
- input:
  - '5'
  - '5'
  - '5'
  expected: '5

    '
starter_code: ''
---

Lies drei ganze Zahlen ein und gib die größte aus, ohne fertige Hilfen wie max. Bei `4`, `9`, `2`:

```
9
```
