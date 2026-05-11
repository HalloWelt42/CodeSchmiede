---
schema_version: 1
id: 042-armstrong
revision: 1
titel: Armstrong-Zahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, ziffern, potenz]
pfade: [python_mathe2]
voraussetzungen: [016-quersumme, 021-potenz]
quelle:
  url: https://de.wikipedia.org/wiki/Narzisstische_Zahl
  notiz: Klassische Aufgabe -- auch "narzisstische Zahl" genannt.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_armstrong
hints:
  - kosten: 0
    text: |
      Bei einer 3-stelligen Armstrong-Zahl ist die Summe der dritten
      Potenzen ihrer Ziffern gleich der Zahl selbst. Bei 4-stelligen
      die vierten Potenzen, usw.
  - kosten: 15
    text: |
      `s = str(n)`, `k = len(s)`. Dann prüfe
      `sum(int(c)**k for c in s) == n`.
tests_sichtbar:
  - input: [153]
    expected: true
  - input: [9]
    expected: true
  - input: [10]
    expected: false
  - input: [371]
    expected: true
tests_versteckt:
  - input: [0]
    expected: true
  - input: [1]
    expected: true
  - input: [407]
    expected: true
  - input: [8208]
    expected: true
  - input: [9474]
    expected: true
  - input: [9475]
    expected: false
  - input: [123]
    expected: false
starter_code: |
  def ist_armstrong(n: int) -> bool:
      # Deine Lösung hier
      pass
---

# Armstrong-Zahl

Eine **Armstrong-Zahl** (auch *narzisstische Zahl*) ist eine Zahl,
die gleich der Summe ihrer Ziffern hoch der Anzahl ihrer Ziffern ist.

## Beispiele

| `n`     | Stellen | Rechnung                  | Armstrong?  |
|---------|---------|---------------------------|-------------|
| `153`   | 3       | $1^3 + 5^3 + 3^3 = 153$   | `True`      |
| `9474`  | 4       | $9^4 + 4^4 + 7^4 + 4^4 = 9474$ | `True` |
| `9`     | 1       | $9^1 = 9$                 | `True`      |
| `10`    | 2       | $1^2 + 0^2 = 1 \ne 10$    | `False`     |

## Hinweis

Alle einstelligen Zahlen (`0` bis `9`) sind Armstrong-Zahlen --
für `n = 1` ist die Bedingung `n^1 = n` trivial erfüllt.

## Hintergrund

Es gibt nur **89** Armstrong-Zahlen im Dezimalsystem, die größte
hat 39 Stellen. Nach 5-stelligen Armstrongs gibt es eine ganze Weile
keine, das macht das Suchen interessant.
