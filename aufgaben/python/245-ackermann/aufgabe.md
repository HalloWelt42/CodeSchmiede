---
schema_version: 1
id: 245-ackermann
revision: 1
titel: Ackermann-Funktion
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [rekursion, mathematik, klassiker]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Rekursions-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ackermann
hints:
  - kosten: 0
    text: |
      A(0, n) = n + 1
      A(m, 0) = A(m-1, 1)        wenn m > 0
      A(m, n) = A(m-1, A(m, n-1))  wenn m > 0 und n > 0
      Achtung: waechst extrem schnell -- nur kleine m, n testen!
  - kosten: 15
    text: |
      Direkte Umsetzung der drei Faelle. Prüfe nicht-negative Werte.
      Bei m == 4 wird der Wert riesig (A(4,2) = 2^65536 - 3).
      Wir testen nur m <= 3.
tests_sichtbar:
  - input: [0, 0]
    expected: 1
  - input: [1, 1]
    expected: 3
  - input: [2, 2]
    expected: 7
  - input: [3, 3]
    expected: 61
tests_versteckt:
  - input: [0, 5]
    expected: 6
  - input: [1, 0]
    expected: 2
  - input: [1, 5]
    expected: 7
  - input: [2, 0]
    expected: 3
  - input: [2, 4]
    expected: 11
  - input: [3, 0]
    expected: 5
  - input: [3, 4]
    expected: 125
  - input: [3, 5]
    expected: 253
starter_code: |
  def ackermann(m: int, n: int) -> int:
      # Deine Lösung hier
      pass
---

# Ackermann-Funktion

Schreibe `ackermann(m, n)`, die klassische **Ackermann-Funktion**
für nicht-negative ganze Zahlen.

$$A(m, n) = \begin{cases}
n + 1 & \text{wenn } m = 0 \\
A(m-1, 1) & \text{wenn } m > 0, n = 0 \\
A(m-1, A(m, n-1)) & \text{wenn } m > 0, n > 0
\end{cases}$$

## Beispiele

| `m` | `n` | `A(m, n)` |
|-----|-----|-----------|
| 0   | 0   | 1         |
| 0   | 5   | 6         |
| 1   | 0   | 2         |
| 1   | 5   | 7         |
| 2   | 2   | 7         |
| 3   | 3   | 61        |
| 3   | 4   | 125       |
| 3   | 5   | 253       |

## Idee -- direkte Rekursion

Drei Faelle, eine doppelt verschachtelte Rekursion -- der Klassiker.

## Warum so beruehmt?

Die Ackermann-Funktion ist **berechenbar**, aber **nicht primitiv
rekursiv**. Sie waechst extrem schnell:

| `(m, n)` | `A(m, n)`              |
|----------|------------------------|
| `(3, 3)` | 61                     |
| `(4, 0)` | 13                     |
| `(4, 1)` | 65533                  |
| `(4, 2)` | $2^{65536} - 3$ (so groß!) |
| `(5, 0)` | 65533                  |

Sie war historisch (Wilhelm Ackermann, 1928) **das** Beispiel dafür,
dass berechenbar > primitiv rekursiv.

## Stolperstein -- Rekursionstiefe

Schon bei `A(4, 2)` sprengt jede einfache Implementierung den
Speicher. Wir testen nur bis `m = 3`, `n = 5`.
