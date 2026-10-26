---
schema_version: 1
id: j151-pfeil
revision: 1
titel: Vom Rezept zum Pfeil
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- pfeilfunktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`const halbieren = x => ...;`'
tests_sichtbar:
- input: []
  expected: '21 2.5

    '
starter_code: '// halbieren als Pfeilfunktion


  console.log(halbieren(42), halbieren(5));

  '
---

Früher stand hier `function halbieren(x) { return x / 2; }`. Leg `halbieren` jetzt als Pfeilfunktion in einer Zeile an, ohne geschweifte Klammern, damit herauskommt:

```
21 2.5
```
