---
schema_version: 1
id: j086-quersumme
revision: 1
titel: Quersumme
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- while
- rest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Solange noch Ziffern da sind (zahl > 0): letzte Ziffer dazuzählen, dann abschneiden.'
tests_sichtbar:
- input:
  - '472'
  expected: 'Zahl? Quersumme: 13

    '
tests_versteckt:
- input:
  - '9'
  expected: 'Zahl? Quersumme: 9

    '
- input:
  - '10203'
  expected: 'Zahl? Quersumme: 6

    '
starter_code: ''
---

Die Quersumme ist die Summe aller Ziffern einer Zahl. Ohne die Zahl in Text zu verwandeln: `% 10` liefert die letzte Ziffer, `Math.floor(zahl / 10)` streicht sie. Bei der Eingabe `472`:

```
Zahl? Quersumme: 13
```
