---
schema_version: 1
id: k057-verteilen-mit-eingabe
revision: 1
titel: Verteilen nach Wunsch
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- eingabe
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Wie in Kapitel 3, nur dass die Zahlen jetzt eingelesen werden.
tests_sichtbar:
- input:
  - '17'
  - '5'
  expected: 'Jeder: 3

    Rest: 2

    '
tests_versteckt:
- input:
  - '9'
  - '4'
  expected: 'Jeder: 2

    Rest: 1

    '
- input:
  - '12'
  - '3'
  expected: 'Jeder: 4

    Rest: 0

    '
starter_code: ''
---

Lies erst die Zahl der Fische, dann die Zahl der Pinguine ein (ohne Fragetext) und gib aus, wie viele jeder bekommt und wie viele übrig bleiben. Bei `17` und `5`:

```
Jeder: 3
Rest: 2
```
