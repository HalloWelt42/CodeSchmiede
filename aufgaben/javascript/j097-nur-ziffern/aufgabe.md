---
schema_version: 1
id: j097-nur-ziffern
revision: 1
titel: Nur die Ziffern
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- continue
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`"0123456789".includes(z)` sagt, ob z eine Ziffer ist; `!` dreht es um.'
tests_sichtbar:
- input:
  - A-12-B7
  expected: 'Nummer? 127

    '
tests_versteckt:
- input:
  - 2026/10/26
  expected: 'Nummer? 20261026

    '
- input:
  - Fisch
  expected: "Nummer? \n"
starter_code: ''
---

Aus einer Bestellnummer wie `A-12-B7` sollen nur die Ziffern übrig bleiben. Geh mit for ... of durch die Eingabe, überspringe mit `continue` alles, was keine Ziffer ist, und sammle den Rest. Bei der Eingabe `A-12-B7`:

```
Nummer? 127
```
