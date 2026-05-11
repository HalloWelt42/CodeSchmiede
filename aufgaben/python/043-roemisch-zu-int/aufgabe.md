---
schema_version: 1
id: 043-roemisch-zu-int
revision: 1
titel: Römisch zu Integer
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [strings, dict, roemisch, schleifen]
pfade: [python_mathe2]
voraussetzungen: [022-wortzaehler]
quelle:
  url: https://de.wikipedia.org/wiki/R%C3%B6mische_Zahlen
  notiz: Klassische LeetCode/HackerRank-Aufgabe in eigener Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: roemisch_zu_int
hints:
  - kosten: 0
    text: |
      Werte: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
      Wenn ein Zeichen kleiner ist als das nächste, wird es subtrahiert,
      sonst addiert.
  - kosten: 15
    text: |
      Schleife durch jedes Zeichen, dabei Wert in einem Dict
      nachschlagen. Vergleiche mit Nachfolger.
tests_sichtbar:
  - input: ["III"]
    expected: 3
  - input: ["IV"]
    expected: 4
  - input: ["MCMXCIV"]
    expected: 1994
  - input: ["LVIII"]
    expected: 58
tests_versteckt:
  - input: ["I"]
    expected: 1
  - input: ["MMMCMXCIX"]
    expected: 3999
  - input: ["XL"]
    expected: 40
  - input: ["XC"]
    expected: 90
  - input: ["CD"]
    expected: 400
  - input: ["CM"]
    expected: 900
  - input: [""]
    expected: 0
starter_code: |
  def roemisch_zu_int(s: str) -> int:
      # Deine Lösung hier -- I=1, V=5, X=10, L=50, C=100, D=500, M=1000
      pass
---

# Römisch zu Integer

Schreibe eine Funktion `römisch_zu_int(s)`, die eine römische Zahl
in eine Dezimalzahl umwandelt.

| Zeichen | Wert |
|---------|------|
| `I`     | 1    |
| `V`     | 5    |
| `X`     | 10   |
| `L`     | 50   |
| `C`     | 100  |
| `D`     | 500  |
| `M`     | 1000 |

## Subtraktionsregel

Steht ein kleineres Zeichen vor einem größeren, wird es **abgezogen**:

- `IV` = `5 - 1` = `4`
- `IX` = `10 - 1` = `9`
- `XL` = `50 - 10` = `40`
- `XC` = `100 - 10` = `90`
- `CD` = `500 - 100` = `400`
- `CM` = `1000 - 100` = `900`

## Beispiele

| Eingabe       | Ergebnis |
|---------------|----------|
| `"III"`       | `3`      |
| `"IV"`        | `4`      |
| `"LVIII"`     | `58`     |
| `"MCMXCIV"`   | `1994`   |
| `"MMMCMXCIX"` | `3999`   |
| `""`          | `0`      |

## Idee

Vergleiche jedes Zeichen mit seinem **Nachfolger**: ist der Nachfolger
größer, ziehe ab; sonst addiere.
