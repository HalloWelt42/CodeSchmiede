---
schema_version: 1
id: k134-alle-zeigen
revision: 1
titel: Alle Schubladen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- woerterbuch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: items für die Paare, values für die Summe.
tests_sichtbar:
- input: []
  expected: 'Pinguine: 12

    Robben: 3

    Möwen: 7

    Zusammen: 22

    '
starter_code: 'zaehlung = {"Pinguine": 12, "Robben": 3, "Möwen": 7}

  '
---

Gib jedes Tier mit seiner Anzahl aus und am Ende die Gesamtzahl:

```
Pinguine: 12
Robben: 3
Möwen: 7
Zusammen: 22
```
