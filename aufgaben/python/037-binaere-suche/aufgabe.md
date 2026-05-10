---
schema_version: 1
id: 037-binaere-suche
revision: 1
titel: Binaere Suche
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [algorithmen, suche, listen, schleifen]
pfade: [python_algorithmen]
voraussetzungen: [012-listen-sortieren]
quelle:
  url: https://de.wikipedia.org/wiki/Bin%C3%A4re_Suche
  notiz: Klassischer Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: binaere_suche
hints:
  - kosten: 0
    text: |
      Die Liste ist sortiert. Halbiere immer den Suchbereich:
      wenn das Element in der Mitte zu klein ist, suche rechts weiter,
      sonst links.
  - kosten: 15
    text: |
      Variablen `links = 0` und `rechts = len(liste) - 1`. Schleife:
      `mitte = (links + rechts) // 2`. Vergleichen, dann `links` oder
      `rechts` anpassen.
  - kosten: 30
    text: |
      ```
      links, rechts = 0, len(liste) - 1
      while links <= rechts:
          mitte = (links + rechts) // 2
          if liste[mitte] == ziel:
              return mitte
          if liste[mitte] < ziel:
              links = mitte + 1
          else:
              rechts = mitte - 1
      return -1
      ```
tests_sichtbar:
  - input: [[1, 3, 5, 7, 9], 5]
    expected: 2
  - input: [[1, 3, 5, 7, 9], 1]
    expected: 0
  - input: [[1, 3, 5, 7, 9], 9]
    expected: 4
  - input: [[1, 3, 5, 7, 9], 4]
    expected: -1
tests_versteckt:
  - input: [[], 1]
    expected: -1
  - input: [[42], 42]
    expected: 0
  - input: [[42], 17]
    expected: -1
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8]
    expected: 7
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11]
    expected: -1
  - input: [[-100, -50, 0, 50, 100], -50]
    expected: 1
starter_code: |
  def binaere_suche(liste: list[int], ziel: int) -> int:
      # Deine Loesung hier -- Index zurueckgeben oder -1 falls nicht gefunden.
      pass
---

# Binaere Suche

Schreibe eine Funktion `binaere_suche(liste, ziel)`, die in einer
**aufsteigend sortierten** Liste das Ziel sucht und seinen **Index**
zurueckgibt. Falls das Ziel nicht enthalten ist: `-1`.

## Beispiele

| Liste              | Ziel | Ergebnis |
|--------------------|------|----------|
| `[1,3,5,7,9]`      | `5`  | `2`      |
| `[1,3,5,7,9]`      | `1`  | `0`      |
| `[1,3,5,7,9]`      | `9`  | `4`      |
| `[1,3,5,7,9]`      | `4`  | `-1`     |
| `[]`               | `1`  | `-1`     |

## Idee

Halbiere bei jedem Schritt den Suchbereich. Variablen `links`,
`rechts`, `mitte`. Wenn `liste[mitte] == ziel`: gefunden. Sonst eine
der beiden Haelften verwerfen.

## Komplexitaet

Lineare Suche braucht im Worst-Case $O(n)$ Schritte, die binaere
Suche $O(\log n)$. Bei $n = 1.000.000$ ist das der Unterschied
zwischen einer Million und 20 Vergleichen.

> Voraussetzung: die Liste muss sortiert sein. Bei unsortierten Daten
> waere lineare Suche schneller (kein vorheriges Sortieren noetig).
