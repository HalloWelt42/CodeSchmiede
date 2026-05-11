---
schema_version: 1
id: 249-bereich-filtern
revision: 1
titel: Zahlen im Bereich [a, b] filtern
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, filter, vergleich]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 246
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: im_bereich
hints:
  - kosten: 0
    text: |
      Liefere alle Zahlen aus der Liste, die im inklusiven Bereich
      [a, b] liegen -- in der urspruenglichen Reihenfolge.
      a > b → [].
  - kosten: 5
    text: |
      [x for x in zahlen if a <= x <= b].
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 2, 4]
    expected: [2, 3, 4]
  - input: [[], 0, 10]
    expected: []
  - input: [[1, 2, 3], 10, 20]
    expected: []
  - input: [[1, 2, 3], 5, 1]
    expected: []
tests_versteckt:
  - input: [[5, 5, 5], 5, 5]
    expected: [5, 5, 5]
  - input: [[1, 2, 3, 4, 5], 1, 1]
    expected: [1]
  - input: [[1, 2, 3, 4, 5], 5, 5]
    expected: [5]
  - input: [[-3, -1, 0, 1, 3], -2, 2]
    expected: [-1, 0, 1]
  - input: [[10, 20, 30, 40, 50, 60], 25, 45]
    expected: [30, 40]
  - input: [[3, 1, 4, 1, 5, 9, 2, 6], 2, 5]
    expected: [3, 4, 5, 2]
starter_code: |
  def im_bereich(zahlen: list, a, b) -> list:
      # Deine Lösung hier
      pass
---

# Zahlen im Bereich [a, b] filtern

Schreibe `im_bereich(zahlen, a, b)`, die alle Zahlen aus der Liste
liefert, die im **inklusiven** Bereich `[a, b]` liegen --
in der **urspruenglichen Reihenfolge**.

Bei `a > b` → `[]`.

## Beispiele

| Liste                    | a   | b   | Ergebnis      |
|--------------------------|-----|-----|---------------|
| `[1, 2, 3, 4, 5]`        | 2   | 4   | `[2, 3, 4]`   |
| `[3, 1, 4, 1, 5, 9, 2]`  | 2   | 5   | `[3, 4, 5, 2]`|
| `[5, 5, 5]`              | 5   | 5   | `[5, 5, 5]`   |
| `[1, 2, 3]`              | 5   | 1   | `[]`          |
| `[]`                     | 0   | 10  | `[]`          |

## Idee

```python
def im_bereich(zahlen, a, b):
    return [x for x in zahlen if a <= x <= b]
```

`a <= x <= b` ist Pythons **chained comparison**, das wie in der
Mathematik liest.

## Pendant -- Anzahl

Aufgabe **246-bereich-zaehlen** liefert nur die Anzahl, nicht die
Werte. Beide haben **dieselbe Filter-Logik** -- nur das Aggregat
unterscheidet.

## Verallgemeinerung

Mit einer **Predicate-Funktion**:

```python
def filter_pred(liste, predicate):
    return [x for x in liste if predicate(x)]

# im Bereich [2, 4]:
filter_pred([1,2,3,4,5], lambda x: 2 <= x <= 4)
```

Sehr universell -- aber in Tests schwer zu serialisieren (Funktionen
gehen schlecht durch JSON). Daher hier die spezialisierte Variante.
