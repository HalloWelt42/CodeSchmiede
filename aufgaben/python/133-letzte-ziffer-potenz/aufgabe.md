---
schema_version: 1
id: 133-letzte-ziffer-potenz
revision: 1
titel: Letzte Ziffer von a hoch b
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, modulo, potenz, optimierung]
pfade: [python_mathe2]
voraussetzungen: [021-potenz]
quelle:
  url: null
  notiz: Klassische Modular-Arithmetik-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: letzte_ziffer
hints:
  - kosten: 0
    text: |
      Letzte Ziffer von a^b ist (a^b) % 10. Aber a^b kann riesig werden!
      Trick: Modular-Exponentiation -- pow(a, b, 10).
  - kosten: 15
    text: |
      Sonderfall b=0: Ergebnis ist 1, also letzte Ziffer 1.
      Pythons `pow(a, b, mod)` macht das in O(log b).
tests_sichtbar:
  - input: [3, 5]
    expected: 3
  - input: [2, 10]
    expected: 4
  - input: [7, 100]
    expected: 1
  - input: [1, 1000000]
    expected: 1
tests_versteckt:
  - input: [0, 5]
    expected: 0
  - input: [5, 0]
    expected: 1
  - input: [10, 1]
    expected: 0
  - input: [9, 9]
    expected: 9
  - input: [999, 999]
    expected: 9
  - input: [123, 4567]
    expected: 7
starter_code: |
  def letzte_ziffer(a: int, b: int) -> int:
      # Deine Lösung hier -- letzte Ziffer von a^b. Schnell mit pow(a, b, 10).
      pass
---

# Letzte Ziffer von a hoch b

Schreibe eine Funktion `letzte_ziffer(a, b)`, die die **letzte Ziffer**
von $a^b$ zurückgibt -- ohne $a^b$ selbst zu berechnen.

## Warum nicht einfach `(a**b) % 10`?

Bei `a = 999, b = 999` wäre $a^b$ eine Zahl mit über 2997 Stellen.
Mit `pow(a, b, 10)` rechnet Python das **modular** -- also nur die
Reste behaltend. $O(\log b)$ statt $O(b)$.

## Beispiele

| `a` | `b` | Letzte Ziffer | Wegen      |
|-----|-----|---------------|------------|
| `3` | `5` | `3`           | 3^5 = 243  |
| `2` | `10`| `4`           | 1024       |
| `7` | `100`| `1`          | endet auf 1|
| `5` | `0` | `1`           | a^0 = 1    |
| `0` | `5` | `0`           | 0^5 = 0    |
| `999`|`999`|`9`          |            |

## Hintergrund

Modulare Exponentiation ist das **Herzstück** von RSA und vielen
Krypto-Verfahren. Der Trick: bei jedem Quadrieren / Multiplizieren
gleich modulo nehmen, dann werden die Zwischenwerte nie größer
als der Modul.
