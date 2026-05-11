---
schema_version: 1
id: 031-zip-listen
revision: 1
titel: Zwei Listen verzahnen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [listen, zip, schleifen]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Eigene Reformulierung -- Variation des Zip-Klassikers.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: verzahne
hints:
  - kosten: 0
    text: |
      Element 0 aus a, Element 0 aus b, Element 1 aus a, Element 1 aus b ...
      Wenn eine Liste laenger ist, haenge ihre restlichen Elemente am
      Ende an.
  - kosten: 9
    text: |
      Schleife `for i in range(min(len(a), len(b)))` baut den
      verzahnten Teil. Danach `a[i+1:]` oder `b[i+1:]` als Rest
      anhängen, je nachdem welche laenger ist.
tests_sichtbar:
  - input: [[1, 2, 3], ["a", "b", "c"]]
    expected: [1, "a", 2, "b", 3, "c"]
  - input: [[1, 2], [10, 20, 30, 40]]
    expected: [1, 10, 2, 20, 30, 40]
  - input: [[], [1, 2, 3]]
    expected: [1, 2, 3]
  - input: [[1, 2, 3], []]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[], []]
    expected: []
  - input: [[1, 2, 3, 4, 5], ["a"]]
    expected: [1, "a", 2, 3, 4, 5]
  - input: [["x"], ["y"]]
    expected: ["x", "y"]
  - input: [[1, 1, 1], [2, 2, 2]]
    expected: [1, 2, 1, 2, 1, 2]
starter_code: |
  def verzahne(a: list, b: list) -> list:
      # Deine Lösung hier -- abwechselnd aus a und b, Reste anhaengen.
      pass
---

# Zwei Listen verzahnen

Schreibe eine Funktion `verzahne(a, b)`, die die Elemente abwechselnd
aus `a` und `b` in eine neue Liste schreibt -- erst `a[0]`, dann `b[0]`,
dann `a[1]`, dann `b[1]`, und so weiter.

Wenn eine der Listen laenger ist, werden die **restlichen Elemente
einfach hinten angehängt**.

## Beispiele

| `a`             | `b`              | Ergebnis                |
|-----------------|------------------|-------------------------|
| `[1,2,3]`       | `["a","b","c"]`  | `[1,"a",2,"b",3,"c"]`   |
| `[1,2]`         | `[10,20,30,40]`  | `[1,10,2,20,30,40]`     |
| `[]`            | `[1,2,3]`        | `[1,2,3]`               |
| `[1,2,3]`       | `[]`             | `[1,2,3]`               |
| `[]`            | `[]`             | `[]`                    |

## Idee

Schleife bis zum kürzeren Ende mit Indizes, dann den Rest des
laengeren mit Slicing anhängen.

## Verwandt

Pythons eingebautes `zip()` liefert Tupel-Paare und stoppt am
kürzeren Ende -- es macht also etwas anderes. Mit `itertools.chain`
und `zip_longest` könnte man das hier ebenfalls bauen, aber zum
Lernen ist die Schleifen-Variante lehrreicher.
