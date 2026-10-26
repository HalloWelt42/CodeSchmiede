---
schema_version: 1
id: j101-erstes-array
revision: 1
titel: Das erste Array
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- array
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Index 0 ist der erste, `fische.length - 1` der letzte.
tests_sichtbar:
- input: []
  expected: 'Erster: Hering

    Letzter: Dorsch

    Anzahl: 4

    '
starter_code: 'const fische = ["Hering", "Makrele", "Sprotte", "Dorsch"];

  '
---

Gib aus dem Array den ersten und den letzten Fisch aus und dazu, wie viele es sind:

```
Erster: Hering
Letzter: Dorsch
Anzahl: 4
```
