---
schema_version: 1
id: 001-fizzbuzz
revision: 1
titel: FizzBuzz
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 10
tags: [if-else, modulo, schleifen, klassiker]
pfade: [python_grundlagen]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Fizz_buzz
  notiz: Klassischer Programmier-Klassiker, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: fizzbuzz
hints:
  - kosten: 0
    text: Der Modulo-Operator `%` liefert den Rest einer ganzzahligen Division. `15 % 3` ergibt `0`.
  - kosten: 10
    text: Pruefe zuerst die Bedingung fuer "FizzBuzz" (teilbar durch 15), danach die einzelnen Bedingungen fuer 3 und 5.
  - kosten: 25
    text: |
      Geruest:

      ```
      if n % 15 == 0: return "FizzBuzz"
      if n % 3 == 0: return "Fizz"
      if n % 5 == 0: return "Buzz"
      return str(n)
      ```
tests_sichtbar:
  - input: [1]
    expected: "1"
  - input: [3]
    expected: "Fizz"
  - input: [5]
    expected: "Buzz"
  - input: [15]
    expected: "FizzBuzz"
tests_versteckt:
  - input: [99]
    expected: "Fizz"
  - input: [100]
    expected: "Buzz"
  - input: [45]
    expected: "FizzBuzz"
  - input: [7]
    expected: "7"
  - input: [30]
    expected: "FizzBuzz"
starter_code: |
  def fizzbuzz(n: int) -> str:
      # Deine Loesung hier
      pass
---

# FizzBuzz

Schreibe eine Funktion `fizzbuzz(n)`, die fuer eine positive Ganzzahl `n`
einen String zurueckgibt:

- `"FizzBuzz"` -- wenn `n` durch **3 und 5** teilbar ist
- `"Fizz"` -- wenn `n` nur durch **3** teilbar ist
- `"Buzz"` -- wenn `n` nur durch **5** teilbar ist
- die Zahl als String -- in allen anderen Faellen

## Beispiele

| Eingabe | Ausgabe    |
|--------:|------------|
|       1 | `"1"`      |
|       3 | `"Fizz"`   |
|       5 | `"Buzz"`   |
|      15 | `"FizzBuzz"` |
|       7 | `"7"`      |

## Hintergrund

FizzBuzz ist eine der bekanntesten Einsteiger-Aufgaben weltweit. Sie testet,
ob du Verzweigungen (`if`/`elif`/`else`) und den Modulo-Operator `%`
sinnvoll kombinieren kannst.

> Mathematisch:
>
> $$\text{fizzbuzz}(n) = \begin{cases} \text{FizzBuzz} & \text{wenn } n \bmod 15 = 0 \\ \text{Fizz} & \text{wenn } n \bmod 3 = 0 \\ \text{Buzz} & \text{wenn } n \bmod 5 = 0 \\ \text{str}(n) & \text{sonst} \end{cases}$$

## Worauf zu achten ist

- Pruefe `n % 15 == 0` **vor** `n % 3 == 0` und `n % 5 == 0`, sonst greift
  immer der `Fizz`-Fall fuer Vielfache von 15
- Gib die Zahl im Else-Fall als **String** zurueck, nicht als `int`
