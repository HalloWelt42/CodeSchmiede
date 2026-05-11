---
schema_version: 1
id: 207-skalarprodukt
revision: 1
titel: Skalarprodukt zweier Vektoren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [vektor, mathematik, zip, lineare-algebra]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Lineare Algebra Grundlage
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: skalarprodukt
hints:
  - kosten: 0
    text: |
      Berechne das Skalarprodukt: a . b = sum(a_i * b_i).
      Beide Vektoren müssen gleich lang sein -- sonst 0.
      Bei [] und [] -> 0.
  - kosten: 10
    text: |
      sum(x * y for x, y in zip(a, b)).
      Wenn len(a) != len(b) -> 0 vorab.
tests_sichtbar:
  - input: [[1, 2, 3], [4, 5, 6]]
    expected: 32
  - input: [[1, 0], [0, 1]]
    expected: 0
  - input: [[], []]
    expected: 0
  - input: [[1, 2], [3]]
    expected: 0
tests_versteckt:
  - input: [[1, 1, 1], [1, 1, 1]]
    expected: 3
  - input: [[2, 3], [4, 5]]
    expected: 23
  - input: [[-1, 2], [3, -4]]
    expected: -11
  - input: [[10, 20, 30], [1, 2, 3]]
    expected: 140
  - input: [[5], [6]]
    expected: 30
  - input: [[1.5, 2.5], [2, 4]]
    expected: 13.0
starter_code: |
  def skalarprodukt(a: list, b: list):
      # Deine Lösung hier -- bei verschiedener Laenge → 0
      pass
---

# Skalarprodukt zweier Vektoren

Schreibe `skalarprodukt(a, b)`, die das **Skalarprodukt** (auch
Punkt-Produkt, dot product) zweier gleichlanger Vektoren
zurückgibt.

$$\vec{a} \cdot \vec{b} = \sum_{i} a_i \cdot b_i$$

Bei verschiedener Laenge → `0`. Bei `[] [] → 0`.

## Beispiele

| `a`           | `b`           | Skalarprodukt |
|---------------|---------------|---------------|
| `[1, 2, 3]`   | `[4, 5, 6]`   | `32` (4+10+18)|
| `[1, 0]`      | `[0, 1]`      | `0`           |
| `[2, 3]`      | `[4, 5]`      | `23`          |
| `[-1, 2]`     | `[3, -4]`     | `-11`         |
| `[1.5, 2.5]`  | `[2, 4]`      | `13.0`        |

## Geometrische Bedeutung

$$\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos(\theta)$$

Daraus folgt:

- **0** = Vektoren stehen **senkrecht** aufeinander.
- **positiv** = Winkel < 90° (gleiche Richtung).
- **negativ** = Winkel > 90° (entgegengesetzt).

Klassiker in der **Physik** (Arbeit = Kraft x Weg) und in
**Machine Learning** (cosine similarity).

## Erweiterung

`numpy.dot(a, b)` macht das hocheffizient mit BLAS. Für kurze
Listen ist Pythons `sum`-Comprehension absolut ausreichend.
