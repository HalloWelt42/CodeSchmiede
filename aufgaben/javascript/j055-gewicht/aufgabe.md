---
schema_version: 1
id: j055-gewicht
revision: 1
titel: Fang auf der Waage
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- eingabe
- nan
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`Number("2.5 kg")` wäre NaN; `parseFloat` nimmt die Zahl vorne.'
tests_sichtbar:
- input:
  - 2.5 kg
  expected: 'Gewicht? Preis: 10 Euro

    '
tests_versteckt:
- input:
  - 0.75 kg
  expected: 'Gewicht? Preis: 3 Euro

    '
- input:
  - 3kg
  expected: 'Gewicht? Preis: 12 Euro

    '
starter_code: ''
---

Die Waage schreibt das Gewicht mit Einheit, etwa `2.5 kg`. Fisch die Zahl mit `parseFloat` heraus und rechne den Preis bei 4 Euro je Kilo. Bei der Eingabe `2.5 kg`:

```
Gewicht? Preis: 10 Euro
```
