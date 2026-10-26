---
schema_version: 1
id: j034-gerecht-teilen
revision: 1
titel: Gerecht teilen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- rechnen
- rest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Wie oft passt 5 ganz in 23? `Math.floor` rundet ab.
- kosten: 2
  text: Der Rest kommt von `%`.
tests_sichtbar:
- input: []
  expected: 'Jeder: 4

    Möwen: 3

    '
starter_code: 'const fische = 23;

  const pinguine = 5;

  '
---

23 Fische für 5 Pinguine. Jeder bekommt gleich viele ganze Fische, der Rest geht an die Möwen. Gib aus:

```
Jeder: 4
Möwen: 3
```
