---
schema_version: 1
id: 246-bereich-zaehlen
revision: 1
titel: Zahlen im Bereich [a, b] zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, vergleich, zaehlen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Filter-und-Zähl-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: im_bereich_zaehlen
hints:
  - kosten: 0
    text: |
      Wie viele Zahlen liegen im INKLUSIVEN Bereich [a, b]?
      sum(1 for x in zahlen if a <= x <= b).
      a > b liefert 0.
  - kosten: 5
    text: |
      sum(a <= x <= b for x in zahlen) -- Pythons booleans sind 0/1.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 2, 4]
    expected: 3
  - input: [[], 0, 10]
    expected: 0
  - input: [[1, 2, 3], 0, 10]
    expected: 3
  - input: [[1, 2, 3], 10, 20]
    expected: 0
tests_versteckt:
  - input: [[5, 5, 5], 5, 5]
    expected: 3
  - input: [[1, 2, 3, 4, 5], 5, 1]
    expected: 0
  - input: [[1, 2, 3, 4, 5], 1, 1]
    expected: 1
  - input: [[1, 2, 3, 4, 5], 5, 5]
    expected: 1
  - input: [[-3, -1, 0, 1, 3], -2, 2]
    expected: 3
  - input: [[10, 20, 30, 40, 50, 60], 25, 45]
    expected: 2
starter_code: |
  def im_bereich_zaehlen(zahlen: list, a, b) -> int:
      # Deine Lösung hier -- inklusive [a, b]
      pass
---

# Zahlen im Bereich [a, b] zählen

Schreibe `im_bereich_zählen(zahlen, a, b)`, die zählt, wie viele
Zahlen aus der Liste im **inklusiven** Bereich `[a, b]` liegen.

Bei `a > b` → `0`.

## Beispiele

| Liste              | a   | b   | Anzahl |
|--------------------|-----|-----|--------|
| `[1, 2, 3, 4, 5]`  | 2   | 4   | `3`    |
| `[1, 2, 3, 4, 5]`  | 1   | 1   | `1`    |
| `[1, 2, 3]`        | 10  | 20  | `0`    |
| `[5, 5, 5]`        | 5   | 5   | `3`    |
| `[-3, -1, 0, 1, 3]`| -2  | 2   | `3`    |

## Idee

`a <= x <= b` ist Pythons **chained comparison** -- liest sich wie
in Mathematik. In den meisten anderen Sprachen müsste man
`x >= a and x <= b` schreiben.

## Idee -- Boolean-Trick

Da `True == 1` und `False == 0` in Python, ist `sum` über Booleans
das Gleiche wie eine Zähl-Funktion. Sehr kurz, sehr Pythonisch.

## Stolperstein -- Inklusiv vs Exklusiv

`a <= x <= b` schließt **beide** Grenzen ein. Für halb-offene
Bereiche `[a, b)` wäre es `a <= x < b`. Für offene `(a, b)`:
`a < x < b`.

## Verwandt

Aufgabe **249-bereich-filtern** liefert nicht nur die Anzahl, sondern
die Werte selbst.
