---
schema_version: 1
id: 100-yacht-wurf
revision: 1
titel: Yacht-Würfel-Wurf bewerten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [zahlen, listen, dict, spiel]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (yacht), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: yacht_punkte
hints:
  - kosten: 0
    text: |
      Yacht ist ein einfaches Würfelspiel. Pro Wurf 5 Würfel, der Spieler
      wählt eine Wertungs-Kategorie und bekommt entsprechende Punkte.
      Kategorien: zahlen (1-6), full_house, four_of_a_kind, little_straight,
      big_straight, choice, yacht.
  - kosten: 30
    text: |
      Erst Counter() machen, dann pro Kategorie:
      - "ones".."sixes": Anzahl × Wert
      - "full_house": ein Paar + ein Drilling -> Summe aller Würfel, sonst 0
      - "four_of_a_kind": vier gleiche -> 4 × Wert, sonst 0
      - "little_straight": {1,2,3,4,5} -> 30, sonst 0
      - "big_straight": {2,3,4,5,6} -> 30, sonst 0
      - "choice": Summe aller Würfel
      - "yacht": fünf gleiche -> 50, sonst 0
tests_sichtbar:
  - input: [[5, 1, 5, 5, 5], "yacht"]
    expected: 0
  - input: [[1, 1, 1, 1, 1], "yacht"]
    expected: 50
  - input: [[1, 1, 1, 3, 3], "ones"]
    expected: 3
  - input: [[3, 3, 5, 3, 3], "fives"]
    expected: 5
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], "little_straight"]
    expected: 30
  - input: [[2, 3, 4, 5, 6], "big_straight"]
    expected: 30
  - input: [[1, 3, 4, 5, 6], "little_straight"]
    expected: 0
  - input: [[5, 6, 5, 6, 5], "full_house"]
    expected: 27
  - input: [[2, 2, 4, 4, 4], "four_of_a_kind"]
    expected: 0
  - input: [[3, 3, 3, 3, 1], "four_of_a_kind"]
    expected: 12
  - input: [[1, 2, 3, 4, 5], "choice"]
    expected: 15
  - input: [[3, 3, 3, 3, 3], "fours"]
    expected: 0
  - input: [[5, 5, 5, 5, 5], "full_house"]
    expected: 0
starter_code: |
  def yacht_punkte(wurf: list[int], kategorie: str) -> int:
      # Deine Lösung hier -- Kategorien: ones, twos, threes, fours,
      # fives, sixes, full_house, four_of_a_kind, little_straight,
      # big_straight, choice, yacht.
      pass
---

# Yacht-Würfel-Wurf bewerten

Yacht ist ein einfaches Würfelspiel mit fuenf Würfeln. Pro Runde
wählt der Spieler eine **Wertungs-Kategorie** -- die Punktzahl
hängt von der Kategorie und dem Wurf ab.

Schreibe eine Funktion `yacht_punkte(wurf, kategorie)`, die die
Punkte berechnet.

## Kategorien

| Kategorie         | Wertung                                              |
|-------------------|------------------------------------------------------|
| `ones`-`sixes`    | Anzahl der entsprechenden Augenzahl × Wert            |
| `full_house`      | Paar + Drilling: Summe aller Würfel, sonst 0        |
| `four_of_a_kind`  | mind. vier gleiche: 4 × diese Augenzahl, sonst 0     |
| `little_straight` | genau {1,2,3,4,5}: 30, sonst 0                       |
| `big_straight`    | genau {2,3,4,5,6}: 30, sonst 0                       |
| `choice`          | Summe aller Würfel                                  |
| `yacht`           | alle fuenf gleich: 50, sonst 0                       |

## Beispiele

| Wurf            | Kategorie         | Punkte |
|-----------------|-------------------|--------|
| `[1,1,1,1,1]`   | `yacht`           | `50`   |
| `[5,1,5,5,5]`   | `yacht`           | `0`    |
| `[1,1,1,3,3]`   | `ones`            | `3`    |
| `[3,3,5,3,3]`   | `fives`           | `5`    |
| `[5,6,5,6,5]`   | `full_house`      | `27`   |
| `[3,3,3,3,1]`   | `four_of_a_kind`  | `12`   |
| `[1,2,3,4,5]`   | `little_straight` | `30`   |
| `[1,2,3,4,5]`   | `choice`          | `15`   |

## Hintergrund

Yacht ist Vorgaenger von Yahtzee, das in den 1950ern die
amerikanische Familienspielwelt eroberte. Die Punkte-Logik ist
eine schöne Übung in **Kategorisierung + Bedingungen**.
