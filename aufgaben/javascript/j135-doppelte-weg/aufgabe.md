---
schema_version: 1
id: j135-doppelte-weg
revision: 1
titel: Doppelte weg
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- set
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`new Set(array)` wirft Doppelte weg.'
- kosten: 2
  text: 'Für join braucht es ein Array: in einer Schleife mit push füllen.'
tests_sichtbar:
- input:
  - Hering,Aal,Hering,Butt,Aal
  expected: 'Fische? 5 Fische, 3 verschiedene

    Hering, Aal, Butt

    '
tests_versteckt:
- input:
  - Aal
  expected: 'Fische? 1 Fische, 1 verschiedene

    Aal

    '
- input:
  - a,a,a,b
  expected: 'Fische? 4 Fische, 2 verschiedene

    a, b

    '
starter_code: ''
---

Lies eine Liste von Fischen mit Kommas ein und gib aus, wie viele es waren und wie viele verschiedene, und die verschiedenen in der Reihenfolge ihres ersten Auftretens. Bei der Eingabe `Hering,Aal,Hering,Butt,Aal`:

```
Fische? 5 Fische, 3 verschiedene
Hering, Aal, Butt
```
