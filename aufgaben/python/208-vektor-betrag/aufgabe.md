---
schema_version: 1
id: 208-vektor-betrag
revision: 1
titel: Vektor-Betrag (euklidische Norm)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [vektor, mathematik, sqrt, lineare-algebra]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Lineare Algebra Grundlage
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: betrag
hints:
  - kosten: 0
    text: |
      Berechne die euklidische Norm: sqrt(sum(x**2)).
      Auf 4 Nachkommastellen runden.
      Bei [] -> 0.0.
  - kosten: 10
    text: |
      math.sqrt(sum(x * x for x in v)) und round(..., 4).
tests_sichtbar:
  - input: [[3, 4]]
    expected: 5.0
  - input: [[1, 0]]
    expected: 1.0
  - input: [[]]
    expected: 0.0
  - input: [[0, 0, 0]]
    expected: 0.0
tests_versteckt:
  - input: [[1, 1]]
    expected: 1.4142
  - input: [[1, 1, 1]]
    expected: 1.7321
  - input: [[5, 12]]
    expected: 13.0
  - input: [[-3, -4]]
    expected: 5.0
  - input: [[6, 8, 10]]
    expected: 14.1421
  - input: [[2.5, 6]]
    expected: 6.5
starter_code: |
  import math

  def betrag(v: list) -> float:
      # Deine Lösung hier -- euklidische Norm, 4 Nachkommastellen
      pass
---

# Vektor-Betrag (euklidische Norm)

Schreibe `betrag(v)`, die die **Laenge** (euklidische Norm) eines
Vektors berechnet -- gerundet auf 4 Nachkommastellen.

$$|\vec{v}| = \sqrt{\sum_i v_i^2}$$

Bei `[]` → `0.0`.

## Beispiele

| Vektor       | Betrag    |
|--------------|-----------|
| `[3, 4]`     | `5.0`     |
| `[5, 12]`    | `13.0`    |
| `[1, 1]`     | `1.4142`  |
| `[1, 1, 1]`  | `1.7321`  |
| `[-3, -4]`   | `5.0`     |
| `[6, 8, 10]` | `14.1421` |

## Idee

```python
import math

def betrag(v):
    return round(math.sqrt(sum(x * x for x in v)), 4)
```

## Pythagoras-Tripel

Bei Vektoren wie `[3, 4]`, `[5, 12]`, `[8, 15]` ergibt die Norm eine
**ganze Zahl** -- das sind die altbekannten **pythagoraeischen
Tripel** (siehe Aufgabe 084).

## Andere Normen

Die euklidische Norm ist die `L2`-Norm. Es gibt mehr:

| Norm  | Formel                            | Bedeutung                |
|-------|-----------------------------------|--------------------------|
| `L0`  | Anzahl Nicht-Null-Komponenten     | Sparsity                 |
| `L1`  | Summe Absolutwerte                | "Manhattan"-Distanz      |
| `L2`  | Wurzel der Quadrat-Summe          | Euklidisch (hier)        |
| `L∞`  | Maximaler Absolutwert             | "Schach-Koenig"-Distanz  |

Im Maschinenlernen kommen alle vor -- L1/L2 z.B. als
**Regularisierungsterm** in linearen Modellen.
