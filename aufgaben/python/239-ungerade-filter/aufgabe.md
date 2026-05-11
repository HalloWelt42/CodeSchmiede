---
schema_version: 1
id: 239-ungerade-filter
revision: 1
titel: Nur ungerade Zahlen behalten
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
  notiz: Pendant zu 238
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: nur_ungerade
hints:
  - kosten: 0
    text: |
      Liefere alle UNGERADEN Zahlen aus der Liste -- Reihenfolge
      wie im Original.
  - kosten: 2
    text: |
      [x for x in liste if x % 2 != 0].
      Achtung: -3 % 2 ist 1 in Python (nicht -1) -- die Filter-Variante
      mit "!= 0" ist robust.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5]]
    expected: [1, 3, 5]
  - input: [[]]
    expected: []
  - input: [[2, 4, 6]]
    expected: []
  - input: [[1, 3, 5]]
    expected: [1, 3, 5]
tests_versteckt:
  - input: [[0]]
    expected: []
  - input: [[0, 1, 2, 3]]
    expected: [1, 3]
  - input: [[-3, -2, -1, 0, 1]]
    expected: [-3, -1, 1]
  - input: [[7]]
    expected: [7]
  - input: [[100, 99, 98, 97]]
    expected: [99, 97]
  - input: [[10]]
    expected: []
starter_code: |
  def nur_ungerade(zahlen: list[int]) -> list[int]:
      # Deine Lösung hier
      pass
---

# Nur ungerade Zahlen behalten

Schreibe `nur_ungerade(zahlen)`, die alle **ungeraden Zahlen**
(`x % 2 != 0`) aus der Liste liefert.

## Beispiele

| Liste              | Ergebnis        |
|--------------------|-----------------|
| `[1, 2, 3, 4, 5]`  | `[1, 3, 5]`     |
| `[1, 3, 5]`        | `[1, 3, 5]`     |
| `[2, 4, 6]`        | `[]`            |
| `[0]`              | `[]`            |
| `[-3, -2, -1, 0, 1]`| `[-3, -1, 1]`  |

## Stolperstein -- Negative Modulo

In **Python** gilt `-3 % 2 == 1` (nicht -1, wie in C/Java). Darum
funktioniert `if x % 2 != 0` auch mit negativen Zahlen sauber.

In Sprachen mit "C-Modulo" müsste man `if x % 2 != 0` schreiben
und sich klarmachen, dass `-3 % 2 == -1` -- der Filter funktioniert
trotzdem, weil `-1 != 0`.

## Pendant

Aufgabe **238-gerade-filter** ist das Gegenstück. Beide zusammen
zerlegen die Liste -- ohne Verlust:
`nur_gerade(xs) + nur_ungerade(xs)` enthält jede Zahl genau einmal,
nur in zwei Gruppen aufgeteilt.
