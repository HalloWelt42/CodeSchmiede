---
schema_version: 1
id: 248-alle-rotationen
revision: 1
titel: Alle Rotationen einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [listen, rotation, slicing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Listen-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: alle_rotationen
hints:
  - kosten: 0
    text: |
      Liefere ALLE n Rotationen einer Liste der Laenge n als
      Liste-of-Lists. Erste ist die Originalliste.
      [1,2,3] → [[1,2,3], [2,3,1], [3,1,2]].
      Bei [] → [].
  - kosten: 10
    text: |
      [list(liste[i:] + liste[:i]) for i in range(len(liste))].
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
  - input: [[1]]
    expected: [[1]]
  - input: [[]]
    expected: []
  - input: [[1, 2]]
    expected: [[1, 2], [2, 1]]
tests_versteckt:
  - input: [["a", "b", "c", "d"]]
    expected: [["a", "b", "c", "d"], ["b", "c", "d", "a"], ["c", "d", "a", "b"], ["d", "a", "b", "c"]]
  - input: [[1, 1, 1]]
    expected: [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
  - input: [[5, 10]]
    expected: [[5, 10], [10, 5]]
  - input: [[1, 2, 3, 4]]
    expected: [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
starter_code: |
  def alle_rotationen(liste: list) -> list[list]:
      # Deine Lösung hier -- erste ist Original, dann je 1 weiter
      pass
---

# Alle Rotationen einer Liste

Schreibe `alle_rotationen(liste)`, die **alle n Rotationen** einer
Liste der Laenge `n` zurückgibt -- die **erste** ist das Original,
jede weitere ist um 1 nach links rotiert.

## Beispiele

| Eingabe   | Alle Rotationen                                  |
|-----------|--------------------------------------------------|
| `[1,2,3]` | `[[1,2,3], [2,3,1], [3,1,2]]`                    |
| `[1,2]`   | `[[1,2], [2,1]]`                                 |
| `[1]`     | `[[1]]`                                          |
| `[]`      | `[]`                                             |
| `[1,1,1]` | `[[1,1,1], [1,1,1], [1,1,1]]` (alle gleich)      |

## Idee -- Slicing

Pro Index `i`: `liste[i:]` ist der Schwanz, `liste[:i]` der Kopf --
zusammengesetzt ergibt das die i-te Rotation.

## Anwendung

- **Necklace-Probleme** in Kombinatorik (wieviele unterschiedliche
  Halsketten gibt es bei k Perlen?).
- **De-Bruijn-Sequenzen** und zyklische Codes.
- **String-Matching**: ist `s2` eine Rotation von `s1`?
  Trick: `s1 + s1` enthält alle Rotationen als Substrings.

## Verwandt

Aufgabe **030-rotation** rotiert die Liste **einmal** um k Stellen.
Hier liefern wir **alle n** Rotationen auf einmal.
