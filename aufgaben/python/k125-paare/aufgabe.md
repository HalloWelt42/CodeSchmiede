---
schema_version: 1
id: k125-paare
revision: 1
titel: Wer fing was?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- aufzaehlen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`for name, f in zip(namen, faenge):`'
tests_sichtbar:
- input: []
  expected: 'Pia fing 5

    Pit fing 3

    Paul fing 2

    '
starter_code: 'namen = ["Pia", "Pit", "Paul"]

  faenge = [5, 3, 2]

  '
---

Gib zu jedem Namen seinen Fang aus, mit zip:

```
Pia fing 5
Pit fing 3
Paul fing 2
```
