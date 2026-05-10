---
schema_version: 1
id: 036-acronym
revision: 1
titel: Akronym aus Satz
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [strings, split, comprehension]
pfade: [python_strings]
voraussetzungen: [006-erstes-wort]
quelle:
  url: null
  notiz: Standard-String-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: akronym
hints:
  - kosten: 0
    text: |
      `text.split()` zerlegt nach Whitespace. Aus jedem Wort den
      ersten Buchstaben holen, alles in Grossbuchstaben.
  - kosten: 10
    text: |
      Eine Zeile:

      ```
      return "".join(w[0].upper() for w in text.split())
      ```
tests_sichtbar:
  - input: ["world wide web"]
    expected: "WWW"
  - input: ["Application Programming Interface"]
    expected: "API"
  - input: [""]
    expected: ""
  - input: ["Hallo"]
    expected: "H"
tests_versteckt:
  - input: ["new York city"]
    expected: "NYC"
  - input: ["    leerzeichen   am   rand   "]
    expected: "L"
  - input: ["Just In Time"]
    expected: "JIT"
  - input: ["a b c d e"]
    expected: "ABCDE"
starter_code: |
  def akronym(text: str) -> str:
      # Deine Lösung hier
      pass
---

# Akronym aus Satz

Schreibe eine Funktion `akronym(text)`, die aus jedem Wort des Textes
den **ersten Buchstaben** nimmt und sie zu einem grossgeschriebenen
Akronym zusammensetzt.

Worte werden an Whitespace getrennt; mehrfache Leerzeichen oder
fuehrende/abschliessende Whitespaces werden korrekt ignoriert.

## Beispiele

| Eingabe                                | Ergebnis |
|----------------------------------------|----------|
| `"world wide web"`                     | `"WWW"`  |
| `"Application Programming Interface"`  | `"API"`  |
| `""`                                   | `""`     |
| `"Hallo"`                              | `"H"`    |
| `"new York city"`                      | `"NYC"`  |

## Idee

`text.split()` -- ohne Argument splittet es an beliebigen Whitespace
und ignoriert leere Bestandteile. Genau, was hier gebraucht wird.

## Hintergrund

Akronyme sind ueberall in der Tech-Welt: API, HTTP, JIT, AST, SQL.
Die meisten lassen sich mit dieser kleinen Funktion automatisch aus
einem Satz erzeugen.
