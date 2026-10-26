---
schema_version: 1
id: j091-einmaleins
revision: 1
titel: Das Einmaleins
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Von 1 bis einschließlich 10.
tests_sichtbar:
- input:
  - '7'
  expected: 'Reihe? 1 x 7 = 7

    2 x 7 = 14

    3 x 7 = 21

    4 x 7 = 28

    5 x 7 = 35

    6 x 7 = 42

    7 x 7 = 49

    8 x 7 = 56

    9 x 7 = 63

    10 x 7 = 70

    '
tests_versteckt:
- input:
  - '3'
  expected: 'Reihe? 1 x 3 = 3

    2 x 3 = 6

    3 x 3 = 9

    4 x 3 = 12

    5 x 3 = 15

    6 x 3 = 18

    7 x 3 = 21

    8 x 3 = 24

    9 x 3 = 27

    10 x 3 = 30

    '
- input:
  - '12'
  expected: 'Reihe? 1 x 12 = 12

    2 x 12 = 24

    3 x 12 = 36

    4 x 12 = 48

    5 x 12 = 60

    6 x 12 = 72

    7 x 12 = 84

    8 x 12 = 96

    9 x 12 = 108

    10 x 12 = 120

    '
starter_code: "const n = Number(prompt(\"Reihe? \"));\nfor (let i = 1; ___; i++) {\n  console.log(`${i} x ${n} = ${i * n}`);\n\
  }\n"
---

Lies eine Zahl und gib ihre Einmaleinsreihe von 1 bis 10 aus. Bei der Eingabe `7` beginnt es so:

```
Reihe? 1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
```

und endet mit `10 x 7 = 70`.
