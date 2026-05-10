---
schema_version: 1
id: 056-laengste-aufsteigende
revision: 1
titel: Laengste aufsteigende Teilfolge
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [listen, schleifen, monotone-folge]
pfade: [python_listen3]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Variante des LIS-Klassikers, aber zusammenhaengend
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: laengste_aufsteigend
hints:
  - kosten: 0
    text: |
      "Aufsteigend" hier: streng monoton wachsend (jedes Element strikt
      größer als das vorherige). Zusammenhaengend, also direkte
      Nachbarn in der Liste.
  - kosten: 15
    text: |
      Schleife mit "aktuelle Laenge" und "beste Laenge". Wenn
      `liste[i] > liste[i-1]`: aktuell + 1, sonst zurück auf 1.
tests_sichtbar:
  - input: [[1, 2, 3, 1, 2]]
    expected: 3
  - input: [[5, 4, 3, 2, 1]]
    expected: 1
  - input: [[1, 1, 1, 1]]
    expected: 1
  - input: [[]]
    expected: 0
tests_versteckt:
  - input: [[42]]
    expected: 1
  - input: [[1, 2, 3, 4, 5, 6, 7, 8]]
    expected: 8
  - input: [[3, 1, 4, 1, 5, 9, 2, 6]]
    expected: 3
  - input: [[10, 20, 1, 2, 3, 4, 5]]
    expected: 5
starter_code: |
  def laengste_aufsteigend(liste: list[int]) -> int:
      # Deine Lösung hier -- streng monoton, zusammenhaengend.
      pass
---

# Laengste aufsteigende Teilfolge

Schreibe eine Funktion `laengste_aufsteigend(liste)`, die die **Laenge
der laengsten zusammenhaengenden, streng monoton aufsteigenden
Teilfolge** zurueckgibt.

"Streng monoton" heisst: jedes Element ist **größer** als das
vorherige -- nicht gleich. "Zusammenhaengend" heisst: direkte Nachbarn,
keine Luecken.

## Beispiele

| Eingabe              | Ergebnis | Wegen                  |
|----------------------|----------|------------------------|
| `[1,2,3,1,2]`        | `3`      | `[1,2,3]`              |
| `[5,4,3,2,1]`        | `1`      | jedes Einzelelement    |
| `[1,1,1,1]`          | `1`      | nicht streng           |
| `[]`                 | `0`      | leer                   |
| `[3,1,4,1,5,9,2,6]`  | `3`      | `[1,5,9]`              |
| `[10,20,1,2,3,4,5]`  | `5`      | `[1,2,3,4,5]`          |

## Idee

Lineare Schleife, ein Zähler fuer die aktuelle und einer fuer die
beste Laenge. Bei jedem Schritt: ist das aktuelle Element größer als
das vorherige, Zähler hoch; sonst zurück auf 1.

## Variante (nicht zusammenhaengend)

Die "klassische" LIS (Longest Increasing Subsequence, mit Luecken
erlaubt) ist deutlich kniffliger -- $O(n \log n)$ ist optimal, aber
nicht trivial. Diese Aufgabe hier ist die **einfachere Variante** mit
zusammenhaengender Folge.
