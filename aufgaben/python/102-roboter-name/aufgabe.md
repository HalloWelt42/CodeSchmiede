---
schema_version: 1
id: 102-roboter-name
revision: 1
titel: Roboter-Name generieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [strings, zufall, format]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (robot-name), eigene Formulierung -- ohne State, deterministisch via Seed
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: roboter_name
hints:
  - kosten: 0
    text: |
      Format: zwei Großbuchstaben + drei Ziffern. Z.B. "RX837".
      Eingabe ist ein `seed` (int). Gleicher Seed → gleicher Name.
  - kosten: 7
    text: |
      `random.Random(seed)` gibt dir einen lokalen Generator. Damit
      `choice('A...Z')` zweimal + `randint(0, 9)` dreimal.
tests_sichtbar:
  - input: [42]
    expected: "UD043"
  - input: [0]
    expected: "MY604"
  - input: [1]
    expected: "ES141"
  - input: [9999]
    expected: "DF123"
tests_versteckt:
  - input: [100]
    expected: "EO726"
  - input: [123456]
    expected: "ZZ402"
  - input: [42]
    expected: "UD043"
starter_code: |
  def roboter_name(seed: int) -> str:
      # Deine Lösung hier -- Format AANNN, deterministisch via random.Random(seed).
      pass
---

# Roboter-Name generieren

Schreibe eine Funktion `roboter_name(seed)`, die einen Roboter-Namen
im Format **zwei Großbuchstaben + drei Ziffern** generiert (z.B.
`"AB123"`).

Der Name muss bei **gleichem Seed reproduzierbar** sein.

## Beispiele

| Seed   | Name      |
|--------|-----------|
| `42`   | `"UD043"` |
| `0`    | `"MY604"` |
| `1`    | `"ES141"` |
| `9999` | `"DF123"` |

## Idee

`random.Random(seed)` ist ein **lokaler Generator** -- er beruehrt
nicht das globale `random`-State. Gut für Tests und parallele
Verarbeitung.

## Hintergrund

Die Original-Aufgabe auf Exercism baut die **Eindeutigkeit** über
einen State: ein Roboter merkt sich seinen Namen, neue müssen
unique sein. Hier vereinfacht: gleicher Seed → gleicher Name,
keine Zustands-Fragen.
