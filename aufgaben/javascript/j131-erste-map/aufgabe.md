---
schema_version: 1
id: j131-erste-map
revision: 1
titel: Die erste Map
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- map
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`new Map()`, dann `set`, `get`, `size` und `has`.'
tests_sichtbar:
- input: []
  expected: 'Hering: 12

    Sorten: 2

    Lachs da: false

    '
starter_code: ''
---

Lege eine Map `lager` an, setze `Hering` auf `12` und `Aal` auf `3` und gib aus:

```
Hering: 12
Sorten: 2
Lachs da: false
```
