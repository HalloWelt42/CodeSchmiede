---
schema_version: 1
id: 243-zeilen-umkehren
revision: 1
titel: Jede Zeile zeichenweise umdrehen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [strings, listen, slicing, comprehension]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Map-Operation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zeilen_umkehren
hints:
  - kosten: 0
    text: |
      Liefere die Liste mit jeder Zeile zeichenweise umgedreht.
      Reihenfolge der Zeilen bleibt!
      ["abc", "def"] -> ["cba", "fed"].
  - kosten: 4
    text: |
      [z[::-1] for z in zeilen].
tests_sichtbar:
  - input: [["abc", "def"]]
    expected: ["cba", "fed"]
  - input: [[]]
    expected: []
  - input: [[""]]
    expected: [""]
  - input: [["a"]]
    expected: ["a"]
tests_versteckt:
  - input: [["Hallo", "Welt"]]
    expected: ["ollaH", "tleW"]
  - input: [["12345"]]
    expected: ["54321"]
  - input: [["abc", "ab", "a"]]
    expected: ["cba", "ba", "a"]
  - input: [["", "x", "yz"]]
    expected: ["", "x", "zy"]
  - input: [["A B C"]]
    expected: ["C B A"]
starter_code: |
  def zeilen_umkehren(zeilen: list[str]) -> list[str]:
      # Deine Lösung hier
      pass
---

# Jede Zeile zeichenweise umdrehen

Schreibe `zeilen_umkehren(zeilen)`, die für jede Zeile in der Liste
die **Zeichenreihenfolge umdreht**. Die **Reihenfolge der Zeilen**
selbst bleibt erhalten.

## Beispiele

| Eingabe              | Ergebnis             |
|----------------------|----------------------|
| `["abc", "def"]`     | `["cba", "fed"]`     |
| `["Hallo", "Welt"]`  | `["ollaH", "tleW"]`  |
| `["12345"]`          | `["54321"]`          |
| `[""]`               | `[""]`               |
| `[]`                 | `[]`                 |

## Idee

`s[::-1]` ist Pythons Slicing-Trick für **String/Liste umkehren**:
Start, Stop weglassen, Step `-1` -- liest die Sequenz rückwärts.

## Anwendung

- Spiegelschrift-Effekt für Texte/Banner.
- Test-Pattern für Palindrom-Detektoren.
- Praxis bei rechts-nach-links-Sprachen wie Hebraeisch oder Arabisch
  (in echt sind die aber "logisch" links nach rechts gespeichert,
  die Anzeige dreht).
