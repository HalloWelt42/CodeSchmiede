---
schema_version: 1
id: 327-tau-funktion
revision: 1
titel: Tau-Funktion -- Anzahl der Teiler
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, mathematik, teiler, zahlentheorie]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Tau_function
  notiz: Rosetta Code -- Tau function
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: tau
hints:
  - kosten: 0
    text: |
      Liefere die Anzahl der Teiler von n (positiv, inkl. 1 und n).
      n < 1 -> 0. tau(12) = 6 (1, 2, 3, 4, 6, 12).
      Effizient: nur bis sqrt(n) iterieren, Quadrat-Sonderfall.
  - kosten: 8
    text: |
      Schleife i = 1..sqrt(n). Pro Treffer +2, bei i*i == n nur +1.
tests_sichtbar:
  - input: [1]
    expected: 1
  - input: [12]
    expected: 6
  - input: [25]
    expected: 3
  - input: [0]
    expected: 0
tests_versteckt:
  - input: [-5]
    expected: 0
  - input: [2]
    expected: 2
  - input: [6]
    expected: 4
  - input: [36]
    expected: 9
  - input: [100]
    expected: 9
  - input: [97]
    expected: 2
  - input: [1024]
    expected: 11
  - input: [10000]
    expected: 25
starter_code: |
  def tau(n: int) -> int:
      # Tipp: Schleife bis sqrt(n), Quadrat-Sonderfall
      pass
---

# Tau-Funktion -- Anzahl der Teiler

Schreibe `tau(n)`, die die **Anzahl der positiven Teiler** von `n`
liefert -- inklusive `1` und `n` selbst.

Bei `n < 1` → `0`.

## Beispiele

| `n`     | Teiler                              | tau(n) |
|---------|-------------------------------------|--------|
| `1`     | `[1]`                               | `1`    |
| `2`     | `[1, 2]`                            | `2`    |
| `6`     | `[1, 2, 3, 6]`                      | `4`    |
| `12`    | `[1, 2, 3, 4, 6, 12]`               | `6`    |
| `25`    | `[1, 5, 25]`                        | `3`    |
| `36`    | `[1, 2, 3, 4, 6, 9, 12, 18, 36]`    | `9`    |
| `97`    | `[1, 97]` (Primzahl)                | `2`    |
| `1024`  | $2^0, 2^1, \dots, 2^{10}$           | `11`   |

## Idee -- Schleife bis Wurzel

Pro Treffer `i` als Teiler bekommt man **automatisch** `n // i`
als Partner-Teiler -- daher `+= 2`. Bei Quadratzahlen
(`i * i == n`) sind beide Teiler gleich, also nur `+= 1`.

## Hintergrund -- Multiplikative Funktion

Tau ist **multiplikativ**: bei teilerfremden `a, b` gilt
$\tau(a \cdot b) = \tau(a) \cdot \tau(b)$. Wenn $n = p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots$
die Primfaktor-Zerlegung ist, dann:

$$\tau(n) = (e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$$

Beispiel: $12 = 2^2 \cdot 3^1$, also $\tau(12) = (2+1)(1+1) = 6$.

## Vergleich mit Aufgabe 138

**138-alle-teiler** liefert die **Liste** der Teiler.
**327 hier** liefert nur die **Anzahl** -- effizienter, weil
keine Speicherung der Teiler noetig.
