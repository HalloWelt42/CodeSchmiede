---
schema_version: 1
id: j124-preisliste
revision: 1
titel: Die Preisliste
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- objekt
- for_in
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`for (const fisch in preise)` liefert die Namen.'
tests_sichtbar:
- input: []
  expected: 'Hering: 2.50 Euro

    Aal: 5.00 Euro

    Makrele: 3.20 Euro

    3 Sorten

    '
starter_code: 'const preise = { Hering: 2.5, Aal: 5, Makrele: 3.2 };

  '
---

Gib alle Preise mit `for ... in` aus, jeden mit zwei Stellen, und darunter die Zahl der Sorten mit `Object.keys`:

```
Hering: 2.50 Euro
Aal: 5.00 Euro
Makrele: 3.20 Euro
3 Sorten
```
