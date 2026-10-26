---
schema_version: 1
id: j152-preise-mit-map
revision: 1
titel: Preise mit map
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
  text: '`preise.map(p => ...)` liefert ein neues Array mit den Texten.'
tests_sichtbar:
- input: []
  expected: '2.50 Euro | 1.75 Euro | 4.50 Euro

    '
starter_code: 'const preise = [2.5, 1.75, 4.5];

  '
---

Mach mit `map` aus den Preisen Texte mit zwei Stellen und `Euro`, und gib sie mit join aus:

```
2.50 Euro | 1.75 Euro | 4.50 Euro
```
