---
schema_version: 1
id: 230-ist-aufsteigend
revision: 1
titel: Ist die Liste aufsteigend sortiert?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, vergleich, all, zip]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Listen-Prüfung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_aufsteigend
hints:
  - kosten: 0
    text: |
      Prüfe ob die Liste NICHT-FALLEND sortiert ist (also a[i] <= a[i+1]).
      Leere Liste / 1-elementig → True.
      Gleiche Werte sind erlaubt.
  - kosten: 10
    text: |
      all(a <= b for a, b in zip(liste, liste[1:])).
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: true
  - input: [[1, 3, 2]]
    expected: false
  - input: [[]]
    expected: true
  - input: [[5]]
    expected: true
tests_versteckt:
  - input: [[1, 1, 2, 2, 3]]
    expected: true
  - input: [[5, 4, 3, 2, 1]]
    expected: false
  - input: [[1, 2, 3, 3, 2]]
    expected: false
  - input: [[1, 2]]
    expected: true
  - input: [[2, 1]]
    expected: false
  - input: [[-3, -2, -1, 0, 1]]
    expected: true
  - input: [[1.5, 2.5, 3.5]]
    expected: true
starter_code: |
  def ist_aufsteigend(liste: list) -> bool:
      # Deine Lösung hier -- a[i] <= a[i+1] erlaubt (nicht-fallend)
      pass
---

# Ist die Liste aufsteigend sortiert?

Schreibe `ist_aufsteigend(liste)`, die `True` zurückgibt, wenn die
Liste **nicht-fallend** sortiert ist -- also `a[i] <= a[i+1]` für
alle Indizes. Gleiche Werte hintereinander sind erlaubt.

Leere oder 1-elementige Liste → `True`.

## Beispiele

| Liste              | Aufsteigend? |
|--------------------|--------------|
| `[1, 2, 3, 4]`     | `True`       |
| `[1, 1, 2, 2, 3]`  | `True` (Duplikate erlaubt) |
| `[5, 4, 3, 2, 1]`  | `False`      |
| `[1, 3, 2]`        | `False`      |
| `[1, 2, 3, 3, 2]`  | `False`      |
| `[]`               | `True`       |

## Idee

```python
def ist_aufsteigend(liste):
    return all(a <= b for a, b in zip(liste, liste[1:]))
```

`zip(liste, liste[1:])` paart **aufeinanderfolgende** Elemente:
`zip([1,2,3], [2,3]) → (1,2), (2,3)`. `all` liefert `True`, sobald
alle Paare die Bedingung erfüllen -- bei leerer Liste auch (vacuous
truth).

## Strikt aufsteigend

Wer `<` statt `<=` will (also keine Duplikate):

```python
return all(a < b for a, b in zip(liste, liste[1:]))
```

## Verwandt

- `sorted(liste) == liste` ist eine **wahrere** Variante, aber **doppelt
  so langsam** (Sortieren ist `O(n log n)`, Linear-Check `O(n)`).
- Aufgabe **178-LIS** (laengste aufsteigende Teilfolge) baut auf
  diesem Konzept auf.
