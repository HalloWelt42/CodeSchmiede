---
schema_version: 1
id: j111-letzter-geht
revision: 1
titel: Der Letzte geht
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- arraymethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: pop liefert den herausgenommenen Wert.
tests_sichtbar:
- input: []
  expected: 'Geht: Ida

    [ ''Pia'', ''Ole'' ]

    '
starter_code: 'const schlange = ["Pia", "Ole", "Ida"];

  '
---

Der Letzte in der Schlange gibt auf. Nimm ihn mit `pop` heraus und gib ihn und die übrige Schlange aus:

```
Geht: Ida
[ 'Pia', 'Ole' ]
```
