---
schema_version: 1
id: k185-mittelwert
revision: 1
titel: Mittelwert und Median
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
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
  text: '`from statistics import mean, median` holt beide Werkzeuge.'
tests_sichtbar:
- input:
  - '2'
  - '9'
  - '4'
  - ende
  expected: 'Mittelwert: 5

    Median: 4

    '
tests_versteckt:
- input:
  - '1'
  - '2'
  - ende
  expected: 'Mittelwert: 1.5

    Median: 1.5

    '
- input:
  - '7'
  - ende
  expected: 'Mittelwert: 7

    Median: 7

    '
starter_code: ''
---

Lies ganze Zahlen ein, bis `ende` kommt, und gib Mittelwert und Median mit `mean` und `median` aus dem Modul statistics aus. Bei `2`, `9`, `4`, `ende`:

```
Mittelwert: 5
Median: 4
```
