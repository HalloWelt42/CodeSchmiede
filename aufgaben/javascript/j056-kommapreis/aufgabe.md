---
schema_version: 1
id: j056-kommapreis
revision: 1
titel: Preis mit zwei Stellen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- eingabe
- nachkommastellen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst rechnen, dann `.toFixed(2)`.
- kosten: 2
  text: 'Um eine Rechnung herum braucht es Klammern: `(anzahl * 1.75).toFixed(2)`.'
tests_sichtbar:
- input:
  - '2'
  expected: 'Limonaden? Preis: 3.50 Euro

    '
tests_versteckt:
- input:
  - '4'
  expected: 'Limonaden? Preis: 7.00 Euro

    '
- input:
  - '3'
  expected: 'Limonaden? Preis: 5.25 Euro

    '
starter_code: ''
---

Lies die Zahl der Limonaden ein (je `1.75`) und gib den Preis immer mit zwei Stellen aus. Bei der Eingabe `2`:

```
Limonaden? Preis: 3.50 Euro
```
