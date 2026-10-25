---
schema_version: 1
id: k233-wo-steht
revision: 1
titel: Wo steht der Name?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- algorithmus
- suchen
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Schleife über `range(len(namen))`, beim Treffer sofort `return i`.
- kosten: 2
  text: Gibt es mehrere, zählt der erste Treffer.
tests_sichtbar:
- input:
  - Paul
  expected: 'Stelle 2

    '
- input:
  - Bodo
  expected: 'Nicht gefunden

    '
tests_versteckt:
- input:
  - Pit
  expected: 'Stelle 1

    '
- input:
  - Pia
  expected: 'Stelle 0

    '
starter_code: 'kolonie = ["Pia", "Pit", "Paul", "Polly", "Pit"]

  '
---

Schreibe ohne `index` und ohne `in` eine Funktion `stelle(namen, gesucht)`, die die Stelle (ab 0) zurückgibt oder -1. Lies einen Namen ein. Bei `Paul`:

```
Stelle 2
```

Bei `Bodo`: `Nicht gefunden`.
