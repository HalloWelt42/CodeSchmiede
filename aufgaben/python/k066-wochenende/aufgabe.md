---
schema_version: 1
id: k066-wochenende
revision: 1
titel: Frei?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- logik
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Vergleiche, verknüpft mit `or`.
tests_sichtbar:
- input:
  - Sonntag
  expected: 'True

    '
tests_versteckt:
- input:
  - Montag
  expected: 'False

    '
- input:
  - Samstag
  expected: 'True

    '
starter_code: ''
---

Pit hat frei, wenn Samstag **oder** Sonntag ist. Lies den Wochentag ein und gib aus, ob Pit frei hat. Bei `Sonntag`:

```
True
```
