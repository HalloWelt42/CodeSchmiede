---
schema_version: 1
id: k214-countdown
revision: 1
titel: Wie lange noch?
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
  text: Zwei Daten abziehen ergibt eine Zeitspanne, `.days` die Zahl der Tage.
tests_sichtbar:
- input:
  - '2026-10-25'
  - '2026-12-24'
  expected: 'Noch 60 Tage

    '
tests_versteckt:
- input:
  - '2026-02-27'
  - '2026-03-01'
  expected: 'Noch 2 Tage

    '
- input:
  - '2028-02-28'
  - '2028-03-01'
  expected: 'Noch 2 Tage

    '
starter_code: ''
---

Lies zwei Daten in der Form `2026-10-25` ein, erst heute, dann den Tag der Klassenfahrt, und gib aus, wie viele Tage es noch sind. Bei `2026-10-25` und `2026-12-24`:

```
Noch 60 Tage
```
