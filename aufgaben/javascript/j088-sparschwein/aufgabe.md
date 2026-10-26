---
schema_version: 1
id: j088-sparschwein
revision: 1
titel: Das Sparschwein
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 7
tags:
- kurs
- while
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Drei Sammler vor der Schleife: anzahl, summe, groesste.'
- kosten: 2
  text: Ein abgelehnter Betrag landet im if, alle anderen im else.
tests_sichtbar:
- input:
  - '2.5'
  - '-1'
  - '6'
  - fertig
  expected: 'Betrag? Betrag? Nur positive Beträge!

    Betrag? Betrag? Einzahlungen: 2

    Summe: 8.50 Euro

    Größte: 6.00 Euro

    '
tests_versteckt:
- input: []
  expected: 'Betrag? Einzahlungen: 0

    Summe: 0.00 Euro

    Größte: 0.00 Euro

    '
- input:
  - '1'
  - '1.25'
  - '0'
  - '3'
  expected: 'Betrag? Betrag? Betrag? Nur positive Beträge!

    Betrag? Betrag? Einzahlungen: 3

    Summe: 5.25 Euro

    Größte: 3.00 Euro

    '
starter_code: ''
---

Lies Beträge ein, bis `fertig` kommt oder nichts mehr. Beträge bis 0 werden abgelehnt mit `Nur positive Beträge!` und nicht gezählt. Am Ende stehen die Zahl der Einzahlungen, die Summe und die größte Einzahlung, je mit zwei Stellen. Bei den Eingaben `2.5`, `-1`, `6` und `fertig`:

```
Betrag? Betrag? Nur positive Beträge!
Betrag? Betrag? Einzahlungen: 2
Summe: 8.50 Euro
Größte: 6.00 Euro
```
