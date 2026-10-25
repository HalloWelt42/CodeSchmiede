---
schema_version: 1
id: k227-schwaerzen
revision: 1
titel: Geheime Nummern
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
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
  text: '`re.sub(r"\d", "#", satz)`.'
tests_sichtbar:
- input:
  - Ruf Pia unter 0171 2345 an
  expected: 'Ruf Pia unter #### #### an

    '
tests_versteckt:
- input:
  - keine Nummer
  expected: 'keine Nummer

    '
starter_code: ''
---

Lies einen Satz ein und ersetze jede Ziffer durch `#`, damit keine Telefonnummer verraten wird. Bei `Ruf Pia unter 0171 2345 an`:

```
Ruf Pia unter #### #### an
```
