---
schema_version: 1
id: 197-hex-zu-rgb
revision: 1
titel: Hex-Farbe zu RGB-Tripel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [strings, zahlen, basis, farben]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Web-/Grafik-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: hex_zu_rgb
hints:
  - kosten: 0
    text: |
      Wandle einen Hex-Farbcode wie "#ff0000" in [r, g, b] um.
      Akzeptiere mit oder ohne #. Ungueltige Eingaben -> [0, 0, 0].
      Ausgabe: 3 Ints im Bereich 0-255.
  - kosten: 10
    text: |
      lstrip("#") entfernt das #. Pro Komponente int(s, 16).
      Pruefe: Laenge 6 und alle Zeichen Hex.
tests_sichtbar:
  - input: ["#ff0000"]
    expected: [255, 0, 0]
  - input: ["#00ff00"]
    expected: [0, 255, 0]
  - input: ["0000ff"]
    expected: [0, 0, 255]
  - input: ["#ffffff"]
    expected: [255, 255, 255]
tests_versteckt:
  - input: ["#000000"]
    expected: [0, 0, 0]
  - input: ["#808080"]
    expected: [128, 128, 128]
  - input: ["FF8000"]
    expected: [255, 128, 0]
  - input: ["#abc"]
    expected: [0, 0, 0]
  - input: [""]
    expected: [0, 0, 0]
  - input: ["#xyz123"]
    expected: [0, 0, 0]
  - input: ["#1A2B3C"]
    expected: [26, 43, 60]
starter_code: |
  def hex_zu_rgb(s: str) -> list[int]:
      # Deine Lösung hier -- 6-stelliger Hex (mit/ohne #), invalid -> [0,0,0]
      pass
---

# Hex-Farbe zu RGB-Tripel

Schreibe `hex_zu_rgb(s)`, die einen Hex-Farbcode wie `"#ff0000"` in
ein RGB-Tripel `[255, 0, 0]` umwandelt.

- Mit oder ohne fuehrendes `#`.
- Gross-/Kleinschreibung egal.
- Ungueltige Eingabe (falsche Laenge, Nicht-Hex) → `[0, 0, 0]`.

## Beispiele

| Hex          | RGB                  |
|--------------|----------------------|
| `"#ff0000"`  | `[255, 0, 0]`        |
| `"#00ff00"`  | `[0, 255, 0]`        |
| `"0000ff"`   | `[0, 0, 255]`        |
| `"#808080"`  | `[128, 128, 128]`    |
| `"FF8000"`   | `[255, 128, 0]`      |
| `"#1A2B3C"`  | `[26, 43, 60]`       |
| `"#abc"`     | `[0, 0, 0]`          |
| `""`         | `[0, 0, 0]`          |

## Idee

```python
def hex_zu_rgb(s):
    s = s.lstrip("#")
    if len(s) != 6 or not all(c in "0123456789abcdefABCDEF" for c in s):
        return [0, 0, 0]
    return [int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)]
```

## Erweiterung -- Kurzform

In CSS gibt's auch die **Kurzform** `#abc` = `#aabbcc`
(jede Stelle verdoppelt). Die ist hier explizit nicht erlaubt --
sie waere als Erweiterung leicht einbaubar.

## Hintergrund

Hex-Farben sind seit den fruehen 90ern Web-Standard. Vor CSS gab's
sie schon in HTML 1.0 als `<font color="#ff0000">`. Heute sind
sie zusammen mit `rgb()` und `hsl()` die haeufigste Farb-Notation
im Web.
