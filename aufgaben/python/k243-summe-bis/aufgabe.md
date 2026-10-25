---
schema_version: 1
id: k243-summe-bis
revision: 1
titel: Summe bis n
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
  text: 'Abbruchfall: die Summe bis 0 ist 0.'
- kosten: 2
  text: 'Sonst: `n + summe(n - 1)`.'
tests_sichtbar:
- input:
  - '5'
  expected: 'Summe: 15

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Summe: 0

    '
- input:
  - '100'
  expected: 'Summe: 5050

    '
starter_code: ''
---

Schreibe ohne Schleife eine rekursive Funktion `summe(n)`, die 1 + 2 + ... + n berechnet. Lies n ein. Bei `5`:

```
Summe: 15
```
