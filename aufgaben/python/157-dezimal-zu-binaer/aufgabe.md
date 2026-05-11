---
schema_version: 1
id: 157-dezimal-zu-binaer
revision: 1
titel: Dezimal zu Binaer (eigene Implementierung)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [zahlen, basis, schleifen, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Basis-Konvertierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zu_binaer
hints:
  - kosten: 0
    text: |
      Konvertiere eine nicht-negative ganze Zahl in ihre
      Binaer-Darstellung als String. 0 -> "0", 1 -> "1",
      5 -> "101", 255 -> "11111111".
      bin() und Format-Strings sind verboten -- selber rechnen!
  - kosten: 15
    text: |
      Wiederholt n % 2 (Rest-Bit) und n //= 2.
      Bits in umgekehrter Reihenfolge sammeln, am Ende drehen.
      Sonderfall n == 0 → "0".
tests_sichtbar:
  - input: [0]
    expected: "0"
  - input: [1]
    expected: "1"
  - input: [5]
    expected: "101"
  - input: [255]
    expected: "11111111"
tests_versteckt:
  - input: [2]
    expected: "10"
  - input: [10]
    expected: "1010"
  - input: [16]
    expected: "10000"
  - input: [1024]
    expected: "10000000000"
  - input: [12345]
    expected: "11000000111001"
  - input: [4]
    expected: "100"
starter_code: |
  def zu_binaer(n: int) -> str:
      # Deine Lösung hier -- ohne bin() oder f"{n:b}"
      pass
---

# Dezimal zu Binaer (eigene Implementierung)

Schreibe eine Funktion `zu_binaer(n)`, die eine nicht-negative ganze
Zahl in ihre **Binaer-Darstellung** als String umwandelt -- ohne
`bin()` oder Format-String.

## Beispiele

| `n`     | Binaer           |
|---------|------------------|
| `0`     | `"0"`            |
| `1`     | `"1"`            |
| `2`     | `"10"`           |
| `5`     | `"101"`          |
| `10`    | `"1010"`         |
| `255`   | `"11111111"`     |
| `1024`  | `"10000000000"`  |

## Idee -- klassisches Divisionsverfahren

```
n      n % 2     n // 2
13      1          6
 6      0          3
 3      1          1
 1      1          0
```

Bits (von unten nach oben gelesen): `1101` → `"1101"`.

```python
def zu_binaer(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))
```

## Verallgemeinerung

Mit Basis `b` statt `2` funktioniert das Verfahren fuer **jede
Zahlenbasis**. Fuer Hex (16) braucht man zusaetzlich die Ziffern
`A-F`. Siehe Aufgabe **159-bit-zaehlen** als Anwendung.

## Hintergrund

Computer rechnen intern binaer -- jede Speicherzelle ist 1 oder 0.
Die Konvertierung zwischen Basen ist die Bruecke zwischen mensch-
lesbaren Zahlen und der Hardware-Realitaet.
