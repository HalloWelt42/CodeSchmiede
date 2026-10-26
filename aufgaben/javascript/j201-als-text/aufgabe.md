---
schema_version: 1
id: j201-als-text
revision: 1
titel: Als Text verschicken
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- json
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`JSON.stringify(fang)` liefert den Text.'
tests_sichtbar:
- input: []
  expected: '{"fisch":"Hering","anzahl":3,"frisch":true}

    43 Zeichen

    '
starter_code: 'const fang = { fisch: "Hering", anzahl: 3, frisch: true };

  '
---

Mach aus dem Objekt einen JSON-Text und gib ihn und seine Länge aus:

```
{"fisch":"Hering","anzahl":3,"frisch":true}
43 Zeichen
```
