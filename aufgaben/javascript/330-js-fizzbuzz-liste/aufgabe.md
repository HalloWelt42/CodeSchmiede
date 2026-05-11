---
schema_version: 1
id: 330-js-fizzbuzz-liste
revision: 1
titel: JavaScript -- FizzBuzz als Liste
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [javascript, array, klassiker, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/FizzBuzz
  notiz: Rosetta Code -- FizzBuzz, JS-Sammelvariante
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: fizzbuzzListe
hints:
  - kosten: 0
    text: |
      Liefere ein Array mit FizzBuzz-Strings fuer die Zahlen 1..n.
      Regeln wie Klassiker (3->Fizz, 5->Buzz, 15->FizzBuzz).
      n <= 0 -> [].
  - kosten: 7
    text: |
      Array.from({length: n}, (_, i) => ...) ist die moderne Form.
      Index ist 0-basiert, also i+1 verwenden.
tests_sichtbar:
  - input: [5]
    expected: ["1", "2", "Fizz", "4", "Buzz"]
  - input: [0]
    expected: []
  - input: [3]
    expected: ["1", "2", "Fizz"]
  - input: [15]
    expected: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
starter_code: |
  function fizzbuzzListe(n) {
      // Tipp: Array.from({length: n}, (_, i) => ...)
  }
---

# JavaScript -- FizzBuzz als Liste

Schreibe `fizzbuzzListe(n)`, die FizzBuzz fuer die Zahlen `1..n`
als Array liefert.

Regeln:
- durch **3 und 5** → `"FizzBuzz"`
- nur durch **3** → `"Fizz"`
- nur durch **5** → `"Buzz"`
- sonst → die Zahl als String

`n <= 0` → `[]`.

## Beispiele

| `n` | Ergebnis                                                |
|-----|---------------------------------------------------------|
| `5` | `["1", "2", "Fizz", "4", "Buzz"]`                       |
| `15`| `["1", ..., "FizzBuzz"]`                                |
| `0` | `[]`                                                    |

## Idee -- modernes JS

`Array.from({ length: n }, fn)` ist das **moderne Pattern** zum
Erzeugen eines Arrays mit n Elementen, ohne `new Array(n).fill()`-
Trick.

## Idee -- ternaer (kompakt)

Schoener Pythonismus: leerer String ist falsy, also greift `||`.

## Vergleich mit Python

| Sprache    | Pattern                                |
|------------|-----------------------------------------|
| Python     | `[... for i in range(1, n+1)]`         |
| JavaScript | `Array.from({length: n}, (_, i) => ...)`|

JS hat kein direktes `range(n)`. Mit Spread + Keys:
`[...Array(n).keys()].map(...)` -- aber `Array.from` ist klarer.
