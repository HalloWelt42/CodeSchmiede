---
schema_version: 1
id: k212-neujahr
revision: 1
titel: Neujahr
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- datum
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Jahr, Monat, Tag: `date(2027, 1, 1)`.'
tests_sichtbar:
- input: []
  expected: '2027-01-01

    4

    '
starter_code: 'from datetime import date


  neujahr = date(___)

  print(neujahr)

  print(neujahr.weekday())

  '
---

Ergänze die Lücke `___`, damit Neujahr 2027 entsteht und sein Wochentag als Zahl erscheint:

```
2027-01-01
4
```
