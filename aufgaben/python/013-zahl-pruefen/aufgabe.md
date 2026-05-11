---
schema_version: 1
id: 013-zahl-pruefen
revision: 1
titel: Primzahl-Prüfung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 32
schaetz_minuten: 12
tags: [mathematik, schleifen, modulo, primzahlen]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: https://de.wikipedia.org/wiki/Primzahl
  notiz: Klassiker zum Üben von Schleifen und Effizienz
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_primzahl
hints:
  - kosten: 0
    text: Eine Primzahl ist nur durch 1 und sich selbst ohne Rest teilbar.
  - kosten: 7
    text: |
      Prüfe alle Zahlen von 2 bis n-1 -- wenn eine davon `n` teilt,
      ist es keine Primzahl. Vorsicht mit den Sonderfällen `n < 2`.
  - kosten: 15
    text: |
      Schneller: nur bis $\sqrt{n}$ prüfen reicht.

      ```
      from math import isqrt
      if n < 2: return False
      for t in range(2, isqrt(n) + 1):
          if n % t == 0: return False
      return True
      ```
tests_sichtbar:
  - input: [2]
    expected: true
  - input: [4]
    expected: false
  - input: [7]
    expected: true
  - input: [1]
    expected: false
  - input: [0]
    expected: false
tests_versteckt:
  - input: [13]
    expected: true
  - input: [25]
    expected: false
  - input: [97]
    expected: true
  - input: [100]
    expected: false
  - input: [-7]
    expected: false
  - input: [997]
    expected: true
  - input: [1000]
    expected: false
starter_code: |
  def ist_primzahl(n: int) -> bool:
      # Deine Lösung hier
      pass
---

# Primzahl-Prüfung

Schreibe eine Funktion `ist_primzahl(n)`, die `True` zurückgibt, wenn
`n` eine **Primzahl** ist -- also nur durch 1 und sich selbst ohne Rest
teilbar -- und sonst `False`.

## Beispiele

| n   | Ergebnis |
|----:|----------|
| 2   | `True`   |
| 7   | `True`   |
| 4   | `False`  |
| 1   | `False`  |
| 0   | `False`  |
| -7  | `False`  |

## Hinweise

- **Sonderfälle:** `0`, `1` und alle negativen Zahlen sind **keine**
  Primzahlen.
- `2` ist die kleinste Primzahl (und die einzige gerade Primzahl).
- Du brauchst nur bis $\sqrt{n}$ zu prüfen -- jeder Teiler über
  $\sqrt{n}$ hat einen Partner darunter.

## Hintergrund

Die Primzahlen sind die Bausteine der natürlichen Zahlen. Jede
natürliche Zahl > 1 lässt sich auf genau eine Weise als Produkt von
Primzahlen schreiben (Fundamentalsatz der Arithmetik).
