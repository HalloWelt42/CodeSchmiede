---
schema_version: 1
id: 168-kassen-wechsel
revision: 1
titel: Wechselgeld in EUR-Stueckelung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [greedy, listen, geld, schleifen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Greedy-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: wechselgeld
hints:
  - kosten: 0
    text: |
      Gegeben ein Betrag in CENT. Liefere die Anzahl jeder Stueckelung
      von oben nach unten als Liste:
      [200, 100, 50, 20, 10, 5, 2, 1] (in Cent).
      Greedy: immer die groesste passende Muenze nehmen.
  - kosten: 10
    text: |
      Pro Stueckelung: anzahl = betrag // stueck, betrag %= stueck.
      Loesung als Liste in der Reihenfolge der Stueckelungen sammeln.
tests_sichtbar:
  - input: [0]
    expected: [0, 0, 0, 0, 0, 0, 0, 0]
  - input: [1]
    expected: [0, 0, 0, 0, 0, 0, 0, 1]
  - input: [200]
    expected: [1, 0, 0, 0, 0, 0, 0, 0]
  - input: [388]
    expected: [1, 1, 1, 1, 1, 1, 1, 1]
tests_versteckt:
  - input: [99]
    expected: [0, 0, 1, 2, 0, 1, 2, 0]
  - input: [555]
    expected: [2, 1, 1, 0, 0, 1, 0, 0]
  - input: [1000]
    expected: [5, 0, 0, 0, 0, 0, 0, 0]
  - input: [3]
    expected: [0, 0, 0, 0, 0, 0, 1, 1]
  - input: [7]
    expected: [0, 0, 0, 0, 0, 1, 1, 0]
  - input: [199]
    expected: [0, 1, 1, 2, 0, 1, 2, 0]
starter_code: |
  def wechselgeld(cent: int) -> list[int]:
      # Deine Lösung hier -- 8 Werte fuer [200,100,50,20,10,5,2,1]
      pass
---

# Wechselgeld in EUR-Stueckelung

Schreibe eine Funktion `wechselgeld(cent)`, die fuer einen Betrag
in **Cent** die Anzahl jeder EUR-Muenz-/-Schein-Stueckelung
(in dieser Reihenfolge) zurueckgibt:

```
[200, 100, 50, 20, 10, 5, 2, 1]   (alle in Cent)
```

Die Strategie ist **greedy**: immer die groesste Muenze nehmen, die
noch passt.

## Beispiele

| Cent   | Aufteilung                                   |
|--------|----------------------------------------------|
| `0`    | `[0,0,0,0,0,0,0,0]`                          |
| `1`    | `[0,0,0,0,0,0,0,1]` -- ein 1ct               |
| `200`  | `[1,0,0,0,0,0,0,0]` -- ein 2-Euro            |
| `388`  | `[1,1,1,1,1,1,1,1]` -- jeder Wert genau 1x   |
| `99`   | `[0,0,1,2,0,1,2,0]` -- 50 + 2*20 + 5 + 2*2   |
| `1000` | `[5,0,0,0,0,0,0,0]` -- 5 mal 2-Euro          |

## Idee

```python
STUECKELUNG = [200, 100, 50, 20, 10, 5, 2, 1]

def wechselgeld(cent):
    out = []
    for s in STUECKELUNG:
        out.append(cent // s)
        cent %= s
    return out
```

## Greedy ist hier garantiert optimal

Die Euro-Stueckelung ist ein **kanonisches Muenz-System** -- Greedy
liefert garantiert die minimale Stueck-Anzahl. Bei kuenstlichen
Stueckelungen wie `[1, 3, 4]` versagt Greedy (siehe Aufgabe 143).
