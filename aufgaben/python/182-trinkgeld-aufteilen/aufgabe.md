---
schema_version: 1
id: 182-trinkgeld-aufteilen
revision: 1
titel: Rechnung mit Trinkgeld aufteilen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 8
tags: [zahlen, runden, prozent, alltag]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Alltags-Rechnung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: pro_person
hints:
  - kosten: 0
    text: |
      Berechne den Betrag pro Person:
      gesamt = rechnung * (1 + tip_prozent/100), geteilt durch personen.
      Auf 2 Nachkommastellen gerundet.
      personen <= 0 oder rechnung < 0 → 0.0.
  - kosten: 10
    text: |
      round((rechnung * (1 + tip_prozent / 100)) / personen, 2).
tests_sichtbar:
  - input: [100.0, 10, 2]
    expected: 55.0
  - input: [50.0, 0, 1]
    expected: 50.0
  - input: [0.0, 15, 3]
    expected: 0.0
  - input: [85.5, 18, 4]
    expected: 25.22
tests_versteckt:
  - input: [120.0, 20, 4]
    expected: 36.0
  - input: [100.0, 100, 1]
    expected: 200.0
  - input: [33.33, 10, 3]
    expected: 12.22
  - input: [50.0, 15, 0]
    expected: 0.0
  - input: [-50.0, 10, 2]
    expected: 0.0
  - input: [200.0, 25, 5]
    expected: 50.0
starter_code: |
  def pro_person(rechnung: float, tip_prozent: float, personen: int) -> float:
      # Deine Lösung hier -- auf 2 Stellen gerundet
      pass
---

# Rechnung mit Trinkgeld aufteilen

Schreibe `pro_person(rechnung, tip_prozent, personen)`, die berechnet,
wieviel jeder beim Restaurant zahlen muss -- inklusive **Trinkgeld**
und gleichmaessig aufgeteilt.

**Sonderfaelle**: bei `personen <= 0` oder `rechnung < 0` → `0.0`.
Liefere auf **2 Nachkommastellen** gerundet.

## Beispiele

| Rechnung | Tip | Personen | Pro Person |
|----------|-----|----------|------------|
| `100`    | `10%`| `2`     | `55.00`    |
| `50`     | `0%`| `1`      | `50.00`    |
| `120`    | `20%`| `4`     | `36.00`    |
| `85.50`  | `18%`| `4`     | `25.22`    |
| `200`    | `25%`| `5`     | `50.00`    |

## Idee

```python
def pro_person(rechnung, tip_prozent, personen):
    if personen <= 0 or rechnung < 0:
        return 0.0
    gesamt = rechnung * (1 + tip_prozent / 100)
    return round(gesamt / personen, 2)
```

## Hintergrund -- Trinkgeld-Konvention

In Deutschland sind 5-10% ueblich, in den USA werden 15-20% erwartet,
in Japan ist Trinkgeld eher unueblich oder sogar unhoeflich. Beim
Programmieren von Kassen-Apps (z.B. Lightspeed, Paymo) ist die
Aufteilung mit Trinkgeld eine der ersten Funktionen, die man baut.
