---
schema_version: 1
id: k203-eisscholle
revision: 1
titel: Die Eisscholle als Klasse
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- klasse
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Methoden greifen mit `self.breite` auf die Eigenschaften zu.
tests_sichtbar:
- input:
  - '3'
  - '4'
  expected: 'Fläche: 12

    Umfang: 14

    '
tests_versteckt:
- input:
  - '1'
  - '1'
  expected: 'Fläche: 1

    Umfang: 4

    '
starter_code: ''
---

Schreibe eine Klasse `Scholle` mit den Eigenschaften `breite` und `laenge` und den Methoden `flaeche()` und `umfang()`. Lies Breite und Länge ein. Bei `3` und `4`:

```
Fläche: 12
Umfang: 14
```
