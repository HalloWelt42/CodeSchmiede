---
schema_version: 1
id: j084-verdoppeln
revision: 1
titel: Fische vermehren sich
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Solange es weniger als das Ziel sind: verdoppeln und einen Tag zählen.'
tests_sichtbar:
- input:
  - '100'
  expected: 'Ziel? Nach 7 Tagen: 128 Fische

    '
tests_versteckt:
- input:
  - '1'
  expected: 'Ziel? Nach 0 Tagen: 1 Fische

    '
- input:
  - '1000'
  expected: 'Ziel? Nach 10 Tagen: 1024 Fische

    '
starter_code: ''
---

Im Aquarium verdoppeln sich die Fische jeden Tag, am Anfang ist es einer. Lies ein Ziel ein und gib aus, nach wie vielen Tagen es erreicht oder überschritten ist. Bei der Eingabe `100`:

```
Ziel? Nach 7 Tagen: 128 Fische
```
