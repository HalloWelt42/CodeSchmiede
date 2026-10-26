---
schema_version: 1
id: j217-nacheinander
revision: 1
titel: Nacheinander oder zugleich
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- async
- promise
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Nacheinander: eine for ... of-Schleife mit `await kochen(ms)`.'
- kosten: 2
  text: 'Zugleich: alle drei Aufrufe in `Promise.all([...])`, dann ein await.'
tests_sichtbar:
- input: []
  expected: 'Nacheinander: höchstens 1 auf dem Herd

    Zugleich: höchstens 3 auf dem Herd

    '
starter_code: "let aufDemHerd = 0;\nlet hoechstens = 0;\nfunction kochen(ms) {\n  aufDemHerd++;\n  hoechstens = Math.max(hoechstens,\
  \ aufDemHerd);\n  return new Promise((erfuellen) => {\n    setTimeout(() => {\n      aufDemHerd--;\n      erfuellen();\n\
  \    }, ms);\n  });\n}\n"
---

Die Küche kocht dieselben drei Gerichte einmal nacheinander (jedes await wartet) und einmal zugleich (Promise.all). Der Startcode zählt mit, wie viele Gerichte gleichzeitig auf dem Herd stehen; gib nach jeder Runde den höchsten Stand aus. Nacheinander steht immer nur eins drauf, zugleich alle drei:

```
Nacheinander: höchstens 1 auf dem Herd
Zugleich: höchstens 3 auf dem Herd
```
