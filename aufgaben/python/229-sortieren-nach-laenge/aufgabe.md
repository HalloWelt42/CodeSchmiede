---
schema_version: 1
id: 229-sortieren-nach-laenge
revision: 1
titel: Strings nach Laenge sortieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [strings, listen, sortieren, key]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Sortier-Aufgabe mit key
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: nach_laenge
hints:
  - kosten: 0
    text: |
      Sortiere eine Liste von Strings AUFSTEIGEND nach LAENGE.
      Bei gleicher Laenge: alphabetisch.
      Original-Liste nicht verändern.
  - kosten: 10
    text: |
      sorted mit key=lambda s: (len(s), s).
      Tupel-Sortierung: zuerst nach laenge, dann alphabetisch.
tests_sichtbar:
  - input: [["banana", "apple", "cherry", "fig"]]
    expected: ["fig", "apple", "banana", "cherry"]
  - input: [[]]
    expected: []
  - input: [["a"]]
    expected: ["a"]
  - input: [["aa", "bb", "ccc"]]
    expected: ["aa", "bb", "ccc"]
tests_versteckt:
  - input: [["abc", "ab", "a"]]
    expected: ["a", "ab", "abc"]
  - input: [["xx", "x", "xxx", "xxxx"]]
    expected: ["x", "xx", "xxx", "xxxx"]
  - input: [["banane", "apfel", "birne"]]
    expected: ["apfel", "birne", "banane"]
  - input: [["", "a", "ab"]]
    expected: ["", "a", "ab"]
  - input: [["zzz", "aaa", "yy", "bb"]]
    expected: ["bb", "yy", "aaa", "zzz"]
starter_code: |
  def nach_laenge(strings: list[str]) -> list[str]:
      # Deine Lösung hier -- bei gleicher Laenge alphabetisch
      pass
---

# Strings nach Laenge sortieren

Schreibe `nach_laenge(strings)`, die eine Liste von Strings
**aufsteigend nach Laenge** sortiert. Bei gleicher Laenge:
**alphabetisch** (das ist die Standard-Tie-Breaking-Regel).

Original-Liste **nicht** verändern.

## Beispiele

| Eingabe                            | Ergebnis                            |
|------------------------------------|-------------------------------------|
| `["banana", "apple", "cherry", "fig"]` | `["fig", "apple", "banana", "cherry"]` |
| `["abc", "ab", "a"]`               | `["a", "ab", "abc"]`                |
| `["banane", "apfel", "birne"]`     | `["apfel", "birne", "banane"]` (5,5,6) |
| `["zzz", "aaa", "yy", "bb"]`       | `["bb", "yy", "aaa", "zzz"]`        |

## Idee -- key mit Tupel

```python
def nach_laenge(strings):
    return sorted(strings, key=lambda s: (len(s), s))
```

Pythons `sorted` mit Tupel-Key sortiert **lexikographisch** über
das Tupel: zuerst nach `len(s)`, bei Gleichstand nach `s` selbst.

## Warum nicht zwei separate Sortierungen?

Wegen Pythons **stabiler Sortierung** könnte man auch:

```python
return sorted(sorted(strings), key=len)
```

Erst alphabetisch, dann nach Laenge -- die Stabilitaet erhaelt die
alphabetische Reihenfolge bei Gleichstand. Funktioniert -- aber
liest sich verwirrender.

## Anwendung

- Auto-Vervollstaendigung: zuerst kürzere Vorschlaege.
- Tabellen-Spalten dynamisch dimensionieren.
- Sortier-Visualisierungen / Lehre.
