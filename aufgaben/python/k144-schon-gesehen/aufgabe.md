---
schema_version: 1
id: k144-schon-gesehen
revision: 1
titel: Schon gesehen?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- menge
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Beginne mit `gesehen = set()`.
- kosten: 2
  text: Erst mit `in` nachschauen, dann mit `add` hineinlegen.
tests_sichtbar:
- input:
  - Hering
  - Lachs
  - Hering
  - ende
  expected: 'neu: Hering

    neu: Lachs

    kenne ich: Hering

    '
tests_versteckt:
- input:
  - ende
  expected: ''
- input:
  - Wels
  - Wels
  - Wels
  - ende
  expected: 'neu: Wels

    kenne ich: Wels

    kenne ich: Wels

    '
starter_code: ''
---

Lies Fischarten ein, bis `ende` kommt. Melde jede Art beim ersten Mal mit `neu:` und danach mit `kenne ich:`. Bei `Hering`, `Lachs`, `Hering`, `ende`:

```
neu: Hering
neu: Lachs
kenne ich: Hering
```
