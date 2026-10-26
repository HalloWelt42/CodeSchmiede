---
schema_version: 1
id: j103-jeden-gruessen
revision: 1
titel: Jeden begrüßen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- array
- for_of
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`for (const gast of gaeste)`'
tests_sichtbar:
- input: []
  expected: 'Moin, Pia!

    Moin, Ole!

    Moin, Ida!

    '
starter_code: 'const gaeste = ["Pia", "Ole", "Ida"];

  '
---

Begrüße jeden Gast im Array mit einer eigenen Zeile:

```
Moin, Pia!
Moin, Ole!
Moin, Ida!
```
