---
schema_version: 1
id: 044-int-zu-roemisch
revision: 3
titel: Integer zu Römisch
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [zahlen, schleifen, roemisch, greedy]
voraussetzungen: [043-roemisch-zu-int]
quelle:
  url: https://de.wikipedia.org/wiki/R%C3%B6mische_Zahlen
  notiz: Die umgekehrte Richtung - klassische Greedy-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: int_zu_roemisch
hints:
  - kosten: 0
    text: |
      Gehe alle Werte vom größten zum kleinsten durch (inkl.
      Sonderfälle 900, 400, 90, 40, 9, 4) und ziehe so viele wie
      möglich vom n ab, füge das jeweilige Symbol hinzu.
  - kosten: 12
    text: |
      Liste von Tupeln `(wert, symbol)` absteigend, dann pro Tupel
      `n // wert` mal Symbol anhängen und `n %= wert`.
tests_sichtbar:
  - input: [3]
    expected: "III"
  - input: [4]
    expected: "IV"
  - input: [9]
    expected: "IX"
  - input: [1994]
    expected: "MCMXCIV"
tests_versteckt:
  - input: [1]
    expected: "I"
  - input: [3998]
    expected: "MMMCMXCVIII"
  - input: [42]
    expected: "XLII"
  - input: [67]
    expected: "LXVII"
  - input: [450]
    expected: "CDL"
  - input: [960]
    expected: "CMLX"
  - input: [2888]
    expected: "MMDCCCLXXXVIII"
starter_code: |
  def int_zu_roemisch(n: int) -> str:
      # Deine Lösung hier - Eingabe 1 bis 3999.
      pass
---

# Integer zu Römisch

Schreibe eine Funktion `int_zu_roemisch(n)`, die eine Dezimalzahl
zwischen `1` und `3999` als römische Zahl zurückgibt.

## Symbole + Sonderfälle

| Wert | Symbol |
|------|--------|
| 1000 | `M`    |
| 900  | `CM`   |
| 500  | `D`    |
| 400  | `CD`   |
| 100  | `C`    |
| 90   | `XC`   |
| 50   | `L`    |
| 40   | `XL`   |
| 10   | `X`    |
| 9    | `IX`   |
| 5    | `V`    |
| 4    | `IV`   |
| 1    | `I`    |

## Greedy

Gehe vom größten Wert nach unten. Solange `n >= wert`, hänge das
Symbol an und ziehe ab. So entsteht die kanonische Schreibweise.

## Beispiele

| `n`    | Römisch          |
|--------|-------------------|
| `3`    | `III`             |
| `4`    | `IV`              |
| `9`    | `IX`              |
| `58`   | `LVIII`           |
| `1994` | `MCMXCIV`         |
| `3999` | `MMMCMXCIX`       |
| `3888` | `MMMDCCCLXXXVIII` |

## Hintergrund

Die Römer selbst haben übrigens keinen klaren Standard für
Subtraktionsschreibweise gehabt - `IIII` neben `IV` war lange
üblich (Uhrenziffernblätter zeigen das oft heute noch).
