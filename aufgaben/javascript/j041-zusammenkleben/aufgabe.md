---
schema_version: 1
id: j041-zusammenkleben
revision: 1
titel: Zusammengeklebt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- text
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwischen Texten klebt das Plus, ohne Leerzeichen.
tests_sichtbar:
- input: []
  expected: 'Fischbrötchen

    '
starter_code: 'const vorne = "Fisch";

  const hinten = "brötchen";

  console.log(___);

  '
---

Klebe die beiden Teile mit `+` zu einem Wort zusammen und gib es aus:

```
Fischbrötchen
```
