---
schema_version: 1
id: 055-prefix-summe
revision: 1
titel: Prefix-Summen-Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [listen, schleifen, akkumulator]
pfade: [python_listen3]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Bausteine fuer viele Range-Summen-Probleme
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: prefix_summe
hints:
  - kosten: 0
    text: |
      Liefere eine Liste, in der das i-te Element die Summe aller
      Elemente von Index 0 bis i (inklusive) ist.
  - kosten: 10
    text: |
      Schleife mit Akkumulator:

      ```
      summe = 0
      out = []
      for x in zahlen:
          summe += x
          out.append(summe)
      return out
      ```
  - kosten: 20
    text: |
      `itertools.accumulate(zahlen)` macht das in einer Zeile.
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: [1, 3, 6, 10]
  - input: [[]]
    expected: []
  - input: [[5]]
    expected: [5]
  - input: [[1, -1, 1, -1]]
    expected: [1, 0, 1, 0]
tests_versteckt:
  - input: [[10, 20, 30]]
    expected: [10, 30, 60]
  - input: [[0, 0, 0, 0]]
    expected: [0, 0, 0, 0]
  - input: [[1, 1, 1, 1, 1, 1]]
    expected: [1, 2, 3, 4, 5, 6]
starter_code: |
  def prefix_summe(zahlen: list[int]) -> list[int]:
      # Deine Lösung hier
      pass
---

# Prefix-Summen-Liste

Schreibe eine Funktion `prefix_summe(zahlen)`, die eine Liste der
**Praefix-Summen** zurueckgibt. Das Element an Index `i` ist die
Summe aller Elemente von Index 0 bis i.

## Beispiele

| Eingabe          | Ergebnis           |
|------------------|--------------------|
| `[1,2,3,4]`      | `[1,3,6,10]`       |
| `[]`             | `[]`               |
| `[5]`            | `[5]`              |
| `[1,-1,1,-1]`    | `[1,0,1,0]`        |
| `[10,20,30]`     | `[10,30,60]`       |

## Wozu das gut ist

Mit Praefix-Summen kannst du **jede Range-Summe in O(1)** beantworten.
Suche die Summe von Index `l` bis `r`? `praefix[r] - praefix[l-1]`.
Das macht aus quadratischen Algorithmen oft lineare.

## Tipp

Mit Pythons `itertools.accumulate` geht es als Einzeiler:

```
from itertools import accumulate
return list(accumulate(zahlen))
```

Die manuelle Schleife ist trotzdem lehrreich -- das Akkumulator-Pattern
brauchst du oft.
