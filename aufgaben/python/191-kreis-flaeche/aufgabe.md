---
schema_version: 1
id: 191-kreis-flaeche
revision: 1
titel: Kreis-Flaeche und Umfang
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [mathematik, geometrie, runden]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Geometrie-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kreis
hints:
  - kosten: 0
    text: |
      Liefere [flaeche, umfang] eines Kreises mit Radius r.
      Beide auf 2 Nachkommastellen gerundet.
      r < 0 -> [0.0, 0.0]. Verwende math.pi.
  - kosten: 4
    text: |
      flaeche = pi * r^2, umfang = 2 * pi * r.
      [round(flaeche, 2), round(umfang, 2)].
tests_sichtbar:
  - input: [1]
    expected: [3.14, 6.28]
  - input: [0]
    expected: [0.0, 0.0]
  - input: [-5]
    expected: [0.0, 0.0]
  - input: [2]
    expected: [12.57, 12.57]
tests_versteckt:
  - input: [3]
    expected: [28.27, 18.85]
  - input: [10]
    expected: [314.16, 62.83]
  - input: [0.5]
    expected: [0.79, 3.14]
  - input: [100]
    expected: [31415.93, 628.32]
  - input: [7]
    expected: [153.94, 43.98]
starter_code: |
  import math

  def kreis(r: float) -> list[float]:
      # Deine Lösung hier -- [flaeche, umfang] auf 2 Stellen
      pass
---

# Kreis-Flaeche und Umfang

Schreibe `kreis(r)`, die für einen Kreis mit Radius `r` die
**Flaeche** und den **Umfang** als Liste `[flaeche, umfang]`
zurückgibt -- beide auf **2 Nachkommastellen** gerundet.

Bei `r < 0` (oder `r == 0`) → `[0.0, 0.0]`.

## Formeln

$$A = \pi r^2 \qquad U = 2 \pi r$$

## Beispiele

| `r`   | Flaeche | Umfang |
|-------|---------|--------|
| `0`   | `0.0`   | `0.0`  |
| `1`   | `3.14`  | `6.28` |
| `2`   | `12.57` | `12.57`|
| `3`   | `28.27` | `18.85`|
| `10`  | `314.16`| `62.83`|
| `0.5` | `0.79`  | `3.14` |

## Spezialfall r=2

Bei `r = 2` sind Flaeche und Umfang gleich (`12.57`):
$\pi \cdot 4 = 2\pi \cdot 2$. Das ist der einzige Radius, für den
das gilt.

## Hintergrund

Pi war seit der Antike interessant -- Archimedes berechnete es über
Polygone bis auf $3.14$. Heute kennen wir billionen Stellen, aber
für praktische Geometrie reichen 6-15 Stellen vollkommen.
