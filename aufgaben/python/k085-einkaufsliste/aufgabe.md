---
schema_version: 1
id: k085-einkaufsliste
revision: 1
titel: Die Einkaufsliste
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- while
- abbruch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`while True` und `break`, sobald fertig kommt.'
tests_sichtbar:
- input:
  - Hering
  - Sprotte
  - fertig
  expected: '- Hering

    - Sprotte

    Anzahl: 2

    '
tests_versteckt:
- input:
  - Eis
  - fertig
  expected: '- Eis

    Anzahl: 1

    '
- input:
  - fertig
  expected: 'Anzahl: 0

    '
starter_code: ''
---

Lies Wörter ein, bis `fertig` kommt, und gib jedes mit einem Spiegelstrich davor aus; danach die Anzahl. Bei `Hering`, `Sprotte`, `fertig`:

```
- Hering
- Sprotte
Anzahl: 2
```
