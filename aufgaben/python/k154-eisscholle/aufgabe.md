---
schema_version: 1
id: k154-eisscholle
revision: 1
titel: Die Eisscholle
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- funktion
- rueckgabe
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Funktion gibt mit `return` das Produkt zurück, ausgegeben wird außerhalb.
tests_sichtbar:
- input:
  - '3'
  - '4'
  expected: 'Fläche: 12

    '
tests_versteckt:
- input:
  - '1'
  - '1'
  expected: 'Fläche: 1

    '
- input:
  - '10'
  - '0'
  expected: 'Fläche: 0

    '
starter_code: ''
---

Schreibe eine Funktion `flaeche(breite, laenge)`, die die Fläche einer Eisscholle zurückgibt. Lies Breite und Länge als ganze Zahlen ein. Bei `3` und `4`:

```
Fläche: 12
```
