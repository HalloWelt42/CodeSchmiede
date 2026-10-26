---
schema_version: 1
id: j157-kette
revision: 1
titel: Die Kette
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- rueckrufmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: filter, dann map, dann sort, dann join, alles mit Punkten hintereinander.
tests_sichtbar:
- input: []
  expected: 'FRIEDA, GUSTAV, PAULA

    '
starter_code: 'const namen = ["Pia", "Gustav", "Ole", "Paula", "Kim", "Frieda"];

  '
---

Mach in **einer** Kette aus Methoden aus den Namen eine Liste der Namen mit mehr als drei Buchstaben, in Großbuchstaben, alphabetisch:

```
FRIEDA, GUSTAV, PAULA
```
