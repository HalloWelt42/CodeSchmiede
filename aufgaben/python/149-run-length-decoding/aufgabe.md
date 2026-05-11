---
schema_version: 1
id: 149-run-length-decoding
revision: 1
titel: Run-Length-Decoding
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [strings, parsing, kompression]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 035-run-length (Encoding)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rle_decode
hints:
  - kosten: 0
    text: |
      Eingabe-Format: <Zahl><Zeichen><Zahl><Zeichen>...
      Bsp.: "3a2b1c" -> "aaabbc". Bei leerer Eingabe -> "".
      Mehrstellige Zahlen wie "10a" sind erlaubt.
  - kosten: 15
    text: |
      Einmal durchlaufen: solange aktuelles Zeichen Ziffer, an Zahl
      anhaengen. Sonst: Zahl ist abgeschlossen, Zeichen liegt vor uns,
      n*c an Output anhaengen, Zustand reset.
tests_sichtbar:
  - input: ["3a2b1c"]
    expected: "aaabbc"
  - input: [""]
    expected: ""
  - input: ["1a"]
    expected: "a"
  - input: ["5x"]
    expected: "xxxxx"
tests_versteckt:
  - input: ["10a"]
    expected: "aaaaaaaaaa"
  - input: ["2a3b4c"]
    expected: "aabbbcccc"
  - input: ["1a1b1c"]
    expected: "abc"
  - input: ["3 2!"]
    expected: "   !!"
  - input: ["100z"]
    expected: "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
starter_code: |
  def rle_decode(s: str) -> str:
      # Deine Lösung hier -- mehrstellige Zahlen unterstuetzen
      pass
---

# Run-Length-Decoding

Schreibe eine Funktion `rle_decode(s)`, die einen **lauflaengen-
kodierten String** wieder entpackt.

Format: `<Zahl><Zeichen>` paarweise -- die Zahl kann mehrstellig sein.

## Beispiele

| Eingabe   | Dekodiert                    |
|-----------|------------------------------|
| `"3a2b1c"`| `"aaabbc"`                   |
| `"5x"`    | `"xxxxx"`                    |
| `"10a"`   | `"aaaaaaaaaa"`               |
| `"3 2!"`  | `"   !!"` (Leerzeichen + !)  |
| `""`      | `""`                         |

## Idee

Einmal durchlaufen, Ziffern sammeln, beim ersten Nicht-Ziffer-Zeichen
die Wiederholung erzeugen.

```python
def rle_decode(s):
    teile = []
    zahl = ""
    for c in s:
        if c.isdigit():
            zahl += c
        else:
            teile.append(c * int(zahl))
            zahl = ""
    return "".join(teile)
```

## Pendant: Encoding (Aufgabe 035)

Encoding macht das Umgekehrte -- aus `"aaabbc"` wird `"3a2b1c"`. Wenn
beide Funktionen korrekt sind, gilt fuer alle Strings ohne Ziffern:
`rle_decode(rle_encode(s)) == s`.

## Praxis

Dieses einfache Format steckt z.B. in **PCX-Bildern**, **BMP-Run-Length-
Codierung** und alten **Fax-Standards** (Modified Huffman). Effizient
nur bei Daten mit langen gleichen Laeufen -- bei zufaelligen Daten
oft groesser als das Original.
