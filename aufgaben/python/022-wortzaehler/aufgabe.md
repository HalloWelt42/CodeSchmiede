---
schema_version: 1
id: 022-wortzaehler
revision: 1
titel: Wortzähler aus Satz
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, dict, split, schleifen]
pfade: [python_dicts]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Dict-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: wortzaehler
hints:
  - kosten: 0
    text: |
      `text.split()` zerlegt den Satz an Whitespace -- und liefert eine
      Liste der Woerter.
  - kosten: 10
    text: |
      Schleife ueber die Woerter, jedes Wort als Schluessel ins Dict
      eintragen und dabei `dict.get(wort, 0) + 1` als Wert setzen.
  - kosten: 25
    text: |
      `collections.Counter` macht das in einer Zeile -- aber zum
      Lernen lieber per Hand.
tests_sichtbar:
  - input: ["der die das"]
    expected: { "der": 1, "die": 1, "das": 1 }
  - input: ["hallo hallo welt"]
    expected: { "hallo": 2, "welt": 1 }
  - input: [""]
    expected: {}
  - input: ["a a a a a"]
    expected: { "a": 5 }
tests_versteckt:
  - input: ["the quick brown fox jumps over the lazy dog"]
    expected: { "the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1 }
  - input: ["x"]
    expected: { "x": 1 }
  - input: ["abc abc def abc def ghi"]
    expected: { "abc": 3, "def": 2, "ghi": 1 }
starter_code: |
  def wortzaehler(text: str) -> dict[str, int]:
      # Deine Lösung hier
      pass
---

# Wortzähler aus Satz

Schreibe eine Funktion `wortzaehler(text)`, die zählt, wie oft jedes
Wort im Text vorkommt, und das Ergebnis als **Dictionary** zurueckgibt.

Die Worte werden an Whitespace getrennt; Gross-/Kleinschreibung wird
**unterschieden** (`"der"` und `"Der"` sind unterschiedlich). Bei einem
leeren String liefere ein leeres Dictionary.

## Beispiele

| Eingabe                | Ergebnis                            |
|------------------------|-------------------------------------|
| `"der die das"`        | `{"der":1, "die":1, "das":1}`       |
| `"hallo hallo welt"`   | `{"hallo":2, "welt":1}`             |
| `""`                   | `{}`                                |
| `"a a a a a"`          | `{"a":5}`                           |

## Idee

Mit `text.split()` bekommst du die Liste der Woerter. Dann durchlaeufst
du sie und zaehlst per Dict mit. Die Reihenfolge der Schluessel im
Ergebnis spielt keine Rolle -- Python-Dicts garantieren seit 3.7
zwar Insertion-Order, der Test prueft aber gegen einen Dict-Vergleich.

## Hintergrund

Wortzähler sind die Eintrittskarte zu **Text-Statistik** und einem
grossen Teil von NLP -- vom simplen Such-Index bis zur
TF-IDF-Berechnung. Wer Python und Dict-Operationen kann, kann genau
solche Sachen bauen.
