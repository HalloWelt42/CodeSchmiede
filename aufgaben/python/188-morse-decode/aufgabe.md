---
schema_version: 1
id: 188-morse-decode
revision: 1
titel: Morse-Code -- zurueck in Text
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [strings, dict, mapping, morse]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 187-morse-encode
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: morse_decode
hints:
  - kosten: 0
    text: |
      Wandle einen Morse-String in Text. Buchstaben mit Leerzeichen
      getrennt, Woerter mit " / ". Ergebnis in GROSSBUCHSTABEN.
      Leere Eingabe → "".
  - kosten: 10
    text: |
      Invertiertes Dict {".-": "A", ...}.
      morse.split(" / ") → fuer jedes Wort split(" ") und mappen.
tests_sichtbar:
  - input: ["... --- ..."]
    expected: "SOS"
  - input: [".... .- .-.. .-.. --- / .-- . .-.. -"]
    expected: "HALLO WELT"
  - input: [""]
    expected: ""
  - input: [".-"]
    expected: "A"
tests_versteckt:
  - input: ["."]
    expected: "E"
  - input: ["-"]
    expected: "T"
  - input: [".---- ..--- ...--"]
    expected: "123"
  - input: [".-- .. . / --. . .... - ..."]
    expected: "WIE GEHTS"
  - input: ["-.-. --- -.. . / .-- ..- -. -.. . .-."]
    expected: "CODE WUNDER"
  - input: ["...---..."]
    expected: ""
starter_code: |
  def morse_decode(morse: str) -> str:
      # Deine Lösung hier
      pass
---

# Morse-Code zurueck in Text

Schreibe `morse_decode(morse)`, die einen Morse-String wieder zu
**Text** zurueckverwandelt.

- Buchstaben sind mit **einem Leerzeichen** getrennt.
- Woerter mit **" / "**.
- Ergebnis: **Grossbuchstaben** (Morse kennt kein Klein/Gross).
- Leere Eingabe → `""`.
- Unbekannte Sequenzen werden ignoriert.

## Beispiele

| Morse                                | Text         |
|--------------------------------------|--------------|
| `"... --- ..."`                      | `"SOS"`      |
| `".... .- .-.. .-.. --- / .-- . .-.. -"` | `"HALLO WELT"` |
| `".---- ..--- ...--"`                | `"123"`      |
| `".-- .. . / --. . .... - ..."`      | `"WIE GEHTS"`|

## Idee

Invertiertes Dict, Wort-fuer-Wort dekodieren:

```python
TABELLE = {".-": "A", "-...": "B", ...}

def morse_decode(morse):
    if not morse:
        return ""
    woerter = []
    for wort in morse.split(" / "):
        zeichen = [TABELLE[t] for t in wort.split() if t in TABELLE]
        if zeichen:
            woerter.append("".join(zeichen))
    return " ".join(woerter)
```

## Stolperstein -- Trennung mit Spaces

Morse hat **drei** Trenner-Stufen:
- **kein** Trenner: zwischen Punkten/Strichen eines Buchstabens.
- **ein Leerzeichen**: zwischen Buchstaben.
- **Drei Leerzeichen** (oder " / "): zwischen Woertern.

Wenn man die Wort-Trenner falsch waehlt (z.B. nur 1 Leerzeichen),
laesst sich der Code nicht mehr eindeutig zerlegen. Darum hier die
explizite `" / "`-Konvention.

## Hintergrund

Morse ist ein **selbst-synchronisierender Code** -- ein einziger
verlorener Punkt verschiebt nur einen Buchstaben, nicht den ganzen
Rest. Das ist mit ein Grund, warum er ueber laute Funkverbindungen
und schlechte Telegraphenleitungen funktionierte.
