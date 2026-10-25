---
schema_version: 1
id: k044-erster-letzter
revision: 1
titel: Erster und letzter Buchstabe
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- text
- index
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der erste hat den Index 0, der letzte den Index -1.
tests_sichtbar:
- input: []
  expected: 'W

    s

    '
starter_code: 'wort = "Walross"

  '
---

Gib den ersten und den letzten Buchstaben von `wort` aus, jeden in seiner Zeile:

```
W
s
```
