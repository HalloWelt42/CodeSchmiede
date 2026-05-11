---
schema_version: 1
id: 263-zahlen-aus-text
revision: 1
titel: Alle Ganzzahlen aus Text extrahieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [strings, regex, parsing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Regex-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zahlen_extrahieren
hints:
  - kosten: 0
    text: |
      Extrahiere alle GANZZAHLEN aus dem Text -- inkl. negative.
      "abc 123 def -45" → [123, -45].
      Reihenfolge wie im Text.
      Bei keiner Zahl → [].
  - kosten: 12
    text: |
      re.findall(r"-?\d+", text), dann int(s) pro Match.
tests_sichtbar:
  - input: ["abc 123 def 456"]
    expected: [123, 456]
  - input: ["keine Zahlen hier"]
    expected: []
  - input: [""]
    expected: []
  - input: ["nur 42"]
    expected: [42]
tests_versteckt:
  - input: ["Zimmer -1, Tuer -2"]
    expected: [-1, -2]
  - input: ["1 2 3 4 5"]
    expected: [1, 2, 3, 4, 5]
  - input: ["Preis: 12.99 Euro"]
    expected: [12, 99]
  - input: ["IP 192.168.1.1"]
    expected: [192, 168, 1, 1]
  - input: ["Telefon: 0123/4567890"]
    expected: [123, 4567890]
  - input: ["Score: -10 vs +5"]
    expected: [-10, 5]
starter_code: |
  import re

  def zahlen_extrahieren(text: str) -> list[int]:
      # Deine Lösung hier -- inkl. negative Zahlen
      pass
---

# Alle Ganzzahlen aus Text extrahieren

Schreibe `zahlen_extrahieren(text)`, die alle **Ganzzahlen** aus
einem Text extrahiert -- inklusive negativer.

Reihenfolge wie im Text. Bei keiner Zahl → `[]`.

**Hinweis**: Eine Dezimalzahl wie `"12.99"` wird als zwei Ganzzahlen
`[12, 99]` interpretiert, weil `.` kein Ziffer-Zeichen ist und kein
Vorzeichen einleitet.

## Beispiele

| Text                       | Zahlen               |
|----------------------------|----------------------|
| `"abc 123 def 456"`        | `[123, 456]`         |
| `"nur 42"`                 | `[42]`               |
| `"Zimmer -1, Tür -2"`     | `[-1, -2]`           |
| `"Preis: 12.99 Euro"`      | `[12, 99]`           |
| `"IP 192.168.1.1"`         | `[192, 168, 1, 1]`   |
| `"Score: -10 vs +5"`       | `[-10, 5]`           |
| `"keine Zahlen hier"`      | `[]`                 |

## Idee -- Regex

`-?\d+` matcht eine optionale `-` gefolgt von einer oder mehreren
Ziffern. `re.findall` liefert alle Treffer als Liste von Strings,
die wir mit `int(...)` konvertieren.

## Stolperstein -- Vorzeichen

Im Test `"Score: -10 vs +5"` extrahieren wir `[-10, 5]` -- das `+`
wird **nicht** mitgenommen, weil `re.findall(r"-?\d+", ...)` nur
das `-` als Teil der Zahl erkennt. Wer auch `+` mitnehmen will:

## Anwendung

- Log-Parsing: alle HTTP-Status-Codes aus einer Log-Zeile.
- Preis-Listen aus HTML scrapen.
- Sensor-Daten aus Freitext.
