---
schema_version: 1
id: 316-counter-most-common
revision: 1
titel: Top-N häufigste Werte
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [counter, dicts, listen, sortieren]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: collections.Counter most_common
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: top_n
hints:
  - kosten: 0
    text: |
      Liefere die N häufigsten Werte als Liste von [wert, anzahl]-Paaren,
      absteigend nach Anzahl. Bei Gleichstand: kleinerer Wert zuerst.
      n <= 0 → []. n > Anzahl unique → alle.
  - kosten: 12
    text: |
      Counter zählt. sorted(c.items(), key=(-anzahl, wert))[:n] sortiert
      nach Anzahl absteigend, bei Gleichstand wert aufsteigend.
tests_sichtbar:
  - input: [[1, 2, 2, 3, 3, 3], 2]
    expected: [[3, 3], [2, 2]]
  - input: [[], 5]
    expected: []
  - input: [[1, 1, 1, 2, 2, 3], 1]
    expected: [[1, 3]]
  - input: [[1, 2, 3], 0]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], 3]
    expected: [[1, 1], [2, 1], [3, 1]]
  - input: [["a", "b", "a", "c", "a"], 2]
    expected: [["a", 3], ["b", 1]]
  - input: [[1, 1, 2, 2, 3, 3], 3]
    expected: [[1, 2], [2, 2], [3, 2]]
  - input: [[7, 7, 7, 7, 7], 5]
    expected: [[7, 5]]
  - input: [[1], 1]
    expected: [[1, 1]]
  - input: [[5, 5, 5, 1, 1], 10]
    expected: [[5, 3], [1, 2]]
starter_code: |
  from collections import Counter

  def top_n(liste: list, n: int) -> list[list]:
      # Tipp: Counter + sortieren mit Tupel-Key (-anzahl, wert)
      pass
---

# Top-N häufigste Werte

Schreibe `top_n(liste, n)`, die die **N häufigsten Werte** als Liste
von `[wert, anzahl]`-Paaren liefert -- absteigend nach Anzahl. Bei
Gleichstand: **kleinerer Wert zuerst**.

`n <= 0` → `[]`. `n` größer als Anzahl unique → alle.

## Beispiele

| Liste                  | n | Ergebnis                       |
|------------------------|---|---------------------------------|
| `[1, 2, 2, 3, 3, 3]`   | 2 | `[[3, 3], [2, 2]]`             |
| `[1, 1, 2, 2, 3, 3]`   | 3 | `[[1, 2], [2, 2], [3, 2]]`     |
| `["a","b","a","c","a"]`| 2 | `[["a", 3], ["b", 1]]`         |
| `[7, 7, 7, 7, 7]`      | 5 | `[[7, 5]]`                     |
| `[5, 5, 5, 1, 1]`      |10 | `[[5, 3], [1, 2]]`             |

## Idee

Tupel-Key sortiert lexikographisch:
- erstes Element: `-anzahl` → absteigend nach Anzahl
- zweites Element: `wert` → bei Gleichstand aufsteigend

## Vergleich mit `Counter.most_common`

`c.most_common(n)` liefert das fast direkt -- aber bei Gleichstand
ist die Reihenfolge **insertion-order** des Counter, nicht lexikographisch
des Werts. Daher hier eigene Sortierung.

## Anwendung

- **Tag-Cloud**: Top 20 Tags zeigen.
- **Log-Analyse**: häufigste Fehler-Codes.
- **Spam-Filter**: häufigste Wörter in markierter Mail.
