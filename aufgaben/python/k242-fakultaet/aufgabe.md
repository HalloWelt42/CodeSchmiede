---
schema_version: 1
id: k242-fakultaet
revision: 1
titel: Der Abbruchfall
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- rekursion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die kleinste Fakultät ist 0! und die ist 1.
tests_sichtbar:
- input: []
  expected: '120

    '
starter_code: "def fakultaet(n):\n    if n == ___:\n        return 1\n    return n * fakultaet(n - 1)\n\n\nprint(fakultaet(5))\n"
---

Ergänze die Lücke `___`, damit die Fakultät ihren Abbruchfall hat:

```
120
```
