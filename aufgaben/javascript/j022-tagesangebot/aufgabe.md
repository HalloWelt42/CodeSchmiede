---
schema_version: 1
id: j022-tagesangebot
revision: 1
titel: Das Tagesangebot
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- variablen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`let angebot = "Hering";` legt den Namen an.'
- kosten: 2
  text: 'Text und Name passen in ein `console.log`: `console.log("Heute:", angebot);`'
tests_sichtbar:
- input: []
  expected: 'Heute: Hering

    '
starter_code: ''
---

Lege mit `let` einen Namen `angebot` mit dem Wert `"Hering"` an und gib ihn so aus:

```
Heute: Hering
```
