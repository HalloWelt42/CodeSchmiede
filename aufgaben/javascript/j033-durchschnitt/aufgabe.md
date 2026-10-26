---
schema_version: 1
id: j033-durchschnitt
revision: 1
titel: Durchschnittlicher Fang
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ohne Klammern würde nur mittwoch durch 3 geteilt, Punkt vor Strich.
- kosten: 2
  text: '`(montag + dienstag + mittwoch) / 3`'
tests_sichtbar:
- input: []
  expected: 'Durchschnitt: 7

    '
starter_code: 'const montag = 4;

  const dienstag = 7;

  const mittwoch = 10;

  '
---

An drei Tagen fängt Pit 4, 7 und 10 Fische. Rechne den Durchschnitt aus: alle zusammenzählen, dann durch 3 teilen. Achte auf die Klammern:

```
Durchschnitt: 7
```
