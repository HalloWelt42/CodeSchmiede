---
schema_version: 1
id: k193-einkaufszettel
revision: 1
titel: Der Einkaufszettel
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- datei
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Beim Schreiben das `\n` nicht vergessen.
- kosten: 2
  text: Beim Lesen hilft `enumerate(datei, 1)`.
tests_sichtbar:
- input:
  - Hering
  - Eis
  - ende
  expected: '1. Hering

    2. Eis

    '
tests_versteckt:
- input:
  - ende
  expected: ''
- input:
  - A
  - B
  - C
  - ende
  expected: '1. A

    2. B

    3. C

    '
starter_code: ''
---

Lies Waren ein, bis `ende` kommt, und schreibe jede in eine eigene Zeile der Datei `einkauf.txt`. Lies die Datei danach wieder und gib die Zeilen nummeriert aus. Bei `Hering`, `Eis`, `ende`:

```
1. Hering
2. Eis
```
