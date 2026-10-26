---
schema_version: 1
id: j133-telefonbuch
revision: 1
titel: Das Telefonbuch
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 5
tags:
- kurs
- map
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Nummer bleibt Text, sonst verschwindet die führende Null.
- kosten: 2
  text: Ein zweiter Eintrag mit demselben Namen überschreibt den ersten.
tests_sichtbar:
- input:
  - Pia 0815
  - Ole 4711
  - ''
  - Ole
  expected: 'Eintrag? Eintrag? Eintrag? Einträge: 2

    Wen suchst du? Ole: 4711

    '
tests_versteckt:
- input:
  - Ida 0042
  - ''
  - Bo
  expected: 'Eintrag? Eintrag? Einträge: 1

    Wen suchst du? Bo steht nicht drin

    '
- input:
  - A 1
  - B 2
  - A 3
  - ''
  - A
  expected: 'Eintrag? Eintrag? Eintrag? Eintrag? Einträge: 2

    Wen suchst du? A: 3

    '
starter_code: ''
---

Lies Einträge wie `Pia 0815` in eine Map, bis eine leere Antwort kommt, gib die Zahl der Einträge aus und frag dann, wen du suchst. Bei den Eingaben `Pia 0815`, `Ole 4711`, einer leeren Antwort und `Ole`:

```
Eintrag? Eintrag? Eintrag? Einträge: 2
Wen suchst du? Ole: 4711
```
