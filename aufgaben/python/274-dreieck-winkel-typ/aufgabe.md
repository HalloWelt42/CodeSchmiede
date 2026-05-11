---
schema_version: 1
id: 274-dreieck-winkel-typ
revision: 1
titel: Dreieck-Typ nach Winkel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [geometrie, mathematik, dreieck, klassifikation]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 193 (nach Seiten)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dreieck_winkel
hints:
  - kosten: 0
    text: |
      Klassifiziere ein Dreieck mit Seiten a, b, c nach WINKELN:
      "spitz" (alle < 90°), "recht" (genau 90°),
      "stumpf" (einer > 90°), "ungueltig".
      Pythagoras umgekehrt: c² < a² + b² → spitz, == → recht, > → stumpf.
  - kosten: 15
    text: |
      Sortiere Seiten -> c ist die laengste.
      c² vs a² + b² mit math.isclose() bei "recht".
tests_sichtbar:
  - input: [3, 4, 5]
    expected: "recht"
  - input: [5, 5, 5]
    expected: "spitz"
  - input: [3, 3, 5]
    expected: "stumpf"
  - input: [1, 2, 5]
    expected: "ungueltig"
tests_versteckt:
  - input: [6, 8, 10]
    expected: "recht"
  - input: [5, 12, 13]
    expected: "recht"
  - input: [4, 5, 6]
    expected: "spitz"
  - input: [2, 2, 3]
    expected: "stumpf"
  - input: [-1, 4, 5]
    expected: "ungueltig"
  - input: [1, 1, 1]
    expected: "spitz"
  - input: [7, 24, 25]
    expected: "recht"
  - input: [3, 4, 6]
    expected: "stumpf"
starter_code: |
  import math

  def dreieck_winkel(a: float, b: float, c: float) -> str:
      # Deine Lösung hier -- "spitz"/"recht"/"stumpf"/"ungueltig"
      pass
---

# Dreieck-Typ nach Winkel

Schreibe `dreieck_winkel(a, b, c)`, die ein Dreieck nach den
**Winkeln** klassifiziert:

| Typ          | Bedingung                                |
|--------------|-------------------------------------------|
| `"spitz"`    | alle Winkel < 90°                         |
| `"recht"`    | ein Winkel = 90° (rechtwinkliges Dreieck) |
| `"stumpf"`   | ein Winkel > 90°                          |
| `"ungueltig"`| keine Seite > 0 oder Dreiecks-Ungleichung |

## Pythagoras umgedreht

Sei `c` die laengste Seite:

- `c² < a² + b²` → spitzwinklig
- `c² == a² + b²` → rechtwinklig (Pythagoras!)
- `c² > a² + b²` → stumpfwinklig

## Beispiele

| a | b | c  | Typ            |
|---|---|----|----------------|
| 3 | 4 | 5  | `"recht"`      |
| 5 | 12| 13 | `"recht"`      |
| 7 | 24| 25 | `"recht"`      |
| 5 | 5 | 5  | `"spitz"`      |
| 4 | 5 | 6  | `"spitz"`      |
| 3 | 3 | 5  | `"stumpf"`     |
| 3 | 4 | 6  | `"stumpf"`     |
| 1 | 2 | 5  | `"ungueltig"`  |

## Idee

```python
import math

def dreieck_winkel(a, b, c):
    if min(a, b, c) <= 0:
        return "ungueltig"
    seiten = sorted([a, b, c])
    aa, bb, cc = seiten
    if aa + bb <= cc:
        return "ungueltig"
    summe = aa * aa + bb * bb
    quadrat = cc * cc
    if math.isclose(summe, quadrat):
        return "recht"
    if quadrat < summe:
        return "spitz"
    return "stumpf"
```

`math.isclose` fuer Float-Vergleich -- vermeidet Rundungs-Fehler bei
Werten wie `5.0000000001`.

## Verwandt

| Aufgabe              | Was?                          |
|----------------------|-------------------------------|
| **193-dreieck-typ**  | nach **Seiten** (gleichseitig, ...) |
| **274 hier**         | nach **Winkeln** (spitz, recht, stumpf) |
| **270-heron-flaeche**| Flaeche aus Seiten            |
