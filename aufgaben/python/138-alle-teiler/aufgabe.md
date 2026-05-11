---
schema_version: 1
id: 138-alle-teiler
revision: 1
titel: Alle Teiler einer Zahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, listen, sqrt, mathematik]
pfade: [python_mathe]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Teiler-Auflistung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: alle_teiler
hints:
  - kosten: 0
    text: |
      Liefere alle Teiler von n (inkl. 1 und n) in aufsteigender Reihenfolge.
      Bei n < 1 → []. Negative Eingaben behandelt wie ungültig.
  - kosten: 8
    text: |
      Effizient: Schleife nur bis sqrt(n). Pro Treffer i auch n//i
      einfuegen. Set verwenden gegen Doppelte (Quadratzahlen!).
tests_sichtbar:
  - input: [1]
    expected: [1]
  - input: [6]
    expected: [1, 2, 3, 6]
  - input: [12]
    expected: [1, 2, 3, 4, 6, 12]
  - input: [0]
    expected: []
tests_versteckt:
  - input: [-5]
    expected: []
  - input: [2]
    expected: [1, 2]
  - input: [25]
    expected: [1, 5, 25]
  - input: [36]
    expected: [1, 2, 3, 4, 6, 9, 12, 18, 36]
  - input: [100]
    expected: [1, 2, 4, 5, 10, 20, 25, 50, 100]
  - input: [97]
    expected: [1, 97]
starter_code: |
  def alle_teiler(n: int) -> list[int]:
      # Deine Lösung hier -- aufsteigend, inkl. 1 und n. n<1 → [].
      pass
---

# Alle Teiler einer Zahl

Schreibe eine Funktion `alle_teiler(n)`, die alle natürlichen Teiler
von `n` als **aufsteigend sortierte Liste** zurückgibt -- inklusive
`1` und `n` selbst.

Bei `n < 1` → `[]`.

## Beispiele

| `n`  | Teiler                              |
|------|-------------------------------------|
| `1`  | `[1]`                               |
| `6`  | `[1, 2, 3, 6]`                      |
| `12` | `[1, 2, 3, 4, 6, 12]`               |
| `25` | `[1, 5, 25]`                        |
| `36` | `[1, 2, 3, 4, 6, 9, 12, 18, 36]`    |
| `97` | `[1, 97]` (Primzahl)                |
| `0`  | `[]`                                |

## Idee

Schleife nur bis $\sqrt{n}$. Wenn `i` Teiler ist, ist `n // i` auch
einer (das **Partner-Teiler-Pattern**). Quadratzahlen wie 25 haben
einen Sonderfall: bei `i == n // i` nur einmal einfuegen.

## Hintergrund

Damit kann man prüfen, ob eine Zahl **vollkommen** ist (siehe 040-perfekte-zahl),
**überfluessig** (sum > 2n) oder **defizient** (sum < 2n) -- ein
Klassiker der Zahlentheorie.
