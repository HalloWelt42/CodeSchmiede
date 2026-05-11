---
schema_version: 1
id: 328-js-tau-funktion
revision: 1
titel: JavaScript -- Tau-Funktion
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [javascript, zahlen, mathematik, teiler]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Tau_function
  notiz: Rosetta Code -- Tau function, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: tau
hints:
  - kosten: 0
    text: |
      Anzahl positiver Teiler von n. n < 1 -> 0.
      Schleife i = 1..sqrt(n), pro Treffer +2 (Partner i und n/i),
      bei i*i == n nur +1.
  - kosten: 15
    text: |
      let z = 0; for (let i = 1; i*i <= n; i++) { if (n % i === 0) z += i*i === n ? 1 : 2; }
tests_sichtbar:
  - input: [1]
    expected: 1
  - input: [12]
    expected: 6
  - input: [25]
    expected: 3
  - input: [0]
    expected: 0
starter_code: |
  function tau(n) {
      // Tipp: Schleife bis sqrt(n), Quadrat-Sonderfall
  }
---

# JavaScript -- Tau-Funktion

Schreibe `tau(n)`, die die **Anzahl der positiven Teiler** von `n`
liefert. Bei `n < 1` → `0`.

## Beispiele

| `n`  | Teiler                          | tau(n) |
|------|----------------------------------|--------|
| `1`  | `[1]`                            | `1`    |
| `2`  | `[1, 2]`                         | `2`    |
| `12` | `[1, 2, 3, 4, 6, 12]`            | `6`    |
| `25` | `[1, 5, 25]` (Quadrat!)          | `3`    |
| `97` | `[1, 97]` (Primzahl)             | `2`    |

## Idee

Pro Teiler `i` bekommt man `n / i` als Partner -- `+= 2`. Bei
Quadratzahlen (`i² = n`) sind beide Teiler gleich, also `+= 1`.

## Vergleich

Pythons `//` und JavaScripts `Math.floor` haben den gleichen
Effekt, aber wir brauchen hier nur Modulo (`%`) -- der Vergleich
`i * i === n` ist exakt fuer ganze Zahlen.
