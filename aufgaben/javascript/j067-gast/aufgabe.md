---
schema_version: 1
id: j067-gast
revision: 1
titel: Ein Name für jeden
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- wahrheit
- logik
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der leere Text gilt als falsch, und `||` nimmt dann den Wert rechts.
- kosten: 2
  text: '`prompt("Name? ") || "Gast"`'
tests_sichtbar:
- input:
  - Ole
  expected: 'Name? Moin, Ole!

    '
- input:
  - ''
  expected: 'Name? Moin, Gast!

    '
tests_versteckt:
- input: []
  expected: 'Name? Moin, Gast!

    '
- input:
  - Ida
  expected: 'Name? Moin, Ida!

    '
starter_code: ''
---

Wer bei der Frage nach dem Namen nur Enter drückt, soll trotzdem begrüßt werden, als Gast. Bei der Eingabe `Ole`:

```
Name? Moin, Ole!
```

Bei leerer Eingabe heißt es `Moin, Gast!`.
