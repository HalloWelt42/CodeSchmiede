---
schema_version: 1
id: 317-namedtuple-punkt
revision: 1
titel: NamedTuple-Punkt -- Distanz und Mittelpunkt
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [namedtuple, geometrie, klassen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: collections.namedtuple in Aktion
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: punkt_paar_info
hints:
  - kosten: 0
    text: |
      Erzeuge intern einen Punkt-NamedTuple mit Feldern x, y. Berechne
      fuer zwei Punkte (4-Tupel: x1, y1, x2, y2) die Distanz und den
      Mittelpunkt.
      Liefere [distanz, mid_x, mid_y] auf 4 Nachkommastellen.
  - kosten: 15
    text: |
      from collections import namedtuple
      P = namedtuple('P', ['x', 'y'])
      a, b = P(x1, y1), P(x2, y2)
      math.hypot(b.x - a.x, b.y - a.y) und (a.x + b.x) / 2 etc.
tests_sichtbar:
  - input: [0, 0, 3, 4]
    expected: [5.0, 1.5, 2.0]
  - input: [1, 1, 1, 1]
    expected: [0.0, 1.0, 1.0]
  - input: [0, 0, 0, 0]
    expected: [0.0, 0.0, 0.0]
  - input: [0, 0, 10, 0]
    expected: [10.0, 5.0, 0.0]
tests_versteckt:
  - input: [-3, -4, 0, 0]
    expected: [5.0, -1.5, -2.0]
  - input: [5, 12, 0, 0]
    expected: [13.0, 2.5, 6.0]
  - input: [0, 0, 1, 1]
    expected: [1.4142, 0.5, 0.5]
  - input: [10, 10, 10, 20]
    expected: [10.0, 10.0, 15.0]
  - input: [-5, 0, 5, 0]
    expected: [10.0, 0.0, 0.0]
  - input: [1.5, 2.5, 4.5, 6.5]
    expected: [5.0, 3.0, 4.5]
starter_code: |
  import math
  from collections import namedtuple

  def punkt_paar_info(x1: float, y1: float, x2: float, y2: float) -> list[float]:
      # Tipp: namedtuple Punkt mit x, y; dann Distanz + Mittelpunkt
      pass
---

# NamedTuple-Punkt: Distanz und Mittelpunkt

Schreibe `punkt_paar_info(x1, y1, x2, y2)`, die fuer zwei Punkte die
**Distanz** und den **Mittelpunkt** als Liste `[distanz, mid_x, mid_y]`
zurueckgibt -- alle auf **4 Nachkommastellen** gerundet.

Implementiere intern einen `namedtuple` `Punkt` mit Feldern `x, y`.

## Beispiele

| `(x1, y1)` | `(x2, y2)` | Distanz | Mittelpunkt |
|------------|------------|---------|--------------|
| `(0, 0)`   | `(3, 4)`   | `5.0`   | `(1.5, 2.0)`|
| `(5, 12)`  | `(0, 0)`   | `13.0`  | `(2.5, 6.0)`|
| `(0, 0)`   | `(1, 1)`   | `1.4142`| `(0.5, 0.5)`|
| `(-5, 0)`  | `(5, 0)`   | `10.0`  | `(0.0, 0.0)`|

## Idee mit namedtuple

```python
import math
from collections import namedtuple

Punkt = namedtuple('Punkt', ['x', 'y'])

def punkt_paar_info(x1, y1, x2, y2):
    a = Punkt(x1, y1)
    b = Punkt(x2, y2)
    distanz = math.hypot(b.x - a.x, b.y - a.y)
    mid_x = (a.x + b.x) / 2
    mid_y = (a.y + b.y) / 2
    return [round(distanz, 4), round(mid_x, 4), round(mid_y, 4)]
```

`namedtuple` ist eine **leichte Klasse** ohne Boilerplate -- perfekt
fuer kleine Daten-Container mit benannten Feldern. Liest sich besser
als `(x, y)` Tupel oder `{"x": ..., "y": ...}` Dict.

## NamedTuple vs Klasse vs dataclass

| Form              | Mutable? | Schnell? | Boilerplate |
|-------------------|----------|----------|--------------|
| `namedtuple`      | nein     | sehr     | minimal      |
| `class`           | ja       | mittel   | viel         |
| `dataclass`       | ja       | mittel   | wenig        |
| `dataclass(frozen=True)` | nein | mittel | wenig      |
| `NamedTuple` (typing)| nein  | sehr     | wenig + Typen|

Fuer Punkte ist `NamedTuple` ideal -- klein, immutable, hashable
(kann als Dict-Key dienen).
