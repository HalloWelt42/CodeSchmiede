---
schema_version: 1
id: 213-woerter-zaehlen
revision: 1
titel: Anzahl Wörter im Text
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [strings, split, zaehlen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Text-Statistik
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: woerter_zaehlen
hints:
  - kosten: 0
    text: |
      Zähle die Anzahl der Wörter in einem Text. Mehrfache
      Leerzeichen zählen als ein Trenner. Leerer/whitespace-only
      Text → 0.
  - kosten: 10
    text: |
      str.split() ohne Argument splittet an beliebigem Whitespace
      und filtert leere Strings raus. Dann len().
tests_sichtbar:
  - input: ["Hallo Welt"]
    expected: 2
  - input: [""]
    expected: 0
  - input: ["nur"]
    expected: 1
  - input: ["eins zwei drei vier"]
    expected: 4
tests_versteckt:
  - input: ["    "]
    expected: 0
  - input: ["  viele   Leerzeichen   hier  "]
    expected: 3
  - input: ["a b c d e f g h i j"]
    expected: 10
  - input: ["der schnelle braune Fuchs"]
    expected: 4
  - input: ["1 2 3"]
    expected: 3
  - input: ["wort"]
    expected: 1
  - input: ["a"]
    expected: 1
starter_code: |
  def woerter_zaehlen(text: str) -> int:
      # Deine Lösung hier
      pass
---

# Anzahl Wörter im Text

Schreibe `wörter_zählen(text)`, die die **Anzahl der Wörter** in
einem Text zurückgibt. Mehrfache Whitespaces zählen als ein
Trenner; fuehrende/nachfolgende Leerzeichen werden ignoriert.

Bei leerem oder nur Whitespace-haltigem Text → `0`.

## Beispiele

| Eingabe                           | Anzahl |
|-----------------------------------|--------|
| `""`                              | `0`    |
| `"    "`                          | `0`    |
| `"nur"`                           | `1`    |
| `"Hallo Welt"`                    | `2`    |
| `"eins zwei drei vier"`           | `4`    |
| `"  viele   Leerzeichen   hier "` | `3`    |
| `"a b c d e f g h i j"`           | `10`   |

## Idee

```python
def wörter_zählen(text):
    return len(text.split())
```

Eine Zeile -- Pythons `str.split()` ohne Argument macht alles
Würdige: trennen an Whitespace, leere Stücke filtern, fertig.

## Verwandt

| Aufgabe                | Was?                          |
|------------------------|--------------------------------|
| **022-wortzähler**    | Häufigkeit pro Wort (Dict)   |
| **048-laengstes-wort** | das laengste Wort             |
| **148-wörter-umkehren** | Wort-Reihenfolge umdrehen   |
| **213-wörter-zählen** | nur die Anzahl (diese)       |

## Hintergrund

Wörter zählen ist die Basis vieler Text-Statistiken: Lesezeit
(Faustregel: 200-300 Wörter pro Minute), Lexikalische Dichte,
Twitter-Tweetlaenge (früher 140, jetzt 280 Zeichen oder ~50 Wörter).
