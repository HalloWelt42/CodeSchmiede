---
schema_version: 1
id: 333-string-zahl-inkrement
revision: 1
titel: Numerischen String inkrementieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [strings, zahlen, parsing]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Increment_a_numerical_string
  notiz: Rosetta Code -- Increment a numerical string
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: inkrement
hints:
  - kosten: 0
    text: |
      Erhoehe einen numerischen String um 1 und liefere das Ergebnis
      als String zurueck.
      "499" -> "500", "-1" -> "0", "9999" -> "10000".
      Bei ungueltiger Eingabe -> "".
  - kosten: 5
    text: |
      str(int(s) + 1) und ein try/except um Fehler abzufangen.
tests_sichtbar:
  - input: ["499"]
    expected: "500"
  - input: ["0"]
    expected: "1"
  - input: ["-1"]
    expected: "0"
  - input: ["abc"]
    expected: ""
tests_versteckt:
  - input: ["9999"]
    expected: "10000"
  - input: ["-100"]
    expected: "-99"
  - input: ["1"]
    expected: "2"
  - input: ["999999999999999999"]
    expected: "1000000000000000000"
  - input: [""]
    expected: ""
  - input: ["+5"]
    expected: "6"
  - input: ["12.5"]
    expected: ""
starter_code: |
  def inkrement(s: str) -> str:
      # Tipp: int konvertieren, +1, dann zurueck zu str
      pass
---

# Numerischen String inkrementieren

Schreibe `inkrement(s)`, die einen numerischen String um `1`
erhoeht und das Ergebnis als String zurueckgibt.

Bei ungueltiger Eingabe (Buchstaben, leerer String, Dezimalpunkt)
-> `""`.

## Beispiele

| Eingabe                      | Ergebnis              |
|------------------------------|------------------------|
| `"499"`                      | `"500"`                |
| `"0"`                        | `"1"`                  |
| `"-1"`                       | `"0"`                  |
| `"-100"`                     | `"-99"`                |
| `"9999"`                     | `"10000"`              |
| `"999999999999999999"`       | `"1000000000000000000"`|
| `"+5"`                       | `"6"`                  |
| `"abc"`                      | `""`                   |
| `"12.5"`                     | `""` (kein int)        |
| `""`                         | `""`                   |

## Idee

```python
def inkrement(s):
    try:
        return str(int(s) + 1)
    except ValueError:
        return ""
```

Pythons `int` akzeptiert fuehrendes `+`/`-`, aber kein Dezimalpunkt.
Beliebig grosse Zahlen sind kein Problem -- Python hat unbegrenzte
ganze Zahlen.

## Stolperstein -- in anderen Sprachen

In **C** oder **Java** ist `int` 32 oder 64 Bit -- bei
`"99999999999999999999"` haette man Overflow. In Python passiert
das nie.

In **JavaScript** gibt es seit ES2020 `BigInt`, aber `parseInt`
liefert ein normales Number (bis $2^{53}$). Fuer sehr grosse
Zahlen muss man dort `BigInt(s) + 1n` nutzen.

## Anwendung

- **Versions-Strings** (`"v1.2.3"` -> `"v1.2.4"`)
- **Sequenz-IDs** in Dateinamen
- **Rendering-Iteration** ("frame_0042.png")
