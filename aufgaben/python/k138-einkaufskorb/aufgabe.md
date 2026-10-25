---
schema_version: 1
id: k138-einkaufskorb
revision: 1
titel: Der Einkaufskorb
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- woerterbuch
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Wörterbuch für den Korb, gezählt mit get.
- kosten: 3
  text: 'Unbekannte Ware: melden und mit continue weiter.'
tests_sichtbar:
- input:
  - Hering
  - Eis
  - Hering
  - Wal
  - kasse
  expected: 'Wal: gibt es nicht

    Hering x 2

    Eis x 1

    Gesamt: 8

    '
tests_versteckt:
- input:
  - kasse
  expected: 'Gesamt: 0

    '
- input:
  - Lachs
  - Lachs
  - Robbe
  - Eis
  - kasse
  expected: 'Robbe: gibt es nicht

    Lachs x 2

    Eis x 1

    Gesamt: 12

    '
starter_code: 'preise = {"Hering": 3, "Lachs": 5, "Eis": 2}

  '
---

Die Preisliste steht schon da. Lies Waren ein, bis `kasse` kommt. Unbekannte Waren werden mit `gibt es nicht` gemeldet, alle anderen gezählt. Gib an der Kasse jede Ware mit Anzahl und am Ende den Gesamtpreis aus. Bei `Hering`, `Eis`, `Hering`, `Wal`, `kasse`:

```
Wal: gibt es nicht
Hering x 2
Eis x 1
Gesamt: 8
```
