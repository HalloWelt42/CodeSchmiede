---
schema_version: 1
id: k225-namen-finden
revision: 1
titel: Namen finden
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
  text: 'Ein Großbuchstabe: `[A-ZÄÖÜ]`, danach beliebig viele Buchstaben: `\w*`.'
tests_sichtbar:
- input:
  - heute fingen Pia und Pit mit Paul
  expected: 'Pia

    Pit

    Paul

    3 Namen

    '
tests_versteckt:
- input:
  - Übermorgen kommt Örni
  expected: 'Übermorgen

    Örni

    2 Namen

    '
- input:
  - nur kleine wörter
  expected: '0 Namen

    '
starter_code: ''
---

Lies einen Satz ein und gib alle Wörter aus, die mit einem Großbuchstaben beginnen, je Zeile eines, und danach ihre Anzahl. Bei `heute fingen Pia und Pit mit Paul`:

```
Pia
Pit
Paul
3 Namen
```
