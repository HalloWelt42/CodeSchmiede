---
schema_version: 1
id: k104-summe-liste
revision: 1
titel: Der Wochenfang
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- liste
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mit `liste + [wert]` hängst du ein Element hinten an.
- kosten: 2
  text: Danach eine zweite Schleife für die Summe.
tests_sichtbar:
- input:
  - '2'
  - '0'
  - '4'
  - '1'
  - '3'
  expected: '[2, 0, 4, 1, 3]

    10

    '
tests_versteckt:
- input:
  - '1'
  - '1'
  - '1'
  - '1'
  - '1'
  expected: '[1, 1, 1, 1, 1]

    5

    '
starter_code: ''
---

Lies fünf ganze Zahlen ein (die Fänge von Montag bis Freitag), lege sie in einer Liste ab und gib die Liste und die Summe aus. Bei `2`, `0`, `4`, `1`, `3`:

```
[2, 0, 4, 1, 3]
10
```
