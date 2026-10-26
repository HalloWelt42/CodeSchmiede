---
schema_version: 1
id: j213-versprochen
revision: 1
titel: Versprochen ist versprochen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 4
tags:
- kurs
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
  text: '`new Promise((erfuellen) => { setTimeout(() => erfuellen(wert), ms); })`'
tests_sichtbar:
- input: []
  expected: 'Warte auf den Fisch ...

    Angekommen: Hering

    '
starter_code: ''
---

Schreib `warte(ms, wert)`, die ein Promise liefert, das nach ms Millisekunden mit wert erfüllt wird, und gib mit `then` aus, was kommt:

```
Warte auf den Fisch ...
Angekommen: Hering
```
