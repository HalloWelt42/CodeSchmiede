---
schema_version: 1
id: 166-subset-sum
revision: 1
titel: Teilmengen-Summe (Subset-Sum, Existenz)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 50
schaetz_minuten: 18
tags: [dp, listen, set, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches NP-vollstaendiges Problem (DP-Loesung)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: subset_sum
hints:
  - kosten: 0
    text: |
      Existiert eine Teilmenge der Liste, deren Summe genau "ziel" ist?
      Gib True/False zurueck. Leere Teilmenge ist erlaubt
      (ergibt 0). Negative Werte muessen nicht behandelt werden.
  - kosten: 20
    text: |
      Set-Trick: erreichbare Summen aufbauen. start = {0}.
      Pro Zahl x: erreichbar |= {s + x for s in erreichbar}.
      Am Ende: ziel in erreichbar.
tests_sichtbar:
  - input: [[3, 34, 4, 12, 5, 2], 9]
    expected: true
  - input: [[3, 34, 4, 12, 5, 2], 30]
    expected: false
  - input: [[], 0]
    expected: true
  - input: [[], 5]
    expected: false
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], 11]
    expected: true
  - input: [[1, 2, 3, 4, 5], 16]
    expected: false
  - input: [[7], 7]
    expected: true
  - input: [[7], 8]
    expected: false
  - input: [[1, 5, 11, 5], 11]
    expected: true
  - input: [[2, 4, 6, 8], 1]
    expected: false
  - input: [[5, 5, 5, 5], 20]
    expected: true
  - input: [[1, 1, 1, 1], 0]
    expected: true
starter_code: |
  def subset_sum(zahlen: list[int], ziel: int) -> bool:
      # Deine Lösung hier -- Set-Trick oder DP
      pass
---

# Teilmengen-Summe (Subset-Sum)

Gegeben sind eine Liste **nicht-negativer** ganzer Zahlen und ein
Zielwert `ziel`. Schreibe `subset_sum(zahlen, ziel)`, die zurueckgibt,
ob **eine Teilmenge** existiert, deren Summe genau `ziel` ist.

Die leere Teilmenge zaehlt (Summe `0`).

## Beispiele

| Zahlen                   | Ziel | Loesung?                         |
|--------------------------|------|----------------------------------|
| `[3, 34, 4, 12, 5, 2]`   | `9`  | `True` (4 + 5)                   |
| `[3, 34, 4, 12, 5, 2]`   | `30` | `False` (max 60 aber 30 nicht)   |
| `[1, 5, 11, 5]`          | `11` | `True` (1 + 5 + 5 oder 11)       |
| `[2, 4, 6, 8]`           | `1`  | `False` (alle gerade)            |
| `[]`                     | `0`  | `True` (leere Menge)             |

## Idee -- Erreichbare Summen als Set

Pro neue Zahl `x` koennen wir entweder weglassen (Summen unveraendert)
oder dazunehmen (Summen + x). Das Set wird in jeder Runde erweitert.

```python
def subset_sum(zahlen, ziel):
    erreichbar = {0}
    for x in zahlen:
        erreichbar |= {s + x for s in erreichbar}
        if ziel in erreichbar:
            return True
    return ziel == 0
```

Effizienz: `O(n * S)`, wo `S` die Anzahl unterscheidbarer Summen ist
(maximal `Sum(zahlen) + 1`).

## Klassische DP-Tabelle

Aequivalent als Boolean-Tabelle `dp[i][s]`:

```python
def subset_sum(zahlen, ziel):
    dp = [False] * (ziel + 1)
    dp[0] = True
    for x in zahlen:
        for s in range(ziel, x - 1, -1):
            if dp[s - x]:
                dp[s] = True
    return dp[ziel]
```

Rueckwaerts iterieren, damit eine Zahl nicht doppelt verbraucht wird.

## Hintergrund

Subset-Sum ist **NP-vollstaendig** -- der allgemeine Fall hat keinen
bekannten Polynomial-Algorithmus. Die DP-Loesung ist
**pseudo-polynomial**: `O(n*S)` ist nur polynomial in den
**Werten**, nicht in der **Bit-Laenge** der Eingabe. Mit grossen
Zielen wird die Loesung exponentiell.
