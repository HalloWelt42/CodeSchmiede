---
schema_version: 1
id: 326-js-summe-quadrate
revision: 1
titel: JavaScript -- Summe der Quadrate
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [javascript, zahlen, mathematik, formel]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Sum_of_squares
  notiz: Rosetta Code -- Sum of squares, JS-Version
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: summeQuadrate
hints:
  - kosten: 0
    text: |
      Berechne 1² + 2² + ... + n². n <= 0 -> 0.
      Geschlossene Formel ist O(1): n*(n+1)*(2n+1)/6.
  - kosten: 10
    text: |
      Math.floor(n*(n+1)*(2*n+1)/6) -- Floor wegen Float-Trick.
tests_sichtbar:
  - input: [0]
    expected: 0
  - input: [1]
    expected: 1
  - input: [3]
    expected: 14
  - input: [10]
    expected: 385
starter_code: |
  function summeQuadrate(n) {
      // Tipp: Formel ist O(1)
  }
---

# JavaScript -- Summe der Quadrate

Schreibe `summeQuadrate(n)`, die `1² + 2² + ... + n²` berechnet.

Bei `n <= 0` → `0`.

## Beispiele

| `n`  | Ergebnis | Berechnung   |
|------|----------|--------------|
| `0`  | `0`      | leere Summe  |
| `1`  | `1`      | `1²`         |
| `3`  | `14`     | `1+4+9`      |
| `10` | `385`    |              |

## Geschlossene Formel

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

## Idee -- O(1) per Formel

```javascript
function summeQuadrate(n) {
    if (n <= 0) return 0;
    return Math.floor((n * (n + 1) * (2 * n + 1)) / 6);
}
```

`Math.floor` ist hier nicht streng noetig (das Produkt
`n(n+1)(2n+1)` ist immer durch 6 teilbar), aber durch
Float-Arithmetik koennte ein Werte wie `385.0000000001` entstehen.
Floor sichert die ganze Zahl.

## Vergleich mit Python

In Python hilft `//` (Integer-Division), in JavaScript braucht
man `Math.floor`. Pythons `//` ist exakt, JS `/` ist immer Float.
