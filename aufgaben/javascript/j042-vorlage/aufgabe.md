---
schema_version: 1
id: j042-vorlage
revision: 1
titel: Die erste Vorlage
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- text
- vorlage
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Wie bei `${name}`: Dollar und geschweifte Klammern um den Namen.'
tests_sichtbar:
- input: []
  expected: 'Pit hat 3 Fische und 2 Muscheln.

    '
starter_code: 'const name = "Pit";

  const fische = 3;

  const muscheln = 2;

  console.log(`${name} hat ___ Fische und ___ Muscheln.`);

  '
---

Ergänze die Vorlage, damit herauskommt:

```
Pit hat 3 Fische und 2 Muscheln.
```
