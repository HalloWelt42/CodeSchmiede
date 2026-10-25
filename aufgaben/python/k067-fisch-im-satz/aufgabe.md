---
schema_version: 1
id: k067-fisch-im-satz
revision: 1
titel: Fisch im Satz?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- enthalten
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
  text: '`"Fisch" in satz` liefert True oder False.'
tests_sichtbar:
- input:
  - Heute gibt es Fischstäbchen
  expected: 'True

    '
tests_versteckt:
- input:
  - Heute gibt es Nudeln
  expected: 'False

    '
- input:
  - fisch klein
  expected: 'False

    '
starter_code: ''
---

Lies einen Satz ein und gib aus, ob das Wort `Fisch` darin vorkommt. Bei `Heute gibt es Fischstäbchen`:

```
True
```
