---
schema_version: 1
id: j116-zusammenlegen
revision: 1
titel: Zwei Schichten
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- arraymethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`frueh.concat(spaet)` liefert ein neues Array mit allen.'
tests_sichtbar:
- input: []
  expected: 'Kunden: 5

    Zuerst: Ole

    Zuletzt: Kim

    '
starter_code: 'const frueh = ["Ole", "Ida", "Bo"];

  const spaet = ["Lu", "Kim"];

  '
---

Pit und Pia haben je eine Liste der Kunden ihrer Schicht. Füg sie mit `concat` zusammen und gib aus, wie viele es insgesamt waren und wer zuerst und wer zuletzt kam:

```
Kunden: 5
Zuerst: Ole
Zuletzt: Kim
```
