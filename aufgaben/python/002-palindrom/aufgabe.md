---
schema_version: 1
id: 002-palindrom
revision: 1
titel: Palindrom-Prüfung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [strings, slicing, schleifen]
pfade: [python_grundlagen]
voraussetzungen: [001-fizzbuzz]
quelle:
  url: https://de.wikipedia.org/wiki/Palindrom
  notiz: Klassische String-Aufgabe, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_palindrom
hints:
  - kosten: 0
    text: Ein Palindrom liest sich vorwaerts genauso wie rueckwaerts.
  - kosten: 3
    text: In Python kannst du einen String mit `text[::-1]` umkehren.
  - kosten: 9
    text: |
      Eleganteste Lösung:

      ```
      return text == text[::-1]
      ```
tests_sichtbar:
  - input: ["anna"]
    expected: true
  - input: ["hallo"]
    expected: false
  - input: ["a"]
    expected: true
  - input: [""]
    expected: true
tests_versteckt:
  - input: ["rentner"]
    expected: true
  - input: ["regallager"]
    expected: true
  - input: ["Anna"]
    expected: false
  - input: ["ab"]
    expected: false
  - input: ["aa"]
    expected: true
  - input: ["abcba"]
    expected: true
starter_code: |
  def ist_palindrom(text: str) -> bool:
      # Deine Loesung hier
      pass
---

# Palindrom-Prüfung

Schreibe eine Funktion `ist_palindrom(text)`, die `True` zurückgibt, wenn
der eingegebene String ein **Palindrom** ist -- also vorwärts und
rückwärts identisch -- und sonst `False`.

## Beispiele

| Eingabe       | Ausgabe |
|---------------|---------|
| `"anna"`      | `True`  |
| `"rentner"`   | `True`  |
| `"hallo"`     | `False` |
| `"Anna"`      | `False` |
| `""`          | `True`  |

## Worauf zu achten ist

- **Groß-/Kleinschreibung zählt** -- `"Anna"` ist kein Palindrom in
  dieser Aufgabe
- **Leerzeichen werden mitgezählt** -- vereinfache, indem du davon
  ausgehst, dass keine Leerzeichen vorkommen
- Der **leere String** gilt per Konvention als Palindrom

## Hintergrund

Palindrome sind eine schöne Spielwiese für **String-Slicing**. Python
bietet hier eine besonders kompakte Notation: `text[::-1]` liefert den
String rückwärts.

> Mathematisch: ein Wort $w = w_0 w_1 \dots w_{n-1}$ ist ein Palindrom,
> wenn für alle $i$ gilt $w_i = w_{n-1-i}$.
