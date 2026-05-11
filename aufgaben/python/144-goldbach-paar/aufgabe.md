---
schema_version: 1
id: 144-goldbach-paar
revision: 1
titel: Goldbach-Paar
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 15
tags: [primzahlen, mathematik, paare]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Goldbachs Vermutung 1742
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: goldbach_paar
hints:
  - kosten: 0
    text: |
      Liefere für eine gerade Zahl n > 2 das kleinste Paar
      (p, q) zweier Primzahlen mit p + q == n und p <= q.
      Bei ungerader Zahl oder n <= 2 → None.
  - kosten: 15
    text: |
      Iteriere p = 2, 3, 5, 7, ... bis p <= n/2.
      Wenn p prim und (n - p) prim → Treffer (p, n-p).
tests_sichtbar:
  - input: [4]
    expected: [2, 2]
  - input: [10]
    expected: [3, 7]
  - input: [3]
    expected: null
  - input: [100]
    expected: [3, 97]
tests_versteckt:
  - input: [6]
    expected: [3, 3]
  - input: [8]
    expected: [3, 5]
  - input: [12]
    expected: [5, 7]
  - input: [24]
    expected: [5, 19]
  - input: [50]
    expected: [3, 47]
  - input: [2]
    expected: null
  - input: [7]
    expected: null
starter_code: |
  def goldbach_paar(n: int):
      # Deine Lösung hier -- (p, q) oder None
      pass
---

# Goldbach-Paar

Schreibe eine Funktion `goldbach_paar(n)`, die für eine **gerade Zahl
n > 2** das **kleinste Primzahl-Paar** `(p, q)` mit `p + q == n` und
`p <= q` zurückgibt.

Bei ungeraden Zahlen oder `n <= 2` → `None`.

## Beispiele

| `n`  | Paar       |
|------|------------|
| `4`  | `(2, 2)`   |
| `6`  | `(3, 3)`   |
| `8`  | `(3, 5)`   |
| `10` | `(3, 7)`   |
| `12` | `(5, 7)`   |
| `24` | `(5, 19)`  |
| `100`| `(3, 97)`  |
| `7`  | `None`     |

## Goldbachs Vermutung (1742)

> Jede gerade Zahl größer 2 ist als Summe zweier Primzahlen
> darstellbar.

Bis heute ist die Vermutung **unbewiesen**, aber bis $4 \cdot 10^{18}$
empirisch verifiziert. Eulers Antwort an Goldbach war: "Ich halte sie
für ein vollkommen sicheres Theorem, ungeachtet, dass ich sie nicht
beweisen kann."

