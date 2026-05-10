---
schema_version: 1
id: 004-vokale-zaehlen
revision: 1
titel: Vokale zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 8
tags: [strings, schleifen, count]
pfade: [python_strings]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Einsteiger-Aufgabe, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: vokale_zaehlen
hints:
  - kosten: 0
    text: Eine Schleife `for buchstabe in text` durchläuft jeden einzelnen Buchstaben.
  - kosten: 10
    text: Vokale sind a, e, i, o, u. Auch in Großschrift.
  - kosten: 25
    text: |
      Idiomatisch:

      ```
      return sum(1 for c in text.lower() if c in "aeiou")
      ```
tests_sichtbar:
  - input: ["anna"]
    expected: 2
  - input: ["hallo"]
    expected: 2
  - input: [""]
    expected: 0
  - input: ["xyz"]
    expected: 0
tests_versteckt:
  - input: ["AEIOU"]
    expected: 5
  - input: ["python"]
    expected: 1
  - input: ["aaaa"]
    expected: 4
  - input: ["Programmieren"]
    expected: 5
  - input: ["bcdfg"]
    expected: 0
starter_code: |
  def vokale_zaehlen(text: str) -> int:
      # Deine Lösung hier
      pass
---

# Vokale zählen

Schreibe eine Funktion `vokale_zaehlen(text)`, die zählt, wie viele
Vokale (`a`, `e`, `i`, `o`, `u`) im übergebenen String vorkommen --
unabhängig von Groß- oder Kleinschreibung.

## Beispiele

| Eingabe         | Ausgabe |
|-----------------|--------:|
| `"anna"`        | `2`     |
| `"hallo"`       | `2`     |
| `"AEIOU"`       | `5`     |
| `"xyz"`         | `0`     |

## Hinweise

- Die deutschen Umlaute `ä`, `ö`, `ü` zählen in dieser Aufgabe **nicht**
  als Vokale -- nur die fünf ASCII-Vokale.
- Großschreibung soll mitgezählt werden -- entweder über
  `text.lower()` normalisieren oder beide Schreibweisen prüfen.
