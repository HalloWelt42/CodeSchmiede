---
schema_version: 1
id: k103-jeden-gruessen
revision: 1
titel: Alle begrüßen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- liste
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: for über die Liste, f-String im Block.
tests_sichtbar:
- input: []
  expected: 'Moin Pit!

    Moin Pia!

    Moin Paul!

    '
starter_code: 'kolonie = ["Pit", "Pia", "Paul"]

  '
---

Begrüße jeden Pinguin der Liste in einer eigenen Zeile:

```
Moin Pit!
Moin Pia!
Moin Paul!
```
