---
schema_version: 1
id: k226-datum-zerlegen
revision: 1
titel: Ein Datum zerlegen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- regex
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 22
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Punkt im Muster heißt sonst irgendein Zeichen; der echte Punkt ist `\.`.
- kosten: 2
  text: '`\d{1,2}` heißt eine oder zwei Ziffern.'
tests_sichtbar:
- input:
  - 24.12.2026
  expected: 'Tag 24, Monat 12, Jahr 2026

    '
- input:
  - 24-12-2026
  expected: 'Kein Datum

    '
tests_versteckt:
- input:
  - 1.2.2027
  expected: 'Tag 1, Monat 2, Jahr 2027

    '
- input:
  - 24.12.26
  expected: 'Kein Datum

    '
starter_code: ''
---

Lies ein Datum wie `24.12.2026` ein und zerlege es mit Gruppen. Passt die Eingabe nicht zum Muster Tag.Monat.Jahr (ein oder zwei Ziffern, ein oder zwei Ziffern, vier Ziffern), erscheint `Kein Datum`. Bei `24.12.2026`:

```
Tag 24, Monat 12, Jahr 2026
```
