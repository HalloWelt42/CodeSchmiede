---
schema_version: 1
id: j065-eis-kaufen
revision: 1
titel: Reicht es für ein Eis?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- wahrheit
- logik
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Drei Bedingungen müssen alle stimmen: genug Geld, nicht zu früh, nicht zu spät.'
- kosten: 2
  text: '`geld >= 2 && stunde >= 10 && stunde < 18`'
tests_sichtbar:
- input:
  - '3'
  - '12'
  expected: 'Geld? Stunde? Eis: true

    '
tests_versteckt:
- input:
  - '1'
  - '12'
  expected: 'Geld? Stunde? Eis: false

    '
- input:
  - '5'
  - '18'
  expected: 'Geld? Stunde? Eis: false

    '
- input:
  - '2'
  - '10'
  expected: 'Geld? Stunde? Eis: true

    '
starter_code: ''
---

Ein Eis kostet 2 Euro, und es gibt nur eins, wenn die Bude offen hat. Lies das Geld und die Stunde (0 bis 23) ein; geöffnet ist von 10 bis vor 18 Uhr. Bei den Eingaben `3` und `12`:

```
Geld? Stunde? Eis: true
```
