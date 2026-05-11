---
schema_version: 1
id: 109-anagramm-gruppen
revision: 1
titel: Wörter nach Anagramm gruppieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, dict, sortieren, gruppierung]
pfade: [python_dicts]
voraussetzungen: [008-anagramm-pruefen]
quelle:
  url: null
  notiz: Inspiration aus Exercism (anagram), Variante als Gruppierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gruppiere
hints:
  - kosten: 0
    text: |
      Zwei Wörter sind Anagramme, wenn sie nach Sortieren der
      Buchstaben identisch sind. Liefere Liste von Listen --
      jede Innen-Liste ist eine Anagramm-Gruppe.
  - kosten: 15
    text: |
      `defaultdict(list)`. Pro Wort: `key = "".join(sorted(wort.lower()))`.
      Dict-Werte sammeln. Am Ende `sorted(dict.values())` für stabile
      Ausgabe (jede Gruppe sortiert + Liste der Gruppen sortiert).
tests_sichtbar:
  - input: [["eat", "tea", "tan", "ate", "nat", "bat"]]
    expected: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
  - input: [[]]
    expected: []
  - input: [["abc"]]
    expected: [["abc"]]
  - input: [["", ""]]
    expected: [["", ""]]
tests_versteckt:
  - input: [["listen", "silent", "enlist"]]
    expected: [["enlist", "listen", "silent"]]
  - input: [["a", "b", "c"]]
    expected: [["a"], ["b"], ["c"]]
  - input: [["abc", "cba", "bca", "xyz", "zyx"]]
    expected: [["abc", "bca", "cba"], ["xyz", "zyx"]]
  - input: [["Eat", "TEA", "ate"]]
    expected: [["Eat", "TEA", "ate"]]
starter_code: |
  def gruppiere(woerter: list[str]) -> list[list[str]]:
      # Deine Lösung hier -- pro Gruppe alphabetisch, Gruppen alphabetisch.
      pass
---

# Wörter nach Anagramm gruppieren

Schreibe eine Funktion `gruppiere(wörter)`, die eine Liste von
Wörtern nach **Anagramm-Klassen** gruppiert.

Zwei Wörter sind Anagramme, wenn sie die gleichen Buchstaben in
beliebiger Reihenfolge enthalten -- Groß-/Kleinschreibung wird
ignoriert.

## Beispiele

| Eingabe                                   | Ergebnis                                       |
|-------------------------------------------|------------------------------------------------|
| `["eat","tea","tan","ate","nat","bat"]`   | `[["ate","eat","tea"], ["bat"], ["nat","tan"]]`|
| `[]`                                      | `[]`                                           |
| `["listen","silent","enlist"]`            | `[["enlist","listen","silent"]]`               |
| `["Eat","TEA","ate"]`                     | `[["Eat","TEA","ate"]]`                        |

## Sortier-Regel

- Pro Gruppe: alphabetisch sortiert
- Gruppen unter sich: alphabetisch nach erstem Element

## Hintergrund

Klassisches Bewerbungsgespraechs-Problem. Der Kniff: ein **stabiler
Schlüssel** pro Wort -- typisch sind sortierte Buchstaben oder ein
Counter. Beides klassifiziert Anagramme zuverlaessig.
