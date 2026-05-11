---
schema_version: 1
id: 241-eigenes-join
revision: 1
titel: Eigenes join ohne str.join
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, listen, schleifen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Implementierung von Builtin
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: verbinden
hints:
  - kosten: 0
    text: |
      Verbinde Strings einer Liste mit einem Trenner zu einem String.
      OHNE str.join() -- selber bauen.
      Bei [] → "". Bei einem Element → das Element.
  - kosten: 15
    text: |
      result = ""; for i, s in enumerate(strings):
        if i > 0: result += trenner
        result += s
      return result.
tests_sichtbar:
  - input: [["a", "b", "c"], ", "]
    expected: "a, b, c"
  - input: [[], ", "]
    expected: ""
  - input: [["solo"], ", "]
    expected: "solo"
  - input: [["a", "b"], "-"]
    expected: "a-b"
tests_versteckt:
  - input: [["1", "2", "3"], ""]
    expected: "123"
  - input: [["x"], "abc"]
    expected: "x"
  - input: [["", "", ""], "-"]
    expected: "--"
  - input: [["Hallo", "Welt"], " "]
    expected: "Hallo Welt"
  - input: [["a", "b", "c", "d", "e"], "/"]
    expected: "a/b/c/d/e"
  - input: [["A", "B"], " und "]
    expected: "A und B"
starter_code: |
  def verbinden(strings: list[str], trenner: str) -> str:
      # Deine Lösung hier -- OHNE str.join
      pass
---

# Eigenes `join` ohne str.join

Schreibe `verbinden(strings, trenner)`, die eine Liste von Strings
zu einem einzelnen String **mit Trenner zwischen jedem Paar**
zusammenfuegt -- **ohne** `str.join` zu nutzen.

## Beispiele

| Liste              | Trenner | Ergebnis        |
|--------------------|---------|-----------------|
| `["a", "b", "c"]`  | `", "`  | `"a, b, c"`     |
| `["solo"]`         | `", "`  | `"solo"`        |
| `[]`               | `", "`  | `""`            |
| `["1", "2", "3"]`  | `""`    | `"123"`         |
| `["", "", ""]`     | `"-"`   | `"--"`          |
| `["A", "B"]`       | `" und "`| `"A und B"`    |

## Idee

Erstes Element ohne Trenner, alle weiteren mit. Dadurch landet der
Trenner **zwischen** den Elementen, nicht davor oder dahinter.

## Stolperstein -- String-Konkatenation in Schleife

In Python ist `out += s` in einer Schleife eigentlich **O(n^2)** --
weil jedes Mal ein neuer String erzeugt wird. Bei tausenden Elementen
besser:

Aber wir wollen ja `join` **vermeiden** -- dann lieber die naive
Variante akzeptieren oder selbst das `"".join` nochmal hand-bauen.

## Hintergrund

`str.join` ist in CPython hochoptimiert -- in normalem Code
verwenden, hier nur didaktisch nachgebaut.
