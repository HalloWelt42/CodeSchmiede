---
schema_version: 1
id: k156-gerade-pruefen
revision: 1
titel: Gerade oder nicht
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- funktion
- rueckgabe
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`return n % 2 == 0` gibt gleich den Wahrheitswert zurück.'
- kosten: 2
  text: Die Schleife läuft bis n einschließlich.
tests_sichtbar:
- input:
  - '7'
  expected: '2

    4

    6

    '
tests_versteckt:
- input:
  - '1'
  expected: ''
- input:
  - '4'
  expected: '2

    4

    '
starter_code: ''
---

Schreibe eine Funktion `ist_gerade(n)`, die `True` oder `False` zurückgibt. Lies eine Zahl n ein und gib mit ihrer Hilfe alle geraden Zahlen von 1 bis n aus, je Zeile eine. Bei `7`:

```
2
4
6
```
