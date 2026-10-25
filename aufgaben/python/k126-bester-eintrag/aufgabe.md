---
schema_version: 1
id: k126-bester-eintrag
revision: 1
titel: Der beste Eintrag
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- tupel
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Merke dir Name und Punkte des bisher Besten als Paar.
tests_sichtbar:
- input: []
  expected: 'Pia hat gewonnen mit 42 Punkten

    '
starter_code: 'liste = [("Pit", 17), ("Pia", 42), ("Paul", 8)]

  '
---

Die Rangliste besteht aus Paaren `(name, punkte)`, aber unsortiert. Finde den Namen mit den meisten Punkten:

```
Pia hat gewonnen mit 42 Punkten
```
