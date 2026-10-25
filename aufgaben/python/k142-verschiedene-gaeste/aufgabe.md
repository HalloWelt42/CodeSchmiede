---
schema_version: 1
id: k142-verschiedene-gaeste
revision: 1
titel: Verschiedene Gäste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
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
  text: '`set(gaeste)` wirft die Doppelten hinaus.'
tests_sichtbar:
- input: []
  expected: 'Verschiedene: 3

    '
starter_code: 'gaeste = ["Pia", "Pit", "Pia", "Paul", "Pit"]

  anzahl = len(___)

  print("Verschiedene:", anzahl)

  '
---

Auf der Gästeliste stehen manche doppelt. Ergänze die Lücke `___`, damit gezählt wird, wie viele verschiedene Gäste kommen:

```
Verschiedene: 3
```
