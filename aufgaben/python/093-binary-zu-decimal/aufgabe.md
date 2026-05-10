---
schema_version: 1
id: 093-binary-zu-decimal
revision: 1
titel: Binär zu Dezimal
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, strings, basis-konvertierung]
pfade: [python_codes]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (binary), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: binaer_zu_dezimal
hints:
  - kosten: 0
    text: |
      Schleife von rechts: jede 1 traegt $2^i$ bei. Ungültige Zeichen
      (alles außer 0/1) → -1.
  - kosten: 15
    text: |
      Ohne `int(text, 2)` zu nutzen: Schleife mit `enumerate(reversed(text))`,
      summieren wenn Zeichen `'1'` ist.
tests_sichtbar:
  - input: ["1"]
    expected: 1
  - input: ["1010"]
    expected: 10
  - input: ["10001101000"]
    expected: 1128
  - input: ["0"]
    expected: 0
tests_versteckt:
  - input: ["100"]
    expected: 4
  - input: ["1001"]
    expected: 9
  - input: ["11111111"]
    expected: 255
  - input: ["10000000000"]
    expected: 1024
  - input: [""]
    expected: -1
  - input: ["12"]
    expected: -1
  - input: ["1A"]
    expected: -1
  - input: ["10 10"]
    expected: -1
starter_code: |
  def binaer_zu_dezimal(text: str) -> int:
      # Deine Lösung hier -- ungültige Zeichen oder leerer String → -1.
      pass
---

# Binär zu Dezimal

Schreibe eine Funktion `binaer_zu_dezimal(text)`, die einen
Binär-String in seine Dezimal-Zahl umwandelt.

Bei ungültigen Zeichen oder leerer Eingabe → `-1`.

**Verboten**: `int(text, 2)` -- das wäre Cheating. Schreib die
Konvertierung selbst.

## Beispiele

| Eingabe          | Ergebnis |
|------------------|----------|
| `"0"`            | `0`      |
| `"1"`            | `1`      |
| `"1010"`         | `10`     |
| `"11111111"`     | `255`    |
| `"10001101000"`  | `1128`   |
| `""`             | `-1`     |
| `"12"`           | `-1`     |

## Idee

Lies den String von rechts nach links. Jede Position $i$ (0-basiert)
trägt $\text{ziffer} \cdot 2^i$ bei.

## Hintergrund

Binär ist die Sprache, in der **alle Computer** rechnen. Direkt
mit Bits und Basen umgehen zu können, hilft beim Verständnis von
Speicher, Netzwerk-Protokollen und Bitmasken.
