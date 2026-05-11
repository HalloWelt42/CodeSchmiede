---
schema_version: 1
id: 140-fisher-yates
revision: 1
titel: Fisher-Yates-Shuffle (mit Seed)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 15
tags: [listen, shuffle, zufall, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Shuffle-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: shuffle_seed
hints:
  - kosten: 0
    text: |
      Mische die Liste mit Fisher-Yates. Verwende random.Random(seed)
      für determinstische Ergebnisse pro seed.
  - kosten: 15
    text: |
      Von hinten nach vorn: für i in range(n-1, 0, -1):
        j = rng.randint(0, i)   # 0..i inkl.
        tausche a[i] und a[j].
      Original-Liste nicht verändern (Kopie!).
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 42]
    expected: [4, 2, 3, 5, 1]
  - input: [[], 0]
    expected: []
  - input: [[7], 99]
    expected: [7]
  - input: [[1, 2], 1]
    expected: [2, 1]
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], 1]
    expected: [3, 4, 5, 1, 2]
  - input: [[1, 2, 3, 4, 5], 7]
    expected: [5, 1, 4, 2, 3]
  - input: [["a", "b", "c"], 5]
    expected: ["a", "b", "c"]
  - input: [[10, 20, 30, 40], 100]
    expected: [10, 30, 40, 20]
  - input: [[1, 2], 0]
    expected: [1, 2]
starter_code: |
  import random

  def shuffle_seed(a: list, seed: int) -> list:
      # Deine Lösung hier -- Fisher-Yates mit random.Random(seed).randint(0, i)
      pass
---

# Fisher-Yates-Shuffle (mit Seed)

Schreibe eine Funktion `shuffle_seed(a, seed)`, die eine **gemischte
Kopie** der Liste zurückgibt -- deterministisch für einen gegebenen
`seed`.

Verwende `random.Random(seed).randint(0, i)` für die Index-Wahl, damit
das Ergebnis exakt reproduzierbar ist.

## Algorithmus (Fisher-Yates / Knuth-Shuffle)

Iteriere von hinten nach vorn. Tausche jedes Element `a[i]` mit einem
zufaellig gewählten Element aus `a[0..i]` (inklusive `i` selbst).

## Wichtig

- **Original nicht verändern** → erst kopieren.
- Bei leerer Liste oder einem Element: unverändert zurückgeben.
- `random.Random(seed)` liefert eine eigene Instanz, keine Beruehrung
  des globalen Generators.

## Hintergrund

Der Algorithmus ist seit 1938 bekannt und in praktisch jeder Standard-
Bibliothek umgesetzt (Python: `random.shuffle`). Trotzdem lohnt sich
das Selbst-Bauen: viele Naiv-Versionen sind subtil verzerrt
(z.B. wenn `j` zufaellig aus `0..n-1` statt `0..i` gewählt wird).
