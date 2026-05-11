---
schema_version: 1
id: 086-quadrat-summen-differenz
revision: 1
titel: Differenz Quadrat-Summen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, summen, formel, project-euler]
pfade: [python_mathe2]
voraussetzungen: []
quelle:
  url: https://projecteuler.net/problem=6
  notiz: Project Euler 6, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: differenz
hints:
  - kosten: 0
    text: |
      Berechne $S_1 = (1+2+\ldots+n)^2$ und $S_2 = 1^2+2^2+\ldots+n^2$.
      Gib $S_1 - S_2$ zurück.
  - kosten: 8
    text: |
      Schneller mit Formel:
      $S_1 = (n(n+1)/2)^2$ und $S_2 = n(n+1)(2n+1)/6$.
tests_sichtbar:
  - input: [1]
    expected: 0
  - input: [5]
    expected: 170
  - input: [10]
    expected: 2640
  - input: [100]
    expected: 25164150
tests_versteckt:
  - input: [0]
    expected: 0
  - input: [2]
    expected: 4
  - input: [50]
    expected: 1582700
  - input: [1000]
    expected: 250166416500
starter_code: |
  def differenz(n: int) -> int:
      # Deine Lösung hier -- (Summe der ersten n)² - (Summe der Quadrate).
      pass
---

# Differenz Quadrat-Summen

Schreibe eine Funktion `differenz(n)`, die folgendes berechnet:

$$
\left( \sum_{k=1}^{n} k \right)^2 - \sum_{k=1}^{n} k^2
$$

## Beispiele

| `n`   | $\sum k$ | $(\sum k)^2$ | $\sum k^2$ | Differenz |
|-------|---------|--------------|------------|-----------|
| `1`   | 1       | 1            | 1          | `0`       |
| `5`   | 15      | 225          | 55         | `170`     |
| `10`  | 55      | 3025         | 385        | `2640`    |
| `100` | 5050    | 25502500     | 338350     | `25164150`|

## Hintergrund

Project Euler Problem 6. Mit den geschlossenen Formeln

$$
\sum_{k=1}^n k = \frac{n(n+1)}{2}, \qquad
\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}
$$

geht das in $O(1)$ statt $O(n)$.
