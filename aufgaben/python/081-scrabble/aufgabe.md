---
schema_version: 1
id: 081-scrabble
revision: 1
titel: Scrabble-Punktzahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [strings, dict, schleifen, spiel]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: https://en.wikipedia.org/wiki/Scrabble_letter_distributions
  notiz: Inspiration aus Exercism (scrabble-score), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: scrabble_punkte
hints:
  - kosten: 0
    text: |
      Engl. Scrabble-Werte: A=E=I=O=U=L=N=R=S=T=1, D=G=2, B=C=M=P=3,
      F=H=V=W=Y=4, K=5, J=X=8, Q=Z=10. Groß/klein egal.
  - kosten: 15
    text: |
      Lookup per Dict. Loop über `wort.upper()`, summiere die Punkte.
tests_sichtbar:
  - input: ["a"]
    expected: 1
  - input: ["A"]
    expected: 1
  - input: ["f"]
    expected: 4
  - input: ["at"]
    expected: 2
tests_versteckt:
  - input: ["zoo"]
    expected: 12
  - input: ["street"]
    expected: 6
  - input: ["quirky"]
    expected: 22
  - input: ["OxyphenButazone"]
    expected: 41
  - input: [""]
    expected: 0
  - input: ["pinata"]
    expected: 8
starter_code: |
  def scrabble_punkte(wort: str) -> int:
      # Deine Lösung hier -- englisches Scrabble.
      pass
---

# Scrabble-Punktzahl

Schreibe eine Funktion `scrabble_punkte(wort)`, die die **Scrabble-Punkte**
des englischen Worts berechnet.

| Buchstaben               | Punkte |
|--------------------------|--------|
| A E I O U L N R S T      | 1      |
| D G                      | 2      |
| B C M P                  | 3      |
| F H V W Y                | 4      |
| K                        | 5      |
| J X                      | 8      |
| Q Z                      | 10     |

Groß-/Kleinschreibung egal. Leerer String → 0.

## Beispiele

| Wort           | Punkte |
|----------------|--------|
| `"a"`          | `1`    |
| `"f"`          | `4`    |
| `"at"`         | `2`    |
| `"zoo"`        | `12`   |
| `"street"`     | `6`    |
| `"quirky"`     | `22`   |
| `"OxyphenButazone"` | `41` |

## Hintergrund

Scrabble wurde 1938 vom amerikanischen Architekten Alfred Butts
erfunden. Die Punkte spiegeln die **Häufigkeit** der Buchstaben im
Englischen wider -- seltene Buchstaben (J, Q, X, Z) bringen viele
Punkte.
