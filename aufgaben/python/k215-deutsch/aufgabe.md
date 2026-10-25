---
schema_version: 1
id: k215-deutsch
revision: 1
titel: Auf Deutsch, bitte
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- datum
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`strftime("%d.%m.%Y")`.'
tests_sichtbar:
- input:
  - '2026-03-07'
  expected: '07.03.2026

    '
tests_versteckt:
- input:
  - '2026-12-24'
  expected: '24.12.2026

    '
starter_code: ''
---

Lies ein Datum in der Form `2026-10-25` ein und gib es in deutscher Schreibweise aus. Bei `2026-03-07`:

```
07.03.2026
```
