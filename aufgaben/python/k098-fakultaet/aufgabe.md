---
schema_version: 1
id: k098-fakultaet
revision: 1
titel: Die Fakultät
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- for
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Sammler, der bei 1 beginnt, weil mal 0 alles zunichte machte.
- kosten: 3
  text: '`produkt *= i` in einer Schleife über range(1, n + 1).'
tests_sichtbar:
- input:
  - '5'
  expected: '120

    '
tests_versteckt:
- input:
  - '0'
  expected: '1

    '
- input:
  - '10'
  expected: '3628800

    '
- input:
  - '1'
  expected: '1

    '
starter_code: ''
---

Lies eine Zahl n ein und gib das Produkt 1 · 2 · ... · n aus (die Fakultät). Für n = 0 ist das Ergebnis 1. Bei `5`:

```
120
```
