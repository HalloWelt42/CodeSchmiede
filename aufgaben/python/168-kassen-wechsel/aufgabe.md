---
schema_version: 1
id: 168-kassen-wechsel
revision: 3
titel: Wechselgeld in EUR-Stückelung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [greedy, listen, geld, schleifen]
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
      Gegeben ein Betrag in CENT. Liefere die Anzahl jeder Stückelung
      von oben nach unten als Liste:
      [200, 100, 50, 20, 10, 5, 2, 1] (in Cent).
      Greedy: immer die größte passende Münze nehmen.
  - kosten: 10
    text: |
      Pro Stückelung: anzahl = betrag // stück, betrag %= stück.
      Lösung als Liste in der Reihenfolge der Stückelungen sammeln.
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
  - input: [98]
    expected: [0, 0, 1, 2, 0, 1, 1, 1]
  - input: [555]
    expected: [2, 1, 1, 0, 0, 1, 0, 0]
  - input: [1400]
    expected: [7, 0, 0, 0, 0, 0, 0, 0]
  - input: [3]
    expected: [0, 0, 0, 0, 0, 0, 1, 1]
  - input: [7]
    expected: [0, 0, 0, 0, 0, 1, 1, 0]
  - input: [199]
    expected: [0, 1, 1, 2, 0, 1, 2, 0]
starter_code: |
  def wechselgeld(cent: int) -> list[int]:
      # Deine Lösung hier - 8 Werte für [200,100,50,20,10,5,2,1]
      pass
---

# Wechselgeld in EUR-Stückelung

Schreibe eine Funktion `wechselgeld(cent)`, die für einen Betrag
in **Cent** die Anzahl jeder EUR-Münz-/-Schein-Stückelung
(in dieser Reihenfolge) zurückgibt:

```
[200, 100, 50, 20, 10, 5, 2, 1]   (alle in Cent)
```

Die Strategie ist **greedy**: immer die größte Münze nehmen, die
noch passt.

## Beispiele

| Cent   | Aufteilung                                   |
|--------|----------------------------------------------|
| `0`    | `[0,0,0,0,0,0,0,0]`                          |
| `1`    | `[0,0,0,0,0,0,0,1]` - ein 1ct               |
| `200`  | `[1,0,0,0,0,0,0,0]` - ein 2-Euro            |
| `388`  | `[1,1,1,1,1,1,1,1]` - jeder Wert genau 1x   |
| `99`   | `[0,0,1,2,0,1,2,0]` - 50 + 2*20 + 5 + 2*2   |
| `1000` | `[5,0,0,0,0,0,0,0]` - 5 mal 2-Euro          |

## Greedy ist hier garantiert optimal

Die Euro-Stückelung ist ein **kanonisches Münz-System** - Greedy
liefert garantiert die minimale Stück-Anzahl. Bei künstlichen
Stückelungen wie `[1, 3, 4]` versagt Greedy (siehe Aufgabe 143).
