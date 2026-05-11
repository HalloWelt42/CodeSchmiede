---
schema_version: 1
id: 164-zwei-summe-hash
revision: 1
titel: Zwei-Summe (unsortiert, Hash)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [listen, dicts, suchen, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 1 -- der Klassiker schlechthin
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zwei_summe
hints:
  - kosten: 0
    text: |
      Gegeben: unsortierte Liste + Zielwert.
      Liefere die zwei Indizes [i, j] (i < j), die zusammen das Ziel
      ergeben. Wenn keins existiert: [].
      Garantiert hoechstens eine Loesung.
  - kosten: 15
    text: |
      Dict gesehen: zahl -> index. Pro neue Zahl x:
      wenn (ziel - x) in gesehen: gefunden!
      Sonst gesehen[x] = aktueller_index.
tests_sichtbar:
  - input: [[2, 7, 11, 15], 9]
    expected: [0, 1]
  - input: [[3, 2, 4], 6]
    expected: [1, 2]
  - input: [[3, 3], 6]
    expected: [0, 1]
  - input: [[1, 2, 3], 7]
    expected: []
tests_versteckt:
  - input: [[1, 5, 9, 3], 8]
    expected: [1, 3]
  - input: [[-1, -2, -3, -4, -5], -8]
    expected: [2, 4]
  - input: [[0, 4, 3, 0], 0]
    expected: [0, 3]
  - input: [[5, 5, 11], 10]
    expected: [0, 1]
  - input: [[], 5]
    expected: []
  - input: [[7], 7]
    expected: []
starter_code: |
  def zwei_summe(zahlen: list[int], ziel: int) -> list[int]:
      # Deine Lösung hier -- Hash-Dict, O(n)
      pass
---

# Zwei-Summe (unsortiert, Hash)

Gegeben ist eine **unsortierte** Liste und ein Zielwert. Schreibe
`zwei_summe(zahlen, ziel)`, die `[i, j]` mit `i < j` und
`zahlen[i] + zahlen[j] == ziel` zurueckgibt -- oder `[]`, falls
kein Paar existiert.

## Beispiele

| Liste            | Ziel | Indizes  | Werte           |
|------------------|------|----------|-----------------|
| `[2, 7, 11, 15]` | `9`  | `[0, 1]` | `2 + 7`         |
| `[3, 2, 4]`      | `6`  | `[1, 2]` | `2 + 4`         |
| `[3, 3]`         | `6`  | `[0, 1]` | `3 + 3`         |
| `[1, 5, 9, 3]`   | `8`  | `[1, 3]` | `5 + 3`         |
| `[1, 2, 3]`      | `7`  | `[]`     | unmoeglich      |

## Idee -- Hash-Dict (O(n))

Beim Durchlaufen merken wir uns jede Zahl mit ihrem Index. Pro neuer
Zahl `x` schauen wir, ob `ziel - x` schon gesehen wurde.

```python
def zwei_summe(zahlen, ziel):
    gesehen = {}
    for i, x in enumerate(zahlen):
        rest = ziel - x
        if rest in gesehen:
            return [gesehen[rest], i]
        gesehen[x] = i
    return []
```

Eine einzige Schleife → linear in der Listengroesse.

## Vergleich mit "Sortiert + Two Pointers" (Aufgabe 163)

| Liste sortiert? | Beste Strategie     | Komplexitaet |
|-----------------|---------------------|--------------|
| ja              | Two Pointers        | O(n)         |
| nein            | Hash                | O(n)         |
| nein            | Sortieren + 2P      | O(n log n)   |

Bei unsortierten Listen ist Hash schneller -- aber braucht mehr
Speicher (`O(n)` extra).

## Hintergrund

`zwei_summe` ist die wohl meistgesuchte Coding-Interview-Aufgabe der
Welt -- LeetCode-Aufgabe **Nummer 1**. Wer den Hash-Trick draufhat,
ist schon halb in der naechsten Runde.
