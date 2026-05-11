---
schema_version: 1
id: 253-floor-zu-vielfache
revision: 1
titel: Abrunden zum nächsten Vielfachen von k
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, runden, modulo, floor]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 252
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: floor_vielfache
hints:
  - kosten: 0
    text: |
      Runde n ABWAERTS zum nächsten Vielfachen von k.
      n = 13, k = 5 → 10. n = 10, k = 5 → 10.
      k <= 0 → n unverändert.
      Negative n: -13 mit k=5 → -15.
  - kosten: 10
    text: |
      n // k * k -- Pythons // ist Floor-Division (rundet abwärts).
tests_sichtbar:
  - input: [13, 5]
    expected: 10
  - input: [10, 5]
    expected: 10
  - input: [0, 5]
    expected: 0
  - input: [9, 10]
    expected: 0
tests_versteckt:
  - input: [25, 7]
    expected: 21
  - input: [100, 100]
    expected: 100
  - input: [199, 100]
    expected: 100
  - input: [-13, 5]
    expected: -15
  - input: [-10, 5]
    expected: -10
  - input: [-1, 5]
    expected: -5
  - input: [50, 0]
    expected: 50
starter_code: |
  def floor_vielfache(n: int, k: int) -> int:
      # Deine Lösung hier -- abwaerts (Richtung -unendlich)
      pass
---

# Abrunden zum nächsten Vielfachen von k

Schreibe `floor_vielfache(n, k)`, die `n` **abwärts** zum nächsten
Vielfachen von `k` rundet (Richtung -unendlich).

- Bei `k <= 0` → `n` unverändert.
- Wenn `n` bereits Vielfaches ist → `n` selbst.
- Negative Werte: weiter weg von 0 ("abwärts" mathematisch).

## Beispiele

| `n`  | `k`  | Ergebnis | Bemerkung               |
|------|------|----------|-------------------------|
| 13   | 5    | 10       | abgerundet auf 10       |
| 10   | 5    | 10       | bereits Vielfaches      |
| 9    | 10   | 0        | abgerundet auf 0        |
| 25   | 7    | 21       | 25 → 21                 |
| 199  | 100  | 100      | knapp unter 200         |
| -13  | 5    | -15      | abwärts (negativer)    |
| -1   | 5    | -5       | direkt nach -5          |

## Idee

```python
def floor_vielfache(n, k):
    if k <= 0:
        return n
    return n // k * k
```

Pythons `//` rundet immer **abwärts** (Richtung -unendlich), auch
bei negativen Zahlen. Das macht es zur perfekten Floor-Division
für diese Aufgabe.

## Vergleich C-Modulo vs Python

In **C** rundet `/` Richtung 0:
```c
-13 / 5    // -2 (nicht -3)
```

In **Python**:
```python
-13 // 5   # -3 (Richtung -inf)
```

Daher liefert Python `-13 // 5 * 5 = -15`, was wir wollen.
C würde `-10` liefern.

## Verwandt

| Aufgabe                  | Was?                          |
|--------------------------|-------------------------------|
| **247-runden-zu-vielfache** | Naechstes Vielfache (round)|
| **252-ceil-zu-vielfache**| Aufrunden (ceil)              |
| **253 hier**             | Abrunden (floor)              |

Die drei zusammen decken **alle** Rundungs-Richtungen ab.
