---
schema_version: 1
id: 094-decimal-zu-binary
revision: 1
titel: Dezimal zu Binär
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, strings, basis-konvertierung]
pfade: [python_codes]
voraussetzungen: [093-binary-zu-decimal]
quelle:
  url: null
  notiz: Klassische Umkehrung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dezimal_zu_binaer
hints:
  - kosten: 0
    text: |
      Wiederhole: Rest bei Division durch 2 ist die nächste Bit-Ziffer
      von rechts. Dann ganzzahlig durch 2 teilen. Stoppe bei 0.
  - kosten: 7
    text: |
      Verboten: `bin(n)`. Eigene Schleife. Für n=0 → "0" als Sonderfall.
tests_sichtbar:
  - input: [0]
    expected: "0"
  - input: [1]
    expected: "1"
  - input: [10]
    expected: "1010"
  - input: [255]
    expected: "11111111"
tests_versteckt:
  - input: [2]
    expected: "10"
  - input: [4]
    expected: "100"
  - input: [9]
    expected: "1001"
  - input: [1024]
    expected: "10000000000"
  - input: [1128]
    expected: "10001101000"
  - input: [65535]
    expected: "1111111111111111"
starter_code: |
  def dezimal_zu_binaer(n: int) -> str:
      # Deine Lösung hier -- ohne bin() zu verwenden.
      pass
---

# Dezimal zu Binär

Schreibe eine Funktion `dezimal_zu_binaer(n)`, die eine
nicht-negative ganze Zahl als Binär-String zurückgibt.

**Verboten**: `bin(n)`. Eigene Schleife.

## Beispiele

| `n`     | Ergebnis             |
|---------|----------------------|
| `0`     | `"0"`                |
| `1`     | `"1"`                |
| `10`    | `"1010"`             |
| `255`   | `"11111111"`         |
| `1024`  | `"10000000000"`      |

## Idee

```
ziffern = []
while n > 0:
    ziffern.append(str(n % 2))
    n //= 2
return "".join(reversed(ziffern)) or "0"
```

`n = 0` ist der Sonderfall -- die Schleife wird nie betreten,
deshalb das `or "0"` am Ende.
