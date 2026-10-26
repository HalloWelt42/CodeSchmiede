---
schema_version: 1
id: j072-eis-haelt
revision: 1
titel: Hält das Eis?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- verzweigung
- else
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ein if mit else: genau einer der beiden Wege läuft.'
- kosten: 2
  text: Bei genau 0 Grad taut es schon.
tests_sichtbar:
- input:
  - '-4'
  expected: 'Grad? Eis hält

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Grad? Eis taut

    '
- input:
  - '12'
  expected: 'Grad? Eis taut

    '
- input:
  - '-0.5'
  expected: 'Grad? Eis hält

    '
starter_code: ''
---

Lies die Temperatur ein. Unter 0 Grad gib `Eis hält` aus, sonst `Eis taut`. Bei der Eingabe `-4`:

```
Grad? Eis hält
```
