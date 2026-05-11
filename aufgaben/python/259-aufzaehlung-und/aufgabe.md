---
schema_version: 1
id: 259-aufzaehlung-und
revision: 1
titel: Aufzählung mit Komma und "und"
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, listen, formatierung, sprache]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische i18n-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: aufzaehlung
hints:
  - kosten: 0
    text: |
      Verbinde Strings einer Liste zu einer deutschen Aufzählung.
      [] → ""
      ["a"] → "a"
      ["a", "b"] → "a und b"
      ["a", "b", "c"] → "a, b und c"
      ["a", "b", "c", "d"] → "a, b, c und d"
  - kosten: 10
    text: |
      Sonderfaelle: 0, 1, 2 Elemente getrennt.
      Sonst: ", ".join(wörter[:-1]) + " und " + wörter[-1].
tests_sichtbar:
  - input: [["a", "b", "c"]]
    expected: "a, b und c"
  - input: [["a", "b"]]
    expected: "a und b"
  - input: [[]]
    expected: ""
  - input: [["a"]]
    expected: "a"
tests_versteckt:
  - input: [["Hans", "Maria", "Klaus"]]
    expected: "Hans, Maria und Klaus"
  - input: [["Apfel", "Birne", "Orange", "Banane"]]
    expected: "Apfel, Birne, Orange und Banane"
  - input: [["nur", "zwei"]]
    expected: "nur und zwei"
  - input: [["allein"]]
    expected: "allein"
  - input: [["1", "2", "3", "4", "5", "6"]]
    expected: "1, 2, 3, 4, 5 und 6"
starter_code: |
  def aufzaehlung(woerter: list[str]) -> str:
      # Deine Lösung hier
      pass
---

# Aufzählung mit Komma und "und"

Schreibe `aufzählung(wörter)`, die eine Liste von Strings zu einer
**deutschen Aufzählung** zusammenfuegt -- mit Kommas zwischen
allen Elementen und " und " vor dem letzten.

## Beispiele

| Eingabe                       | Ergebnis                       |
|-------------------------------|--------------------------------|
| `[]`                          | `""`                           |
| `["a"]`                       | `"a"`                          |
| `["a", "b"]`                  | `"a und b"`                    |
| `["a", "b", "c"]`             | `"a, b und c"`                 |
| `["Hans", "Maria", "Klaus"]`  | `"Hans, Maria und Klaus"`      |
| `["Apfel", "Birne", "Orange", "Banane"]` | `"Apfel, Birne, Orange und Banane"` |

## Idee

```python
def aufzählung(wörter):
    if not wörter:
        return ""
    if len(wörter) == 1:
        return wörter[0]
    if len(wörter) == 2:
        return f"{wörter[0]} und {wörter[1]}"
    return ", ".join(wörter[:-1]) + " und " + wörter[-1]
```

Drei Sonderfaelle (0, 1, 2 Elemente), dann der allgemeine Fall.

## Englisch -- "Oxford Comma"

Im Englischen gibt's die Diskussion über das **Oxford Comma**:

- Mit: `"a, b, and c"` (Komma vor "and")
- Ohne: `"a, b and c"`

Im Deutschen ist "und" **ohne Komma davor** Standard.

## Anwendung

- Personen-Listen in Texten ("Anwesend waren X, Y und Z").
- Auto-generierte Berichte mit dynamischen Listen.
- Email-Empfaenger-Anzeige in UIs ("An: Hans, Maria und Klaus").
