---
schema_version: 1
id: 329-fizzbuzz-liste
revision: 1
titel: FizzBuzz als Liste 1 bis n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [zahlen, listen, klassiker, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/FizzBuzz
  notiz: Rosetta Code -- FizzBuzz, Sammelvariante
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: fizzbuzz_liste
hints:
  - kosten: 0
    text: |
      Liefere FizzBuzz fuer alle Zahlen von 1 bis n als Liste von
      Strings. Regeln wie Klassiker:
      - durch 3 und 5: "FizzBuzz"
      - nur durch 3: "Fizz"
      - nur durch 5: "Buzz"
      - sonst: Zahl als String
      n <= 0 -> [].
  - kosten: 10
    text: |
      Listen-Comprehension. Pro i pruefen, am elegantesten ist
      "Fizz" * (i%3==0) + "Buzz" * (i%5==0) or str(i).
tests_sichtbar:
  - input: [5]
    expected: ["1", "2", "Fizz", "4", "Buzz"]
  - input: [0]
    expected: []
  - input: [3]
    expected: ["1", "2", "Fizz"]
  - input: [15]
    expected: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
tests_versteckt:
  - input: [1]
    expected: ["1"]
  - input: [-3]
    expected: []
  - input: [6]
    expected: ["1", "2", "Fizz", "4", "Buzz", "Fizz"]
  - input: [10]
    expected: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
  - input: [30]
    expected: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz", "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz"]
starter_code: |
  def fizzbuzz_liste(n: int) -> list[str]:
      # Tipp: Comprehension oder klassische Schleife
      pass
---

# FizzBuzz als Liste 1 bis n

Sammelvariante des FizzBuzz-Klassikers (Aufgabe 001 liefert nur
einen Wert): liefere die FizzBuzz-Strings fuer **alle Zahlen
von 1 bis n** als Liste.

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
| `15`| `[..., "FizzBuzz"]` (15 ist erste FizzBuzz)             |
| `1` | `["1"]`                                                 |
| `0` | `[]`                                                    |

## Idee 1 -- klassisch

```python
def fizzbuzz_liste(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out
```

## Idee 2 -- elegant mit String-Multiplikation

```python
def fizzbuzz_liste(n):
    return [
        ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i)
        for i in range(1, n + 1)
    ]
```

Pythonismus: `"Fizz" * True` ist `"Fizz"`, `"Fizz" * False` ist
`""`. `"" or str(i)` liefert die Zahl, sobald keine Regel greift.

## Vergleich mit Aufgabe 001

**001-fizzbuzz**: `fizzbuzz(n)` → einzelner String fuer eine Zahl.
**329 hier**: `fizzbuzz_liste(n)` → Liste fuer 1..n.

In der Praxis ist die Listen-Variante haeufiger -- man will meist
den ganzen Lauf, nicht einzelne Werte.
