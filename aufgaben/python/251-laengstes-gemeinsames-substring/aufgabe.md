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

```python
def lcs(a, b):
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return ""
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_i = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_i = i
    return a[end_i - max_len:end_i]
```

`O(n * m)` Zeit und Speicher. Mit `O(min(n, m))` Speicher geht's
auch -- nur die letzte Zeile merken.

## Anwendung

- **Diff-Tools** zum Identifizieren gemeinsamer Code-Stücke.
- **Plagiats-Erkennung** in Texten.
- **Bioinformatik** beim Vergleich von DNA/RNA-Sequenzen.
- **Versions-Merge** in Versionskontroll-Systemen (rcs, git).
