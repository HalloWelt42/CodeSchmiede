---
schema_version: 1
id: k074-gerade-ungerade
revision: 1
titel: Gerade oder ungerade
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- verzweigung
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der Rest beim Teilen durch 2 entscheidet.
- kosten: 2
  text: f-String mit `{zahl}` in beiden Zweigen.
tests_sichtbar:
- input:
  - '7'
  expected: '7 ist ungerade

    '
tests_versteckt:
- input:
  - '10'
  expected: '10 ist gerade

    '
- input:
  - '-3'
  expected: '-3 ist ungerade

    '
starter_code: ''
---

Lies eine ganze Zahl ein und gib aus, ob sie gerade oder ungerade ist. Bei `7`:

```
7 ist ungerade
```
