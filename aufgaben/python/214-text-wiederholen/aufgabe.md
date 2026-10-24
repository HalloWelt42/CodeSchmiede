---
schema_version: 1
id: 214-text-wiederholen
revision: 3
titel: Text wiederholen bis Ziel-Länge
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, multiplikation, slicing]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische String-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: wiederhole
hints:
  - kosten: 0
    text: |
      Wiederhole "muster" so oft wie nötig, bis "länge" Zeichen
      zusammenkommen, dann auf länge slicen.
      "ab" mit länge=5 → "ababa".
      Bei muster == "" oder länge <= 0 → "".
  - kosten: 8
    text: |
      anzahl = länge // len(muster) + 1, dann (muster * anzahl)[:länge].
tests_sichtbar:
  - input: ["ab", 5]
    expected: "ababa"
  - input: ["x", 3]
    expected: "xxx"
  - input: ["", 5]
    expected: ""
  - input: ["abc", 0]
    expected: ""
tests_versteckt:
  - input: ["uvw", 8]
    expected: "uvwuvwuv"
  - input: ["a", 100]
    expected: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  - input: ["mnop", 3]
    expected: "mno"
  - input: ["klm", 12]
    expected: "klmklmklmklm"
  - input: ["hi", 1]
    expected: "h"
  - input: ["abc", -1]
    expected: ""
starter_code: |
  def wiederhole(muster: str, laenge: int) -> str:
      # Deine Lösung hier
      pass
---

# Text wiederholen bis Ziel-Länge

Schreibe `wiederhole(muster, laenge)`, die das Muster **so oft
wiederholt** und dann **abschneidet**, dass das Ergebnis genau
`laenge` Zeichen lang ist.

Bei leerem Muster oder `laenge <= 0` → `""`.

## Beispiele

| Muster   | Länge | Ergebnis       |
|----------|--------|----------------|
| `"ab"`   | `5`    | `"ababa"`      |
| `"x"`    | `3`    | `"xxx"`        |
| `"abc"`  | `7`    | `"abcabca"`    |
| `"abcd"` | `3`    | `"abc"` (nur abgeschnitten) |
| `"xyz"`  | `9`    | `"xyzxyzxyz"`  |
| `""`     | `5`    | `""`           |

## Idee - Multiplikation + Slice

Die `+1` stellt sicher, dass wir **mindestens** `laenge` Zeichen haben.
Das Slicing schneidet auf die genaue Länge.

## Beispiel-Rechnung "ab" mit länge=5

`5 // 2 + 1 = 3` → `"ab" * 3 = "ababab"` → `[:5] = "ababa"`.

## Anwendung

Padding-Strings, Banner-Trenner (`"-" * 80`), Mock-Daten generieren,
und der **Cesar-Schlüssel-Trick** in der Vigenere-Chiffre (Aufgabe
105: Schlüssel auf Klartext-Länge bringen).
