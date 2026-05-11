---
schema_version: 1
id: 237-paare-aus-liste
revision: 1
titel: Liste in nicht-überlappende Paare
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, slicing, paare]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Aufteilungs-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: paare
hints:
  - kosten: 0
    text: |
      Teile die Liste in nicht-überlappende 2-er-Paare.
      [1,2,3,4,5,6] → [[1,2],[3,4],[5,6]].
      Ungerade Anzahl: das letzte Element wird IGNORIERT.
      Bei [] → [].
  - kosten: 10
    text: |
      [list(liste[i:i+2]) for i in range(0, len(liste) // 2 * 2, 2)].
      Oder zip(liste[::2], liste[1::2]).
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: [[1, 2], [3, 4]]
  - input: [[]]
    expected: []
  - input: [[1, 2, 3]]
    expected: [[1, 2]]
  - input: [[1]]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3, 4, 5, 6]]
    expected: [[1, 2], [3, 4], [5, 6]]
  - input: [["a", "b", "c", "d"]]
    expected: [["a", "b"], ["c", "d"]]
  - input: [[1, 2]]
    expected: [[1, 2]]
  - input: [[1, 2, 3, 4, 5]]
    expected: [[1, 2], [3, 4]]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
starter_code: |
  def paare(liste: list) -> list[list]:
      # Deine Lösung hier -- ungerade Anzahl: letztes Element ignorieren
      pass
---

# Liste in nicht-überlappende Paare

Schreibe `paare(liste)`, die eine Liste in **2-er-Paare** zerlegt.
Bei ungerader Anzahl wird das **letzte Element ignoriert**.

## Beispiele

| Eingabe                  | Ergebnis                          |
|--------------------------|-----------------------------------|
| `[1, 2, 3, 4]`           | `[[1, 2], [3, 4]]`                |
| `[1, 2, 3, 4, 5, 6]`     | `[[1, 2], [3, 4], [5, 6]]`        |
| `[1, 2, 3]`              | `[[1, 2]]` (3 wird ignoriert)     |
| `[]`                     | `[]`                              |
| `[1]`                    | `[]`                              |

## Idee 1 -- Slicing

```python
def paare(liste):
    n = len(liste) // 2 * 2  # gerader Cut
    return [list(liste[i:i + 2]) for i in range(0, n, 2)]
```

## Idee 2 -- zip mit Schritt-Slicing

```python
def paare(liste):
    return [list(p) for p in zip(liste[::2], liste[1::2])]
```

`liste[::2]` sind die Elemente an geraden Indizes (0, 2, 4...),
`liste[1::2]` an ungeraden (1, 3, 5...). `zip` schneidet die
laengere automatisch ab.

## Stolperstein -- Letztes Element bei ungerader Laenge

Beide Varianten ignorieren das letzte Element automatisch -- bei
Idee 1 durch das `// 2 * 2`, bei Idee 2 durch `zip`'s Verhalten.

## Verwandt

| Aufgabe             | Was?                       |
|---------------------|----------------------------|
| **029-chunks**      | k-er-Bloecke (allgemein)   |
| **031-zip-listen**  | zwei Listen verzahnen      |
| **174 alt**         | (gelöscht, war Duplikat)  |
| **237-paare**       | hier, immer 2-er-Paare     |
