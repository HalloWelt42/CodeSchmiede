---
schema_version: 1
id: 309-primzahlen-gen
revision: 1
titel: Primzahl-Generator bis n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [generator, yield, primzahlen, sieb]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Generator + Sieb-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: primzahlen_bis
hints:
  - kosten: 0
    text: |
      Liefere alle Primzahlen <= n als Liste.
      Intern: Generator mit Sieb des Eratosthenes ODER Trial-Division.
      n < 2 → [].
  - kosten: 25
    text: |
      Sieb: bool-Liste der Groesse n+1, false markieren.
      Generator: yield i wenn sieb[i] True.
tests_sichtbar:
  - input: [10]
    expected: [2, 3, 5, 7]
  - input: [1]
    expected: []
  - input: [2]
    expected: [2]
  - input: [20]
    expected: [2, 3, 5, 7, 11, 13, 17, 19]
tests_versteckt:
  - input: [0]
    expected: []
  - input: [-5]
    expected: []
  - input: [3]
    expected: [2, 3]
  - input: [30]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  - input: [50]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  - input: [100]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  - input: [7]
    expected: [2, 3, 5, 7]
starter_code: |
  def primzahlen_bis(n: int) -> list[int]:
      # Tipp: Sieb des Eratosthenes ODER Trial-Division im Generator
      pass
---

# Primzahl-Generator bis n

Schreibe `primzahlen_bis(n)`, die alle **Primzahlen ≤ n** als Liste
liefert -- intern via **Generator** (`yield`).

`n < 2` → `[]`.

## Beispiele

| `n`  | Primzahlen                                           |
|------|------------------------------------------------------|
| `1`  | `[]`                                                 |
| `2`  | `[2]`                                                |
| `10` | `[2, 3, 5, 7]`                                       |
| `20` | `[2, 3, 5, 7, 11, 13, 17, 19]`                       |
| `30` | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`               |
| `50` | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]` |

Bis 100 gibt es **25 Primzahlen**.

## Idee 1 -- Sieb des Eratosthenes mit Generator

```python
def primzahlen_bis(n):
    def gen():
        if n < 2:
            return
        sieb = [True] * (n + 1)
        sieb[0] = sieb[1] = False
        for i in range(2, n + 1):
            if sieb[i]:
                yield i
                for j in range(i * i, n + 1, i):
                    sieb[j] = False
    return list(gen())
```

**Wichtig**: Das `yield` kommt **VOR** dem Streichen, sonst
verpasst man `i = 2`. Generator-Logik und Sieb-Logik werden
verschraenkt.

## Idee 2 -- Trial-Division im Generator

```python
def primzahlen_bis(n):
    def ist_prim(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    def gen():
        for k in range(2, n + 1):
            if ist_prim(k):
                yield k
    return list(gen())
```

Klarer, aber langsamer (`O(n*sqrt(n))` statt `O(n*log log n)`).

## Verwandt

- **039-eratosthenes**: Sieb als reine Listen-Funktion
- **127-primzahlen-bis-n-zahl**: nur die Anzahl
- **309 hier**: Liste mit Generator-Pattern
