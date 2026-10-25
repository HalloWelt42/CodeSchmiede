---
schema_version: 1
id: k173-sichere-zahl
revision: 1
titel: Die sichere Zahl
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- ausnahme
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Umwandlung mit int gehört in den try-Block.
tests_sichtbar:
- input:
  - '21'
  expected: 'Doppelt: 42

    '
- input:
  - einundzwanzig
  expected: 'Keine Zahl

    '
tests_versteckt:
- input:
  - '2.5'
  expected: 'Keine Zahl

    '
- input:
  - '-4'
  expected: 'Doppelt: -8

    '
starter_code: ''
---

Lies einen Text ein. Ist er eine ganze Zahl, gib ihr Doppeltes aus, sonst `Keine Zahl`. Bei `21`:

```
Doppelt: 42
```

Bei `einundzwanzig`:

```
Keine Zahl
```
