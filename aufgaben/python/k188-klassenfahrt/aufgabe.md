---
schema_version: 1
id: k188-klassenfahrt
revision: 1
titel: Die Klassenfahrt
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- modul
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Zwei Imports: `import math` und `from statistics import mean, median`.'
- kosten: 3
  text: 'Busse: `math.ceil(len(alter) / plaetze)`.'
tests_sichtbar:
- input:
  - '3'
  - '11'
  - '12'
  - '11'
  - '40'
  - ende
  expected: 'Busse: 2

    Mittleres Alter: 18.5

    Median: 11.5

    '
tests_versteckt:
- input:
  - '50'
  - '10'
  - ende
  expected: 'Busse: 1

    Mittleres Alter: 10

    Median: 10

    '
- input:
  - '2'
  - '9'
  - '10'
  - '11'
  - ende
  expected: 'Busse: 2

    Mittleres Alter: 10

    Median: 10

    '
starter_code: ''
---

Für die Klassenfahrt: lies erst die Plätze je Bus, dann die Alter der Mitfahrenden, bis `ende` kommt. Gib aus, wie viele Busse nötig sind (mit `math.ceil`), dann das mittlere Alter mit `mean` auf eine Stelle gerundet und den Median mit `median` aus statistics. Bei `3`, `11`, `12`, `11`, `40`, `ende`:

```
Busse: 2
Mittleres Alter: 18.5
Median: 11.5
```
