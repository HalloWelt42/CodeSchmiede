---
schema_version: 1
id: 308-fibonacci-bis-n-gen
revision: 1
titel: Fibonacci-Generator bis Maximum
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [generator, yield, fibonacci, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Generator-Pattern für Fibonacci
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: fibs_bis
hints:
  - kosten: 0
    text: |
      Liefere alle Fibonacci-Zahlen <= max als Liste.
      F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
      max < 0 → []. max == 0 → [0]. max == 1 → [0, 1, 1].
      Intern: while-Generator mit a, b = 0, 1.
  - kosten: 12
    text: |
      def gen(): a, b = 0, 1; while a <= max: yield a; a, b = b, a+b
tests_sichtbar:
  - input: [10]
    expected: [0, 1, 1, 2, 3, 5, 8]
  - input: [0]
    expected: [0]
  - input: [-1]
    expected: []
  - input: [1]
    expected: [0, 1, 1]
tests_versteckt:
  - input: [100]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  - input: [2]
    expected: [0, 1, 1, 2]
  - input: [50]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
  - input: [144]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
  - input: [4]
    expected: [0, 1, 1, 2, 3]
  - input: [21]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21]
starter_code: |
  def fibs_bis(max_wert: int) -> list[int]:
      # Tipp: while-Generator mit a, b = 0, 1
      pass
---

# Fibonacci-Generator bis Maximum

Schreibe `fibs_bis(max_wert)`, die alle **Fibonacci-Zahlen** bis
einschließlich `max_wert` als Liste liefert.

Fibonacci: $F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}$.

`max_wert < 0` → `[]`. `max_wert >= 0` → mindestens `[0]`.

## Beispiele

| `max_wert` | Ergebnis                                |
|------------|------------------------------------------|
| `-1`       | `[]`                                    |
| `0`        | `[0]`                                   |
| `1`        | `[0, 1, 1]`                             |
| `10`       | `[0, 1, 1, 2, 3, 5, 8]`                 |
| `21`       | `[0, 1, 1, 2, 3, 5, 8, 13, 21]`         |
| `100`      | `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]` |
| `144`      | `[..., 89, 144]`                        |

## Idee -- Generator intern

Der Generator endet, wenn `a` zu groß wird. Die Tupel-Zuweisung
`a, b = b, a + b` ist Pythons elegante Form für den Fibonacci-
Schritt -- in C/Java braucht man eine Hilfsvariable.

## Warum Generator?

Bei sehr großen `max_wert` (oder unbekanntem Limit) kann man den
Generator iterieren, bis man genug hat -- ohne die ganze Liste im
Speicher zu halten.

Das ist mit einer Liste nicht so elegant moeglich.

## Verwandt

- **003-fibonacci**: nur n-tes Element
- **092-fibonacci-folge**: erste n Elemente
- **308 hier**: alle bis Maximum (mit Generator-Pattern)
