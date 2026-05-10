---
schema_version: 1
id: 040-perfekte-zahl
revision: 1
titel: Perfekte Zahl prüfen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [zahlen, teiler, schleifen]
pfade: [python_mathe2]
voraussetzungen: [018-ggt]
quelle:
  url: https://de.wikipedia.org/wiki/Vollkommene_Zahl
  notiz: Klassische Zahlentheorie, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_perfekt
hints:
  - kosten: 0
    text: |
      Eine perfekte Zahl ist gleich der Summe ihrer echten Teiler --
      also aller Teiler ohne sich selbst.
  - kosten: 15
    text: |
      Schleife `i in range(1, n)` und alle `i` summieren, bei denen
      `n % i == 0`. Prüfe `summe == n` am Ende.
  - kosten: 25
    text: |
      Schneller: Teiler treten in Paaren auf. Bis `sqrt(n)` reicht.
tests_sichtbar:
  - input: [6]
    expected: true
  - input: [28]
    expected: true
  - input: [10]
    expected: false
  - input: [1]
    expected: false
tests_versteckt:
  - input: [496]
    expected: true
  - input: [8128]
    expected: true
  - input: [12]
    expected: false
  - input: [496]
    expected: true
  - input: [27]
    expected: false
  - input: [2]
    expected: false
starter_code: |
  def ist_perfekt(n: int) -> bool:
      # Deine Lösung hier
      pass
---

# Perfekte Zahl prüfen

Schreibe eine Funktion `ist_perfekt(n)`, die `True` zurueckgibt, wenn
`n` eine **vollkommene Zahl** (perfekte Zahl) ist -- also gleich der
Summe aller ihrer **echten Teiler** (Teiler ohne `n` selbst).

## Beispiele

| `n`    | Echte Teiler                     | Summe | Perfekt?  |
|--------|----------------------------------|-------|-----------|
| `6`    | `1, 2, 3`                        | `6`   | `True`    |
| `28`   | `1, 2, 4, 7, 14`                 | `28`  | `True`    |
| `10`   | `1, 2, 5`                        | `8`   | `False`   |
| `496`  | `1,2,4,8,16,31,62,124,248`       | `496` | `True`    |

## Hintergrund

Die ersten vier perfekten Zahlen sind **6, 28, 496, 8128**. Schon den
alten Griechen war klar, dass sie etwas Besonderes sind. Euklid bewies:
Wenn $2^p - 1$ eine Primzahl ist (eine "Mersenne-Primzahl"), dann
ist $2^{p-1} \cdot (2^p - 1)$ eine perfekte Zahl.

Bis heute (2026) sind nur **51 perfekte Zahlen** bekannt. Ob es
unendlich viele gibt: ungeloest. Ob es ungerade perfekte Zahlen gibt:
ebenfalls ungeloest. Eine erstaunlich rege Front in einer Frage, die
auf "summier mal die Teiler" zurueckgeht.
