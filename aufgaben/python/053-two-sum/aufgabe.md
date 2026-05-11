---
schema_version: 1
id: 053-two-sum
revision: 1
titel: Two-Sum
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [listen, dict, suche, hashing]
pfade: [python_listen3]
voraussetzungen: [022-wortzaehler]
quelle:
  url: null
  notiz: Klassisches Interview-Problem (LeetCode 1), eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: two_sum
hints:
  - kosten: 0
    text: |
      Gesucht: zwei Indizes, deren Werte sich zur Zielsumme addieren.
      Naive Lösung: doppelte Schleife. O(n^2).
  - kosten: 15
    text: |
      Schneller mit Dict: pro Element prüfen, ob "ziel - x" bereits
      gesehen wurde. Falls ja, Indizes zurückgeben.
  - kosten: 25
    text: |
      ```
      gesehen = {}
      for i, x in enumerate(zahlen):
          rest = ziel - x
          if rest in gesehen:
              return [gesehen[rest], i]
          gesehen[x] = i
      return []
      ```
tests_sichtbar:
  - input: [[2, 7, 11, 15], 9]
    expected: [0, 1]
  - input: [[3, 2, 4], 6]
    expected: [1, 2]
  - input: [[3, 3], 6]
    expected: [0, 1]
  - input: [[1, 2, 3], 100]
    expected: []
tests_versteckt:
  - input: [[], 5]
    expected: []
  - input: [[5], 5]
    expected: []
  - input: [[1, -1, 0], 0]
    expected: [0, 1]
  - input: [[10, 20, 30, 50], 60]
    expected: [0, 3]
  - input: [[2, 7, 11, 15], 17]
    expected: [0, 3]
starter_code: |
  def two_sum(zahlen: list[int], ziel: int) -> list[int]:
      # Deine Lösung hier -- gibt zwei Indizes [i, j] mit i<j zurück,
      # oder [] falls kein Paar existiert.
      pass
---

# Two-Sum

Gegeben eine Liste von Zahlen und eine Zielsumme. Finde **zwei Indizes**
`i < j`, sodass `zahlen[i] + zahlen[j] == ziel`. Gibt es mehrere
gültige Paare, ist jedes davon ein gültiges Ergebnis. Existiert
keines, gib `[]` zurück.

## Beispiele

| Liste            | Ziel | Ergebnis |
|------------------|------|----------|
| `[2,7,11,15]`    | `9`  | `[0,1]`  |
| `[3,2,4]`        | `6`  | `[1,2]`  |
| `[3,3]`          | `6`  | `[0,1]`  |
| `[1,2,3]`        | `100`| `[]`     |
| `[]`             | `5`  | `[]`     |

## Komplexitaet

| Variante     | Zeit     | Speicher |
|--------------|----------|----------|
| Doppelschleife | $O(n^2)$ | $O(1)$   |
| Mit Dict     | $O(n)$   | $O(n)$   |

Das Dict speichert bereits gesehene Werte mit ihrem Index. Pro Element
prüfst du, ob das Komplement (`ziel - x`) schon im Dict ist. Wenn ja,
hast du das Paar.

## Hintergrund

"Two-Sum" ist die **Aufgabe Nr. 1 auf LeetCode** und seit Jahren das
Stoffel-Beispiel für Hashing-Tricks in Interviews. Wer das Pattern
kennt, sieht es überall wieder (Three-Sum, Pair-Differenz, ...).
