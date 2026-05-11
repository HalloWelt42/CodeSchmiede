---
schema_version: 1
id: 325-summe-quadrate
revision: 1
titel: Summe der Quadrate 1 bis n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [zahlen, mathematik, summe, formel]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Sum_of_squares
  notiz: Rosetta Code -- Sum of squares
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: summe_quadrate
hints:
  - kosten: 0
    text: |
      Berechne 1² + 2² + 3² + ... + n².
      n <= 0 -> 0. Geschlossene Formel: n(n+1)(2n+1)/6.
  - kosten: 5
    text: |
      Direkt: sum(i*i for i in range(1, n+1)).
      Schneller (O(1)): n * (n + 1) * (2 * n + 1) // 6.
tests_sichtbar:
  - input: [0]
    expected: 0
  - input: [1]
    expected: 1
  - input: [3]
    expected: 14
  - input: [10]
    expected: 385
tests_versteckt:
  - input: [-5]
    expected: 0
  - input: [2]
    expected: 5
  - input: [4]
    expected: 30
  - input: [5]
    expected: 55
  - input: [100]
    expected: 338350
  - input: [1000]
    expected: 333833500
starter_code: |
  def summe_quadrate(n: int) -> int:
      # Tipp: Formel n(n+1)(2n+1)/6 ist O(1)
      pass
---

# Summe der Quadrate 1 bis n

Schreibe `summe_quadrate(n)`, die `1² + 2² + 3² + ... + n²`
berechnet.

Bei `n <= 0` → `0`.

## Beispiele

| `n`   | Ergebnis | Berechnung           |
|-------|----------|----------------------|
| `0`   | `0`      | leere Summe          |
| `1`   | `1`      | `1²`                 |
| `2`   | `5`      | `1 + 4`              |
| `3`   | `14`     | `1 + 4 + 9`          |
| `10`  | `385`    | `1 + 4 + ... + 100`  |
| `100` | `338350` |                      |

## Geschlossene Formel

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

Der Beweis über Induktion ist Schul-Standard. Carl Friedrich Gauß
hatte als Schüler die analoge Formel für die Summe ohne Quadrat
gefunden ($\frac{n(n+1)}{2}$, siehe Aufgabe 131).

## Idee 1 -- Formel (O(1))

Konstante Zeit -- funktioniert auch bei `n = 10**18` instant.

## Idee 2 -- Schleife (O(n))

Klar lesbar, für kleine `n` völlig ausreichend.

## Anwendung

Summen-Formeln tauchen in **Statistik** (Varianz-Berechnung),
**Physik** (Traegheitsmomente) und **Algorithmik** (Komplexitaets-
Analyse) auf.
