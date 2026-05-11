---
schema_version: 1
id: 178-laengste-aufsteigende-folge
revision: 1
titel: Laengste streng aufsteigende Teilfolge (LIS)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 25
tags: [dp, listen, bisect, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 300 -- LIS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: lis_laenge
hints:
  - kosten: 0
    text: |
      Liefere die LAENGE der laengsten streng aufsteigenden Teilfolge.
      Elemente muessen NICHT zusammenhaengend sein.
      [10,9,2,5,3,7,101,18] → 4 ([2,3,7,18] oder [2,5,7,101]).
      Leere Liste → 0.
  - kosten: 20
    text: |
      Patience-Sort-Trick: tails[i] = kleinstes letztes Element einer
      aufsteigenden Folge der Laenge i+1. bisect_left fuer O(n log n).
tests_sichtbar:
  - input: [[10, 9, 2, 5, 3, 7, 101, 18]]
    expected: 4
  - input: [[]]
    expected: 0
  - input: [[1]]
    expected: 1
  - input: [[1, 2, 3, 4, 5]]
    expected: 5
tests_versteckt:
  - input: [[5, 4, 3, 2, 1]]
    expected: 1
  - input: [[3, 1, 2, 1, 4]]
    expected: 3
  - input: [[7, 7, 7, 7]]
    expected: 1
  - input: [[0, 1, 0, 3, 2, 3]]
    expected: 4
  - input: [[1, 3, 6, 7, 9, 4, 10, 5, 6]]
    expected: 6
  - input: [[10, 22, 9, 33, 21, 50, 41, 60, 80]]
    expected: 6
starter_code: |
  def lis_laenge(zahlen: list[int]) -> int:
      # Deine Lösung hier -- moeglichst O(n log n) mit bisect
      pass
---

# Laengste streng aufsteigende Teilfolge (LIS)

Schreibe `lis_laenge(zahlen)`, die die **Laenge** der laengsten
**streng aufsteigenden Teilfolge** zurueckgibt. Die Elemente
muessen **nicht zusammenhaengend** sein.

## Beispiele

| Liste                              | LIS-Laenge | Beispiel-Folge          |
|------------------------------------|-----------|-------------------------|
| `[10, 9, 2, 5, 3, 7, 101, 18]`     | `4`       | `[2, 3, 7, 18]`         |
| `[1, 2, 3, 4, 5]`                  | `5`       | gesamte Liste           |
| `[5, 4, 3, 2, 1]`                  | `1`       | jede Einzel-Zahl        |
| `[10, 22, 9, 33, 21, 50, 41, 60, 80]` | `6`    | `[10,22,33,50,60,80]`   |

## Idee -- Patience-Sort-Trick (O(n log n))

`tails[i]` = das **kleinste letzte Element** aller aufsteigenden
Teilfolgen der Laenge `i + 1`. Pro neuer Zahl `x` ueberschreiben
wir `tails[bisect_left(tails, x)]` (oder haengen am Ende an).

```python
from bisect import bisect_left

def lis_laenge(zahlen):
    tails = []
    for x in zahlen:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

`tails` ist **kein** echtes Beispiel der laengsten Folge -- nur ihre
Laenge ist garantiert korrekt. Fuer die Folge selbst braucht man
zusaetzlich Vorgaenger-Pointer.

## Naive O(n^2) DP-Loesung

```python
def lis_laenge(zahlen):
    n = len(zahlen)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if zahlen[j] < zahlen[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

Leichter zu lesen, fuer kleine `n` (bis ca. 1000) absolut praktikabel.
Fuer grosse Eingaben deutlich langsamer.

## Anwendung

LIS taucht in **Versionskontrolle** (longest common subsequence ist
verwandt), **Bioinformatik** (DNA-Sequenz-Vergleich) und in
**Patience-Solitaire** auf -- dem Spiel, von dem der Algorithmus seinen
Namen hat.
