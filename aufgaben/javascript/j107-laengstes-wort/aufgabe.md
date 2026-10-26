---
schema_version: 1
id: j107-laengstes-wort
revision: 1
titel: Das längste Wort
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- array
- zerlegen_verbinden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`split(" ")` liefert die Wörter.'
- kosten: 2
  text: Nur bei echt größerer Länge austauschen, dann bleibt bei Gleichstand das erste.
tests_sichtbar:
- input:
  - Pit verkauft frische Heringsbrötchen
  expected: 'Satz? Wörter: 4

    Längstes: Heringsbrötchen

    '
tests_versteckt:
- input:
  - Moin
  expected: 'Satz? Wörter: 1

    Längstes: Moin

    '
- input:
  - ab cd ef
  expected: 'Satz? Wörter: 3

    Längstes: ab

    '
- input:
  - Ein Eisbär isst gern Fisch
  expected: 'Satz? Wörter: 5

    Längstes: Eisbär

    '
starter_code: ''
---

Lies einen Satz, zerlege ihn an den Leerzeichen und gib die Zahl der Wörter und das längste Wort aus (bei gleicher Länge das erste). Bei der Eingabe `Pit verkauft frische Heringsbrötchen`:

```
Satz? Wörter: 4
Längstes: Heringsbrötchen
```
