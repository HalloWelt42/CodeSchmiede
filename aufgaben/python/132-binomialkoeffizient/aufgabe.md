---
schema_version: 1
id: 132-binomialkoeffizient
revision: 1
titel: Binomialkoeffizient n über k
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, kombinatorik, fakultaet]
pfade: [python_mathe2]
voraussetzungen: [017-fakultaet]
quelle:
  url: https://de.wikipedia.org/wiki/Binomialkoeffizient
  notiz: Klassische Mathe-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: binomial
hints:
  - kosten: 0
    text: |
      n über k = n! / (k! * (n-k)!).
      Bei k < 0 oder k > n → 0.
  - kosten: 8
    text: |
      `from math import comb` macht es in einer Zeile. Du darfst auch
      die Pascal-Identität nehmen: C(n,0)=1, C(n,k)=C(n-1,k-1)+C(n-1,k).
tests_sichtbar:
  - input: [5, 2]
    expected: 10
  - input: [0, 0]
    expected: 1
  - input: [10, 0]
    expected: 1
  - input: [10, 10]
    expected: 1
tests_versteckt:
  - input: [10, 5]
    expected: 252
  - input: [49, 6]
    expected: 13983816
  - input: [5, -1]
    expected: 0
  - input: [5, 6]
    expected: 0
  - input: [20, 10]
    expected: 184756
  - input: [100, 50]
    expected: 100891344545564193334812497256
starter_code: |
  def binomial(n: int, k: int) -> int:
      # Deine Lösung hier -- n über k. Bei ungültiger Eingabe → 0.
      pass
---

# Binomialkoeffizient n über k

Schreibe eine Funktion `binomial(n, k)`, die den Binomialkoeffizienten
$\binom{n}{k}$ zurückgibt.

## Formel

$$
\binom{n}{k} = \frac{n!}{k! \cdot (n-k)!}
$$

Bei `k < 0` oder `k > n` → `0`. `n=0, k=0` → `1` (Konvention).

## Beispiele

| `n` | `k` | Ergebnis    |
|-----|-----|-------------|
| `5` | `2` | `10`        |
| `0` | `0` | `1`         |
| `10`| `5` | `252`       |
| `49`| `6` | `13983816`  | (Lotto 6 aus 49)
| `100`|`50`| `100891344545564193334812497256` |

## Hintergrund

49 über 6 = **13.983.816** ist die Anzahl möglicher Lotto-Tipps in
"6 aus 49". Mit einem einzigen Tipp ist die Wahrscheinlichkeit, den
Jackpot zu knacken, also $1 / 13.983.816 \approx 7.15 \cdot 10^{-8}$.

Die Lotto-Wahrscheinlichkeit ist deutlich kleiner als die,
zwei Mal in Folge vom Blitz getroffen zu werden.
