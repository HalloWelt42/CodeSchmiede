---
schema_version: 1
id: k084-summe-bis-n
revision: 1
titel: Alles zusammen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- while
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Sammler summe beginnt vor der Schleife bei 0.
tests_sichtbar:
- input:
  - '4'
  expected: '10

    '
tests_versteckt:
- input:
  - '100'
  expected: '5050

    '
- input:
  - '1'
  expected: '1

    '
starter_code: ''
---

Lies eine Zahl n ein und gib die Summe 1 + 2 + ... + n aus. Bei `4`:

```
10
```
