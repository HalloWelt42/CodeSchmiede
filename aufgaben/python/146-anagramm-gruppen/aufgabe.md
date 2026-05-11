---
schema_version: 1
id: 146-anagramm-gruppen
revision: 1
titel: Anagramm-Gruppen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [strings, dicts, gruppieren, sortieren]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Gruppier-Aufgabe (LeetCode 49)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: anagramm_gruppen
hints:
  - kosten: 0
    text: |
      Gruppiere Strings, die zueinander Anagramme sind. Liefere eine
      Liste von Listen. Innere Listen alphabetisch sortiert,
      aeussere Liste sortiert nach erstem Element.
  - kosten: 15
    text: |
      Schluessel = sortierter String. defaultdict(list) sammelt alle
      Strings mit gleichem Schluessel.
tests_sichtbar:
  - input: [["eat", "tea", "tan", "ate", "nat", "bat"]]
    expected: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
  - input: [[]]
    expected: []
  - input: [[""]]
    expected: [[""]]
  - input: [["a"]]
    expected: [["a"]]
tests_versteckt:
  - input: [["abc", "bca", "cab", "xyz"]]
    expected: [["abc", "bca", "cab"], ["xyz"]]
  - input: [["listen", "silent", "enlists", "google", "gooegl"]]
    expected: [["enlists"], ["gooegl", "google"], ["listen", "silent"]]
  - input: [["aaa", "aaa", "aab"]]
    expected: [["aaa", "aaa"], ["aab"]]
  - input: [["abcd", "dcba", "abc", "cba"]]
    expected: [["abc", "cba"], ["abcd", "dcba"]]
starter_code: |
  def anagramm_gruppen(woerter: list[str]) -> list[list[str]]:
      # Deine Lösung hier -- Schluessel = sorted(wort)
      pass
---

# Anagramm-Gruppen

Schreibe eine Funktion `anagramm_gruppen(woerter)`, die eine Liste
von Strings in **Anagramm-Gruppen** zerlegt.

Zwei Strings sind Anagramme, wenn sie dieselben Buchstaben in
gleicher Anzahl enthalten -- nur in anderer Reihenfolge.

## Sortier-Regel der Ausgabe

- **Innere** Listen: alphabetisch sortiert.
- **Aeussere** Liste: sortiert nach dem **ersten Element** jeder
  Gruppe (d.h. nach dem alphabetisch kleinsten Anagramm).

## Beispiele

| Eingabe                                                | Ausgabe                                                  |
|--------------------------------------------------------|----------------------------------------------------------|
| `["eat", "tea", "tan", "ate", "nat", "bat"]`           | `[["ate","eat","tea"], ["bat"], ["nat","tan"]]`          |
| `["abc", "bca", "cab", "xyz"]`                         | `[["abc","bca","cab"], ["xyz"]]`                         |
| `[]`                                                   | `[]`                                                     |
| `[""]`                                                 | `[[""]]`                                                 |

## Idee

Schluessel = die Buchstaben sortiert. Alle Strings mit gleichem
Schluessel landen in derselben Gruppe.

```python
from collections import defaultdict

def anagramm_gruppen(woerter):
    gruppen = defaultdict(list)
    for w in woerter:
        gruppen["".join(sorted(w))].append(w)
    return sorted([sorted(g) for g in gruppen.values()])
```

## Alternative -- Counter als Schluessel

`Counter(w)` waere natuerlicher als Schluessel, ist aber nicht
hashbar. Man muesste `tuple(sorted(Counter(w).items()))` daraus
machen -- in der Praxis langsamer als `sorted(w)` fuer kurze Strings.

## Hintergrund

Variante: bei sehr langen Strings ist ein **Buchstaben-Histogramm** als
Tuple-Schluessel performanter (`O(n)` pro String statt `O(n log n)` durch
sortieren).
