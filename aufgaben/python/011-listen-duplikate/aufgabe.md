---
schema_version: 1
id: 011-listen-duplikate
revision: 1
titel: Duplikate aus Liste entfernen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [listen, set, reihenfolge]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassische Listen-Operation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ohne_duplikate
hints:
  - kosten: 0
    text: Ein `set` enthält jedes Element nur einmal -- aber die Reihenfolge geht verloren.
  - kosten: 6
    text: |
      Wenn die Reihenfolge bleiben soll: in einer Schleife jedes Element
      nur dann anhängen, wenn es noch nicht in der Ergebnisliste steht.
  - kosten: 11
    text: |
      Idiomatisch (Python 3.7+, dict ist insertion-ordered):

      ```
      return list(dict.fromkeys(zahlen))
      ```
tests_sichtbar:
  - input: [[1, 2, 1, 3]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[5, 5, 5]]
    expected: [5]
  - input: [[1, 2, 3]]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]]
    expected: [3, 1, 4, 5, 9, 2, 6]
  - input: [["a", "b", "a", "c"]]
    expected: ["a", "b", "c"]
  - input: [[42]]
    expected: [42]
  - input: [[1, 1, 1, 1, 1, 2, 2, 3]]
    expected: [1, 2, 3]
starter_code: |
  def ohne_duplikate(zahlen: list) -> list:
      # Deine Lösung hier
      pass
---

# Duplikate aus Liste entfernen

Schreibe eine Funktion `ohne_duplikate(zahlen)`, die eine Liste
zurückgibt, in der jedes Element nur **einmal** vorkommt -- in der
Reihenfolge des **ersten** Auftretens.

## Beispiele

| Eingabe                     | Ausgabe         |
|-----------------------------|-----------------|
| `[1, 2, 1, 3]`              | `[1, 2, 3]`     |
| `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]` | `[3, 1, 4, 5, 9, 2, 6]` |
| `[5, 5, 5]`                 | `[5]`           |
| `[]`                        | `[]`            |

## Hinweise

- **Reihenfolge erhalten:** das erste Auftreten zählt, alle weiteren
  Vorkommen werden weggelassen. `set()` allein reicht also nicht --
  Sets garantieren keine Reihenfolge.
- Die Funktion soll mit beliebigen vergleichbaren Werten arbeiten,
  nicht nur Zahlen.
