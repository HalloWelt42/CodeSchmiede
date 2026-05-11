---
schema_version: 1
id: 314-chain-mit-trenner
revision: 1
titel: Listen verketten mit Trenner-Element
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [generator, yield, listen, chain]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: itertools.chain mit Trenner-Variante
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: verketten_mit_trenner
hints:
  - kosten: 0
    text: |
      Verkette mehrere Listen zu EINER. ZWISCHEN den Listen wird
      ein "trenner"-Element eingefügt. Vor der ersten und nach der
      letzten Liste KEIN Trenner.
      [[1,2], [3,4], [5,6]] mit trenner=0 → [1,2,0,3,4,0,5,6].
      Leere Listen werden geskippt (kein Trenner davor/danach).
      Bei [] (keine Listen) → [].
  - kosten: 25
    text: |
      Generator: Flag erste=True. Pro Liste: wenn nicht erste UND
      vorige war nicht-leer: yield trenner. Dann yield from liste.
tests_sichtbar:
  - input: [[[1, 2], [3, 4]], 0]
    expected: [1, 2, 0, 3, 4]
  - input: [[], 0]
    expected: []
  - input: [[[1, 2, 3]], 0]
    expected: [1, 2, 3]
  - input: [[[1], [2], [3]], 0]
    expected: [1, 0, 2, 0, 3]
tests_versteckt:
  - input: [[[1, 2], [3, 4], [5, 6]], 0]
    expected: [1, 2, 0, 3, 4, 0, 5, 6]
  - input: [[[], []], 99]
    expected: []
  - input: [[[1, 2], [], [3, 4]], 0]
    expected: [1, 2, 0, 3, 4]
  - input: [[[], [1, 2]], 0]
    expected: [1, 2]
  - input: [[[1, 2], []], 0]
    expected: [1, 2]
  - input: [[["a"], ["b"], ["c"]], "-"]
    expected: ["a", "-", "b", "-", "c"]
  - input: [[[1]], 0]
    expected: [1]
starter_code: |
  def verketten_mit_trenner(listen: list[list], trenner) -> list:
      # Tipp: Generator mit yield from + Flag
      pass
---

# Listen verketten mit Trenner-Element

Schreibe `verketten_mit_trenner(listen, trenner)`, die mehrere Listen
zu einer einzigen verkettet -- mit einem **trenner-Element** zwischen
benachbarten Listen.

Regeln:
- Vor der ersten Liste **kein** Trenner.
- Nach der letzten Liste **kein** Trenner.
- **Leere** Listen werden übersprungen (kein Trenner davor/danach).

## Beispiele

| Listen                          | Trenner | Ergebnis                |
|---------------------------------|---------|--------------------------|
| `[[1,2], [3,4], [5,6]]`         | `0`     | `[1,2,0,3,4,0,5,6]`     |
| `[[1], [2], [3]]`               | `0`     | `[1, 0, 2, 0, 3]`       |
| `[[1,2,3]]`                     | `0`     | `[1, 2, 3]`             |
| `[[], []]`                      | `99`    | `[]`                    |
| `[[1,2], [], [3,4]]`            | `0`     | `[1, 2, 0, 3, 4]` (Trenner zwischen 1+3, leere Liste wirkt nicht als Trenner-Stopp) |
| `[["a"], ["b"], ["c"]]`         | `"-"`   | `["a","-","b","-","c"]` |
| `[]`                            | `0`     | `[]`                    |

## Idee -- Generator mit Flag

`yield from` ist eine **delegierende** Yield: liefert alle Werte
des inneren Iterables -- elegant für "leere alle Werte aus dieser
Liste".

`zuerst`-Flag stellt sicher, dass vor der allerersten nicht-leeren
Liste kein Trenner kommt.

## Vergleich -- ohne Trenner

`itertools.chain.from_iterable(listen)` macht die Verkettung **ohne**
Trenner. Mit Trenner ist nicht direkt im Builtin -- daher diese
Aufgabe als Erweiterung.

## Anwendung

- **Pretty-Print** mehrerer Bloecke mit Separator-Zeilen
- **CSV-Generierung** mit Header-Trenner zwischen Sektionen
- **Animations-Loops** mit Pausen-Frames zwischen Aktionen
