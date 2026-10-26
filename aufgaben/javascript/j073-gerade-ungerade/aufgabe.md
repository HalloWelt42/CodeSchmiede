---
schema_version: 1
id: j073-gerade-ungerade
revision: 1
titel: Gerade oder ungerade
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
  text: Kein Rest beim Teilen durch 2 heißt gerade.
tests_sichtbar:
- input:
  - '7'
  expected: 'Zahl? 7 ist ungerade

    '
tests_versteckt:
- input:
  - '10'
  expected: 'Zahl? 10 ist gerade

    '
- input:
  - '0'
  expected: 'Zahl? 0 ist gerade

    '
starter_code: ''
---

Lies eine Zahl und sag, ob sie gerade oder ungerade ist. Bei der Eingabe `7`:

```
Zahl? 7 ist ungerade
```
