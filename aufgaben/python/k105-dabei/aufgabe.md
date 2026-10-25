---
schema_version: 1
id: k105-dabei
revision: 1
titel: Ist er dabei?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- liste
- enthalten
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`name in gaeste` liefert True oder False.'
tests_sichtbar:
- input:
  - Pia
  expected: 'Herein!

    '
tests_versteckt:
- input:
  - Bodo
  expected: 'Nicht auf der Liste.

    '
- input:
  - Polly
  expected: 'Herein!

    '
starter_code: 'gaeste = ["Pit", "Pia", "Paul", "Polly"]

  '
---

Lies einen Namen ein und gib aus, ob er auf der Gästeliste steht: `Herein!` oder `Nicht auf der Liste.`. Bei `Pia`:

```
Herein!
```
