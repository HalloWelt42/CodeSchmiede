---
schema_version: 1
id: 334-js-string-zahl-inkrement
revision: 1
titel: JavaScript -- Numerischen String inkrementieren
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [javascript, strings, zahlen, bigint, modern]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Increment_a_numerical_string
  notiz: Rosetta Code -- Increment a numerical string, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: inkrement
hints:
  - kosten: 0
    text: |
      Erhöhe einen numerischen String um 1. Sehr lange Zahlen
      müssen funktionieren -- nutze BigInt!
      "499" -> "500", "999999999999999999" -> "1000000000000000000".
      Ungültige Eingabe -> "".
  - kosten: 8
    text: |
      try { return (BigInt(s) + 1n).toString(); } catch { return ""; }
tests_sichtbar:
  - input: ["499"]
    expected: "500"
  - input: ["0"]
    expected: "1"
  - input: ["-1"]
    expected: "0"
  - input: ["abc"]
    expected: ""
starter_code: |
  function inkrement(s) {
      // Tipp: BigInt fuer beliebig grosse Zahlen
  }
---

# JavaScript -- Numerischen String inkrementieren

Schreibe `inkrement(s)`, die einen numerischen String um `1`
erhoeht.

**Wichtig**: Sehr lange Zahlen (jenseits Number.MAX_SAFE_INTEGER)
müssen funktionieren -- daher **BigInt** nutzen.

Ungültige Eingabe -> `""`.

## Beispiele

| Eingabe              | Ergebnis              |
|----------------------|------------------------|
| `"499"`              | `"500"`                |
| `"0"`                | `"1"`                  |
| `"-1"`               | `"0"`                  |
| `"9999"`             | `"10000"`              |
| `"999999999999999999"`| `"1000000000000000000"` |
| `"abc"`              | `""`                   |
| `"12.5"`             | `""`                   |

## Idee mit BigInt

`BigInt(s)` parst beliebig große ganze Zahlen. `1n` ist eine
BigInt-Literal-Konstante. `.toString()` macht wieder String draus
(ohne `n`-Suffix).

## Warum nicht parseInt + 1?

Number in JavaScript ist `float64` -- praezise nur bis
`2^53 - 1 = 9007199254740991`. Daruber gehen Werte verloren:

BigInt löst das Problem -- erfordert aber explizite Konvertierung
und das `n`-Suffix.

## Vergleich mit Python

Python hat **immer** unbegrenzte ints. In JS musste man bis ES2020
auf String-basierte Big-Number-Bibliotheken zurückgreifen.
