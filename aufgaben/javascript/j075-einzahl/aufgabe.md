---
schema_version: 1
id: j075-einzahl
revision: 1
titel: Ein Fisch, zwei Fische
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- verzweigung
- bedingter_ausdruck
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`anzahl === 1 ? "Fisch" : "Fische"` liefert das Wort.'
tests_sichtbar:
- input:
  - '1'
  expected: 'Fische? Im Eimer: 1 Fisch

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Fische? Im Eimer: 0 Fische

    '
- input:
  - '7'
  expected: 'Fische? Im Eimer: 7 Fische

    '
starter_code: ''
---

Lies die Zahl der Fische und gib sie mit dem richtigen Wort aus, mit der Kurzform `? :`. Bei der Eingabe `1`:

```
Fische? Im Eimer: 1 Fisch
```

Bei allen anderen Zahlen, auch 0, heißt es Fische.
