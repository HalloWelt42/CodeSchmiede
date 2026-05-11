---
schema_version: 1
id: 227-zip-mit-fuellwert
revision: 1
titel: Zip mit Fuellwert
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [listen, zip, itertools]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: zip_longest-Klassiker
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zip_fuell
hints:
  - kosten: 0
    text: |
      Verzahne zwei Listen zu Paaren [a_i, b_i].
      Wenn eine Liste kuerzer ist, werden die fehlenden Elemente
      mit fuell aufgefuellt (statt abzuschneiden wie zip).
      Bei zwei leeren Listen → [].
  - kosten: 10
    text: |
      itertools.zip_longest(a, b, fillvalue=fuell).
      [list(p) for p in ...] um Tupel zu Listen.
tests_sichtbar:
  - input: [[1, 2, 3], [4, 5, 6], 0]
    expected: [[1, 4], [2, 5], [3, 6]]
  - input: [[1, 2], [4, 5, 6], 0]
    expected: [[1, 4], [2, 5], [0, 6]]
  - input: [[], [], 0]
    expected: []
  - input: [[1, 2, 3], [], "x"]
    expected: [[1, "x"], [2, "x"], [3, "x"]]
tests_versteckt:
  - input: [[1], [1, 2, 3, 4, 5], 0]
    expected: [[1, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
  - input: [[1, 2, 3, 4, 5], [10], 0]
    expected: [[1, 10], [2, 0], [3, 0], [4, 0], [5, 0]]
  - input: [[], [1, 2], -1]
    expected: [[-1, 1], [-1, 2]]
  - input: [[1, 2, 3], [4, 5, 6], -1]
    expected: [[1, 4], [2, 5], [3, 6]]
  - input: [["a", "b"], ["c", "d", "e"], "?"]
    expected: [["a", "c"], ["b", "d"], ["?", "e"]]
starter_code: |
  from itertools import zip_longest

  def zip_fuell(a: list, b: list, fuell) -> list[list]:
      # Deine Lösung hier -- zip_longest mit fillvalue
      pass
---

# Zip mit Fuellwert

Schreibe `zip_fuell(a, b, fuell)`, die zwei Listen zu Paaren
verzahnt -- aber **kuerzere Listen werden aufgefuellt** statt
abgeschnitten (wie das eingebaute `zip` es tut).

## Beispiele

| `a`         | `b`            | `fuell` | Ergebnis                        |
|-------------|----------------|---------|----------------------------------|
| `[1,2,3]`   | `[4,5,6]`      | `0`     | `[[1,4],[2,5],[3,6]]`            |
| `[1,2]`     | `[4,5,6]`      | `0`     | `[[1,4],[2,5],[0,6]]`            |
| `[1,2,3]`   | `[]`           | `"x"`   | `[[1,"x"],[2,"x"],[3,"x"]]`      |
| `[]`        | `[]`           | `0`     | `[]`                             |

## Idee -- itertools.zip_longest

```python
from itertools import zip_longest

def zip_fuell(a, b, fuell):
    return [list(p) for p in zip_longest(a, b, fillvalue=fuell)]
```

`zip_longest` ist die "geht-weiter-bis-die-laengste-Liste-fertig-ist"-
Variante. Pro Element ein Tupel -- wir konvertieren zu Listen.

## Vergleich -- zip vs zip_longest

| Funktion       | Ergebnis-Laenge       | Fuellung |
|----------------|------------------------|----------|
| `zip`          | Laenge der **kuerzeren**| keine    |
| `zip_longest`  | Laenge der **laengeren**| ja       |

`zip` ist wie `min(len_a, len_b)`, `zip_longest` wie `max(len_a, len_b)`.

## Anwendung

- Tabellen aus zwei Spalten unterschiedlicher Laenge.
- Vergleich zweier Versions-Listen mit fehlenden Eintraegen.
- Mathematik: Polynom-Addition, wenn Grade unterschiedlich sind.
