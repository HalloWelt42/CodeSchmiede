---
schema_version: 1
id: k164-ohne-global
revision: 1
titel: Ohne global reparieren
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- sichtbarkeit
- rueckgabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`def treffer(stand):` und `return stand + 10`.'
- kosten: 2
  text: 'Beim Aufruf: `punkte = treffer(punkte)`.'
tests_sichtbar:
- input: []
  expected: 'Punkte: 30

    '
starter_code: "punkte = 0\n\n\ndef treffer():\n    punkte += 10\n\n\ntreffer()\ntreffer()\ntreffer()\nprint(\"Punkte:\", punkte)\n"
---

Dieses Programm bricht mit `UnboundLocalError` ab. Repariere es ohne `global`: die Funktion `treffer` bekommt den Stand als Parameter und gibt den neuen Stand zurück.

```
Punkte: 30
```
