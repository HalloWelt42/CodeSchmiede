---
schema_version: 1
id: j025-steckbrief-kurz
revision: 1
titel: Zwei Namen, eine Zeile
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- variablen
- const
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Zeilen mit `const`, dann ein `console.log` mit vier Werten.
- kosten: 2
  text: '`console.log(name, "ist", alter, "Jahre alt");`'
tests_sichtbar:
- input: []
  expected: 'Pia ist 5 Jahre alt

    '
starter_code: ''
---

Lege mit `const` die Namen `name` (Wert `"Pia"`) und `alter` (Wert `5`, als Zahl) an und gib beide in **einer** Zeile aus:

```
Pia ist 5 Jahre alt
```
