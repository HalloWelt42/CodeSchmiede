---
schema_version: 1
id: j106-groesster-fang
revision: 1
titel: Der beste Tag
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- array
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Merk dir den Index des bisher besten Tags, nicht nur den Wert.
- kosten: 2
  text: Zählschleife über alle Indizes; ist `faenge[i]` größer als `faenge[bester]`, wird i der neue beste.
tests_sichtbar:
- input: []
  expected: 'Bester Tag: 2 mit 9 Fischen

    '
starter_code: 'const faenge = [4, 9, 2, 7, 5];

  '
---

Finde den größten Fang **und** den Tag, an dem er war (Tag 1 ist Index 0), ohne `Math.max`:

```
Bester Tag: 2 mit 9 Fischen
```
