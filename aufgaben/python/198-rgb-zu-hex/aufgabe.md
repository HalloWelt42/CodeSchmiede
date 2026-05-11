---
schema_version: 1
id: 198-rgb-zu-hex
revision: 1
titel: RGB-Tripel zu Hex-Farbe
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, zahlen, basis, farben, formatierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 197
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rgb_zu_hex
hints:
  - kosten: 0
    text: |
      Wandle [r, g, b] mit Werten 0-255 in einen Hex-Farbcode "#rrggbb".
      Werte außerhalb 0-255 werden auf den nächsten gültigen Wert
      geclampt. Ausgabe IMMER kleinbuchstabig und mit fuehrendem #.
  - kosten: 8
    text: |
      f"#{r:02x}{g:02x}{b:02x}". max(0, min(255, x)) zum Clampen.
tests_sichtbar:
  - input: [[255, 0, 0]]
    expected: "#ff0000"
  - input: [[0, 255, 0]]
    expected: "#00ff00"
  - input: [[0, 0, 255]]
    expected: "#0000ff"
  - input: [[255, 255, 255]]
    expected: "#ffffff"
tests_versteckt:
  - input: [[0, 0, 0]]
    expected: "#000000"
  - input: [[128, 128, 128]]
    expected: "#808080"
  - input: [[255, 128, 0]]
    expected: "#ff8000"
  - input: [[26, 43, 60]]
    expected: "#1a2b3c"
  - input: [[300, 0, 0]]
    expected: "#ff0000"
  - input: [[-50, 100, 200]]
    expected: "#0064c8"
  - input: [[1, 2, 3]]
    expected: "#010203"
starter_code: |
  def rgb_zu_hex(rgb: list[int]) -> str:
      # Deine Lösung hier -- "#rrggbb" klein, mit Clamping
      pass
---

# RGB-Tripel zu Hex-Farbe

Schreibe `rgb_zu_hex(rgb)`, die ein RGB-Tripel in einen Hex-Farbcode
`"#rrggbb"` umwandelt -- klein und mit fuehrendem `#`.

Werte außerhalb `0..255` werden **geclampt** (auf 0 bzw. 255).

## Beispiele

| RGB                | Hex          |
|--------------------|--------------|
| `[255, 0, 0]`      | `"#ff0000"`  |
| `[0, 0, 0]`        | `"#000000"`  |
| `[128, 128, 128]`  | `"#808080"`  |
| `[26, 43, 60]`     | `"#1a2b3c"`  |
| `[300, 0, 0]`      | `"#ff0000"` (geclampt) |
| `[-50, 100, 200]`  | `"#0064c8"` (geclampt) |

## Idee

Der Format-Specifier `:02x` formatiert eine Zahl als Hex (klein),
mit mindestens **zwei Stellen** -- bei Bedarf mit fuehrender Null.
Für Großbuchstaben: `:02X`.

## Hintergrund -- Wieso Clampen statt Fehler?

In Bildverarbeitung und CSS-Berechnungen entstehen oft kurzzeitig
Werte außerhalb `0..255` (z.B. nach Filter-Anwendung). Sie auf
gültige Werte zu **clampen** ist die üblichste Reaktion -- ein
Error-Throw wäre meist nicht hilfreich.
