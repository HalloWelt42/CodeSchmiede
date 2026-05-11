---
schema_version: 1
id: 187-morse-encode
revision: 1
titel: Morse-Code -- Text codieren
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
  notiz: Klassische Mapping-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: morse_encode
hints:
  - kosten: 0
    text: |
      Wandle Text in Morse-Code: jeder Buchstabe wird zu Punkten/Strichen,
      Buchstaben getrennt durch ein Leerzeichen, Wörter durch " / ".
      Eingabe Groß/Klein egal. Unbekannte Zeichen ignorieren.
  - kosten: 15
    text: |
      Dict {"A": ".-", "B": "-...", ...}.
      text.upper().split() → pro Wort jeden Buchstaben mappen,
      mit Leerzeichen joinen → Wörter mit " / " joinen.
tests_sichtbar:
  - input: ["SOS"]
    expected: "... --- ..."
  - input: ["HALLO WELT"]
    expected: ".... .- .-.. .-.. --- / .-- . .-.. -"
  - input: [""]
    expected: ""
  - input: ["A"]
    expected: ".-"
tests_versteckt:
  - input: ["E"]
    expected: "."
  - input: ["T"]
    expected: "-"
  - input: ["sos"]
    expected: "... --- ..."
  - input: ["123"]
    expected: ".---- ..--- ...--"
  - input: ["WIE GEHTS"]
    expected: ".-- .. . / --. . .... - ..."
  - input: ["Hallo, Welt!"]
    expected: ".... .- .-.. .-.. --- / .-- . .-.. -"
starter_code: |
  def morse_encode(text: str) -> str:
      # Deine Lösung hier -- A-Z + 0-9, Worttrenner " / "
      pass
---

# Morse-Code: Text codieren

Schreibe `morse_encode(text)`, die einen Text in **Morse-Code**
umwandelt:

- Jeder Buchstabe wird zu einer Folge aus `.` und `-`.
- Buchstaben werden mit **einem Leerzeichen** getrennt.
- Wörter (durch Leerzeichen im Original) werden mit **" / "** getrennt.
- Groß/Klein wird zu Groß.
- **Unbekannte Zeichen** (Satzzeichen, Umlaute) werden ignoriert.

## Code-Tabelle

```
A .-      H ....    O ---     V ...-     1 .----    6 -....
B -...    I ..      P .--.    W .--      2 ..---    7 --...
C -.-.    J .---    Q --.-    X -..-     3 ...--    8 ---..
D -..     K -.-     R .-.     Y -.--     4 ....-    9 ----.
E .       L .-..    S ...     Z --..     5 .....    0 -----
F ..-.    M --      T -
G --.     N -.      U ..-
```

## Beispiele

| Text          | Morse                                |
|---------------|--------------------------------------|
| `"SOS"`       | `"... --- ..."`                      |
| `"HALLO WELT"`| `".... .- .-.. .-.. --- / .-- . .-.. -"` |
| `"E"`         | `"."`                                |
| `"123"`       | `".---- ..--- ...--"`                |

## Idee

```python
TABELLE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
}

def morse_encode(text):
    wörter = []
    for wort in text.upper().split():
        teile = [TABELLE[c] for c in wort if c in TABELLE]
        if teile:
            wörter.append(" ".join(teile))
    return " / ".join(wörter)
```

## Hintergrund

Samuel Morse erfand den Code 1838 zusammen mit Alfred Vail. Die
Buchstabenlaenge ist **anti-proportional zur Häufigkeit** im
Englischen -- **E** (`.`) und **T** (`-`) sind am kürzesten,
weil am häufigsten. Damit ist Morse einer der ersten praktisch
genutzten **Variable-Length-Codes** -- ein Vorlaeufer von Huffman.
