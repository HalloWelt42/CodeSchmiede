---
schema_version: 1
id: j045-ausschnitt
revision: 1
titel: Halbe Brötchen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- text
- textmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`slice(von, bis)` nimmt die Zeichen ab von bis vor bis.'
- kosten: 2
  text: Ohne zweite Zahl geht `slice(5)` bis zum Ende.
tests_sichtbar:
- input: []
  expected: 'Fisch

    brötchen

    '
starter_code: 'const wort = "Fischbrötchen";

  '
---

Zerlege `Fischbrötchen` mit `slice` in seine beiden Hälften:

```
Fisch
brötchen
```
