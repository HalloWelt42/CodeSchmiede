---
schema_version: 1
id: 135-fakultaet-stellen
revision: 1
titel: Anzahl Stellen von n!
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [zahlen, fakultaet, mathematik, log]
pfade: [python_mathe2]
voraussetzungen: [017-fakultaet]
quelle:
  url: null
  notiz: Klassische Aufgabe -- 100! hat 158 Stellen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: stellen_von_fakultaet
hints:
  - kosten: 0
    text: |
      n! direkt berechnen, dann len(str(n!)). Bei n < 0 → 0.
      0! = 1 → 1 Stelle.
  - kosten: 10
    text: |
      Pythons `math.factorial` macht es. Oder eigene Schleife.
      `len(str(...))` zählt die Stellen.
tests_sichtbar:
  - input: [0]
    expected: 1
  - input: [1]
    expected: 1
  - input: [10]
    expected: 7
  - input: [100]
    expected: 158
tests_versteckt:
  - input: [-5]
    expected: 0
  - input: [5]
    expected: 3
  - input: [20]
    expected: 19
  - input: [50]
    expected: 65
  - input: [200]
    expected: 375
  - input: [1000]
    expected: 2568
starter_code: |
  def stellen_von_fakultaet(n: int) -> int:
      # Deine Lösung hier -- Anzahl Dezimalstellen von n!. Bei n<0 → 0.
      pass
---

# Anzahl Stellen von n!

Schreibe eine Funktion `stellen_von_fakultaet(n)`, die zählt,
wie viele **Dezimalstellen** $n!$ hat.

Bei `n < 0` → `0`. `0!` = `1` → `1` Stelle.

## Beispiele

| `n`  | $n!$                                                    | Stellen |
|------|---------------------------------------------------------|---------|
| `0`  | `1`                                                     | `1`     |
| `5`  | `120`                                                   | `3`     |
| `10` | `3628800`                                               | `7`     |
| `20` | `2432902008176640000`                                   | `19`    |
| `100`| (158-stellige Zahl)                                     | `158`   |
| `1000`| (2568-stellige Zahl)                                   | `2568`  |

## Idee

Pythons `math.factorial(n)` rechnet `n!`. `len(str(n_fak))` zählt
die Stellen.

## Hintergrund

Es gibt eine schöne Formel von **Stirling**: $\log_{10}(n!) \approx n \log_{10}(n/e)$.
Damit kann man die Stellenzahl in O(1) abschätzen, ohne $n!$ zu berechnen.
Hier nehmen wir aber die ehrliche Variante.
