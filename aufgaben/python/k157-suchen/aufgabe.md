---
schema_version: 1
id: k157-suchen
revision: 1
titel: Wo steckt Pit?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- funktion
- nichts
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mit `enumerate(namen, 1)` hast du Platz und Name zugleich.
- kosten: 2
  text: 'Nach der Schleife, wenn nichts gefunden: `return None`; prüfen mit `ergebnis is None`.'
tests_sichtbar:
- input:
  - Pit
  expected: 'Pit steht auf Platz 2

    '
- input:
  - Bodo
  expected: 'Bodo ist nicht dabei

    '
tests_versteckt:
- input:
  - Polly
  expected: 'Polly steht auf Platz 4

    '
- input:
  - Pia
  expected: 'Pia steht auf Platz 1

    '
starter_code: 'schlange = ["Pia", "Pit", "Paul", "Polly"]

  '
---

Schreibe eine Funktion `platz(namen, gesucht)`, die den Platz (ab 1 gezählt) eines Namens in der Liste zurückgibt, oder `None`, wenn er nicht drin ist. Lies einen Namen ein und melde das Ergebnis. Bei `Pit`:

```
Pit steht auf Platz 2
```

Bei `Bodo`:

```
Bodo ist nicht dabei
```
