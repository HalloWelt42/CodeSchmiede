---
schema_version: 1
id: 282-markdown-links
revision: 1
titel: Markdown-Links extrahieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [strings, regex, markdown, capture-groups]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Markdown-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: markdown_links
hints:
  - kosten: 0
    text: |
      Extrahiere alle Markdown-Links als Liste von [text, url]-Paaren.
      Format: [text](url).
      "Klick [hier](https://x.de) und [da](http://y.de)" →
      [["hier", "https://x.de"], ["da", "http://y.de"]].
      Bei keinem Link → [].
  - kosten: 20
    text: |
      re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text) liefert
      Liste von Tupeln (text, url). Pro Tupel zu Liste konvertieren.
tests_sichtbar:
  - input: ["Klick [hier](https://x.de) und [da](http://y.de)"]
    expected: [["hier", "https://x.de"], ["da", "http://y.de"]]
  - input: ["nur text, keine Links"]
    expected: []
  - input: [""]
    expected: []
  - input: ["[einer](url1)"]
    expected: [["einer", "url1"]]
tests_versteckt:
  - input: ["[Foo](http://foo.example/path?x=1)"]
    expected: [["Foo", "http://foo.example/path?x=1"]]
  - input: ["[a](1) [b](2) [c](3)"]
    expected: [["a", "1"], ["b", "2"], ["c", "3"]]
  - input: ["[Text mit Leerzeichen](https://lange.url/mit/segmenten)"]
    expected: [["Text mit Leerzeichen", "https://lange.url/mit/segmenten"]]
  - input: ["nur [text] ohne URL"]
    expected: []
  - input: ["nur (url) ohne Text"]
    expected: []
  - input: ["![bild](pic.png)"]
    expected: [["bild", "pic.png"]]
  - input: ["[a](b) text [c](d)"]
    expected: [["a", "b"], ["c", "d"]]
starter_code: |
  import re

  def markdown_links(text: str) -> list[list[str]]:
      # Deine Lösung hier -- [text, url] pro Link
      pass
---

# Markdown-Links extrahieren

Schreibe `markdown_links(text)`, die alle Markdown-Links aus einem
Text extrahiert -- als Liste von `[text, url]`-Paaren.

Markdown-Link-Syntax: `[Anzeigetext](https://url.example)`.

## Beispiele

| Eingabe                                          | Ergebnis                                       |
|--------------------------------------------------|------------------------------------------------|
| `"Klick [hier](https://x.de) und [da](http://y.de)"` | `[["hier","https://x.de"], ["da","http://y.de"]]` |
| `"[einer](url1)"`                                | `[["einer","url1"]]`                           |
| `"[a](1) [b](2) [c](3)"`                         | `[["a","1"], ["b","2"], ["c","3"]]`            |
| `"![bild](pic.png)"`                             | `[["bild","pic.png"]]` (Bild-Syntax matcht auch) |
| `"nur text"`                                     | `[]`                                           |
| `"nur [text] ohne URL"`                          | `[]`                                           |

## Idee -- zwei Capture-Groups

```python
import re

def markdown_links(text):
    return [list(t) for t in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)]
```

Pattern aufgedroeselt:

| Stück       | Bedeutung                                |
|--------------|-------------------------------------------|
| `\[`         | literale eckige Klammer auf              |
| `([^\]]+)`   | Capture: 1+ Zeichen, die NICHT `]` sind  |
| `\]`         | literale eckige Klammer zu               |
| `\(`         | literale runde Klammer auf               |
| `([^)]+)`    | Capture: 1+ Zeichen, die NICHT `)` sind  |
| `\)`         | literale runde Klammer zu                |

`re.findall` mit **mehreren Capture-Groups** liefert eine Liste
von **Tupeln** -- jedes Tupel hat so viele Elemente wie es Groups
gibt. Wir konvertieren Tupel zu Listen.

## Stolperstein -- Negierende Char-Klasse

`[^\]]+` ist die Standardform für "alles außer `]`". Damit greift
das Pattern nicht über das schließende `]` hinaus -- selbst wenn
in der URL Klammern stehen.

## Erweiterungen (nicht hier)

- **Optionaler Titel**: `[text](url "title")` -- Markdown erlaubt das.
- **Reference-Links**: `[text][ref]` und separate `[ref]: url`.
- **Bilder**: `![alt](url)` -- unsere Regex matcht das auch (das `!` ist
  außerhalb der Match-Klammern).

Für einen voll-spec-konformen Markdown-Parser nimmt man eher
`mistune`, `markdown-it-py` oder `python-markdown` -- aber für
"alle Links extrahieren" ist die Regex perfekt.
