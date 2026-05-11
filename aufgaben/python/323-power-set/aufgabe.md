---
schema_version: 1
id: 323-power-set
revision: 1
titel: Potenzmenge -- alle Teilmengen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [kombinatorik, listen, itertools, mengen]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Power_set
  notiz: Rosetta Code -- Power Set
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: potenzmenge
hints:
  - kosten: 0
    text: |
      Liefere alle Teilmengen einer Liste -- inklusive leerer Menge
      und Gesamtmenge. Reihenfolge: nach Groesse aufsteigend, innerhalb
      gleicher Groesse lexikographisch.
      Bei [] -> [[]] (genau eine Teilmenge: die leere).
  - kosten: 20
    text: |
      itertools.combinations(liste, k) fuer k = 0..len(liste).
      Doppelte for-Comprehension flach machen.
tests_sichtbar:
  - input: [[]]
    expected: [[]]
  - input: [[1]]
    expected: [[], [1]]
  - input: [[1, 2]]
    expected: [[], [1], [2], [1, 2]]
  - input: [[1, 2, 3]]
    expected: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
tests_versteckt:
  - input: [["a"]]
    expected: [[], ["a"]]
  - input: [["a", "b"]]
    expected: [[], ["a"], ["b"], ["a", "b"]]
  - input: [[1, 2, 3, 4]]
    expected: [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
  - input: [[5]]
    expected: [[], [5]]
  - input: [[1, 1]]
    expected: [[], [1], [1], [1, 1]]
starter_code: |
  from itertools import combinations

  def potenzmenge(liste: list) -> list[list]:
      # Tipp: combinations(liste, k) fuer k = 0..len
      pass
---

# Potenzmenge -- alle Teilmengen

Schreibe `potenzmenge(liste)`, die **alle Teilmengen** der Liste
liefert -- die leere Menge zaehlt mit, die Gesamtmenge auch.

Reihenfolge: zuerst nach **Groesse aufsteigend**, innerhalb gleicher
Groesse **lexikographisch**.

Anzahl der Teilmengen einer n-elementigen Menge: $2^n$.

## Beispiele

| Liste       | Teilmengen                                              |
|-------------|---------------------------------------------------------|
| `[]`        | `[[]]` (1 Element)                                      |
| `[1]`       | `[[], [1]]` (2 Elemente)                                |
| `[1, 2]`    | `[[], [1], [2], [1, 2]]` (4)                            |
| `[1, 2, 3]` | `[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]` (8) |

Bei vier Elementen waeren es 16, bei zehn schon 1024 Teilmengen.

## Idee

```python
from itertools import combinations

def potenzmenge(liste):
    return [
        list(t)
        for k in range(len(liste) + 1)
        for t in combinations(liste, k)
    ]
```

Doppelte Comprehension: aussen `k` von 0 bis `n`, innen alle
k-elementigen Kombinationen. `combinations` liefert bereits
lexikographisch geordnet.

## Idee -- Bit-Maskierung

```python
def potenzmenge(liste):
    n = len(liste)
    out = []
    for maske in range(2 ** n):
        out.append([liste[i] for i in range(n) if maske & (1 << i)])
    return sorted(out, key=lambda s: (len(s), s))
```

Jede Teilmenge entspricht einer Binaer-Zahl: Bit `i` gesetzt ↔
Element `i` enthalten. Elegant, aber Sortierung am Ende noetig.

## Anwendung

- **Brute-Force-Loesungen** fuer Subset-Sum (Aufgabe 166), Knapsack
- **Feature-Selection** in Machine Learning
- **Mengen-Algebren** und Boolesche Funktionen
