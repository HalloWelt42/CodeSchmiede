---
schema_version: 1
id: j092-fuenferschritte
revision: 1
titel: In Fünferschritten
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der Schritt ist `i += 5`.
- kosten: 2
  text: Vor jede Zahl außer der ersten ein Leerzeichen, etwa mit `? :`.
tests_sichtbar:
- input:
  - '20'
  expected: 'Bis? 0 5 10 15 20

    '
tests_versteckt:
- input:
  - '12'
  expected: 'Bis? 0 5 10

    '
- input:
  - '0'
  expected: 'Bis? 0

    '
starter_code: ''
---

Lies eine Grenze und sammle alle Zahlen von 0 bis zur Grenze in Fünferschritten in einem Text, getrennt durch Leerzeichen. Bei der Eingabe `20`:

```
Bis? 0 5 10 15 20
```
