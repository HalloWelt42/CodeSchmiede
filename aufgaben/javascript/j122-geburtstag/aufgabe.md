---
schema_version: 1
id: j122-geburtstag
revision: 1
titel: Geburtstag
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- objekt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Neue Eigenschaften legt eine einfache Zuweisung an.
tests_sichtbar:
- input: []
  expected: '{ name: ''Pit'', alter: 5, hut: ''Papierkrone'' }

    '
starter_code: 'const pinguin = { name: "Pit", alter: 4 };

  '
---

Pit hat Geburtstag: Zähl sein Alter hoch, gib ihm die neue Eigenschaft `hut` mit `"Papierkrone"` und gib das Objekt aus:

```
{ name: 'Pit', alter: 5, hut: 'Papierkrone' }
```
