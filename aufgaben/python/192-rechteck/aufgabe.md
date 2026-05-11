---
schema_version: 1
id: 192-rechteck
revision: 1
titel: Rechteck-Eigenschaften
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags: [mathematik, geometrie, runden]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Geometrie
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rechteck
hints:
  - kosten: 0
    text: |
      Liefere [flaeche, umfang, diagonale] eines Rechtecks mit
      Breite b und Höhe h. Diagonale via Pythagoras.
      Alle drei Werte auf 2 Nachkommastellen.
      b oder h <= 0 -> [0, 0, 0].
  - kosten: 10
    text: |
      flaeche = b * h
      umfang = 2 * (b + h)
      diagonale = sqrt(b**2 + h**2)
tests_sichtbar:
  - input: [3, 4]
    expected: [12.0, 14.0, 5.0]
  - input: [1, 1]
    expected: [1.0, 4.0, 1.41]
  - input: [0, 5]
    expected: [0, 0, 0]
  - input: [5, 5]
    expected: [25.0, 20.0, 7.07]
tests_versteckt:
  - input: [10, 10]
    expected: [100.0, 40.0, 14.14]
  - input: [6, 8]
    expected: [48.0, 28.0, 10.0]
  - input: [-3, 4]
    expected: [0, 0, 0]
  - input: [0.5, 0.5]
    expected: [0.25, 2.0, 0.71]
  - input: [100, 200]
    expected: [20000.0, 600.0, 223.61]
  - input: [12, 5]
    expected: [60.0, 34.0, 13.0]
starter_code: |
  import math

  def rechteck(b: float, h: float) -> list[float]:
      # Deine Lösung hier -- [flaeche, umfang, diagonale]
      pass
---

# Rechteck-Eigenschaften

Schreibe `rechteck(b, h)`, die für ein Rechteck der Breite `b`
und Höhe `h` drei Werte zurückgibt:

`[flaeche, umfang, diagonale]` -- alle auf **2 Nachkommastellen**.

Bei ungültigen Eingaben (`b <= 0` oder `h <= 0`) → `[0, 0, 0]`.

## Formeln

- Flaeche: $A = b \cdot h$
- Umfang:  $U = 2(b + h)$
- Diagonale: $d = \sqrt{b^2 + h^2}$ (**Pythagoras**)

## Beispiele

| `b`  | `h`  | Flaeche | Umfang | Diagonale |
|------|------|---------|--------|-----------|
| `3`  | `4`  | `12.0`  | `14.0` | `5.0`     |
| `1`  | `1`  | `1.0`   | `4.0`  | `1.41`    |
| `5`  | `5`  | `25.0`  | `20.0` | `7.07`    |
| `6`  | `8`  | `48.0`  | `28.0` | `10.0`    |
| `12` | `5`  | `60.0`  | `34.0` | `13.0`    |

Quadrate sind Sonderfaelle, bei denen $d = b \sqrt{2}$.

## Pythagoras-Klassiker

Die Tripel `(3, 4, 5)`, `(6, 8, 10)`, `(5, 12, 13)` erscheinen oft
in Schulaufgaben -- das sind sogenannte **pythagoraeische Tripel**
(siehe Aufgabe 084), bei denen die Diagonale **ganzzahlig** wird.
Geometrisch beruhigend, weil Wurzeln verschwinden.
