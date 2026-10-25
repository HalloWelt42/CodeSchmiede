---
schema_version: 1
id: k108-ueber-schnitt
revision: 1
titel: Über dem Schnitt
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- liste
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst alles in eine Liste lesen, dann rechnen, dann noch einmal durchgehen.
tests_sichtbar:
- input:
  - '4'
  - '8'
  - '6'
  - '0'
  expected: 'Durchschnitt: 6.0

    8

    '
tests_versteckt:
- input:
  - '1'
  - '2'
  - '3'
  - '10'
  - '0'
  expected: 'Durchschnitt: 4.0

    10

    '
- input:
  - '5'
  - '5'
  - '0'
  expected: 'Durchschnitt: 5.0

    '
starter_code: ''
---

Lies Zahlen ein, bis eine `0` kommt. Gib dann den Durchschnitt aus und danach jede Zahl, die größer als der Durchschnitt ist, in einer eigenen Zeile. Bei `4`, `8`, `6`, `0`:

```
Durchschnitt: 6.0
8
```
