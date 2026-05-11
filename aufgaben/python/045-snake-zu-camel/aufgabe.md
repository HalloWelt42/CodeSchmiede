---
schema_version: 1
id: 045-snake-zu-camel
revision: 1
titel: snake_case zu camelCase
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, split, capitalize, comprehension]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Tooling-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: snake_zu_camel
hints:
  - kosten: 0
    text: |
      `text.split('_')` zerlegt an den Unterstrichen. Erstes Wort
      bleibt klein, danach `.capitalize()` pro Wort.
  - kosten: 15
    text: |
      ```
      teile = text.split('_')
      return teile[0] + ''.join(t.capitalize() for t in teile[1:])
      ```
tests_sichtbar:
  - input: ["hello_world"]
    expected: "helloWorld"
  - input: ["nur_ein_test"]
    expected: "nurEinTest"
  - input: ["einfach"]
    expected: "einfach"
  - input: [""]
    expected: ""
tests_versteckt:
  - input: ["a_b_c_d"]
    expected: "aBCD"
  - input: ["snake_case_to_camel"]
    expected: "snakeCaseToCamel"
  - input: ["x"]
    expected: "x"
  - input: ["__leer__doppelt__"]
    expected: "LeerDoppelt"
starter_code: |
  def snake_zu_camel(text: str) -> str:
      # Deine Lösung hier
      pass
---

# snake_case zu camelCase

Schreibe eine Funktion `snake_zu_camel(text)`, die einen
**snake_case**-String in **camelCase** überfuehrt.

## Beispiele

| Eingabe              | Ergebnis             |
|----------------------|----------------------|
| `"hello_world"`      | `"helloWorld"`       |
| `"nur_ein_test"`     | `"nurEinTest"`       |
| `"einfach"`          | `"einfach"`          |
| `""`                 | `""`                 |
| `"a_b_c_d"`          | `"aBCD"`             |

## Idee

`split('_')` ergibt eine Liste von Bestandteilen. Das **erste** Wort
bleibt klein, **alle weiteren** bekommen einen Großbuchstaben am
Anfang. `''.join(...)` setzt sie wieder zusammen.

## Falle

`"__leer__doppelt__"` enthält leere Bestandteile. `"".capitalize()`
liefert `""`, also kein Crash -- aber das fuehrende `_` macht das
erste Element leer und damit beginnt das Ergebnis mit einem
Großbuchstaben.
