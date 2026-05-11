---
schema_version: 1
id: 101-zwei-eimer
revision: 1
titel: Zwei-Eimer-Problem
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 25
schaetz_minuten: 18
tags: [bfs, sets, suche, ratsel]
pfade: [python_algorithmen2]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Krug-Problem
  notiz: Inspiration aus Exercism (two-bucket), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zwei_eimer
hints:
  - kosten: 0
    text: |
      Zwei Eimer mit Faessungen `a` und `b`. Du startest mit dem
      Eimer (`'a'` oder `'b'`), der voll gefuellt wird. Danach erlaubt:
      - leere einen Eimer
      - fuelle einen Eimer
      - kippe Wasser von einem in den anderen, bis der eine voll oder
        der andere leer ist
      Finde die minimale Zugzahl, um genau `ziel` Liter in einem Eimer
      zu haben. Verbotener Zustand: Start-Eimer leer + anderer voll
      (nicht erlaubt direkt zurück zum Anfang).
  - kosten: 30
    text: |
      BFS! Zustände: `(a_inhalt, b_inhalt)`. Start: je nach
      `start_eimer` entweder `(a, 0)` oder `(0, b)`. Verbotener
      Folgezustand: der gespiegelte Anfangszustand. Liefere die
      Zugzahl, in welchem Eimer das Ziel ist, und den Inhalt des
      anderen Eimers im Moment des Erfolgs.
tests_sichtbar:
  - input: [3, 5, 1, "a"]
    expected: [4, "a", 5]
  - input: [3, 5, 1, "b"]
    expected: [8, "b", 3]
  - input: [7, 11, 2, "a"]
    expected: [14, "a", 11]
  - input: [2, 3, 4, "a"]
    expected: []
tests_versteckt:
  - input: [7, 11, 2, "b"]
    expected: [18, "b", 7]
  - input: [1, 3, 3, "b"]
    expected: [1, "b", 0]
  - input: [2, 3, 1, "a"]
    expected: [4, "a", 3]
  - input: [2, 3, 1, "b"]
    expected: [2, "b", 2]
starter_code: |
  def zwei_eimer(a: int, b: int, ziel: int, start: str) -> list:
      # Deine Lösung hier -- BFS auf Zustaenden (inhalt_a, inhalt_b).
      # Antwort: [zugzahl, gewinner_eimer, inhalt_anderer_eimer] oder
      # [] wenn unloesbar.
      pass
---

# Zwei-Eimer-Problem

Klassisches Logik-Raetsel: Du hast zwei Eimer mit den Fassungen `a`
und `b` Liter. Du sollst genau `ziel` Liter in einem der Eimer
haben.

Erlaubte Zuege:
- **Fuelle** einen Eimer komplett
- **Leere** einen Eimer komplett
- **Kippe** Wasser von einem in den anderen, bis entweder der
  Quell-Eimer leer oder der Ziel-Eimer voll ist

Zähle die **minimale Zugzahl**. Der erste Zug ist immer das
Fuellen des Start-Eimers (`'a'` oder `'b'`).

**Verboten**: der **gespiegelte Anfangszustand** -- wenn du mit
`'a'` startest und damit `(a, 0)` hast, darfst du niemals den
Zustand `(0, b)` direkt erreichen.

## Antwortformat

Liste `[zugzahl, gewinner_eimer, inhalt_anderer]` oder `[]` wenn
unloesbar.

## Beispiele

| a | b | ziel | start | Ergebnis            |
|---|---|------|-------|---------------------|
| 3 | 5 | 1    | `'a'` | `[4, 'a', 5]`       |
| 3 | 5 | 1    | `'b'` | `[8, 'b', 3]`       |
| 7 | 11| 2    | `'a'` | `[14, 'a', 11]`     |
| 2 | 3 | 4    | `'a'` | `[]` (unloesbar)    |
| 1 | 3 | 3    | `'b'` | `[1, 'b', 0]`       |

## Hintergrund

Das Krug-Problem geht zurück auf das **Mathematische Brettspiel**
des 17. Jahrhunderts. In "Stirb langsam: Jetzt erst recht" lösen
Bruce Willis und Samuel L. Jackson die 4-Liter-Aufgabe mit einem
3- und einem 5-Liter-Eimer.
