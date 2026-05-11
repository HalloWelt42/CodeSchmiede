---
schema_version: 1
id: 238-gerade-filter
revision: 1
titel: Nur gerade Zahlen behalten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags: [listen, filter, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Filter
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: nur_gerade
hints:
  - kosten: 0
    text: |
      Liefere alle GERADEN Zahlen aus der Liste.
      Reihenfolge wie im Original.
      Null zählt als gerade.
  - kosten: 2
    text: |
      [x for x in liste if x % 2 == 0].
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5]]
    expected: [2, 4]
  - input: [[]]
    expected: []
  - input: [[1, 3, 5]]
    expected: []
  - input: [[2, 4, 6]]
    expected: [2, 4, 6]
tests_versteckt:
  - input: [[0]]
    expected: [0]
  - input: [[0, 1, 2, 3]]
    expected: [0, 2]
  - input: [[-2, -1, 0, 1, 2]]
    expected: [-2, 0, 2]
  - input: [[10, 20, 30, 40, 50]]
    expected: [10, 20, 30, 40, 50]
  - input: [[7]]
    expected: []
  - input: [[100, 99, 98, 97]]
    expected: [100, 98]
starter_code: |
  def nur_gerade(zahlen: list[int]) -> list[int]:
      # Deine Lösung hier
      pass
---

# Nur gerade Zahlen behalten

Schreibe `nur_gerade(zahlen)`, die alle **geraden Zahlen** (`x % 2 == 0`)
aus der Liste liefert -- in der **ursprünglichen Reihenfolge**.

Null zählt als gerade. Negative gerade Zahlen ebenso.

## Beispiele

| Liste              | Ergebnis        |
|--------------------|-----------------|
| `[1, 2, 3, 4, 5]`  | `[2, 4]`        |
| `[2, 4, 6]`        | `[2, 4, 6]`     |
| `[1, 3, 5]`        | `[]`            |
| `[0]`              | `[0]`           |
| `[-2, -1, 0, 1, 2]`| `[-2, 0, 2]`    |

## Idee

Die wohl häufigste Form einer Listen-Comprehension: filtern.

## Mit Builtin filter

Funktional äquivalent, aber Lambda + `filter` liest sich oft
schwerer als die Comprehension. In Python wird die Comprehension
bevorzugt.

## Pendant

Aufgabe **239-ungerade-filter** macht das Gegenstück. Beide zusammen
sind ein Beispiel für **Partition** (Aufgabe 228) auf der Modulo-Achse.
