---
schema_version: 1
id: 096-groesstes-produkt
revision: 1
titel: Größtes Produkt aufeinanderfolgender Ziffern
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 9
tags: [zahlen, strings, sliding-window, project-euler]
pfade: [python_mathe2]
voraussetzungen: [054-sliding-summe]
quelle:
  url: https://projecteuler.net/problem=8
  notiz: Project Euler 8, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: groesstes_produkt
hints:
  - kosten: 0
    text: |
      Sliding-Window: schau dir alle Fenster der Laenge `n` an,
      multipliziere die Ziffern, behalte das größte Produkt.
  - kosten: 11
    text: |
      `text[i:i+n]` ist das Fenster. `prod = 1`, dann pro Zeichen
      `prod *= int(c)`. Mit `max(...)` über alle Fenster.
tests_sichtbar:
  - input: ["123", 1]
    expected: 3
  - input: ["1027839564", 2]
    expected: 56
  - input: ["73167176531330624919225119674426574742355349194934", 6]
    expected: 23520
  - input: ["0000", 2]
    expected: 0
tests_versteckt:
  - input: ["12345", 5]
    expected: 120
  - input: ["12345", 6]
    expected: -1
  - input: ["", 1]
    expected: -1
  - input: ["123", 0]
    expected: 1
  - input: ["987654321", 3]
    expected: 504
  - input: ["a12", 2]
    expected: -1
starter_code: |
  def groesstes_produkt(text: str, n: int) -> int:
      # Deine Lösung hier -- ungültige Eingaben (Nicht-Ziffern, n > len)
      # → -1. n=0 liefert 1 (leeres Produkt).
      pass
---

# Größtes Produkt aufeinanderfolgender Ziffern

Schreibe eine Funktion `größtes_produkt(text, n)`, die in einem
Ziffern-String das **größte Produkt** von $n$ aufeinanderfolgenden
Ziffern findet.

## Sonderfälle

- Wenn `text` leer ist und `n > 0` → `-1`
- Wenn `n` größer als die String-Länge ist → `-1`
- Wenn `n == 0` → `1` (leeres Produkt)
- Wenn der String nicht-Ziffern enthält → `-1`

## Beispiele

| String          | n  | Ergebnis | Wegen          |
|-----------------|----|---------:|----------------|
| `"123"`         | 1  | `3`      | max einzelne   |
| `"1027839564"`  | 2  | `56`     | "7·8"          |
| `"12345"`       | 5  | `120`    | 1·2·3·4·5      |
| `"0000"`        | 2  | `0`      |                |
| `"123"`         | 0  | `1`      | leeres Produkt |
| `"a12"`         | 2  | `-1`     | ungültig       |

## Hintergrund

Project Euler Problem 8 liefert eine 1000-stellige Zahl und fragt
nach dem größten Produkt 13 aufeinanderfolgender Ziffern.
Antwort: 23.514.624.000.
