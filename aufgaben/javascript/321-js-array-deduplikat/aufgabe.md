---
schema_version: 1
id: 321-js-array-deduplikat
revision: 1
titel: JavaScript -- Array dedupen mit Set
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [javascript, array, set, spread, modern]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Set + Spread Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dedup
hints:
  - kosten: 0
    text: |
      Entferne Duplikate aus einem Array, behalte ERSTES Vorkommen.
      Reihenfolge wie im Original.
      Klassisch: [...new Set(arr)] -- elegant und schnell.
  - kosten: 5
    text: |
      Set behaelt insertion-order. [...] ist Spread, macht Array draus.
tests_sichtbar:
  - input: [[1, 2, 2, 3, 3, 3]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[5, 5, 5]]
    expected: [5]
  - input: [["a", "b", "a", "c"]]
    expected: ["a", "b", "c"]
starter_code: |
  function dedup(arr) {
      // Tipp: [...new Set(arr)]
  }
---

# JavaScript -- Array dedupen mit Set

Schreibe `dedup(arr)`, die Duplikate aus einem Array entfernt --
**erstes Vorkommen** wird behalten, Reihenfolge bleibt.

## Beispiele

| Array                    | Dedupliziert        |
|--------------------------|----------------------|
| `[1, 2, 2, 3, 3, 3]`     | `[1, 2, 3]`         |
| `[5, 5, 5]`              | `[5]`               |
| `["a", "b", "a", "c"]`   | `["a", "b", "c"]`   |
| `[]`                     | `[]`                |

## Idee -- modernes JS

```javascript
const dedup = (arr) => [...new Set(arr)];
```

Drei Schritte in einer Zeile:
1. `new Set(arr)` -- erzeugt Set aus dem Array (Duplikate raus)
2. `[...]` -- Spread macht aus dem Set wieder ein Array
3. Reihenfolge bleibt erhalten -- JS-Sets sind **insertion-ordered**

## Set-Eigenschaften in JS

- **Eindeutigkeit** via `===`-Vergleich
- **Insertion-Order** beim Iterieren
- `set.has(x)` ist `O(1)`
- `set.add(x)`, `set.delete(x)`, `set.size`

## Vergleich mit klassischem Filter-Ansatz

```javascript
const dedup = (arr) => arr.filter((x, i, a) => a.indexOf(x) === i);
```

Funktioniert, aber `O(n²)` -- jedes Element ruft `indexOf` auf.
Set-Variante ist `O(n)`.

## Stolperstein -- Object-Eindeutigkeit

```javascript
[...new Set([{a: 1}, {a: 1}])]  // bleibt 2 Eintraege!
```

Sets vergleichen Referenzen, nicht Inhalte. Bei Objekten muss man
manuell deduplizieren (z.B. via JSON-Stringify als Key).

## Vergleich mit Python

Python: `list(dict.fromkeys(arr))` -- nutzt insertion-order von
dict (seit 3.7). JavaScript hat das selbe Pattern, aber mit Set
direkt.
