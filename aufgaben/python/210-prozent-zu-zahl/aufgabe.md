---
schema_version: 1
id: 210-prozent-zu-zahl
revision: 1
titel: Prozent-String zur Zahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, strings, parsing, prozent]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 209
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: aus_prozent
hints:
  - kosten: 0
    text: |
      Parse einen Prozent-String wie "50%" zu 0.5.
      Akzeptiere mit/ohne %, mit Komma oder Punkt.
      "50%" → 0.5, "12,5%" → 0.125, "100" → 1.0.
      Bei ungültiger Eingabe → 0.0.
  - kosten: 15
    text: |
      strip("%"), Komma zu Punkt, float(), durch 100.
      In try/except wegen ungültiger Eingaben.
tests_sichtbar:
  - input: ["50%"]
    expected: 0.5
  - input: ["100"]
    expected: 1.0
  - input: ["0%"]
    expected: 0.0
  - input: ["12.5%"]
    expected: 0.125
tests_versteckt:
  - input: ["12,5%"]
    expected: 0.125
  - input: ["-50%"]
    expected: -0.5
  - input: ["150%"]
    expected: 1.5
  - input: [""]
    expected: 0.0
  - input: ["abc"]
    expected: 0.0
  - input: ["  75% "]
    expected: 0.75
  - input: ["33.33%"]
    expected: 0.3333
starter_code: |
  def aus_prozent(s: str) -> float:
      # Deine Lösung hier -- mit/ohne %, Komma oder Punkt
      pass
---

# Prozent-String zur Zahl

Schreibe `aus_prozent(s)`, die einen **Prozent-String** wie `"50%"`
in eine Bruchzahl (`0.5`) umwandelt.

Akzeptiere:
- mit oder ohne `%`-Zeichen
- mit `,` oder `.` als Dezimaltrenner
- mit fuehrenden/nachfolgenden Leerzeichen
- mit Vorzeichen

Bei ungültiger Eingabe → `0.0`.

## Beispiele

| Eingabe      | Ergebnis  |
|--------------|-----------|
| `"50%"`      | `0.5`     |
| `"100"`      | `1.0`     |
| `"12.5%"`    | `0.125`   |
| `"12,5%"`    | `0.125`   |
| `"-50%"`     | `-0.5`    |
| `"  75% "`   | `0.75`    |
| `""`         | `0.0`     |
| `"abc"`      | `0.0`     |

## Idee

```python
def aus_prozent(s):
    s = s.strip().rstrip("%").replace(",", ".")
    try:
        return float(s) / 100
    except ValueError:
        return 0.0
```

Drei Schritte:

1. **Reinigen**: `strip` + `rstrip("%")` + Komma-zu-Punkt.
2. **Parsen**: `float(s)`.
3. **Skalieren**: durch 100.

`try/except ValueError` faengt sowohl leere Strings als auch
Buchstaben-Eingaben.

## Pendant -- Zahl zu Prozent

Aufgabe **209** macht den Weg hin (`0.5 → "50.00%"`). Zusammen
ist es ein **Round-Trip**: `aus_prozent(zu_prozent(x)) == round(x, 4)`
(bis auf Rundungs-Stellen).

## Hintergrund -- Lokalisierung

In Deutschland ist das **Komma** der Dezimaltrenner (`12,5%`),
in den USA der **Punkt** (`12.5%`). Eine robuste Parse-Funktion
sollte beide erkennen -- so machen es z.B. Excel und LibreOffice
beim Import von CSV-Dateien.
