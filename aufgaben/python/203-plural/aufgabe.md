---
schema_version: 1
id: 203-plural
revision: 1
titel: Singular oder Plural waehlen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [strings, formatierung, sprache]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische i18n-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: plural
hints:
  - kosten: 0
    text: |
      Liefere "n singular" bei n == 1, sonst "n plural".
      Beispiel: plural(1, "Apfel", "Aepfel") -> "1 Apfel".
              plural(2, "Apfel", "Aepfel") -> "2 Aepfel".
      0 zaehlt als plural: "0 Aepfel".
      Negative Zahlen wie der Betrag, Vorzeichen bleibt:
      plural(-1, ...) -> "-1 singular".
  - kosten: 10
    text: |
      Pruefe abs(n) == 1, dann singular, sonst plural.
      Format-String f"{n} {wort}".
tests_sichtbar:
  - input: [1, "Apfel", "Aepfel"]
    expected: "1 Apfel"
  - input: [2, "Apfel", "Aepfel"]
    expected: "2 Aepfel"
  - input: [0, "Apfel", "Aepfel"]
    expected: "0 Aepfel"
  - input: [-1, "Tag", "Tage"]
    expected: "-1 Tag"
tests_versteckt:
  - input: [3, "Hund", "Hunde"]
    expected: "3 Hunde"
  - input: [1, "Frau", "Frauen"]
    expected: "1 Frau"
  - input: [10, "Kind", "Kinder"]
    expected: "10 Kinder"
  - input: [-5, "Stunde", "Stunden"]
    expected: "-5 Stunden"
  - input: [100, "Buch", "Buecher"]
    expected: "100 Buecher"
  - input: [1, "Stueck", "Stuecke"]
    expected: "1 Stueck"
starter_code: |
  def plural(n: int, singular: str, plural: str) -> str:
      # Deine Lösung hier -- "n form" ; abs(n) == 1 -> singular
      pass
---

# Singular oder Plural waehlen

Schreibe `plural(n, singular, plural)`, die ein passendes
**Mehrzahl-Formular** zusammensetzt:

- `n == 1` (oder `n == -1`) → `"n singular"`
- alles andere → `"n plural"`

Negativzahlen verhalten sich wie ihr Betrag, das Vorzeichen bleibt.

## Beispiele

| `n`   | Singular | Plural   | Ergebnis        |
|-------|----------|----------|-----------------|
| `1`   | `Apfel`  | `Aepfel` | `"1 Apfel"`     |
| `2`   | `Apfel`  | `Aepfel` | `"2 Aepfel"`    |
| `0`   | `Apfel`  | `Aepfel` | `"0 Aepfel"`    |
| `-1`  | `Tag`    | `Tage`   | `"-1 Tag"`      |
| `100` | `Buch`   | `Buecher`| `"100 Buecher"` |

## Idee

```python
def plural(n, singular, plural):
    wort = singular if abs(n) == 1 else plural
    return f"{n} {wort}"
```

## Hintergrund -- i18n

In manchen Sprachen gibt es **mehr als zwei** Plural-Formen
(z.B. Russisch: 1, 2-4, 5-20, dann zyklisch). Frameworks wie
**ICU MessageFormat** unterstuetzen das. Im Deutschen reichen
zwei Formen.

## Erweiterung

Eine "smarte" Variante koennte den Plural automatisch ableiten:
"Hund" → "Hunde" (e anhaengen). Das funktioniert aber nur fuer
einen Bruchteil der Substantive -- in der Praxis ist explizite
Angabe robuster.
