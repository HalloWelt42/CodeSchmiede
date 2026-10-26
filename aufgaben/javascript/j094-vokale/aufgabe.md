---
schema_version: 1
id: j094-vokale
revision: 1
titel: Vokale zählen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- for_of
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`"aeiouäöü".includes(z)` fragt, ob z ein Vokal ist.'
- kosten: 2
  text: Vorher alles klein machen, dann zählen auch große Vokale.
tests_sichtbar:
- input:
  - Eisbär
  expected: 'Wort? Vokale: 3

    '
tests_versteckt:
- input:
  - Pfft
  expected: 'Wort? Vokale: 0

    '
- input:
  - OHAUEI
  expected: 'Wort? Vokale: 5

    '
starter_code: ''
---

Zähle die Vokale (a, e, i, o, u, ä, ö, ü, groß oder klein) in einem eingelesenen Wort. Bei der Eingabe `Eisbär`:

```
Wort? Vokale: 3
```
