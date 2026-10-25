---
schema_version: 1
id: k146-nur-bei-pit
revision: 1
titel: Nur bei Pit
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- menge
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`pit - pia` nimmt aus Pits Menge alles heraus, was Pia auch mag.'
tests_sichtbar:
- input: []
  expected: '[''Erdbeer'', ''Zitrone'']

    '
starter_code: 'pit = {"Vanille", "Erdbeer", "Nuss", "Zitrone"}

  pia = {"Nuss", "Schoko", "Vanille"}

  '
---

Welche Sorten mag nur Pit, Pia aber nicht? Gib sie sortiert in einer Liste aus:

```
['Erdbeer', 'Zitrone']
```
