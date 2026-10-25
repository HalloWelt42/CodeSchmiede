---
schema_version: 1
id: k206-fische-zeigen
revision: 1
titel: Fische zeigen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`__str__` gibt einen Text mit return zurück, print ruft sie selbst auf.'
tests_sichtbar:
- input:
  - Hering
  - '120'
  - Lachs
  - '900'
  - ende
  expected: 'Hering (120 g)

    Lachs (900 g)

    '
tests_versteckt:
- input:
  - ende
  expected: ''
starter_code: ''
---

Schreibe eine Klasse `Fisch` mit Art und Gewicht in Gramm und einer Methode `__str__`, die `Art (Gewicht g)` zurückgibt. Lies Paare aus Art und Gewicht ein, bis als Art `ende` kommt, und gib jeden Fisch mit print aus. Bei `Hering`, `120`, `Lachs`, `900`, `ende`:

```
Hering (120 g)
Lachs (900 g)
```
