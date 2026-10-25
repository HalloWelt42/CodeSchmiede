---
schema_version: 1
id: k244-potenz
revision: 1
titel: Hoch hinaus
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rekursion
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Jede Zahl hoch 0 ist 1.
- kosten: 2
  text: '`basis * potenz(basis, exponent - 1)`.'
tests_sichtbar:
- input:
  - '2'
  - '10'
  expected: '1024

    '
tests_versteckt:
- input:
  - '7'
  - '0'
  expected: '1

    '
- input:
  - '-3'
  - '3'
  expected: '-27

    '
starter_code: ''
---

Schreibe ohne `**` und ohne Schleife eine rekursive Funktion `potenz(basis, exponent)`. Lies Basis und Exponent ein (ganze Zahlen, Exponent nicht negativ). Bei `2` und `10`:

```
1024
```
