---
schema_version: 1
id: 234-laenge-rekursiv
revision: 1
titel: Listenlaenge rekursiv ohne len
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [rekursion, listen, slicing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Rekursions-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: laenge
hints:
  - kosten: 0
    text: |
      Berechne die Laenge einer Liste OHNE len() oder __len__.
      Klassische Rekursion: leere Liste → 0,
      sonst → 1 + laenge(rest).
  - kosten: 15
    text: |
      def laenge(liste):
          if not liste:
              return 0
          return 1 + laenge(liste[1:])
tests_sichtbar:
  - input: [[]]
    expected: 0
  - input: [[1]]
    expected: 1
  - input: [[1, 2, 3]]
    expected: 3
  - input: [[1, 2, 3, 4, 5]]
    expected: 5
tests_versteckt:
  - input: [["a"]]
    expected: 1
  - input: [["a", "b", "c"]]
    expected: 3
  - input: [[null, null, null]]
    expected: 3
  - input: [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    expected: 10
  - input: [[[1, 2], [3], []]]
    expected: 3
  - input: [[true, false, true]]
    expected: 3
starter_code: |
  def laenge(liste: list) -> int:
      # Deine Lösung hier -- OHNE len() / __len__, REKURSIV
      pass
---

# Listenlaenge rekursiv ohne `len`

Schreibe `laenge(liste)`, die die Anzahl der Elemente einer Liste
zurückgibt -- **ohne** `len()` oder `__len__()` zu nutzen.

**Rekursive Lösung erwartet** (gehört zur didaktischen Idee).

## Beispiele

| Liste              | Laenge |
|--------------------|--------|
| `[]`               | `0`    |
| `[1]`              | `1`    |
| `[1, 2, 3]`        | `3`    |
| `[null, null, null]` | `3` |
| `[[1, 2], [3], []]`| `3` (3 Elemente, egal was drin ist) |

## Idee -- Rekursion

```python
def laenge(liste):
    if not liste:
        return 0
    return 1 + laenge(liste[1:])
```

Klassisches **Divide and Conquer** im Mini-Stil:
- **Basis**: leere Liste → `0`.
- **Schritt**: 1 + Laenge des Rests.

## Iterativer Vergleich

```python
def laenge(liste):
    z = 0
    for _ in liste:
        z += 1
    return z
```

Auch ohne `len`. In der Praxis bevorzugt -- weil Python kein
Tail-Call-Optimization macht und die Rekursion bei sehr langen
Listen den Stack sprengt (`RecursionError`).

## Stolperstein -- Stack-Limit

Pythons Default-Recursion-Limit ist 1000. Eine Liste mit > 1000
Elementen sprengt die rekursive Variante. Mit `sys.setrecursionlimit`
ließe sich das hochsetzen, aber elegant ist das nicht.

## Hintergrund

Rekursion ist ein wichtiger Lernschritt -- vielleicht **das**
schwerste Konzept für Anfänger. Listen-Laenge zu rekursiv zu
implementieren ist die einfachste Form überhaupt -- jede Stufe
schrumpft das Problem garantiert um eins.
