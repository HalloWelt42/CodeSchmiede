---
schema_version: 1
id: 131-gauss-summe
revision: 1
titel: Gauss-Summe
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [zahlen, formel, mathematik]
pfade: [python_mathe]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Summenformel
  notiz: Klassische Mathe-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gauss_summe
hints:
  - kosten: 0
    text: |
      Summe 1+2+...+n. Mit Gauss-Formel: n*(n+1)/2.
      Bei n < 1 → 0.
  - kosten: 10
    text: |
      Verboten waere `sum(range(1, n+1))`. Ist nicht verboten,
      aber die Formel ist O(1) statt O(n) -- der ganze Witz.
tests_sichtbar:
  - input: [1]
    expected: 1
  - input: [10]
    expected: 55
  - input: [100]
    expected: 5050
  - input: [0]
    expected: 0
tests_versteckt:
  - input: [-5]
    expected: 0
  - input: [2]
    expected: 3
  - input: [3]
    expected: 6
  - input: [50]
    expected: 1275
  - input: [1000000]
    expected: 500000500000
starter_code: |
  def gauss_summe(n: int) -> int:
      # Deine Lösung hier -- 1+2+...+n. Mit Formel in O(1).
      pass
---

# Gauss-Summe

Schreibe eine Funktion `gauss_summe(n)`, die die Summe der ersten
`n` natürlichen Zahlen zurückgibt.

Bei `n < 1` → `0`.

## Formel

$$
\sum_{k=1}^n k = \frac{n(n+1)}{2}
$$

## Beispiele

| `n`       | Ergebnis        |
|-----------|-----------------|
| `1`       | `1`             |
| `10`      | `55`            |
| `100`     | `5050`          |
| `1000000` | `500000500000`  |
| `0`       | `0`             |
| `-5`      | `0`             |

## Hintergrund

Die Anekdote: der 9-jährige Carl Friedrich Gauss soll in der
Volksschule die Aufgabe bekommen haben, alle Zahlen von 1 bis 100 zu
summieren. Wo seine Mitschüler stundenlang rechneten, lieferte
Gauss in Sekunden 5050 ab -- mit der Formel.

Ob die Geschichte stimmt, ist umstritten. Die Formel selbst ist
klar: $1 + 2 + \ldots + n = n(n+1)/2$.
