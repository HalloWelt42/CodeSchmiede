---
schema_version: 1
id: k124-platzierung
revision: 1
titel: Die Siegerehrung
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- aufzaehlen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`enumerate(sieger, 1)` liefert Paare aus Platz und Name.'
tests_sichtbar:
- input: []
  expected: '1. Pia

    2. Pit

    3. Paul

    '
starter_code: 'sieger = ["Pia", "Pit", "Paul"]

  '
---

Gib die Rangliste mit Platz aus, ab 1 gezählt:

```
1. Pia
2. Pit
3. Paul
```
