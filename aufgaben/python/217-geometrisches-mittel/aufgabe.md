---
schema_version: 1
id: 217-geometrisches-mittel
revision: 1
titel: Geometrisches Mittel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [statistik, mathematik, reduce, wurzel]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Statistik-Mittel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: geometrisches_mittel
hints:
  - kosten: 0
    text: |
      G = (x1 * x2 * ... * xn) ^ (1/n).
      Auf 4 Nachkommastellen gerundet.
      Bei leerer Liste → 0.0. Bei einer Null in der Liste → 0.0.
      Bei negativen Zahlen → 0.0 (nicht definiert in der reellen Welt).
  - kosten: 8
    text: |
      Prüfe vorher: alle > 0. Dann Produkt mit math.prod und ^ (1/n).
tests_sichtbar:
  - input: [[1, 2, 4]]
    expected: 2.0
  - input: [[2, 8]]
    expected: 4.0
  - input: [[]]
    expected: 0.0
  - input: [[5]]
    expected: 5.0
tests_versteckt:
  - input: [[1, 1, 1]]
    expected: 1.0
  - input: [[2, 4, 8]]
    expected: 4.0
  - input: [[3, 12, 48]]
    expected: 12.0
  - input: [[1, 2, 3, 4, 5]]
    expected: 2.6052
  - input: [[10, 100, 1000]]
    expected: 100.0
  - input: [[1, 0, 5]]
    expected: 0.0
  - input: [[-1, 2, 3]]
    expected: 0.0
starter_code: |
  import math

  def geometrisches_mittel(zahlen: list[float]) -> float:
      # Deine Lösung hier -- alle > 0 noetig, sonst 0.0
      pass
---

# Geometrisches Mittel

Schreibe `geometrisches_mittel(zahlen)`, das **geometrische Mittel**
einer Liste von Zahlen:

$$G = \sqrt[n]{x_1 \cdot x_2 \cdot \ldots \cdot x_n}$$

Auf **4 Nachkommastellen** gerundet. Bei leerer Liste → `0.0`.
Bei einer Null oder einer negativen Zahl → `0.0` (nicht definiert
in den reellen Zahlen).

## Beispiele

| Liste              | G       | Bemerkung                |
|--------------------|---------|---------------------------|
| `[2, 8]`           | `4.0`   | $\sqrt{16} = 4$           |
| `[1, 2, 4]`        | `2.0`   | $\sqrt[3]{8} = 2$         |
| `[3, 12, 48]`      | `12.0`  | konstanter Faktor 4       |
| `[10, 100, 1000]`  | `100.0` | Zehnerpotenzen            |
| `[1, 0, 5]`        | `0.0`   | Null vorhanden            |
| `[-1, 2, 3]`       | `0.0`   | Negativ                   |

## Geometrisches vs. arithmetisches Mittel

Bei `[1, 100]`:
- **Arithmetisch**: `50.5` (klassischer Durchschnitt).
- **Geometrisch**: `10.0` ($\sqrt{100}$).

Geometrisch eignet sich für **multiplikative Effekte** -- z.B.
**Wachstumsraten** (mittlere jaehrliche Verzinsung), **Aspect-Ratios**
und **prozentuale Veränderungen**.

## Wachstums-Beispiel

Aktie verdoppelt sich Jahr 1 (×2), halbiert sich Jahr 2 (×0.5):
- Arithmetisches Mittel: `(2 + 0.5)/2 = 1.25` (irrefuehrend!)
- Geometrisches Mittel: `sqrt(2 * 0.5) = 1.0` (korrekt: kein Gewinn)

## Hintergrund

Bei numerischer Stabilitaet: bei sehr vielen oder großen Zahlen
besser über `exp(mean(log(x)))` rechnen, um Overflow zu vermeiden.
