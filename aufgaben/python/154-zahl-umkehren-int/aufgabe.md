---
schema_version: 1
id: 154-zahl-umkehren-int
revision: 1
titel: Ganze Zahl umdrehen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [zahlen, strings, vorzeichen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 7 (vereinfacht ohne Overflow)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zahl_umdrehen
hints:
  - kosten: 0
    text: |
      Drehe die Ziffernreihenfolge einer ganzen Zahl um.
      123 -> 321, -123 -> -321, 100 -> 1.
      Vorzeichen bleibt; fuehrende Nullen entfallen.
  - kosten: 10
    text: |
      Per String: int(str(abs(n))[::-1]) und dann mit dem
      ursprunglichen Vorzeichen multiplizieren.
tests_sichtbar:
  - input: [123]
    expected: 321
  - input: [-123]
    expected: -321
  - input: [100]
    expected: 1
  - input: [0]
    expected: 0
tests_versteckt:
  - input: [1]
    expected: 1
  - input: [-1]
    expected: -1
  - input: [12345]
    expected: 54321
  - input: [-100]
    expected: -1
  - input: [1000000]
    expected: 1
  - input: [9876543210]
    expected: 123456789
starter_code: |
  def zahl_umdrehen(n: int) -> int:
      # Deine Lösung hier -- Vorzeichen halten, fuehrende Nullen weg
      pass
---

# Ganze Zahl umdrehen

Schreibe eine Funktion `zahl_umdrehen(n)`, die die **Ziffernreihenfolge**
einer ganzen Zahl umdreht. Vorzeichen bleibt erhalten, fuehrende Nullen
nach dem Umdrehen entfallen automatisch.

## Beispiele

| `n`           | Umgekehrt    |
|---------------|--------------|
| `123`         | `321`        |
| `-123`        | `-321`       |
| `100`         | `1`          |
| `-100`        | `-1`         |
| `0`           | `0`          |
| `1000000`     | `1`          |
| `9876543210`  | `123456789`  |

## Idee -- per String

```python
def zahl_umdrehen(n):
    vorzeichen = -1 if n < 0 else 1
    return vorzeichen * int(str(abs(n))[::-1])
```

`str(abs(n))[::-1]` dreht die Ziffernkette, `int(...)` killt fuehrende
Nullen automatisch.

## Idee -- ohne String

Per Modulo / Division:

```python
def zahl_umdrehen(n):
    vorzeichen = -1 if n < 0 else 1
    n = abs(n)
    ergebnis = 0
    while n > 0:
        ergebnis = ergebnis * 10 + n % 10
        n //= 10
    return vorzeichen * ergebnis
```

Klassische Schul-Variante -- gleichzeitig die Vorlage für
Konvertierungen in andere Zahlensysteme (Basis statt 10).

## Hinweis

In LeetCode 7 muss zusaetzlich auf 32-Bit-Overflow geprüft werden.
Hier nutzen wir Pythons unbegrenzte Integer und sparen den Sonderfall.
