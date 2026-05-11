---
schema_version: 1
id: 332-js-range-expansion
revision: 1
titel: JavaScript -- Bereichs-Notation entpacken
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [javascript, strings, parsing, array, modern]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Range_expansion
  notiz: Rosetta Code -- Range expansion, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bereichEntpacken
hints:
  - kosten: 0
    text: |
      Entpacke "1-3,5,7-9" zu [1,2,3,5,7,8,9]. Negative Untergrenzen
      ("-3--1") muessen funktionieren. Leerer String -> [].
  - kosten: 20
    text: |
      split(",") -- pro Stueck indexOf("-", 1) fuer den Trenner.
      Array.from({length: b-a+1}, (_, i) => a+i) erzeugt den Bereich.
tests_sichtbar:
  - input: ["1-3,5,7-9"]
    expected: [1, 2, 3, 5, 7, 8, 9]
  - input: [""]
    expected: []
  - input: ["5"]
    expected: [5]
  - input: ["1-5"]
    expected: [1, 2, 3, 4, 5]
starter_code: |
  function bereichEntpacken(s) {
      // Tipp: split(",") + indexOf("-", 1) fuer negative Untergrenzen
  }
---

# JavaScript -- Bereichs-Notation entpacken

Schreibe `bereichEntpacken(s)`, die einen Bereichs-String wie
`"1-3,5,7-9"` in das Array `[1, 2, 3, 5, 7, 8, 9]` umwandelt.

- Komma trennt Stuecke
- Bindestrich trennt Unter-/Obergrenze in einem Stueck
- Negative Untergrenzen: `"-3--1"` -> `[-3, -2, -1]`
- Leer -> `[]`

## Beispiele

| Eingabe         | Ergebnis                          |
|-----------------|-----------------------------------|
| `"1-3,5,7-9"`   | `[1, 2, 3, 5, 7, 8, 9]`           |
| `"1-5"`         | `[1, 2, 3, 4, 5]`                 |
| `"5"`           | `[5]`                             |
| `"-3--1,2,4-6"` | `[-3, -2, -1, 2, 4, 5, 6]`        |
| `""`            | `[]`                              |

## Idee

```javascript
function bereichEntpacken(s) {
    if (!s) return [];
    const out = [];
    for (const stueck of s.split(",")) {
        const idx = stueck.indexOf("-", 1);
        if (idx > 0) {
            const a = parseInt(stueck.slice(0, idx), 10);
            const b = parseInt(stueck.slice(idx + 1), 10);
            for (let i = a; i <= b; i++) out.push(i);
        } else {
            out.push(parseInt(stueck, 10));
        }
    }
    return out;
}
```

`indexOf("-", 1)` sucht ab Index 1 -- damit greift ein fuehrendes
Minus (negative Untergrenze) nicht als Trenner.

## Variante mit Array.from + Spread

```javascript
const bereichEntpacken = (s) => {
    if (!s) return [];
    return s.split(",").flatMap((stueck) => {
        const idx = stueck.indexOf("-", 1);
        if (idx <= 0) return [parseInt(stueck, 10)];
        const a = parseInt(stueck.slice(0, idx), 10);
        const b = parseInt(stueck.slice(idx + 1), 10);
        return Array.from({ length: b - a + 1 }, (_, i) => a + i);
    });
};
```

`flatMap` ist die elegante Form, wenn pro Element 0..n Ergebnisse
geliefert werden.

## Vergleich mit Python

Pythons `range(a, b + 1)` liefert direkt einen Iterator. JS hat
keinen direkten `range`, aber `Array.from({length: n}, ...)` macht
das gleiche.
