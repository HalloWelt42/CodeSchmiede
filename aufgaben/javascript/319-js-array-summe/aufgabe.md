---
schema_version: 1
id: 319-js-array-summe
revision: 1
titel: JavaScript -- Array-Summe mit reduce
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [javascript, array, reduce, modern]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Modernes JS, Array.reduce
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: arraySumme
hints:
  - kosten: 0
    text: |
      Summiere alle Zahlen im Array mit Array.reduce.
      Bei leerem Array → 0.
      Arrow function + reduce ist die moderne Form.
  - kosten: 5
    text: |
      arr.reduce((akk, x) => akk + x, 0).
      Der Startwert 0 ist wichtig für den leeren Array-Fall.
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: 10
  - input: [[]]
    expected: 0
  - input: [[5]]
    expected: 5
  - input: [[-1, -2, 3]]
    expected: 0
starter_code: |
  function arraySumme(arr) {
      // Tipp: arr.reduce((a, x) => a + x, 0)
  }
---

# JavaScript -- Array-Summe mit reduce

Schreibe `arraySumme(arr)`, die alle Zahlen im Array summiert.
Bei leerem Array → `0`.

## Beispiele

| Array            | Summe |
|------------------|-------|
| `[1, 2, 3, 4]`   | `10`  |
| `[5]`            | `5`   |
| `[-1, -2, 3]`    | `0`   |
| `[]`             | `0`   |

## Idee -- modernes JS

Oder als **Arrow Function**:

`Array.reduce` ist das JavaScript-Aequivalent von Pythons
`functools.reduce`. Der **Startwert** `0` ist wichtig: ohne ihn
würde `reduce` bei leerem Array einen `TypeError` werfen.

## Vergleich mit Python

| Sprache    | Variante                              |
|------------|---------------------------------------|
| Python     | `sum(arr)` -- builtin, kein reduce    |
| JavaScript | `arr.reduce((a, x) => a + x, 0)`      |
| JavaScript | `arr.reduce((a, b) => a + b, 0)` -- gleich |

Pythons `sum` ist hochoptimiert in C, in JS gibt es kein direktes
Pendant -- `reduce` ist der Standard-Weg.
