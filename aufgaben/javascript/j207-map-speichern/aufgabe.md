---
schema_version: 1
id: j207-map-speichern
revision: 1
titel: Eine Map speichern
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- json
- map
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mit `for (const [ware, menge] of lager)` ein Objekt füllen.
- kosten: 2
  text: Beim Laden mit for ... in die Map wieder aufbauen.
tests_sichtbar:
- input: []
  expected: '{"Hering":12,"Aal":3}

    Wieder da: 2 Sorten, Hering: 12

    '
starter_code: 'const lager = new Map();

  lager.set("Hering", 12);

  lager.set("Aal", 3);

  '
---

JSON kennt keine Maps. Wandle die Map vor dem Speichern in ein Objekt um, gib den JSON-Text aus, lies ihn wieder ein und bau daraus eine neue Map:

```
{"Hering":12,"Aal":3}
Wieder da: 2 Sorten, Hering: 12
```
