---
schema_version: 1
id: 336-js-general-fizzbuzz
revision: 1
titel: JavaScript -- Verallgemeinertes FizzBuzz
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [javascript, array, modulo, modern]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/General_FizzBuzz
  notiz: Rosetta Code -- General FizzBuzz, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: generalFizzbuzz
hints:
  - kosten: 0
    text: |
      Konfigurierbares FizzBuzz: regeln ist Array von [teiler, wort].
      Pro Zahl: Wörter passender Teiler joinen, sonst Zahl als String.
      n <= 0 -> []. Leere Regeln -> nur Zahlen.
  - kosten: 15
    text: |
      Array.from({length: n}, (_, i) => regeln.filter(...).map(...).join('') || ...)
tests_sichtbar:
  - input: [5, [[3, "Fizz"], [5, "Buzz"]]]
    expected: ["1", "2", "Fizz", "4", "Buzz"]
  - input: [3, []]
    expected: ["1", "2", "3"]
  - input: [0, [[3, "Fizz"]]]
    expected: []
  - input: [3, [[3, "Fizz"]]]
    expected: ["1", "2", "Fizz"]
starter_code: |
  function generalFizzbuzz(n, regeln) {
      // Tipp: Array.from + filter + map + join + ||
  }
---

# JavaScript -- Verallgemeinertes FizzBuzz

Schreibe `generalFizzbuzz(n, regeln)`, die FizzBuzz konfigurierbar
spielt -- mit beliebigen `[teiler, wort]`-Paaren.

Pro Zahl 1..n: alle passenden Wörter konkatenieren, sonst Zahl
als String.

`n <= 0` -> `[]`, leere Regeln -> nur Zahlen.

## Beispiele

| `n` | Regeln                          | Ergebnis                         |
|-----|----------------------------------|----------------------------------|
| `5` | `[[3,"Fizz"],[5,"Buzz"]]`       | `["1","2","Fizz","4","Buzz"]`    |
| `6` | `[[2,"Hi"],[3,"Ho"]]`           | `["1","Hi","Ho","Hi","5","HiHo"]`|
| `3` | `[]`                             | `["1","2","3"]`                  |

## Idee -- modernes JS

Schönheit: **Destructuring** `([t]) => ...` zieht das erste
Element des Tupels raus, `[, w]` überspringt das erste und nimmt
das zweite.

## Vergleich -- direkter Loop

Genauso korrekt, weniger funktional aber besser bei Performance-
kritischem Code (kein Closure pro Iteration).

## Anwendung

Konfigurierbares FizzBuzz steckt in **Cron-Jobs**, **Pattern-
Matching** und überall wo "wenn X, dann Wort A; wenn Y, dann
Wort B" zusammengesetzt werden soll.
