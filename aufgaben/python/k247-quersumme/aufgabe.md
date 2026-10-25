---
schema_version: 1
id: k247-quersumme
revision: 1
titel: Die Quersumme
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- rekursion
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine einstellige Zahl ist ihre eigene Quersumme.
- kosten: 2
  text: Sonst letzte Ziffer plus Quersumme des Rests.
tests_sichtbar:
- input:
  - '4711'
  expected: 'Quersumme: 13

    '
tests_versteckt:
- input:
  - '7'
  expected: 'Quersumme: 7

    '
- input:
  - '999999'
  expected: 'Quersumme: 54

    '
starter_code: ''
---

Schreibe eine rekursive Funktion `quersumme(n)`: die letzte Ziffer ist `n % 10`, der Rest `n // 10`. Lies eine Zahl ein. Bei `4711`:

```
Quersumme: 13
```
