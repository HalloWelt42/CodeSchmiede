---
schema_version: 1
id: k172-durch-null
revision: 1
titel: Durch null
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags:
- kurs
- ausnahme
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Teilen durch null löst einen `ZeroDivisionError` aus.
tests_sichtbar:
- input: []
  expected: 'Teilen durch null geht nicht

    '
starter_code: "fische = 12\npinguine = 0\ntry:\n    print(fische / pinguine)\nexcept ___:\n    print(\"Teilen durch null geht\
  \ nicht\")\n"
---

Ergänze die Lücke `___` mit der passenden Fehlerart, damit das Programm nicht abstürzt:

```
Teilen durch null geht nicht
```
