---
schema_version: 1
id: 235-erste-n
revision: 1
titel: Erste n Elemente einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags: [listen, slicing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Slicing-Klassiker
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: erste_n
hints:
  - kosten: 0
    text: |
      Liefere die ersten n Elemente einer Liste.
      n <= 0 → []. n > Listenlaenge → ganze Liste.
      Original-Liste nicht verändern.
  - kosten: 5
    text: |
      list(liste[:n]) -- Slicing erledigt alle Sonderfaelle.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 3]
    expected: [1, 2, 3]
  - input: [[1, 2, 3], 0]
    expected: []
  - input: [[1, 2, 3], 10]
    expected: [1, 2, 3]
  - input: [[], 5]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3], 1]
    expected: [1]
  - input: [[1, 2, 3], -1]
    expected: []
  - input: [["a", "b", "c", "d"], 2]
    expected: ["a", "b"]
  - input: [[1, 2, 3, 4, 5], 5]
    expected: [1, 2, 3, 4, 5]
  - input: [[42], 100]
    expected: [42]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4]
    expected: [1, 2, 3, 4]
starter_code: |
  def erste_n(liste: list, n: int) -> list:
      # Deine Lösung hier -- Slicing
      pass
---

# Erste n Elemente einer Liste

Schreibe `erste_n(liste, n)`, die die **ersten n Elemente** einer
Liste zurückgibt.

- `n <= 0` → `[]`
- `n > len(liste)` → ganze Liste
- Original-Liste **nicht** verändern

## Beispiele

| Liste              | n  | Ergebnis        |
|--------------------|----|-----------------|
| `[1, 2, 3, 4, 5]`  | 3  | `[1, 2, 3]`     |
| `[1, 2, 3]`        | 10 | `[1, 2, 3]`     |
| `[1, 2, 3]`        | 0  | `[]`            |
| `[1, 2, 3]`        | -1 | `[]`            |
| `[]`               | 5  | `[]`            |

## Idee

`liste[:n]` verhaelt sich elegant: bei `n > len(liste)` gibt es einfach
die ganze Liste zurück -- kein Out-of-Bounds-Error. `list(...)`
sorgt dafür, dass wir eine **Kopie** liefern (statt einer Slice-Sicht).

## Stolperstein -- Negatives n

`liste[:-1]` wäre "alle außer dem letzten" -- nicht das, was wir
wollen. Darum die explizite Prüfung `n <= 0 → []`.

## Pendant -- Letzte n Elemente

Aufgabe **236-letzte-n** macht das andere Ende.
