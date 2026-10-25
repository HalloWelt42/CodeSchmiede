---
schema_version: 1
id: k246-fibonacci
revision: 1
titel: Die Kaninchenzahlen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- rekursion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Zwei Abbruchfälle in einem: für n kleiner als 2 ist fib(n) gleich n.'
- kosten: 2
  text: Sonst `fib(n - 1) + fib(n - 2)`.
tests_sichtbar:
- input:
  - '10'
  expected: '55

    '
tests_versteckt:
- input:
  - '0'
  expected: '0

    '
- input:
  - '1'
  expected: '1

    '
- input:
  - '20'
  expected: '6765

    '
starter_code: ''
---

Die Fibonacci-Zahlen beginnen mit 0 und 1, jede weitere ist die Summe der beiden davor: 0, 1, 1, 2, 3, 5, 8 ... Schreibe eine rekursive Funktion `fib(n)` für die n-te Zahl (fib(0) ist 0). Lies n ein (höchstens 20). Bei `10`:

```
55
```
