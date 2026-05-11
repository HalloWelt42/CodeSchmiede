---
schema_version: 1
id: 211-zahl-zu-ziffern
revision: 1
titel: Zahl in Ziffern-Liste zerlegen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [zahlen, listen, modulo, strings]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Ziffer-Verarbeitung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zu_ziffern
hints:
  - kosten: 0
    text: |
      Zerlege eine nicht-negative ganze Zahl in eine Liste ihrer Ziffern,
      höchstwertige zuerst.
      0 -> [0], 12345 -> [1,2,3,4,5]. Negative Zahlen wie ihr Betrag.
  - kosten: 10
    text: |
      Per String: [int(c) for c in str(abs(n))].
      Per Modulo: while n>0 von rechts sammeln + reverse.
tests_sichtbar:
  - input: [0]
    expected: [0]
  - input: [5]
    expected: [5]
  - input: [12345]
    expected: [1, 2, 3, 4, 5]
  - input: [100]
    expected: [1, 0, 0]
tests_versteckt:
  - input: [9]
    expected: [9]
  - input: [10]
    expected: [1, 0]
  - input: [99]
    expected: [9, 9]
  - input: [-123]
    expected: [1, 2, 3]
  - input: [1000000000]
    expected: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - input: [987654321]
    expected: [9, 8, 7, 6, 5, 4, 3, 2, 1]
starter_code: |
  def zu_ziffern(n: int) -> list[int]:
      # Deine Lösung hier -- hoechstwertige Stelle zuerst
      pass
---

# Zahl in Ziffern-Liste zerlegen

Schreibe `zu_ziffern(n)`, die eine nicht-negative ganze Zahl in eine
Liste ihrer **Ziffern** zerlegt -- höchstwertige Stelle zuerst.

`0` → `[0]`. Negative Zahlen werden wie ihr Betrag behandelt.

## Beispiele

| `n`         | Ziffern              |
|-------------|----------------------|
| `0`         | `[0]`                |
| `5`         | `[5]`                |
| `100`       | `[1, 0, 0]`          |
| `12345`     | `[1, 2, 3, 4, 5]`    |
| `-123`      | `[1, 2, 3]`          |
| `987654321` | `[9, 8, 7, 6, 5, 4, 3, 2, 1]` |

## Idee 1 -- per String

```python
def zu_ziffern(n):
    return [int(c) for c in str(abs(n))]
```

Kürzeste Variante -- nutzt aus, dass `str` die Ziffern in
**richtiger Reihenfolge** liefert.

## Idee 2 -- per Modulo

```python
def zu_ziffern(n):
    n = abs(n)
    if n == 0:
        return [0]
    out = []
    while n > 0:
        out.append(n % 10)
        n //= 10
    return list(reversed(out))
```

Das geht **ohne String-Konvertierung**. Wichtig: am Ende umdrehen,
weil wir die niedrigste Stelle zuerst sammeln.

## Pendant -- Ziffern zur Zahl

Aufgabe **212** macht den Weg zurück. Zusammen ist es ein
Round-Trip: `zu_ziffern(212-funktion(zifferliste))`.

## Anwendung

Ziffer-Zerlegung ist die Basis für **Quersumme** (016),
**Armstrong-Zahlen** (042), **Glückliche Zahlen** (141) und viele
weitere zahlentheoretische Aufgaben.
