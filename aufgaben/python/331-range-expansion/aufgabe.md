---
schema_version: 1
id: 331-range-expansion
revision: 1
titel: Bereichs-Notation entpacken
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [strings, parsing, listen, bereiche]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Range_expansion
  notiz: Rosetta Code -- Range expansion
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bereich_entpacken
hints:
  - kosten: 0
    text: |
      Entpacke einen Bereichs-String wie "1-3,5,7-9" in eine Liste
      von Zahlen [1, 2, 3, 5, 7, 8, 9]. Negative Untergrenzen sind
      erlaubt: "-3--1,2,4-6" -> [-3, -2, -1, 2, 4, 5, 6].
      Bei leerem String -> [].
  - kosten: 17
    text: |
      Splitte an "," -- pro Stück prüfen ob Bindestrich (Trenner)
      drin steckt. Bei negativen Untergrenzen ist der Trenner ein
      Bindestrich, der NICHT direkt nach dem ersten Zeichen steht.
tests_sichtbar:
  - input: ["1-3,5,7-9"]
    expected: [1, 2, 3, 5, 7, 8, 9]
  - input: [""]
    expected: []
  - input: ["5"]
    expected: [5]
  - input: ["1-5"]
    expected: [1, 2, 3, 4, 5]
tests_versteckt:
  - input: ["-3--1,2,4-6"]
    expected: [-3, -2, -1, 2, 4, 5, 6]
  - input: ["10-12"]
    expected: [10, 11, 12]
  - input: ["1,2,3"]
    expected: [1, 2, 3]
  - input: ["-5"]
    expected: [-5]
  - input: ["0-0"]
    expected: [0]
  - input: ["1-3,7-9,15"]
    expected: [1, 2, 3, 7, 8, 9, 15]
  - input: ["100-103"]
    expected: [100, 101, 102, 103]
starter_code: |
  def bereich_entpacken(s: str) -> list[int]:
      # Tipp: split an Komma, pro Stueck Bindestrich-Trenner finden
      pass
---

# Bereichs-Notation entpacken

Schreibe `bereich_entpacken(s)`, die einen Bereichs-String in eine
Liste von Ganzzahlen umwandelt.

Format:
- Komma trennt Stücke: `"1-3,5,7-9"`
- Bindestrich trennt Unter- und Obergrenze: `"1-3"` -> `[1, 2, 3]`
- Einzelne Zahlen ohne Bindestrich: `"5"` -> `[5]`
- Negative Untergrenzen: `"-3--1"` -> `[-3, -2, -1]`

Bei leerem String -> `[]`.

## Beispiele

| Eingabe         | Ergebnis                         |
|-----------------|-----------------------------------|
| `"1-3,5,7-9"`   | `[1, 2, 3, 5, 7, 8, 9]`           |
| `"1-5"`         | `[1, 2, 3, 4, 5]`                 |
| `"5"`           | `[5]`                             |
| `"-3--1,2,4-6"` | `[-3, -2, -1, 2, 4, 5, 6]`        |
| `"-5"`          | `[-5]`                            |
| `""`            | `[]`                              |

## Idee

`stück.find("-", 1)` sucht ab Index 1 -- damit wird ein fuehrendes
Minus (negative Untergrenze) **nicht** als Trenner missverstanden.

## Pendant -- Range Extraction

Die umgekehrte Operation gibt's auch in Rosetta:
`[1,2,3,5,7,8,9]` zurück zu `"1-3,5,7-9"`. Tricky weil man
zusammenhängende Folgen erkennen muss.

## Anwendung

- **Drucker-Dialoge**: "Seiten 1-3, 7, 10-15"
- **Cron-Jobs**: "*/5" oder "1-5,10,15"
- **Konfiguration**: Port-Bereiche, IP-Ranges
