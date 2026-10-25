---
schema_version: 1
id: k145-gemeinsam
revision: 1
titel: Was beide mögen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- menge
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`pit & pia` ist das Gemeinsame, `sorted` bringt es in feste Reihenfolge.'
tests_sichtbar:
- input: []
  expected: 'Nuss

    Vanille

    '
starter_code: 'pit = {"Vanille", "Erdbeer", "Nuss", "Zitrone"}

  pia = {"Nuss", "Schoko", "Vanille"}

  '
---

Gib sortiert aus, welche Eissorten Pit und Pia beide mögen, je Sorte eine Zeile:

```
Nuss
Vanille
```
