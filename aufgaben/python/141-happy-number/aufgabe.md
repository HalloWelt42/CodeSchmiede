---
schema_version: 1
id: 141-happy-number
revision: 1
titel: Glückliche Zahl (Happy Number)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 32
schaetz_minuten: 12
tags: [zahlen, zyklus, set, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Project-Euler-Klassiker / LeetCode 202
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: glueckszahl
hints:
  - kosten: 0
    text: |
      n -> Quadratsumme der Ziffern -> wiederholen.
      Endet bei 1 → True (glücklich).
      Endet im Zyklus (z.B. 4) → False.
  - kosten: 15
    text: |
      Set für schon gesehene Zahlen. Sobald n erneut auftaucht
      (und n != 1), ist es ein Zyklus → False.
tests_sichtbar:
  - input: [1]
    expected: true
  - input: [19]
    expected: true
  - input: [4]
    expected: false
  - input: [2]
    expected: false
tests_versteckt:
  - input: [7]
    expected: true
  - input: [10]
    expected: true
  - input: [13]
    expected: true
  - input: [20]
    expected: false
  - input: [100]
    expected: true
  - input: [99]
    expected: false
starter_code: |
  def glueckszahl(n: int) -> bool:
      # Deine Lösung hier -- Quadratsummen-Iteration mit Zyklus-Erkennung
      pass
---

# Glückliche Zahl (Happy Number)

Eine Zahl ist **glücklich**, wenn die wiederholte **Summe der Quadrate
ihrer Ziffern** schließlich bei `1` landet. Sonst gerät sie in einen
Zyklus, der nie `1` erreicht.

## Beispiele

`19` ist glücklich:

```
19  → 1² + 9² = 82
82  → 8² + 2² = 68
68  → 6² + 8² = 100
100 → 1² + 0² + 0² = 1   glücklich!
```

`4` ist nicht glücklich (Zyklus):

```
4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...
```

| `n`   | Ergebnis |
|-------|----------|
| `1`   | `True`   |
| `7`   | `True`   |
| `19`  | `True`   |
| `4`   | `False`  |
| `99`  | `False`  |

## Idee

Set für schon gesehene Zahlen. Solange weiter rechnen, bis entweder
`n == 1` (glücklich) oder `n` schon im Set steht (Zyklus).

## Hintergrund

Mathematisch interessant: alle nicht-glucklichen Zahlen landen im
selben Zyklus `4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4`. Das laesst
sich beweisen, indem man zeigt, dass die Quadratsumme jeder Zahl > 99
kleiner als die Zahl selbst ist (Schranken-Argument).
