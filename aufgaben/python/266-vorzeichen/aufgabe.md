---
schema_version: 1
id: 266-vorzeichen
revision: 1
titel: Vorzeichen-Funktion (sign)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [zahlen, mathematik, vergleich]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Mini-Funktion
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: sign
hints:
  - kosten: 0
    text: |
      Liefere -1 wenn x < 0, 0 wenn x == 0, +1 wenn x > 0.
      Funktioniert mit int und float.
  - kosten: 4
    text: |
      Direkter if/elif/else.
      Oder Trick: (x > 0) - (x < 0).
tests_sichtbar:
  - input: [5]
    expected: 1
  - input: [-5]
    expected: -1
  - input: [0]
    expected: 0
  - input: [0.0]
    expected: 0
tests_versteckt:
  - input: [1]
    expected: 1
  - input: [-1]
    expected: -1
  - input: [100]
    expected: 1
  - input: [-100]
    expected: -1
  - input: [0.5]
    expected: 1
  - input: [-0.5]
    expected: -1
  - input: [1000000000]
    expected: 1
  - input: [-1000000000]
    expected: -1
starter_code: |
  def sign(x) -> int:
      # Deine Lösung hier -- -1, 0, oder 1
      pass
---

# Vorzeichen-Funktion (sign)

Schreibe `sign(x)`, die das **Vorzeichen** einer Zahl liefert:

| Eingabe | Ergebnis |
|---------|----------|
| x > 0   | `1`      |
| x == 0  | `0`      |
| x < 0   | `-1`     |

Funktioniert sowohl mit `int` als auch `float`.

## Beispiele

| `x`         | `sign(x)` |
|-------------|-----------|
| 5           | `1`       |
| -5          | `-1`      |
| 0           | `0`       |
| 0.5         | `1`       |
| -0.5        | `-1`      |
| 1000000000  | `1`       |

## Idee 1 -- if/elif

Klar lesbar, drei Faelle.

## Idee 2 -- Boolean-Trick

Kompakte Variante: `True - True == 0`, `True - False == 1`,
`False - True == -1`. Ein Pythonismus.

## In `math` und `numpy`

- `math.copysign(1, x)` liefert `1.0` oder `-1.0`, **nie** `0` --
  unbrauchbar für unsere Zwecke.
- `numpy.sign(x)` macht genau das, was wir brauchen.

## Anwendung

- **Vergleichs-Funktionen** in alten APIs (cmp(a, b) lieferte -1/0/+1).
- **Steuerung**: "drehe in Richtung Ziel" (+1 oder -1).
- **Mathematische Identitaeten**: $|x| = x \cdot \text{sign}(x)$.
