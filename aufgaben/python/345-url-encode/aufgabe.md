---
schema_version: 1
id: 345-url-encode
revision: 1
titel: URL-Prozent-Codierung (eigene Implementierung)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [strings, codierung, url, web]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/URL_encoding
  notiz: Rosetta Code -- URL encoding (RFC 3986 unreserved)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: url_encode
hints:
  - kosten: 0
    text: |
      Codiere einen String fuer URLs:
      - unreserviert (RFC 3986): A-Z a-z 0-9 - _ . ~ unveraendert
      - alles andere als %XX (zwei Hex-Stellen, gross)
      Hinweis: in UTF-8 codieren, dann Byte-fuer-Byte mit %.
  - kosten: 20
    text: |
      Bytes via s.encode("utf-8"), pro Byte if-else fuer unreserviert
      ODER f"%{b:02X}".
tests_sichtbar:
  - input: ["Hallo"]
    expected: "Hallo"
  - input: ["Hallo Welt"]
    expected: "Hallo%20Welt"
  - input: [""]
    expected: ""
  - input: ["abc-_.~"]
    expected: "abc-_.~"
tests_versteckt:
  - input: ["a/b"]
    expected: "a%2Fb"
  - input: ["100%"]
    expected: "100%25"
  - input: ["?key=value"]
    expected: "%3Fkey%3Dvalue"
  - input: ["foo bar baz"]
    expected: "foo%20bar%20baz"
  - input: ["a+b=c"]
    expected: "a%2Bb%3Dc"
  - input: ["#hash"]
    expected: "%23hash"
  - input: ["abc123"]
    expected: "abc123"
starter_code: |
  def url_encode(s: str) -> str:
      # Tipp: utf-8 encoden, pro byte unreserviert oder %XX
      pass
---

# URL-Prozent-Codierung

Schreibe `url_encode(s)`, die einen String **URL-codiert** -- nach
RFC 3986 (Prozent-Codierung).

Regel:
- **Unreservierte Zeichen** (`A-Z a-z 0-9 - _ . ~`) bleiben unveraendert.
- Alles andere wird zu `%XX` (zwei Hex-Stellen, **gross**).
- Vorher in **UTF-8** kodieren, dann Byte-fuer-Byte verarbeiten.

## Beispiele

| Eingabe         | Ergebnis                  |
|-----------------|----------------------------|
| `"Hallo"`       | `"Hallo"`                 |
| `"Hallo Welt"`  | `"Hallo%20Welt"`          |
| `"100%"`        | `"100%25"`                |
| `"?key=value"`  | `"%3Fkey%3Dvalue"`        |
| `"a+b=c"`       | `"a%2Bb%3Dc"`             |
| `"abc-_.~"`     | `"abc-_.~"` (alles unreserviert) |
| `""`            | `""`                      |

## Idee

```python
UNRES = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~")

def url_encode(s):
    out = []
    for byte in s.encode("utf-8"):
        c = chr(byte)
        if c in UNRES:
            out.append(c)
        else:
            out.append(f"%{byte:02X}")
    return "".join(out)
```

`s.encode("utf-8")` liefert ein `bytes`-Objekt. Iteration darueber
gibt Integer-Werte (0-255). Fuer ASCII-Bytes ist `chr(byte)` das
entsprechende Zeichen.

## Stolperstein -- Umlaute (UTF-8)

`"ä"` ist in UTF-8 `0xC3 0xA4` -- zwei Bytes. Daher wird
`url_encode("ä")` zu `"%C3%A4"` (zwei Prozent-Codes).

## Vergleich mit Builtin

`urllib.parse.quote(s, safe='')` macht praktisch dasselbe -- mit
Default-Liste der "sicheren" Zeichen. Wir bauen es selbst, damit
das Pattern klar wird.

## Pendant

`url_decode` (entgegengesetzte Richtung) waere die Erweiterung:
`%XX` zurueck zu Byte, dann UTF-8-decoden.
