---
schema_version: 1
id: 309-primzahlen-gen
revision: 1
titel: Primzahl-Generator bis n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [generator, yield, primzahlen, sieb]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Generator + Sieb-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: primzahlen_bis
hints:
  - kosten: 0
    text: |
      Liefere alle Primzahlen <= n als Liste.
      Intern: Generator mit Sieb des Eratosthenes ODER Trial-Division.
      n < 2 → [].
  - kosten: 24
    text: |
      Sieb: bool-Liste der Größe n+1, false markieren.
      Generator: yield i wenn sieb[i] True.
tests_sichtbar:
  - input: [10]
    expected: [2, 3, 5, 7]
  - input: [1]
    expected: []
  - input: [2]
    expected: [2]
  - input: [20]
    expected: [2, 3, 5, 7, 11, 13, 17, 19]
tests_versteckt:
  - input: [0]
    expected: []
  - input: [-5]
    expected: []
  - input: [3]
    expected: [2, 3]
  - input: [30]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  - input: [50]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  - input: [100]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  - input: [7]
    expected: [2, 3, 5, 7]
starter_code: |
  def primzahlen_bis(n: int) -> list[int]:
      # Tipp: Sieb des Eratosthenes ODER Trial-Division im Generator
      pass
---

# Primzahl-Generator bis n

Schreibe `primzahlen_bis(n)`, die alle **Primzahlen ≤ n** als Liste
liefert -- intern via **Generator** (`yield`).

`n < 2` → `[]`.

## Beispiele

| `n`  | Primzahlen                                           |
|------|------------------------------------------------------|
| `1`  | `[]`                                                 |
| `2`  | `[2]`                                                |
| `10` | `[2, 3, 5, 7]`                                       |
| `20` | `[2, 3, 5, 7, 11, 13, 17, 19]`                       |
| `30` | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`               |
| `50` | `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]` |

Bis 100 gibt es **25 Primzahlen**.

## Idee 1 -- Sieb des Eratosthenes mit Generator

**Wichtig**: Das `yield` kommt **VOR** dem Streichen, sonst
verpasst man `i = 2`. Generator-Logik und Sieb-Logik werden
verschraenkt.

## Idee 2 -- Trial-Division im Generator

Klarer, aber langsamer (`O(n*sqrt(n))` statt `O(n*log log n)`).

## Verwandt

- **039-eratosthenes**: Sieb als reine Listen-Funktion
- **127-primzahlen-bis-n-zahl**: nur die Anzahl
- **309 hier**: Liste mit Generator-Pattern
