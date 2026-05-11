---
schema_version: 1
id: 265-xor-tausch
revision: 1
titel: XOR-Tausch ohne Hilfsvariable
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [bits, zahlen, xor, tausch]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Bit-Trick
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: xor_tausch
hints:
  - kosten: 0
    text: |
      Tausche zwei ganzen Zahlen mit dem XOR-Trick OHNE Hilfsvariable.
      Liefere [b, a].
      Funktioniert mit positiven, negativen und 0 -- in Python
      sind ints unbegrenzt, das macht XOR sicher.
  - kosten: 15
    text: |
      a ^= b; b ^= a; a ^= b. Drei XOR-Operationen.
      Liefer [a, b] (jetzt vertauscht).
tests_sichtbar:
  - input: [3, 5]
    expected: [5, 3]
  - input: [0, 0]
    expected: [0, 0]
  - input: [1, 2]
    expected: [2, 1]
  - input: [-1, 7]
    expected: [7, -1]
tests_versteckt:
  - input: [42, 99]
    expected: [99, 42]
  - input: [100, 200]
    expected: [200, 100]
  - input: [-5, -3]
    expected: [-3, -5]
  - input: [255, 256]
    expected: [256, 255]
  - input: [1024, 0]
    expected: [0, 1024]
  - input: [-100, 100]
    expected: [100, -100]
  - input: [7, 7]
    expected: [7, 7]
starter_code: |
  def xor_tausch(a: int, b: int) -> list[int]:
      # Deine Lösung hier -- 3 XOR-Operationen, KEINE Hilfsvariable
      pass
---

# XOR-Tausch ohne Hilfsvariable

Schreibe `xor_tausch(a, b)`, die zwei Ganzzahlen tauscht **ohne
Hilfsvariable** -- über den klassischen XOR-Trick.

## Der Trick

```
a ^= b   # a wird zu (a XOR b)
b ^= a   # b wird zu (b XOR a XOR b) = a
a ^= b   # a wird zu (a XOR b XOR a) = b
```

Da `x ^ x == 0` und `x ^ 0 == x` und XOR assoziativ + kommutativ ist,
funktioniert das.

## Beispiele

| `a`   | `b`   | Ergebnis     |
|-------|-------|--------------|
| 3     | 5     | `[5, 3]`     |
| 0     | 0     | `[0, 0]`     |
| -1    | 7     | `[7, -1]`    |
| 42    | 99    | `[99, 42]`   |
| 7     | 7     | `[7, 7]`     |

## Idee

```python
def xor_tausch(a, b):
    a ^= b
    b ^= a
    a ^= b
    return [a, b]
```

## Vergleich -- Pythonisch vs Bit-Trick

In Python ist der **schönste** Tausch:

```python
a, b = b, a
```

Tupel-Zuweisung -- kein Hilfsvariable nötig, **liest** sich
selbsterklärend. Der XOR-Trick ist ein **Show-Off** aus C-Zeiten.

## Wann sinnvoll?

In **Embedded**-Programmierung (sehr kleine RAM-Mengen) oder bei
**Inline-Assembler** kann man so 1 Register sparen. Heute praktisch
nie nötig, aber als **Klassiker** lehrreich -- und in
Bewerbungsgespraechen taucht er auf.

## Stolperstein -- bei `a` und `b` gleicher Variable

Wenn `a` und `b` dieselbe **Speicher-Adresse** wären (in C-Code),
würde der Trick `a` zu **0** machen. In Python kein Problem,
weil wir mit Werten arbeiten.
