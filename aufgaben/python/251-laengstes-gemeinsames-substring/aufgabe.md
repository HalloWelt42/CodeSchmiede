---
schema_version: 1
id: 251-laengstes-gemeinsames-substring
revision: 1
titel: Laengster gemeinsamer Substring (LCS)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 50
schaetz_minuten: 18
tags: [strings, dp, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische DP-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: lcs
hints:
  - kosten: 0
    text: |
      Liefere den LAENGSTEN ZUSAMMENHAENGENDEN Substring, der in
      BEIDEN Strings vorkommt. Bei mehreren gleich-langen Treffern:
      den, der in a als ERSTES anfängt.
      Bei keinem gemeinsamen Zeichen → "".
  - kosten: 25
    text: |
      DP-Tabelle dp[i][j] = Laenge des gemeinsamen Substrings, der
      bei a[i-1] und b[j-1] endet. Position des Maximums merken.
tests_sichtbar:
  - input: ["abcdef", "zcdex"]
    expected: "cde"
  - input: ["", "abc"]
    expected: ""
  - input: ["abc", ""]
    expected: ""
  - input: ["abc", "xyz"]
    expected: ""
tests_versteckt:
  - input: ["abcdef", "abcdef"]
    expected: "abcdef"
  - input: ["aaa", "aaaa"]
    expected: "aaa"
  - input: ["GeeksforGeeks", "GeeksQuiz"]
    expected: "Geeks"
  - input: ["abcdxyz", "xyzabcd"]
    expected: "abcd"
  - input: ["zxabcdezy", "yzabcdezx"]
    expected: "abcdez"
  - input: ["a", "a"]
    expected: "a"
  - input: ["a", "b"]
    expected: ""
starter_code: |
  def lcs(a: str, b: str) -> str:
      # Deine Lösung hier -- DP, bei Gleichstand erster Treffer in a
      pass
---

# Laengster gemeinsamer Substring (LCS)

Schreibe `lcs(a, b)`, die den **laengsten zusammenhängenden
Substring** liefert, der in **beiden** Strings vorkommt.

Bei mehreren gleich-langen Treffern: den, der in `a` zuerst anfängt.
Bei keinem Treffer → `""`.

## Achtung -- Substring vs Subsequence

- **Substring**: zusammenhängende Zeichen ("abc" → "ab", "bc", aber nicht "ac")
- **Subsequence**: Reihenfolge bewahrt, aber Lücken erlaubt

Wir suchen den **Substring** -- die schwerere Aufgabe ist die
Subsequence (LCS-Algorithmus klassisch in DNA-Vergleich).

## Beispiele

| `a`             | `b`             | LCS         |
|-----------------|-----------------|-------------|
| `"abcdef"`      | `"zcdex"`       | `"cde"`     |
| `"GeeksforGeeks"` | `"GeeksQuiz"` | `"Geeks"`   |
| `"abcdxyz"`     | `"xyzabcd"`     | `"abcd"`    |
| `"zxabcdezy"`   | `"yzabcdezx"`   | `"abcdez"`  |
| `"abc"`         | `"xyz"`         | `""`        |

## Idee -- DP-Tabelle

`dp[i][j]` = Laenge des gemeinsamen Substrings, der **endet** bei
`a[i-1]` und `b[j-1]`.

`O(n * m)` Zeit und Speicher. Mit `O(min(n, m))` Speicher geht's
auch -- nur die letzte Zeile merken.

## Anwendung

- **Diff-Tools** zum Identifizieren gemeinsamer Code-Stücke.
- **Plagiats-Erkennung** in Texten.
- **Bioinformatik** beim Vergleich von DNA/RNA-Sequenzen.
- **Versions-Merge** in Versionskontroll-Systemen (rcs, git).
