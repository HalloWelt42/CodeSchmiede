---
schema_version: 1
id: 098-diamond-muster
revision: 1
titel: Diamant aus Buchstaben
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [strings, schleifen, ascii, muster]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (diamond), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: diamant
hints:
  - kosten: 0
    text: |
      Für Eingabe `'C'`: Diamant geht von `A` nach `C` und zurück.
      Jede Zeile hat genau zwei gleiche Buchstaben (außer die
      `A`-Zeile, die hat nur eines). Innen Leerzeichen, außerhalb
      Padding zur Symmetrie. Rückgabe als Liste von Zeilen.
  - kosten: 11
    text: |
      Buchstaben-Index: `i = ord(c) - ord('A')`. Outer Padding pro
      Zeile: `n - i` Leerzeichen. Inner Spacing (zwischen den zwei
      Buchstaben): `2*i - 1` Leerzeichen.
tests_sichtbar:
  - input: ["A"]
    expected: ["A"]
  - input: ["B"]
    expected: [" A ", "B B", " A "]
  - input: ["C"]
    expected: ["  A  ", " B B ", "C   C", " B B ", "  A  "]
tests_versteckt:
  - input: ["D"]
    expected: ["   A   ", "  B B  ", " C   C ", "D     D", " C   C ", "  B B  ", "   A   "]
  - input: ["E"]
    expected: ["    A    ", "   B B   ", "  C   C  ", " D     D ", "E       E", " D     D ", "  C   C  ", "   B B   ", "    A    "]
  - input: ["A"]
    expected: ["A"]
starter_code: |
  def diamant(buchstabe: str) -> list[str]:
      # Deine Lösung hier -- Diamond-Muster, Eingabe ist ein einzelner
      # Großbuchstabe A-Z.
      pass
---

# Diamant aus Buchstaben

Schreibe eine Funktion `diamant(buchstabe)`, die einen Diamant-
Buchstaben-Muster als **Liste von Zeilen** zurückgibt.

## Regeln

- Die Spitze ist immer `A`.
- Die Mitte enthält den eingegebenen Buchstaben (z.B. `C`), zweimal
  mit Leerzeichen dazwischen.
- Jede Zeile hat **gleiche Breite** (mit Whitespace gepolstert),
  sodass das Muster ein echter Diamant wird.

## Beispiel `'C'`

```
  A
 B B
C   C
 B B
  A
```

## Beispiel `'D'`

```
   A
  B B
 C   C
D     D
 C   C
  B B
   A
```

## Hintergrund

Diamond ist ein Exercism-Klassiker -- toll für das Verstaendnis
von **Padding**, **Symmetrie** und **String-Multiplikation** in
Python.
