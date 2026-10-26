---
schema_version: 1
id: j081-countdown
revision: 1
titel: Countdown
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Solange die Zahl größer als 0 ist.
tests_sichtbar:
- input:
  - '3'
  expected: 'Ab? 3

    2

    1

    Start!

    '
tests_versteckt:
- input:
  - '5'
  expected: 'Ab? 5

    4

    3

    2

    1

    Start!

    '
- input:
  - '0'
  expected: 'Ab? Start!

    '
starter_code: "let zahl = Number(prompt(\"Ab? \"));\nwhile (___) {\n  console.log(zahl);\n  zahl--;\n}\nconsole.log(\"Start!\"\
  );\n"
---

Lies eine Startzahl ein und zähle mit while bis 1 herunter, dann `Start!`. Bei der Eingabe `3`:

```
Ab? 3
2
1
Start!
```
