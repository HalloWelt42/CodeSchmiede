---
schema_version: 1
id: k076-eisgroesse
revision: 1
titel: Die Eisgröße
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- verzweigung
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Den größten Betrag zuerst prüfen, sonst gewinnt ein zu früher Fall.
tests_sichtbar:
- input:
  - '4'
  expected: 'Kleines Eis

    '
tests_versteckt:
- input:
  - '9'
  expected: 'Großes Eis

    '
- input:
  - '1'
  expected: 'Waffel ohne Eis

    '
- input:
  - '0'
  expected: 'Nur gucken

    '
starter_code: ''
---

Je nach Talern gibt es ein anderes Eis: ab 5 `Großes Eis`, ab 3 `Kleines Eis`, ab 1 `Waffel ohne Eis`, sonst `Nur gucken`. Lies die Taler ein. Bei `4`:

```
Kleines Eis
```
