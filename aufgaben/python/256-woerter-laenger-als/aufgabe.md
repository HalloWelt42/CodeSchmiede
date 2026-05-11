---
schema_version: 1
id: 256-woerter-laenger-als
revision: 1
titel: Wörter laenger als n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [strings, listen, filter, split]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Text-Filter-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: laenger_als
hints:
  - kosten: 0
    text: |
      Liefere alle Wörter aus dem Text, die LAENGER als n Zeichen sind.
      Reihenfolge wie im Original.
      Mehrfache Whitespaces zählen als ein Trenner.
      Bei text == "" oder n < 0 → [].
  - kosten: 4
    text: |
      [w for w in text.split() if len(w) > n].
tests_sichtbar:
  - input: ["Hallo Welt", 4]
    expected: ["Hallo"]
  - input: ["", 5]
    expected: []
  - input: ["a b c", 0]
    expected: ["a", "b", "c"]
  - input: ["nur kurz", 10]
    expected: []
tests_versteckt:
  - input: ["der schnelle braune Fuchs", 5]
    expected: ["schnelle", "braune"]
  - input: ["ABC AB A", 1]
    expected: ["ABC", "AB"]
  - input: ["Hallo Welt", 0]
    expected: ["Hallo", "Welt"]
  - input: ["python", 5]
    expected: ["python"]
  - input: ["python", 6]
    expected: []
  - input: ["  viele   Leerzeichen   hier  ", 5]
    expected: ["Leerzeichen"]
starter_code: |
  def laenger_als(text: str, n: int) -> list[str]:
      # Deine Lösung hier
      pass
---

# Wörter laenger als n

Schreibe `laenger_als(text, n)`, die alle Wörter aus dem Text
zurückgibt, die **laenger als n Zeichen** sind. Reihenfolge wie
im Original.

`str.split()` ohne Argument trennt an Whitespace und ignoriert
mehrfache Leerzeichen.

## Beispiele

| Text                      | n  | Ergebnis              |
|---------------------------|----|-----------------------|
| `"Hallo Welt"`            | 4  | `["Hallo"]`           |
| `"der schnelle braune Fuchs"` | 5 | `["schnelle", "braune"]` |
| `"ABC AB A"`              | 1  | `["ABC", "AB"]`       |
| `"a b c"`                 | 0  | `["a", "b", "c"]`     |
| `"nur kurz"`              | 10 | `[]`                  |
| `""`                      | 5  | `[]`                  |

## Idee

Die wohl häufigste Form: split + Filter mit Comprehension.

## Pendant

Aufgabe **257-wörter-kürzer-als** macht das Gegenstück mit `<`
statt `>`.

## Anwendung

- **Stop-Word**-Listen erstellen ("nur Wörter > 3 Zeichen filtern").
- **Lesbarkeits-Analyse**: Anteil langer Wörter im Text
  (Flesch-Reading-Ease basiert teils darauf).
- **Tag-Cloud-Vorbereitung**: kurze Fuell-Wörter raus.
