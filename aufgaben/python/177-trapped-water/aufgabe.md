---
schema_version: 1
id: 177-trapped-water
revision: 1
titel: Regenwasser im Histogramm
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 65
schaetz_minuten: 25
tags: [listen, two-pointers, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 42 -- Trapping Rain Water
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: regenwasser
hints:
  - kosten: 0
    text: |
      Gegeben ist ein Hoehenprofil. Berechne die Regenwasser-Menge,
      die zwischen den Saeulen gefangen wird (1 Einheit Breite).
      Beispiel [0,1,0,2,1,0,1,3,2,1,2,1] -> 6.
  - kosten: 25
    text: |
      Two-Pointers-Trick: links/rechts wandern.
      Pro Schritt die kleinere Seite verarbeiten:
      hoehe < bisheriges_max -> Wasser dazwischen,
      sonst max aktualisieren. O(n), O(1) Speicher.
tests_sichtbar:
  - input: [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
    expected: 6
  - input: [[]]
    expected: 0
  - input: [[1, 2, 3, 4]]
    expected: 0
  - input: [[4, 2, 0, 3, 2, 5]]
    expected: 9
tests_versteckt:
  - input: [[3, 0, 3]]
    expected: 3
  - input: [[5, 4, 1, 2]]
    expected: 1
  - input: [[0]]
    expected: 0
  - input: [[2, 2, 2]]
    expected: 0
  - input: [[5, 0, 0, 0, 0, 5]]
    expected: 20
  - input: [[1, 0, 1]]
    expected: 1
  - input: [[5, 4, 3, 2, 1]]
    expected: 0
starter_code: |
  def regenwasser(hoehen: list[int]) -> int:
      # Deine Lösung hier -- Two-Pointers in O(n)
      pass
---

# Regenwasser im Histogramm

Stell dir ein Hoehenprofil vor, in dem jede Saeule 1 Einheit breit
ist. Wenn es regnet, sammeln sich Wasser-Einheiten **zwischen** den
Saeulen. Wieviel Wasser bleibt insgesamt liegen?

## Beispiel

```
        █
█       █ █
█   █ █ █ █ █
█ █ █ █ █ █ █ █
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
```

Antwort: **6** Einheiten.

## Beispiele

| Hoehen                              | Regenwasser |
|-------------------------------------|-------------|
| `[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]` | `6`      |
| `[4, 2, 0, 3, 2, 5]`                | `9`         |
| `[5, 0, 0, 0, 0, 5]`                | `20`        |
| `[1, 2, 3, 4]`                      | `0`         |
| `[5, 4, 3, 2, 1]`                   | `0`         |

## Idee -- Two Pointers (O(n) Zeit, O(1) Speicher)

Pro Position wuerde sich Wasser auf **min(max-links, max-rechts) -
hoehe** sammeln. Naive Loesung: zwei Praefix-Arrays mit den jeweiligen
Maxima -- `O(n)` Zeit, `O(n)` Speicher. Kuerzer per Two-Pointers:

```python
def regenwasser(hoehen):
    if not hoehen:
        return 0
    links, rechts = 0, len(hoehen) - 1
    max_l = max_r = 0
    wasser = 0
    while links <= rechts:
        if hoehen[links] < hoehen[rechts]:
            if hoehen[links] >= max_l:
                max_l = hoehen[links]
            else:
                wasser += max_l - hoehen[links]
            links += 1
        else:
            if hoehen[rechts] >= max_r:
                max_r = hoehen[rechts]
            else:
                wasser += max_r - hoehen[rechts]
            rechts -= 1
    return wasser
```

Wir bewegen immer den **kleineren** Zeiger -- die Begrenzung kommt
also garantiert von der anderen Seite. So sparen wir uns die
Praefix-Arrays.

## Hintergrund

Klassische **Algorithmus-Olympiade**-Aufgabe. Veranschaulicht zwei
wichtige Patterns: **Praefix-Maxima** und **Two Pointers**.
Aequivalent in 2D ist die "Trapping Rain Water II"-Aufgabe, die
einen Heap braucht.
