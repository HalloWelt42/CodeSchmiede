---
schema_version: 1
id: j046-schreihals
revision: 1
titel: Der Schreihals
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
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
  text: '`toUpperCase()` macht groß.'
- kosten: 2
  text: '`"!".repeat(3)` wiederholt das Ausrufezeichen.'
tests_sichtbar:
- input: []
  expected: 'FISCH!!!

    '
starter_code: 'const wort = "fisch";

  '
---

Die Möwe ruft alles, was sie sieht, in Großbuchstaben und mit drei Ausrufezeichen. Mach aus `fisch` den Ruf:

```
FISCH!!!
```
