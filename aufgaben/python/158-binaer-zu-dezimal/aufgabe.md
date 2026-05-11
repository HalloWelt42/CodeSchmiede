---
schema_version: 1
id: 158-binaer-zu-dezimal
revision: 1
titel: Binaer zu Dezimal (eigene Implementierung)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [zahlen, basis, strings, schleifen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 157
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zu_dezimal
hints:
  - kosten: 0
    text: |
      Wandle einen Binaer-String ("0"/"1"-Folge) in eine Dezimal-Zahl um.
      "101" → 5, "0" → 0, "11111111" → 255.
      int(s, 2) ist verboten -- selber rechnen!
  - kosten: 10
    text: |
      Horner-Schema: ergebnis = 0; pro Bit ergebnis = 2 * ergebnis + bit.
      Linke Bits zuerst, rechte zuletzt.
tests_sichtbar:
  - input: ["0"]
    expected: 0
  - input: ["1"]
    expected: 1
  - input: ["101"]
    expected: 5
  - input: ["11111111"]
    expected: 255
tests_versteckt:
  - input: ["10"]
    expected: 2
  - input: ["1010"]
    expected: 10
  - input: ["10000"]
    expected: 16
  - input: ["10000000000"]
    expected: 1024
  - input: ["11000000111001"]
    expected: 12345
  - input: ["00000101"]
    expected: 5
starter_code: |
  def zu_dezimal(b: str) -> int:
      # Deine Lösung hier -- ohne int(b, 2)
      pass
---

# Binaer zu Dezimal (eigene Implementierung)

Schreibe eine Funktion `zu_dezimal(b)`, die einen Binaer-String
(`"0"` und `"1"`) in eine Dezimal-Zahl umwandelt -- ohne `int(b, 2)`.

## Beispiele

| Binaer            | Dezimal |
|-------------------|---------|
| `"0"`             | `0`     |
| `"1"`             | `1`     |
| `"101"`           | `5`     |
| `"1010"`          | `10`    |
| `"11111111"`      | `255`   |
| `"10000000000"`   | `1024`  |
| `"00000101"`      | `5`     |

Fuehrende Nullen sollen ignoriert werden.

## Idee -- Horner-Schema

```
ergebnis = 0
fuer jedes bit von links nach rechts:
    ergebnis = 2 * ergebnis + int(bit)
```

Beispiel `"101"`:

| bit | ergebnis vorher | ergebnis nachher |
|-----|-----------------|------------------|
| 1   | 0               | 1                |
| 0   | 1               | 2                |
| 1   | 2               | 5                |

```python
def zu_dezimal(b):
    n = 0
    for c in b:
        n = 2 * n + int(c)
    return n
```

## Warum Horner ueberhaupt?

Statt jede Stelle einzeln mit `2**i` zu multiplizieren (was wiederholt
exponentiert), faltet Horner alles in **eine** Multiplikation und
eine Addition pro Stelle. Linear, ohne Power-Operation -- genau
das, was Hardware-Decoder tun.

## Verallgemeinerung

Mit Basis `b` statt `2` funktioniert das Schema fuer **jede Basis** --
inklusive Hex (mit `int(c, 16)`-Mapping fuer A-F).
