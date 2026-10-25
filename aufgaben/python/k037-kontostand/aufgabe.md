---
schema_version: 1
id: k037-kontostand
revision: 1
titel: Der Kontostand
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- rechnen
- variablen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Jede Änderung eine Zeile: `konto += 5` und so weiter.'
tests_sichtbar:
- input: []
  expected: '24

    '
starter_code: 'konto = 10

  '
---

Pias Konto startet mit 10 Talern. Sie bekommt 5 dazu, gibt 3 aus, und dann verdoppelt die Pinguinbank alles. Benutze `+=`, `-=` und `*=` und gib am Ende den Kontostand aus:

```
24
```
