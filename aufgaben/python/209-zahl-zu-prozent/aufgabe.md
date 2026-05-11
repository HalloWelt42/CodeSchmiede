---
schema_version: 1
id: 209-zahl-zu-prozent
revision: 1
titel: Zahl in Prozent-String
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [zahlen, strings, formatierung, prozent]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Format-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zu_prozent
hints:
  - kosten: 0
    text: |
      Wandle eine Bruchzahl in einen Prozent-String:
      0.5 -> "50.00%". 1 -> "100.00%". 0 -> "0.00%".
      Genau 2 Nachkommastellen.
  - kosten: 10
    text: |
      f"{anteil * 100:.2f}%".
      Format-Specifier .2f rundet auf 2 Nachkommastellen.
tests_sichtbar:
  - input: [0.5]
    expected: "50.00%"
  - input: [1]
    expected: "100.00%"
  - input: [0]
    expected: "0.00%"
  - input: [0.1234]
    expected: "12.34%"
tests_versteckt:
  - input: [0.001]
    expected: "0.10%"
  - input: [-0.5]
    expected: "-50.00%"
  - input: [1.5]
    expected: "150.00%"
  - input: [0.999]
    expected: "99.90%"
  - input: [0.6666666]
    expected: "66.67%"
  - input: [2]
    expected: "200.00%"
starter_code: |
  def zu_prozent(anteil: float) -> str:
      # Deine Lösung hier -- "XX.YY%" mit 2 Nachkommastellen
      pass
---

# Zahl in Prozent-String

Schreibe `zu_prozent(anteil)`, die eine Bruchzahl (`0.5` = 50 %)
in einen formatierten **Prozent-String** umwandelt -- mit genau
**zwei Nachkommastellen** und einem `%`-Zeichen am Ende.

## Beispiele

| Eingabe      | Ausgabe       |
|--------------|---------------|
| `0`          | `"0.00%"`     |
| `0.5`        | `"50.00%"`    |
| `1`          | `"100.00%"`   |
| `0.1234`     | `"12.34%"`    |
| `0.001`      | `"0.10%"`     |
| `-0.5`       | `"-50.00%"`   |
| `1.5`        | `"150.00%"`   |
| `0.6666666`  | `"66.67%"`    |

## Idee

```python
def zu_prozent(anteil):
    return f"{anteil * 100:.2f}%"
```

`:.2f` rundet auf zwei Nachkommastellen -- mathematisches Runden
("banker's rounding" in CPython, abweichend bei `.5`-Werten).

## Pendant -- Prozent zurück zur Zahl

Aufgabe **210** macht den Weg zurück: `"50%"` → `0.5`. Damit hat
man ein **Round-Trip-Paar**.

## Format-String-Specifier (Mini-Cheat)

| Specifier | Bedeutung                            |
|-----------|---------------------------------------|
| `:.2f`    | 2 Nachkommastellen, Float            |
| `:5d`     | Integer, mind. 5 Stellen breit       |
| `:>10`    | rechtsbuendig in 10 Stellen          |
| `:_`      | Tausender-Trenner als Unterstrich    |
| `:%`      | wie `:.6f` plus `%` und `*100`       |

`f"{0.5:%}"` wäre `"50.000000%"` -- `:.2%` wäre kürzer als unsere
Lösung, aber nicht so explizit.
