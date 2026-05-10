---
schema_version: 1
id: 017-fakultaet
revision: 1
titel: Fakultät n!
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, schleifen, rekursion]
pfade: [python_mathe]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Fakult%C3%A4t_(Mathematik)
  notiz: Standard-Mathe, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: fakultaet
hints:
  - kosten: 0
    text: |
      Per Definition: `0! = 1` und `n! = n * (n-1)!`. Also `5! = 5 * 4 * 3 * 2 * 1 = 120`.
  - kosten: 10
    text: |
      Iterativ mit `range(2, n+1)`:

      ```
      ergebnis = 1
      for i in range(2, n+1):
          ergebnis *= i
      ```
tests_sichtbar:
  - input: [0]
    expected: 1
  - input: [1]
    expected: 1
  - input: [5]
    expected: 120
  - input: [10]
    expected: 3628800
tests_versteckt:
  - input: [2]
    expected: 2
  - input: [7]
    expected: 5040
  - input: [12]
    expected: 479001600
  - input: [20]
    expected: 2432902008176640000
starter_code: |
  def fakultaet(n: int) -> int:
      # Deine Lösung hier
      pass
---

# Fakultät $n!$

Schreibe eine Funktion `fakultaet(n)`, die die **Fakultät** einer
nicht-negativen ganzen Zahl `n` zurueckgibt.

Per Definition gilt:

$$
n! = \begin{cases}
1 & \text{falls } n = 0 \\
n \cdot (n-1)! & \text{sonst}
\end{cases}
$$

## Beispiele

| Eingabe | Ergebnis  |
|---------|-----------|
| `0`     | `1`       |
| `1`     | `1`       |
| `5`     | `120`     |
| `10`    | `3628800` |

## Wege

Du kannst die Aufgabe **iterativ** (Schleife) oder **rekursiv**
(Funktion ruft sich selbst auf) loesen. Beide Wege sind valide --
fuer grosse `n` ist die Iteration in Python aber bequemer.

## Hintergrund

Die Fakultät zählt die Anzahl möglicher Anordnungen von $n$ Objekten.
$5! = 120$ heisst: 5 Buecher kannst du auf 120 verschiedene Arten in
ein Regal sortieren.
