---
schema_version: 1
id: j202-zettel-lesen
revision: 1
titel: Den Zettel lesen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
  text: '`JSON.parse(prompt(...))` baut das Objekt.'
tests_sichtbar:
- input:
  - '{"name":"Pia","stempel":3}'
  expected: 'Kunde? Pia hat 3 Stempel

    '
tests_versteckt:
- input:
  - '{"stempel":0,"name":"Ole","alter":7}'
  expected: 'Kunde? Ole hat 0 Stempel

    '
starter_code: ''
---

Lies einen JSON-Text mit einem Kunden ein und gib Name und Zahl der Stempel aus. Bei der Eingabe `{"name":"Pia","stempel":3}`:

```
Kunde? Pia hat 3 Stempel
```
