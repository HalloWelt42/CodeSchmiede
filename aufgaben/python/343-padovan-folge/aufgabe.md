---
schema_version: 1
id: 343-padovan-folge
revision: 1
titel: Padovan-Folge bis n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [zahlen, folgen, rekursion, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Padovan_sequence
  notiz: Rosetta Code -- Padovan sequence
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: padovan
hints:
  - kosten: 0
    text: |
      Liefere die ersten n Glieder der Padovan-Folge:
      P(0)=P(1)=P(2)=1, P(n) = P(n-2) + P(n-3).
      n <= 0 → [].
      Erste Glieder: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, ...
  - kosten: 10
    text: |
      Iterativ mit drei Variablen a, b, c -- jede Iteration:
      neu = a + b; a, b, c = b, c, neu.
tests_sichtbar:
  - input: [0]
    expected: []
  - input: [1]
    expected: [1]
  - input: [3]
    expected: [1, 1, 1]
  - input: [10]
    expected: [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
tests_versteckt:
  - input: [-3]
    expected: []
  - input: [4]
    expected: [1, 1, 1, 2]
  - input: [15]
    expected: [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37]
  - input: [2]
    expected: [1, 1]
  - input: [5]
    expected: [1, 1, 1, 2, 2]
  - input: [20]
    expected: [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151]
starter_code: |
  def padovan(n: int) -> list[int]:
      # Tipp: Iterativ mit drei rollenden Variablen
      pass
---

# Padovan-Folge bis n

Schreibe `padovan(n)`, die die ersten `n` Glieder der **Padovan-
Folge** liefert.

Definition:
- `P(0) = P(1) = P(2) = 1`
- `P(n) = P(n-2) + P(n-3)` fuer `n >= 3`

`n <= 0` → `[]`.

## Beispiele

| n   | Folge                                                   |
|-----|---------------------------------------------------------|
| 0   | `[]`                                                    |
| 1   | `[1]`                                                   |
| 3   | `[1, 1, 1]`                                             |
| 10  | `[1, 1, 1, 2, 2, 3, 4, 5, 7, 9]`                        |
| 15  | `[..., 12, 16, 21, 28, 37]`                             |

## Idee -- iterativ mit drei Variablen

```python
def padovan(n):
    if n <= 0:
        return []
    folge = [1, 1, 1]
    while len(folge) < n:
        folge.append(folge[-2] + folge[-3])
    return folge[:n]
```

Triviale Indexierung -- `folge[-2]` und `folge[-3]` sind die
beiden vorvorletzten und vorvorvorletzten Werte.

## Hintergrund

Die Padovan-Folge ist nach dem britischen Architekten **Richard
Padovan** benannt (1994). Wie die Fibonacci-Folge basiert sie auf
einer linearen Rekurrenz, aber mit Verzoegerung um 2 statt 1.

Das Verhaeltnis benachbarter Padovan-Zahlen konvergiert gegen die
**plastische Zahl** $\rho \approx 1{,}3247$ -- die Loesung von
$x^3 = x + 1$.

## Verwandte Folgen

- **Fibonacci**: $F(n) = F(n-1) + F(n-2)$ -- Verhaeltnis -> goldener Schnitt
- **Padovan**: $P(n) = P(n-2) + P(n-3)$ -- Verhaeltnis -> plastische Zahl
- **Pell**: $P(n) = 2P(n-1) + P(n-2)$ -- Verhaeltnis -> Silberverhaeltnis
- **Tribonacci**: $T(n) = T(n-1) + T(n-2) + T(n-3)$
