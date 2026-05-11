---
schema_version: 1
id: 046-camel-zu-snake
revision: 1
titel: camelCase zu snake_case
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [strings, schleifen, comprehension]
pfade: [python_strings3]
voraussetzungen: [045-snake-zu-camel]
quelle:
  url: null
  notiz: Klassische Tooling-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: camel_zu_snake
hints:
  - kosten: 0
    text: |
      Vor jedem Großbuchstaben einen Unterstrich einfügen, dann
      alles in Kleinbuchstaben.
  - kosten: 9
    text: |
      Achtung: Vor dem ersten Zeichen kein Unterstrich, auch wenn
      es groß ist.
tests_sichtbar:
  - input: ["helloWorld"]
    expected: "hello_world"
  - input: ["nurEinTest"]
    expected: "nur_ein_test"
  - input: ["einfach"]
    expected: "einfach"
  - input: [""]
    expected: ""
tests_versteckt:
  - input: ["aBCD"]
    expected: "a_b_c_d"
  - input: ["camelCaseToSnake"]
    expected: "camel_case_to_snake"
  - input: ["x"]
    expected: "x"
  - input: ["X"]
    expected: "x"
  - input: ["XmlHttpRequest"]
    expected: "xml_http_request"
starter_code: |
  def camel_zu_snake(text: str) -> str:
      # Deine Lösung hier
      pass
---

# camelCase zu snake_case

Schreibe eine Funktion `camel_zu_snake(text)`, die einen
**camelCase**-String in **snake_case** umwandelt.

## Beispiele

| Eingabe              | Ergebnis                |
|----------------------|-------------------------|
| `"helloWorld"`       | `"hello_world"`         |
| `"nurEinTest"`       | `"nur_ein_test"`        |
| `"einfach"`          | `"einfach"`             |
| `""`                 | `""`                    |
| `"aBCD"`             | `"a_b_c_d"`             |
| `"XmlHttpRequest"`   | `"xml_http_request"`    |

## Idee

Schleife durch jedes Zeichen: ist es **groß** und **nicht das erste**,
fuege vorher `_` ein. Dann den Buchstaben kleingeschrieben anhängen.

## Tipp

Mit `re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()` ginge es per
Regex in einer Zeile. Hier zur Übung lieber mit Schleife.
