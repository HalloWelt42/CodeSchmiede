---
schema_version: 1
id: k183-kreisflaeche
revision: 1
titel: Das runde Eisloch
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
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
  text: '`import math`, dann `math.pi`.'
tests_sichtbar:
- input:
  - '5'
  expected: 'Fläche: 78.54

    '
tests_versteckt:
- input:
  - '1'
  expected: 'Fläche: 3.14

    '
- input:
  - '0'
  expected: 'Fläche: 0.0

    '
starter_code: ''
---

Lies den Radius eines runden Eislochs ein (ganze Zahl) und gib seine Fläche `pi * r * r` auf zwei Stellen gerundet aus. Nimm `pi` aus dem Modul math. Bei `5`:

```
Fläche: 78.54
```
