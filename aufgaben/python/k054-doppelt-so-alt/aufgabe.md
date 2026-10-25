---
schema_version: 1
id: k054-doppelt-so-alt
revision: 1
titel: Doppelt so alt
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- eingabe
- umwandeln
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: input liefert Text; erst mit int umwandeln, dann rechnen.
tests_sichtbar:
- input:
  - '4'
  expected: '8

    '
tests_versteckt:
- input:
  - '11'
  expected: '22

    '
- input:
  - '0'
  expected: '0

    '
starter_code: ''
---

Lies mit `input()` ohne Fragetext eine Zahl ein und gib das Doppelte aus. Bei der Eingabe `4`:

```
8
```
