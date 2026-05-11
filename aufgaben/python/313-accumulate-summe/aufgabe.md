---
schema_version: 1
id: 313-accumulate-summe
revision: 1
titel: Laufende Summen (accumulate)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [generator, yield, listen, prefix-sum]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: itertools.accumulate nachbauen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: laufende_summen
hints:
  - kosten: 0
    text: |
      Liefere die laufenden Summen einer Liste.
      [1, 2, 3, 4] → [1, 3, 6, 10] (1, 1+2, 1+2+3, 1+2+3+4).
      Bei [] → [].
      Intern Generator mit yield.
  - kosten: 8
    text: |
      def gen(): summe=0; for x in liste: summe+=x; yield summe.
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: [1, 3, 6, 10]
  - input: [[]]
    expected: []
  - input: [[5]]
    expected: [5]
  - input: [[1, 1, 1, 1, 1]]
    expected: [1, 2, 3, 4, 5]
tests_versteckt:
  - input: [[10]]
    expected: [10]
  - input: [[1, -1, 1, -1]]
    expected: [1, 0, 1, 0]
  - input: [[100, 200, 300]]
    expected: [100, 300, 600]
  - input: [[0, 0, 0, 0]]
    expected: [0, 0, 0, 0]
  - input: [[-5, -3, -1]]
    expected: [-5, -8, -9]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
starter_code: |
  def laufende_summen(liste: list[int]) -> list[int]:
      # Tipp: Generator mit Akkumulator
      pass
---

# Laufende Summen (accumulate)

Schreibe `laufende_summen(liste)`, die die **kumulierten Summen**
einer Liste liefert -- jedes Element ist die Summe **bis einschließlich
dieser Position**.

`[1, 2, 3, 4]` → `[1, 1+2, 1+2+3, 1+2+3+4]` → `[1, 3, 6, 10]`.

Bei leerer Liste → `[]`.

## Beispiele

| Liste              | Laufende Summen     |
|--------------------|---------------------|
| `[1, 2, 3, 4]`     | `[1, 3, 6, 10]`     |
| `[5]`              | `[5]`               |
| `[1, 1, 1, 1, 1]`  | `[1, 2, 3, 4, 5]`   |
| `[1, -1, 1, -1]`   | `[1, 0, 1, 0]`      |
| `[100, 200, 300]`  | `[100, 300, 600]`   |
| `[]`               | `[]`                |

## Idee -- Generator

Der Akkumulator `summe` wird zwischen den `yield`-Aufrufen
**erhalten** -- das ist die Magie der Generator-Funktionen.

## Mit itertools.accumulate

`accumulate` macht es default mit Addition. Mit dem `func`-
Parameter kann man auch Multiplikation, Maximum oder beliebige
binaere Operationen nehmen:

## Verwandt

- **055-prefix-summe** (gleiche Aufgabe, ohne Generator-Pattern)
- **313 hier** (mit Generator)
- Aufgabe **244-gleitender-mittelwert** (Sliding Mean)

## Anwendung

- **Praefix-Summen-Optimierung**: Range-Summen in `O(1)` nach `O(n)`-Vorbereitung
- **Inkrementelle Statistik**: kumulierte Verkaufszahlen, laufender Score
- **Visualisierung**: Kumulative Charts (z.B. CDF in der Statistik)
