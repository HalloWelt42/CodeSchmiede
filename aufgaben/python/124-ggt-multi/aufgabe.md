---
schema_version: 1
id: 124-ggt-multi
revision: 1
titel: ggT mehrerer Zahlen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, listen, euklid, reduce]
pfade: [python_mathe2]
voraussetzungen: [018-ggt]
quelle:
  url: null
  notiz: Erweiterung des klassischen ggT auf Listen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ggt_liste
hints:
  - kosten: 0
    text: |
      ggT von n Zahlen: paarweise reduzieren --
      `ggt(a, b, c) = ggt(ggt(a, b), c)`. Leere Liste → 0.
  - kosten: 10
    text: |
      `from math import gcd; from functools import reduce`.
      `reduce(gcd, zahlen, 0)` liefert die Antwort.
tests_sichtbar:
  - input: [[12, 18]]
    expected: 6
  - input: [[12, 18, 24]]
    expected: 6
  - input: [[7]]
    expected: 7
  - input: [[]]
    expected: 0
tests_versteckt:
  - input: [[100, 200, 300, 400]]
    expected: 100
  - input: [[17, 19, 23]]
    expected: 1
  - input: [[1071, 462, 105]]
    expected: 21
  - input: [[0, 0, 0]]
    expected: 0
  - input: [[60, 90, 120, 150, 180]]
    expected: 30
starter_code: |
  def ggt_liste(zahlen: list[int]) -> int:
      # Deine Lösung hier -- ggT aller Zahlen, leere Liste → 0.
      pass
---

# ggT mehrerer Zahlen

Schreibe eine Funktion `ggt_liste(zahlen)`, die den **größten
gemeinsamen Teiler** aller Zahlen in der Liste zurückgibt.

Leere Liste → `0`.

## Idee

ggT ist assoziativ: `ggt(a, b, c) = ggt(ggt(a, b), c)`. Damit
reduzierst du paarweise.

```python
from functools import reduce
from math import gcd
return reduce(gcd, zahlen, 0)
```

`reduce(gcd, [12, 18, 24], 0)` rechnet `gcd(0,12)=12`, `gcd(12,18)=6`,
`gcd(6,24)=6`. Der Anker `0` ist das **neutrale Element** für ggT.

## Beispiele

| Liste                   | ggT  |
|-------------------------|------|
| `[12, 18]`              | `6`  |
| `[12, 18, 24]`          | `6`  |
| `[100, 200, 300, 400]`  | `100`|
| `[17, 19, 23]`          | `1`  |
| `[7]`                   | `7`  |
| `[]`                    | `0`  |
