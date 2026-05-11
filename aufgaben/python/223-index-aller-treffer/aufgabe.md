---
schema_version: 1
id: 223-index-aller-treffer
revision: 1
titel: Indizes aller Treffer in Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, suchen, enumerate]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Such-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: alle_indizes
hints:
  - kosten: 0
    text: |
      Liefere ALLE Indizes, an denen "wert" in der Liste vorkommt --
      aufsteigend. Bei keinem Treffer → [].
  - kosten: 10
    text: |
      [i for i, x in enumerate(liste) if x == wert].
tests_sichtbar:
  - input: [[1, 2, 3, 2, 1], 2]
    expected: [1, 3]
  - input: [[], 5]
    expected: []
  - input: [[1, 2, 3], 4]
    expected: []
  - input: [[5, 5, 5], 5]
    expected: [0, 1, 2]
tests_versteckt:
  - input: [["a", "b", "a", "c", "a"], "a"]
    expected: [0, 2, 4]
  - input: [[1, 2, 3, 4, 5], 3]
    expected: [2]
  - input: [[true, false, true, false], true]
    expected: [0, 2]
  - input: [[null, 1, null, 2, null], null]
    expected: [0, 2, 4]
  - input: [[0, 0, 1, 0, 0], 1]
    expected: [2]
  - input: [[1, 2, 3], 1]
    expected: [0]
starter_code: |
  def alle_indizes(liste: list, wert) -> list[int]:
      # Deine Lösung hier
      pass
---

# Indizes aller Treffer in Liste

Schreibe `alle_indizes(liste, wert)`, die **alle Indizes** liefert,
an denen `wert` in der Liste vorkommt -- in **aufsteigender**
Reihenfolge. Bei keinem Treffer → `[]`.

Im Gegensatz zu `list.index(wert)`, das nur den **ersten** Treffer
liefert.

## Beispiele

| Liste              | Wert | Indizes      |
|--------------------|------|--------------|
| `[1, 2, 3, 2, 1]`  | `2`  | `[1, 3]`     |
| `[5, 5, 5]`        | `5`  | `[0, 1, 2]`  |
| `[1, 2, 3]`        | `4`  | `[]`         |
| `["a", "b", "a"]`  | `"a"`| `[0, 2]`     |

## Idee

```python
def alle_indizes(liste, wert):
    return [i for i, x in enumerate(liste) if x == wert]
```

`enumerate` liefert `(index, element)`-Paare -- die elegante Art,
in Python ueber Indizes UND Werte gleichzeitig zu iterieren.

## Pattern -- Index-Sammlung

Diese Idee ist universell:

| Filter-Bedingung    | Beispiel                                   |
|---------------------|---------------------------------------------|
| `x == wert`         | hier (Treffer)                              |
| `x > 0`             | Indizes positiver Werte                     |
| `x % 2 == 0`        | Indizes gerader Zahlen                      |
| `len(x) > 5`        | Indizes langer Strings                      |

Ein einzeiliges Comprehension-Muster fuer alles davon.

## Verwandt

- `liste.index(wert)` → nur **erster** Treffer (oder `ValueError`).
- `liste.count(wert)` → nur die **Anzahl** (Aufgabe 221).
- `alle_indizes(liste, wert)` → alle **Positionen** (hier).
