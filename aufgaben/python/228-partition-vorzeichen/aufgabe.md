---
schema_version: 1
id: 228-partition-vorzeichen
revision: 1
titel: Liste nach Vorzeichen partitionieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [listen, filter, partition]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Aufteilungs-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: partition_vorzeichen
hints:
  - kosten: 0
    text: |
      Teile eine Liste in [negative, nullen, positive] auf.
      Reihenfolge IN den Listen wie im Original.
      Bei [] -> [[], [], []].
  - kosten: 10
    text: |
      Drei Listen vorbereiten und einmal durchlaufen.
      Oder drei List-Comprehensions.
tests_sichtbar:
  - input: [[-2, 0, 3, -1, 5]]
    expected: [[-2, -1], [0], [3, 5]]
  - input: [[]]
    expected: [[], [], []]
  - input: [[1, 2, 3]]
    expected: [[], [], [1, 2, 3]]
  - input: [[-1, -2, -3]]
    expected: [[-1, -2, -3], [], []]
tests_versteckt:
  - input: [[0, 0, 0]]
    expected: [[], [0, 0, 0], []]
  - input: [[1, 0, -1, 0, 1]]
    expected: [[-1], [0, 0], [1, 1]]
  - input: [[5]]
    expected: [[], [], [5]]
  - input: [[-5]]
    expected: [[-5], [], []]
  - input: [[0]]
    expected: [[], [0], []]
  - input: [[10, -10, 0, 5, -5, 0]]
    expected: [[-10, -5], [0, 0], [10, 5]]
starter_code: |
  def partition_vorzeichen(zahlen: list[int]) -> list[list[int]]:
      # Deine Lösung hier -- [neg, null, pos]
      pass
---

# Liste nach Vorzeichen partitionieren

Schreibe `partition_vorzeichen(zahlen)`, die eine Liste in drei
Teile teilt:

`[negative_zahlen, nullen, positive_zahlen]`

Die Reihenfolge **innerhalb** jeder Teil-Liste bleibt wie im Original.

## Beispiele

| Eingabe              | Ergebnis                          |
|----------------------|-----------------------------------|
| `[-2, 0, 3, -1, 5]`  | `[[-2, -1], [0], [3, 5]]`         |
| `[]`                 | `[[], [], []]`                    |
| `[1, 2, 3]`          | `[[], [], [1, 2, 3]]`             |
| `[0, 0, 0]`          | `[[], [0, 0, 0], []]`             |
| `[-5]`               | `[[-5], [], []]`                  |

## Idee 1 -- Drei Comprehensions

```python
def partition_vorzeichen(zahlen):
    return [
        [x for x in zahlen if x < 0],
        [x for x in zahlen if x == 0],
        [x for x in zahlen if x > 0],
    ]
```

Sehr lesbar -- aber die Liste wird **dreimal** durchlaufen.

## Idee 2 -- Eine Schleife

```python
def partition_vorzeichen(zahlen):
    neg, null, pos = [], [], []
    for x in zahlen:
        if x < 0:
            neg.append(x)
        elif x == 0:
            null.append(x)
        else:
            pos.append(x)
    return [neg, null, pos]
```

Effizient -- bei sehr grossen Listen merkbar schneller.

## Pattern -- Allgemeine Partition

Die Idee laesst sich mit einem **Predicate** verallgemeinern:

```python
from itertools import groupby

def partition_nach(liste, schluessel):
    sortiert = sorted(liste, key=schluessel)
    return {k: list(g) for k, g in groupby(sortiert, key=schluessel)}
```

Geht in einer Zeile, wenn die Sortier-Reihenfolge egal ist.
