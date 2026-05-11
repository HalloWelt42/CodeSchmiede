---
schema_version: 1
id: 134-klammer-tiefe
revision: 1
titel: Maximale Klammer-Tiefe
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [strings, schleifen, max, parsing]
pfade: [python_algorithmen2]
voraussetzungen: [115-klammer-balance]
quelle:
  url: null
  notiz: Variation des Klammer-Pruefers
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: max_tiefe
hints:
  - kosten: 0
    text: |
      Nur runde Klammern () zaehlen. Andere Zeichen ignorieren.
      Maximale Verschachtelungstiefe.
  - kosten: 10
    text: |
      Tiefe-Counter, max-Tracker. ( -> tiefe += 1, max ggf. updaten.
      ) -> tiefe -= 1.
tests_sichtbar:
  - input: [""]
    expected: 0
  - input: ["()"]
    expected: 1
  - input: ["(())"]
    expected: 2
  - input: ["((()))"]
    expected: 3
tests_versteckt:
  - input: ["()()()"]
    expected: 1
  - input: ["(()(()()))"]
    expected: 3
  - input: ["abc"]
    expected: 0
  - input: ["(a + (b * (c - d)))"]
    expected: 3
  - input: ["((((((1))))))"]
    expected: 6
starter_code: |
  def max_tiefe(text: str) -> int:
      # Deine Lösung hier -- nur ( und ) zaehlen.
      pass
---

# Maximale Klammer-Tiefe

Schreibe eine Funktion `max_tiefe(text)`, die die **maximale
Verschachtelungstiefe** runder Klammern im Text zurueckgibt.

Andere Zeichen werden ignoriert. Wir nehmen an, dass die Klammern
korrekt verschachtelt sind.

## Beispiele

| Eingabe              | Tiefe |
|----------------------|-------|
| `""`                 | `0`   |
| `"()"`               | `1`   |
| `"(())"`             | `2`   |
| `"((()))"`           | `3`   |
| `"()()()"`           | `1`   |
| `"(a + (b * (c - d)))"` | `3` |
| `"abc"`              | `0`   |

## Idee

Counter pro Zeichen:
- `(` → tiefe + 1, ggf. max updaten
- `)` → tiefe - 1
- alles andere → ignorieren

## Anwendung

In Editoren wird die maximale Tiefe oft als Indikator fuer **Code-
Komplexitaet** genommen -- tief verschachtelter Code ist schwerer
zu lesen.
