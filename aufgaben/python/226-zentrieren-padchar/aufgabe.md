---
schema_version: 1
id: 226-zentrieren-padchar
revision: 1
titel: Text zentrieren mit beliebigem Padding-Zeichen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, formatierung, ascii-art]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische String-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zentrieren
hints:
  - kosten: 0
    text: |
      Zentriere den Text in einem Feld der gegebenen Breite mit dem
      gegebenen Padding-Zeichen. text laenger als breite → unverändert.
      Bei pad mit Laenge != 1 → text unverändert.
      Pythons str.center erlaubt das pad-Zeichen direkt.
  - kosten: 10
    text: |
      text.center(breite, pad). Aber pad muss genau ein Zeichen sein,
      sonst Error oder eigene Prüfung.
tests_sichtbar:
  - input: ["Hi", 6, "*"]
    expected: "**Hi**"
  - input: ["A", 5, "-"]
    expected: "--A--"
  - input: ["abc", 3, "."]
    expected: "abc"
  - input: ["x", 7, "#"]
    expected: "###x###"
tests_versteckt:
  - input: ["test", 10, "."]
    expected: "...test..."
  - input: ["", 4, "_"]
    expected: "____"
  - input: ["WORT", 4, "x"]
    expected: "WORT"
  - input: ["WORT", 6, " "]
    expected: " WORT "
  - input: ["A", 4, "*"]
    expected: "*A**"
  - input: ["xx", 7, "-"]
    expected: "---xx--"
  - input: ["abc", 5, "ab"]
    expected: "abc"
starter_code: |
  def zentrieren(text: str, breite: int, pad: str) -> str:
      # Deine Lösung hier -- pad MUSS ein Zeichen sein, sonst text unverändert
      pass
---

# Text zentrieren mit beliebigem Padding-Zeichen

Schreibe `zentrieren(text, breite, pad)`, die einen Text in einem
Feld der gegebenen Breite **zentriert** und mit dem **angegebenen
Zeichen** auffuellt.

- Wenn `text` schon laenger als `breite` ist → unverändert zurückgeben.
- Wenn `pad` nicht **genau ein Zeichen** lang ist → unverändert.
- Bei ungerader Padding-Anzahl: links eines weniger als rechts
  (Python-`str.center`-Konvention).

## Beispiele

| Text   | Breite | Pad | Ergebnis        |
|--------|--------|-----|-----------------|
| `"Hi"` | `6`    | `*` | `"**Hi**"`      |
| `"A"`  | `5`    | `-` | `"--A--"`       |
| `"x"`  | `7`    | `#` | `"###x###"`     |
| `"A"`  | `4`    | `*` | `"*A**"` (rechts mehr) |
| `"abc"`| `3`    | `.` | `"abc"`         |
| `""`   | `4`    | `_` | `"____"`        |

## Idee

```python
def zentrieren(text, breite, pad):
    if len(pad) != 1:
        return text
    if len(text) >= breite:
        return text
    return text.center(breite, pad)
```

`str.center` macht alles -- aber nur, wenn `pad` genau **ein**
Zeichen ist, sonst wirft Python einen `TypeError`. Wir fangen das
explizit ab.

## Anwendung

- ASCII-Banner: `zentrieren("WILLKOMMEN", 80, "=")` → 80-Zeichen-Banner.
- Tabellen-Spalten zentrieren.
- Test-Output formatieren: `zentrieren(" PASS ", 30, "-")`.

## Verwandt -- ljust/rjust

| Funktion | Wirkung               |
|----------|------------------------|
| `ljust`  | Text links, Pad rechts |
| `rjust`  | Pad links, Text rechts |
| `center` | Pad beidseitig, Text mitte |

Alle drei akzeptieren ein optionales Pad-Zeichen.
