---
schema_version: 1
id: k046-schreihals
revision: 1
titel: Der Schreihals
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- text
- methoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst `strip()`, dann `upper()`; Methoden lassen sich hintereinander aufrufen.
tests_sichtbar:
- input: []
  expected: 'FISCH HER!

    '
starter_code: 'ruf = "   fisch her!  "

  '
---

Der Möwenruf soll ohne die Leerzeichen am Rand und in Großbuchstaben erscheinen:

```
FISCH HER!
```
