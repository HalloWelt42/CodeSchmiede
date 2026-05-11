---
schema_version: 1
id: 200-euklid-ggt
revision: 1
titel: GgT mit Euklid (eigene Implementierung)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [mathematik, ggt, schleifen, rekursion]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Algorithmus, ohne math.gcd
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ggt
hints:
  - kosten: 0
    text: |
      Berechne den groessten gemeinsamen Teiler zweier nicht-negativer
      ganzer Zahlen -- OHNE math.gcd.
      ggt(a, 0) = a. Sonst: ggt(a, b) = ggt(b, a % b).
  - kosten: 15
    text: |
      Iterativ: while b: a, b = b, a % b. Return a.
      Negative Eingaben: Beträge nehmen.
tests_sichtbar:
  - input: [12, 18]
    expected: 6
  - input: [0, 5]
    expected: 5
  - input: [5, 0]
    expected: 5
  - input: [7, 13]
    expected: 1
tests_versteckt:
  - input: [0, 0]
    expected: 0
  - input: [100, 75]
    expected: 25
  - input: [1071, 462]
    expected: 21
  - input: [1, 1]
    expected: 1
  - input: [-12, 18]
    expected: 6
  - input: [12, -18]
    expected: 6
  - input: [-12, -18]
    expected: 6
  - input: [123456, 7890]
    expected: 6
starter_code: |
  def ggt(a: int, b: int) -> int:
      # Deine Lösung hier -- ohne math.gcd
      pass
---

# GgT mit Euklid (eigene Implementierung)

Schreibe `ggt(a, b)`, die den **groessten gemeinsamen Teiler** zweier
ganzer Zahlen liefert -- ohne `math.gcd`.

Negative Eingaben: Betrag nehmen. `ggt(0, 0) = 0`.

## Euklids Algorithmus (300 v. Chr.)

```
ggt(a, 0) = a
ggt(a, b) = ggt(b, a % b)   fuer b > 0
```

Die Folge `a, b, a%b, b%(a%b), ...` schrumpft sehr schnell -- bei
zwei Zahlen mit `n` Stellen ist sie nach `O(n)` Schritten am Ende.

## Beispiele

| `a`     | `b`    | ggt |
|---------|--------|-----|
| `12`    | `18`   | `6` |
| `100`   | `75`   | `25`|
| `1071`  | `462`  | `21`|
| `7`     | `13`   | `1` |
| `0`     | `5`    | `5` |
| `-12`   | `18`   | `6` |

## Idee -- iterativ

```python
def ggt(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
```

Pythons Tupel-Zuweisung macht den Variablen-Tausch in **einer Zeile**
moeglich -- in C oder Java braucht man eine Hilfsvariable.

## Idee -- rekursiv

```python
def ggt(a, b):
    a, b = abs(a), abs(b)
    return a if b == 0 else ggt(b, a % b)
```

Eleganter, aber bei sehr grossen Zahlen Stack-Limit beachten.

## Anwendung

GgT taucht ueberall auf, wo man **Brueche kuerzen** will:
`12/18 → 12/ggt(12,18) / 18/ggt(12,18) = 2/3`. In der Kryptographie
ist Euklids Algorithmus die Basis fuer **modulare Inverse** (RSA).
