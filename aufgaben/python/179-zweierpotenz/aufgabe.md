---
schema_version: 1
id: 179-zweierpotenz
revision: 1
titel: Ist die Zahl eine Zweierpotenz?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [bits, zahlen, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 231
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_zweierpotenz
hints:
  - kosten: 0
    text: |
      Prüfe ob n eine Zweierpotenz ist (1, 2, 4, 8, 16, ...).
      n <= 0 → False. 1 → True (= 2^0).
      Hinweis: Bit-Trick mit n & (n - 1).
  - kosten: 12
    text: |
      Zweierpotenzen haben in Binaer GENAU EIN gesetztes Bit.
      n & (n - 1) löscht das niedrigste Bit. Wenn 0 herauskommt,
      war es das einzige.
tests_sichtbar:
  - input: [1]
    expected: true
  - input: [16]
    expected: true
  - input: [3]
    expected: false
  - input: [0]
    expected: false
tests_versteckt:
  - input: [2]
    expected: true
  - input: [4]
    expected: true
  - input: [1024]
    expected: true
  - input: [-4]
    expected: false
  - input: [6]
    expected: false
  - input: [1023]
    expected: false
  - input: [536870912]
    expected: true
starter_code: |
  def ist_zweierpotenz(n: int) -> bool:
      # Deine Lösung hier -- O(1) mit Bit-Trick
      pass
---

# Ist die Zahl eine Zweierpotenz?

Schreibe `ist_zweierpotenz(n)`, die `True` zurückgibt, wenn `n`
eine **Zweierpotenz** ist -- `1, 2, 4, 8, 16, 32, ...`.

`n <= 0` → `False`.

## Beispiele

| `n`         | Ergebnis | Binaer       |
|-------------|----------|--------------|
| `1`         | `True`   | `1`          |
| `2`         | `True`   | `10`         |
| `4`         | `True`   | `100`        |
| `1024`      | `True`   | `1` und 10 Nullen |
| `0`         | `False`  | `0`          |
| `-4`        | `False`  | (negativ)    |
| `3`         | `False`  | `11`         |
| `6`         | `False`  | `110`        |

## Idee 1 -- Bit-Trick (O(1))

Eine Zweierpotenz hat in Binaer **genau ein** gesetztes Bit. `n - 1`
hat dann an dieser Stelle und allen tieferen Stellen die Bits
**umgeklappt**. Folge: `n & (n - 1) == 0` genau dann, wenn `n` eine
Zweierpotenz ist (und `n > 0`).

## Idee 2 -- Schleife durch Halbierungen

Eindeutig korrekt, aber `O(log n)` statt `O(1)`.

## Hintergrund

Zweierpotenzen sind in der Informatik allgegenwaertig: Speicher-
Größen (1 KB = 1024 B), Bit-Felder, Hash-Tabellen-Größen.
Der Bit-Trick gehört zum Bewerbungsgespraech-Standard wie der
**Brian-Kernighan**-Trick (Aufgabe 159).
