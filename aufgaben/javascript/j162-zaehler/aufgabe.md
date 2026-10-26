---
schema_version: 1
id: j162-zaehler
revision: 1
titel: Der Klickzähler
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- sichtbarkeit
- closure
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`return () => { stand++; return stand; };`'
- kosten: 2
  text: Jeder Aufruf von zaehlerBauen hat sein eigenes stand.
tests_sichtbar:
- input: []
  expected: '1 2 3

    1

    '
starter_code: "function zaehlerBauen() {\n  let stand = 0;\n  // hier eine Funktion zurückgeben\n}\nconst klick = zaehlerBauen();\n\
  console.log(klick(), klick(), klick());\nconst neu = zaehlerBauen();\nconsole.log(neu());\n"
---

Ergänze `zaehlerBauen` so, dass sie eine Funktion zurückgibt, die bei jedem Aufruf um eins weiterzählt und den neuen Stand liefert:

```
1 2 3
1
```
