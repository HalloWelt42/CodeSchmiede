---
schema_version: 1
id: 139-levenshtein
revision: 1
titel: Levenshtein-Distanz
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 25
tags: [strings, dp, distanz, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Edit-Distanz-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: levenshtein
hints:
  - kosten: 0
    text: |
      Liefere die minimale Anzahl Einzeloperationen
      (Einfuegen, Löschen, Ersetzen), um a in b zu verwandeln.
  - kosten: 20
    text: |
      Dynamische Programmierung mit (n+1)x(m+1)-Matrix.
      dp[i][j] = Distanz von a[:i] zu b[:j].
      Bei a[i-1] == b[j-1]: dp[i-1][j-1].
      Sonst: 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]).
tests_sichtbar:
  - input: ["", ""]
    expected: 0
  - input: ["kitten", "sitting"]
    expected: 3
  - input: ["abc", "abc"]
    expected: 0
  - input: ["abc", ""]
    expected: 3
tests_versteckt:
  - input: ["", "abc"]
    expected: 3
  - input: ["sonntag", "samstag"]
    expected: 3
  - input: ["haus", "maus"]
    expected: 1
  - input: ["abcdef", "azced"]
    expected: 3
  - input: ["a", "b"]
    expected: 1
  - input: ["intention", "execution"]
    expected: 5
starter_code: |
  def levenshtein(a: str, b: str) -> int:
      # Deine Lösung hier
      pass
---

# Levenshtein-Distanz

Schreibe eine Funktion `levenshtein(a, b)`, die die **minimale Anzahl
Einzeloperationen** zurückgibt, um den String `a` in den String `b`
umzuwandeln.

Erlaubte Operationen (jede zählt als 1):

- **Einfuegen** eines Zeichens
- **Löschen** eines Zeichens
- **Ersetzen** eines Zeichens

## Beispiele

| `a`         | `b`         | Distanz | Begruendung                   |
|-------------|-------------|---------|-------------------------------|
| `"kitten"`  | `"sitting"` | 3       | k→s, e→i, +g                  |
| `"haus"`    | `"maus"`    | 1       | h→m                           |
| `"abc"`     | `""`        | 3       | drei Löschungen              |
| `"sonntag"` | `"samstag"` | 3       | onn→ams                       |

## Idee -- Dynamische Programmierung

Tabelle `dp[i][j]` = Distanz zwischen den ersten `i` Zeichen von `a`
und den ersten `j` Zeichen von `b`.

```
dp[0][j] = j        (j Einfuegungen)
dp[i][0] = i        (i Löschungen)
dp[i][j] = dp[i-1][j-1]                          falls a[i-1] == b[j-1]
         = 1 + min(dp[i-1][j],     # Löschen
                   dp[i][j-1],     # Einfuegen
                   dp[i-1][j-1])   # Ersetzen     sonst
```

## Hintergrund

Levenshtein steckt hinter Tippfehler-Vorschlaegen, DNA-Sequenz-Alignment,
Plagiats-Erkennung und der "did you mean ..."-Funktion in Suchmaschinen.
