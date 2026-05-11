---
schema_version: 1
id: 165-tuerme-von-hanoi
revision: 1
titel: Türme von Hanoi (Zugfolge)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 15
tags: [rekursion, algorithmen, klassiker]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Rekursionsaufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: hanoi
hints:
  - kosten: 0
    text: |
      Liefere die Zugfolge für die Türme von Hanoi mit n Scheiben.
      Stab-Namen "A", "B", "C" (von, über, nach).
      Format pro Zug: (von, nach), z.B. ("A", "C").
      Bei n == 0 → []. n == 1 → [("A", "C")].
  - kosten: 15
    text: |
      Klassische Rekursion:
      hanoi(n, von, über, nach) =
        hanoi(n-1, von, nach, über)
        + [(von, nach)]
        + hanoi(n-1, über, von, nach)
tests_sichtbar:
  - input: [0]
    expected: []
  - input: [1]
    expected: [["A", "C"]]
  - input: [2]
    expected: [["A", "B"], ["A", "C"], ["B", "C"]]
  - input: [3]
    expected: [["A", "C"], ["A", "B"], ["C", "B"], ["A", "C"], ["B", "A"], ["B", "C"], ["A", "C"]]
tests_versteckt:
  - input: [4]
    expected: [["A", "B"], ["A", "C"], ["B", "C"], ["A", "B"], ["C", "A"], ["C", "B"], ["A", "B"], ["A", "C"], ["B", "C"], ["B", "A"], ["C", "A"], ["B", "C"], ["A", "B"], ["A", "C"], ["B", "C"]]
  - input: [5]
    expected: [["A", "C"], ["A", "B"], ["C", "B"], ["A", "C"], ["B", "A"], ["B", "C"], ["A", "C"], ["A", "B"], ["C", "B"], ["C", "A"], ["B", "A"], ["C", "B"], ["A", "C"], ["A", "B"], ["C", "B"], ["A", "C"], ["B", "A"], ["B", "C"], ["A", "C"], ["B", "A"], ["C", "B"], ["C", "A"], ["B", "A"], ["B", "C"], ["A", "C"], ["A", "B"], ["C", "B"], ["A", "C"], ["B", "A"], ["B", "C"], ["A", "C"]]
starter_code: |
  def hanoi(n: int, von: str = "A", ueber: str = "B", nach: str = "C") -> list:
      # Deine Lösung hier -- Liste von [von, nach]-Paaren
      pass
---

# Türme von Hanoi (Zugfolge)

Schreibe eine Funktion `hanoi(n)`, die für das klassische
**Türme-von-Hanoi**-Problem die komplette Zugfolge zurückgibt.

Drei Stuetzen `A`, `B`, `C`. Zu Beginn liegen `n` Scheiben (groß
unten, klein oben) auf `A`. Ziel: alle nach `C`. Regeln:

1. Pro Zug nur eine Scheibe.
2. Nie eine größere auf eine kleinere.

## Format

Pro Zug ein Paar `[von, nach]`, z.B. `["A", "C"]`.
Bei `n == 0` → `[]`.

## Beispiele

`n = 1`: `[["A", "C"]]`

`n = 2`:
```
A → B   (kleine Scheibe weg)
A → C   (große Scheibe ans Ziel)
B → C   (kleine drüber)
```

`n = 3`: 7 Zuege. `n = 4`: 15. `n = 10`: 1023. Allgemein: $2^n - 1$.

## Idee -- Rekursion

Um `n` Scheiben von `von` nach `nach` zu bringen:

1. Bringe `n-1` Scheiben von `von` nach `über` (nutze `nach` als Zwischenlager).
2. Bewege die unterste Scheibe von `von` nach `nach`.
3. Bringe die `n-1` Scheiben von `über` nach `nach` (nutze `von` als Zwischenlager).

```python
def hanoi(n, von="A", über="B", nach="C"):
    if n == 0:
        return []
    return (
        hanoi(n - 1, von, nach, über)
        + [[von, nach]]
        + hanoi(n - 1, über, von, nach)
    )
```

## Anekdote

Der Legende nach lösen Moenche im Tempel von Brahma das Ratsel mit
**64 Scheiben**. Bei einem Zug pro Sekunde dauert das $2^{64}-1$
Sekunden -- über 580 Milliarden Jahre. Wenn die Moenche fertig sind,
ist das Ende der Welt da.
