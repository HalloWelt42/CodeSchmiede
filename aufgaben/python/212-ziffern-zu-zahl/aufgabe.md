---
schema_version: 1
id: 212-ziffern-zu-zahl
revision: 1
titel: Ziffern-Liste zur Zahl zusammensetzen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [zahlen, listen, horner, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 211
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: aus_ziffern
hints:
  - kosten: 0
    text: |
      Setze eine Ziffern-Liste (hoechstwertige zuerst) zu einer Zahl
      zusammen. [1,2,3] → 123. [0] → 0. [] → 0.
      Ungueltige Eingaben (z.B. Wert > 9) werden wie ihre Modulo-Zahl
      behandelt.
  - kosten: 10
    text: |
      Horner-Schema: ergebnis = 0; pro Ziffer ergebnis = 10 * ergebnis + d.
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: 123
  - input: [[0]]
    expected: 0
  - input: [[]]
    expected: 0
  - input: [[5]]
    expected: 5
tests_versteckt:
  - input: [[1, 0, 0]]
    expected: 100
  - input: [[9, 9, 9]]
    expected: 999
  - input: [[1, 2, 3, 4, 5]]
    expected: 12345
  - input: [[0, 5]]
    expected: 5
  - input: [[1, 0, 0, 0, 0, 0, 0]]
    expected: 1000000
  - input: [[9, 8, 7, 6, 5, 4, 3, 2, 1]]
    expected: 987654321
starter_code: |
  def aus_ziffern(ziffern: list[int]) -> int:
      # Deine Lösung hier -- Horner ist elegant
      pass
---

# Ziffern-Liste zur Zahl zusammensetzen

Schreibe `aus_ziffern(ziffern)`, die eine Liste von Ziffern (jeweils
0-9) zu einer Zahl zusammensetzt -- hoechstwertige Stelle zuerst.

Bei leerer Liste → `0`. Fuehrende Nullen entfallen automatisch.

## Beispiele

| Ziffern             | Zahl       |
|---------------------|------------|
| `[1, 2, 3]`         | `123`      |
| `[0]`               | `0`        |
| `[]`                | `0`        |
| `[1, 0, 0]`         | `100`      |
| `[0, 5]`            | `5`        |
| `[9, 8, 7, 6, 5, 4, 3, 2, 1]` | `987654321` |

## Idee -- Horner-Schema

```python
def aus_ziffern(ziffern):
    n = 0
    for d in ziffern:
        n = 10 * n + d
    return n
```

Pro Stelle "verschieben" wir die bisherige Zahl eine Stelle nach
links (Multiplikation mit 10) und addieren die neue Ziffer.

Beispiel `[1, 2, 3]`:

| Ziffer | n vorher | n nachher  |
|--------|----------|-----|
| 1      | 0        | 1   |
| 2      | 1        | 12  |
| 3      | 12       | 123 |

## Idee -- per Join + int

```python
def aus_ziffern(ziffern):
    if not ziffern:
        return 0
    return int("".join(str(d) for d in ziffern))
```

Liest sich kompakt, macht aber den Umweg ueber String -- bei sehr
grossen Listen langsamer als Horner.

## Anwendung

Pendant zur Aufgabe **211**. Horner ist auch die Grundlage fuer
**Basiskonvertierungen** (Aufgabe 158-binary-zu-dezimal).
