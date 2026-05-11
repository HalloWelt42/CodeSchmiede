---
schema_version: 1
id: 180-string-add
revision: 1
titel: Grosse Zahlen als Strings addieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 15
tags: [strings, zahlen, schleifen, simulation]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 415 -- Add Strings
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zahl_addieren
hints:
  - kosten: 0
    text: |
      Addiere zwei nicht-negative ganze Zahlen, die als Strings
      vorliegen. Liefere das Ergebnis als String.
      VERBOTEN: int(...) oder ähnliche Builtins.
      Selbst Stelle fuer Stelle rechnen wie in der Schule.
  - kosten: 20
    text: |
      Von rechts nach links addieren. Ueber-Trag merken.
      ord(c) - ord('0') liefert die Ziffer als int.
      Am Ende: Ergebnis-Liste umdrehen + zusammenfuegen.
tests_sichtbar:
  - input: ["0", "0"]
    expected: "0"
  - input: ["1", "1"]
    expected: "2"
  - input: ["456", "77"]
    expected: "533"
  - input: ["999", "1"]
    expected: "1000"
tests_versteckt:
  - input: ["123456789", "987654321"]
    expected: "1111111110"
  - input: ["0", "12345"]
    expected: "12345"
  - input: ["99", "99"]
    expected: "198"
  - input: ["1000000000000000", "1"]
    expected: "1000000000000001"
  - input: ["50", "50"]
    expected: "100"
  - input: ["5", "5"]
    expected: "10"
starter_code: |
  def zahl_addieren(a: str, b: str) -> str:
      # Deine Lösung hier -- ohne int(), Stelle fuer Stelle
      pass
---

# Grosse Zahlen als Strings addieren

Schreibe `zahl_addieren(a, b)`, die zwei nicht-negative ganze Zahlen
addiert -- aber **die Eingaben und Ausgabe sind Strings**.

**Verboten**: `int(a) + int(b)` oder vergleichbare Tricks. Du sollst
**Stelle fuer Stelle** addieren wie auf dem Block.

## Beispiele

| `a`               | `b`           | Summe (String)        |
|-------------------|---------------|------------------------|
| `"1"`             | `"1"`         | `"2"`                  |
| `"456"`           | `"77"`        | `"533"`                |
| `"999"`           | `"1"`         | `"1000"`               |
| `"123456789"`     | `"987654321"` | `"1111111110"`         |
| `"0"`             | `"0"`         | `"0"`                  |

## Idee -- Schule-Algorithmus

Von **rechts nach links** Stelle fuer Stelle addieren, Ueber-Trag
merken.

```python
def zahl_addieren(a, b):
    i, j = len(a) - 1, len(b) - 1
    uebertrag = 0
    teile = []
    while i >= 0 or j >= 0 or uebertrag:
        za = ord(a[i]) - ord("0") if i >= 0 else 0
        zb = ord(b[j]) - ord("0") if j >= 0 else 0
        s = za + zb + uebertrag
        teile.append(str(s % 10))
        uebertrag = s // 10
        i -= 1
        j -= 1
    return "".join(reversed(teile))
```

## Warum nicht `int()`?

In Sprachen wie C oder Java gibt es keinen unbegrenzten Integer-Typ.
Wer dort eine `200`-stellige Zahl addieren will, **muss** Stelle fuer
Stelle rechnen. Pythons `int` koennte das zwar -- aber genau dieses
Pattern (Big-Number, GMP, RSA-Math) baut auf der Schul-Methode auf.

## Verwandt

- **180-string-add** (diese Aufgabe)
- **String-Multiplikation** (LeetCode 43)
- **String-Subtraktion** (mit Vorzeichen)
- Implementierung von **Big-Integer-Bibliotheken**.
