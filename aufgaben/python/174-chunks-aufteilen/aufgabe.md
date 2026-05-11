---
schema_version: 1
id: 174-chunks-aufteilen
revision: 1
titel: Liste in Bloecke der Groesse k aufteilen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [listen, slicing, chunking]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Slicing-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: chunks
hints:
  - kosten: 0
    text: |
      Teile a in Bloecke der Groesse k auf -- der letzte Block
      kann kuerzer sein. k <= 0 oder leere Liste → [].
  - kosten: 10
    text: |
      [a[i:i+k] for i in range(0, len(a), k)].
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5, 6], 2]
    expected: [[1, 2], [3, 4], [5, 6]]
  - input: [[1, 2, 3, 4, 5], 2]
    expected: [[1, 2], [3, 4], [5]]
  - input: [[], 3]
    expected: []
  - input: [[1, 2, 3], 0]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], 5]
    expected: [[1, 2, 3, 4, 5]]
  - input: [[1, 2, 3, 4, 5], 10]
    expected: [[1, 2, 3, 4, 5]]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3]
    expected: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  - input: [["a", "b", "c", "d"], 1]
    expected: [["a"], ["b"], ["c"], ["d"]]
  - input: [[1, 2, 3], -1]
    expected: []
  - input: [[1, 2, 3, 4, 5, 6, 7], 3]
    expected: [[1, 2, 3], [4, 5, 6], [7]]
starter_code: |
  def chunks(a: list, k: int) -> list[list]:
      # Deine Lösung hier
      pass
---

# Liste in Bloecke der Groesse k aufteilen

Schreibe eine Funktion `chunks(a, k)`, die eine Liste in Bloecke
der Laenge `k` aufteilt. Der **letzte Block** kann kuerzer sein,
falls die Listengroesse kein Vielfaches von `k` ist.

Bei `k <= 0` → `[]`. Bei `a == []` → `[]`.

## Beispiele

| Liste                | k | Bloecke                       |
|----------------------|---|-------------------------------|
| `[1,2,3,4,5,6]`      | 2 | `[[1,2], [3,4], [5,6]]`       |
| `[1,2,3,4,5]`        | 2 | `[[1,2], [3,4], [5]]`         |
| `[1,2,3,4,5]`        | 5 | `[[1,2,3,4,5]]`               |
| `[1,2,3,4,5]`        | 10| `[[1,2,3,4,5]]`               |
| `[1,2,3,4,5,6,7]`    | 3 | `[[1,2,3], [4,5,6], [7]]`     |

## Idee -- Slicing-Comprehension

```python
def chunks(a, k):
    if k <= 0:
        return []
    return [a[i:i + k] for i in range(0, len(a), k)]
```

Slicing kennt **kein OutOfBounds** -- `a[5:100]` liefert einfach den
Rest der Liste. Genau das brauchen wir fuer den letzten Block.

## Generator-Variante

Wenn die Liste sehr lang ist, lohnt ein Generator (kein doppelter
Speicher):

```python
def chunks(a, k):
    if k <= 0:
        return
    for i in range(0, len(a), k):
        yield a[i:i + k]
```

## Anwendung

Chunking braucht man bei **Batch-Processing**, **API-Pagination**
(maximal 100 IDs pro Request), beim **Drucken in Spalten** oder
beim **Aufteilen in CPU-Worker-Tasks**.
