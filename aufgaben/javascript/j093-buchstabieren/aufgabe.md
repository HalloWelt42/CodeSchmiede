---
schema_version: 1
id: j093-buchstabieren
revision: 1
titel: Buchstabieren
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- for_of
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`for (const z of wort)` liefert die Zeichen.'
tests_sichtbar:
- input:
  - Pit
  expected: 'Wort? P

    I

    T

    '
tests_versteckt:
- input:
  - Möwe
  expected: 'Wort? M

    Ö

    W

    E

    '
starter_code: ''
---

Lies ein Wort und gib es Zeichen für Zeichen aus, jedes groß und in einer eigenen Zeile. Bei der Eingabe `Pit`:

```
Wort? P
I
T
```
