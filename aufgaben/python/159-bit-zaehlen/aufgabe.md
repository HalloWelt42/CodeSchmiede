---
schema_version: 1
id: 159-bit-zaehlen
revision: 1
titel: Gesetzte Bits zaehlen (Hamming-Gewicht)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 10
tags: [bits, zahlen, schleifen, optimierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Brian-Kernighan-Trick / LeetCode 191
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bit_anzahl
hints:
  - kosten: 0
    text: |
      Zaehle die Anzahl gesetzter Bits (1en) in der Binaer-Darstellung
      einer nicht-negativen Zahl. 0 -> 0, 7 -> 3, 255 -> 8.
      bin().count("1") und int.bit_count() sind verboten.
  - kosten: 15
    text: |
      Brian Kernighan: solange n > 0: n &= n - 1; counter += 1.
      Pro Iteration verschwindet das niedrigste gesetzte Bit.
tests_sichtbar:
  - input: [0]
    expected: 0
  - input: [1]
    expected: 1
  - input: [7]
    expected: 3
  - input: [255]
    expected: 8
tests_versteckt:
  - input: [2]
    expected: 1
  - input: [3]
    expected: 2
  - input: [8]
    expected: 1
  - input: [128]
    expected: 1
  - input: [1023]
    expected: 10
  - input: [4294967295]
    expected: 32
  - input: [42]
    expected: 3
starter_code: |
  def bit_anzahl(n: int) -> int:
      # Deine Lösung hier -- ohne bin().count("1")
      pass
---

# Gesetzte Bits zaehlen (Hamming-Gewicht)

Schreibe eine Funktion `bit_anzahl(n)`, die die **Anzahl der gesetzten
Bits** (1-en in der Binaer-Darstellung) einer nicht-negativen ganzen
Zahl zurueckgibt.

`bin().count("1")` und `int.bit_count()` zaehlen nicht -- du sollst
selber rechnen.

## Beispiele

| `n`           | Binaer       | Bit-Anzahl |
|---------------|--------------|------------|
| `0`           | `0`          | `0`        |
| `1`           | `1`          | `1`        |
| `7`           | `111`        | `3`        |
| `8`           | `1000`       | `1`        |
| `255`         | `11111111`   | `8`        |
| `4294967295`  | `1...1` (32) | `32`       |

## Idee 1 -- Modulo-Schleife

```python
def bit_anzahl(n):
    z = 0
    while n > 0:
        z += n & 1
        n >>= 1
    return z
```

Pro Schritt das niedrigste Bit auslesen (`n & 1`), dann nach rechts
schieben.

## Idee 2 -- Brian-Kernighan-Trick (eleganter)

```python
def bit_anzahl(n):
    z = 0
    while n:
        n &= n - 1
        z += 1
    return z
```

`n & (n-1)` loescht **immer das niedrigste gesetzte Bit** -- darum
laeuft die Schleife nur so oft wie 1-en da sind. Bei sparsam besetzten
Zahlen (z.B. `2**31`) ist das deutlich schneller als die Modulo-Schleife.

## Hintergrund

Das Hamming-Gewicht zaehlt z.B. **Fehler-Bits** in Codierungen,
Differenzen zwischen Bit-Strings (Hamming-Distanz = popcount(a ^ b))
oder die Anzahl gesetzter Pixel in Bitmap-Schichten. Moderne CPUs
haben dafuer einen eigenen Befehl `popcnt`.
