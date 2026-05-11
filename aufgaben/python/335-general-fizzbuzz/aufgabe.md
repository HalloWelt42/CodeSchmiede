---
schema_version: 1
id: 335-general-fizzbuzz
revision: 1
titel: Verallgemeinertes FizzBuzz
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [zahlen, listen, dicts, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/General_FizzBuzz
  notiz: Rosetta Code -- General FizzBuzz
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: general_fizzbuzz
hints:
  - kosten: 0
    text: |
      Wie FizzBuzz, aber konfigurierbar: regeln ist eine Liste von
      [teiler, wort]-Paaren. Pro Zahl 1..n: alle Woerter konkatenieren,
      deren Teiler aufgehen. Sonst die Zahl als String.
      Klassisches FizzBuzz: regeln = [[3,"Fizz"],[5,"Buzz"]].
  - kosten: 15
    text: |
      Fuer jedes i: ''.join(wort fuer (teiler, wort) in regeln if i % teiler == 0)
      or str(i)
tests_sichtbar:
  - input: [5, [[3, "Fizz"], [5, "Buzz"]]]
    expected: ["1", "2", "Fizz", "4", "Buzz"]
  - input: [3, []]
    expected: ["1", "2", "3"]
  - input: [0, [[3, "Fizz"]]]
    expected: []
  - input: [3, [[3, "Fizz"]]]
    expected: ["1", "2", "Fizz"]
tests_versteckt:
  - input: [15, [[3, "Fizz"], [5, "Buzz"]]]
    expected: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
  - input: [10, [[2, "Bing"]]]
    expected: ["1", "Bing", "3", "Bing", "5", "Bing", "7", "Bing", "9", "Bing"]
  - input: [6, [[2, "Hi"], [3, "Ho"]]]
    expected: ["1", "Hi", "Ho", "Hi", "5", "HiHo"]
  - input: [4, [[2, "A"], [3, "B"], [4, "C"]]]
    expected: ["1", "A", "B", "AC"]
  - input: [1, [[1, "X"]]]
    expected: ["X"]
  - input: [-3, [[3, "Fizz"]]]
    expected: []
starter_code: |
  def general_fizzbuzz(n: int, regeln: list[list]) -> list[str]:
      # Tipp: pro Zahl alle passenden Woerter konkatenieren
      pass
---

# Verallgemeinertes FizzBuzz

Schreibe `general_fizzbuzz(n, regeln)`, die FizzBuzz **konfigurierbar**
spielt: statt fest `3 -> Fizz, 5 -> Buzz` wird eine Liste von
`[teiler, wort]`-Paaren uebergeben.

Pro Zahl `i` von 1 bis n:
1. Sammle alle Woerter, deren Teiler `i` teilt -- konkateniere sie.
2. Wenn nichts zusammenkommt, nimm `str(i)`.

`n <= 0` oder leere Regelliste behandeln wie folgt:
- `n <= 0` -> `[]`
- leere Regeln -> nur Zahlen `["1", "2", ..., "n"]`

## Beispiele

| `n` | Regeln                            | Ergebnis                          |
|-----|------------------------------------|------------------------------------|
| `5` | `[[3,"Fizz"],[5,"Buzz"]]`         | `["1","2","Fizz","4","Buzz"]`     |
| `15`| `[[3,"Fizz"],[5,"Buzz"]]`         | `[..., "FizzBuzz"]`               |
| `6` | `[[2,"Hi"],[3,"Ho"]]`             | `["1","Hi","Ho","Hi","5","HiHo"]` |
| `4` | `[[2,"A"],[3,"B"],[4,"C"]]`       | `["1","A","B","AC"]`              |
| `3` | `[]`                               | `["1","2","3"]`                   |

## Idee

Generator-Ausdruck `(w for ...)` baut den Wort-Strom. `"".join`
konkateniert. `or str(i)` greift wenn das ergebnis leer ist
(falsy).

## Hintergrund

Klassisches **FizzBuzz** (Aufgabe 001) hat fest `3 -> Fizz, 5 -> Buzz`.
Diese Verallgemeinerung erlaubt:

- **PrimePower**: `[[2,"Bi"],[3,"Tri"],[5,"Quint"]]`
- **Schach**: `[[3,"Hopp"],[5,"Sprung"]]`
- **Spass**: `[[7,"Boom"],[11,"Bang"],[13,"Buzz"]]`

Wer den klassischen FizzBuzz beherrscht, kann das hier in 5 Minuten.
Macht es zur **soliden Erweiterungsaufgabe**.
