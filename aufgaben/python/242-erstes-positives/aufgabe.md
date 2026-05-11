---
schema_version: 1
id: 242-erstes-positives
revision: 1
titel: Erstes positives Element
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, suchen, next]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Suche mit Default
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: erstes_positiv
hints:
  - kosten: 0
    text: |
      Liefere das erste Element > 0 aus der Liste, oder None wenn
      keins existiert.
      [-1, -2, 5, -3] → 5. [-1, -2] → None.
  - kosten: 10
    text: |
      next((x for x in liste if x > 0), None).
      next mit Default ist die elegante Form.
tests_sichtbar:
  - input: [[-1, -2, 5, -3]]
    expected: 5
  - input: [[-1, -2]]
    expected: null
  - input: [[]]
    expected: null
  - input: [[1, 2, 3]]
    expected: 1
tests_versteckt:
  - input: [[0, 0, 0, 1]]
    expected: 1
  - input: [[0, -1, -2]]
    expected: null
  - input: [[100]]
    expected: 100
  - input: [[-100]]
    expected: null
  - input: [[0]]
    expected: null
  - input: [[-5, -3, -1, 1, 3, 5]]
    expected: 1
  - input: [[10, 20, 30, -1, -2]]
    expected: 10
starter_code: |
  def erstes_positiv(zahlen: list):
      # Deine Lösung hier -- next mit Default ist elegant
      pass
---

# Erstes positives Element

Schreibe `erstes_positiv(zahlen)`, die das **erste positive Element**
(`> 0`) aus der Liste liefert -- oder `None`, wenn keins existiert.

## Beispiele

| Liste                  | Ergebnis |
|------------------------|----------|
| `[-1, -2, 5, -3]`      | `5`      |
| `[1, 2, 3]`            | `1`      |
| `[-1, -2]`             | `None`   |
| `[0]`                  | `None`   |
| `[]`                   | `None`   |
| `[10, 20, 30, -1, -2]` | `10`     |

## Idee 1 -- next mit Default

`next` mit zwei Argumenten: erstes ist der Generator, zweites der
**Default**, wenn der Generator leer ist. Sehr elegant.

## Idee 2 -- klassische Schleife

Liest sich vielleicht klarer. Pythonisch ist beides.

## Vorteil von `next`

- **Lazy**: bricht beim ersten Treffer ab (wie die Schleife).
- **Eingriff in beliebige Generatoren** (auch unendliche!).
- **Default** spart die `try/except StopIteration`-Konstruktion.

## Pattern -- "find first matching"

Diese Idee ist universell:

Damit lassen sich alle "find first"-Aufgaben in einer Zeile lösen --
ein wichtiger Pythonismus.
