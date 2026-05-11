---
schema_version: 1
id: 312-drop-while-null
revision: 1
titel: Drop-While null
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [generator, yield, listen, dropwhile]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: itertools.dropwhile nachbauen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: drop_while_null
hints:
  - kosten: 0
    text: |
      Ueberspringe Elemente vom Anfang, SOLANGE sie 0 sind.
      Beim ersten ungleich-0: STOP Skipping, alles ab da behalten
      (auch wenn weitere 0en kommen).
      [0, 0, 0, 1, 0, 2] → [1, 0, 2].
  - kosten: 15
    text: |
      Flag dropping=True. Pro x: if dropping and x==0: skip.
      Sonst dropping=False, yield x.
tests_sichtbar:
  - input: [[0, 0, 0, 1, 0, 2]]
    expected: [1, 0, 2]
  - input: [[]]
    expected: []
  - input: [[1, 2, 3]]
    expected: [1, 2, 3]
  - input: [[0, 0, 0]]
    expected: []
tests_versteckt:
  - input: [[0]]
    expected: []
  - input: [[1, 0]]
    expected: [1, 0]
  - input: [[5, 0, 0]]
    expected: [5, 0, 0]
  - input: [[0, 1, 2, 3]]
    expected: [1, 2, 3]
  - input: [[0, 0, 0, 0, 7]]
    expected: [7]
  - input: [[0, 0, 0, 1, 2, 3, 0, 0, 0]]
    expected: [1, 2, 3, 0, 0, 0]
  - input: [[-1, 0, 1]]
    expected: [-1, 0, 1]
starter_code: |
  def drop_while_null(liste: list[int]) -> list[int]:
      # Tipp: Generator mit Flag fuer "noch im Drop-Modus"
      pass
---

# Drop-While null

Schreibe `drop_while_null(liste)`, die Elemente am Anfang
**uebersprungen**, solange sie `0` sind. Beim ersten Element
**ungleich** `0` wird der Skip-Modus beendet -- ab da werden
alle weiteren Elemente uebernommen, auch wenn `0` darunter sind.

## Beispiele

| Eingabe                       | Ergebnis              |
|-------------------------------|------------------------|
| `[0, 0, 0, 1, 0, 2]`          | `[1, 0, 2]`           |
| `[1, 2, 3]`                   | `[1, 2, 3]`           |
| `[0, 0, 0]`                   | `[]`                  |
| `[0, 0, 0, 1, 2, 3, 0, 0, 0]` | `[1, 2, 3, 0, 0, 0]`  |
| `[-1, 0, 1]`                  | `[-1, 0, 1]` (-1 != 0) |

## Idee -- Generator mit Flag

```python
def drop_while_null(liste):
    def gen():
        dropping = True
        for x in liste:
            if dropping and x == 0:
                continue
            dropping = False
            yield x
    return list(gen())
```

Sobald `dropping = False` gesetzt ist, kommt jedes weitere Element
durch -- auch nullen.

## Mit itertools.dropwhile

```python
from itertools import dropwhile

def drop_while_null(liste):
    return list(dropwhile(lambda x: x == 0, liste))
```

`dropwhile` ist das Standard-Tool fuer dieses Pattern -- spiegelbildlich
zu `takewhile`.

## Vergleich -- takewhile vs dropwhile

Bei `[0, 0, 1, 0, 2]` mit Predicate `x == 0`:

- `takewhile` liefert `[0, 0]` (vorne, solange wahr)
- `dropwhile` liefert `[1, 0, 2]` (uebrig nach Skip vorne)

Zusammen ergeben beide die ganze Liste.

## Anwendung

- Header-Zeilen ueberspringen (Komma getrennt: `# comments` skippen)
- Whitespace-Padding am Anfang entfernen
- "Erst ab erstem echten Wert anfangen"-Logik
