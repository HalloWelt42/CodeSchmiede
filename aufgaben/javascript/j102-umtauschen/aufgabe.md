---
schema_version: 1
id: j102-umtauschen
revision: 1
titel: Fach tauschen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- array
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Makrele steht in Fach 1.
- kosten: 2
  text: '`fische[1] = "Lachs";` und dann `console.log(fische);`'
tests_sichtbar:
- input: []
  expected: '[ ''Hering'', ''Lachs'', ''Sprotte'' ]

    '
starter_code: 'const fische = ["Hering", "Makrele", "Sprotte"];

  '
---

Die Makrele ist ausverkauft. Ersetze sie im Array durch Lachs, über ihren Index, und gib das ganze Array aus:

```
[ 'Hering', 'Lachs', 'Sprotte' ]
```
