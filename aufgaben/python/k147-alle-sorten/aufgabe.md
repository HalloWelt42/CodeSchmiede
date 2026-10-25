---
schema_version: 1
id: k147-alle-sorten
revision: 1
titel: Die ganze Eistheke
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
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
  text: '`|` legt zusammen, auch drei Mengen hintereinander.'
tests_sichtbar:
- input: []
  expected: '6 Sorten

    [''Erdbeer'', ''Minze'', ''Nuss'', ''Schoko'', ''Vanille'', ''Zitrone'']

    '
starter_code: 'pit = {"Vanille", "Erdbeer", "Nuss", "Zitrone"}

  pia = {"Nuss", "Schoko", "Vanille"}

  paul = {"Minze", "Schoko"}

  '
---

Pit, Pia und Paul haben je ihre Lieblingssorten. Wie viele verschiedene Sorten muss die Eisdiele für alle drei bereithalten, und welche sind es (sortiert)?

```
6 Sorten
['Erdbeer', 'Minze', 'Nuss', 'Schoko', 'Vanille', 'Zitrone']
```
