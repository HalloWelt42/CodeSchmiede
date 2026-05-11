---
schema_version: 1
id: 276-hashtags-extrahieren
revision: 1
titel: Hashtags aus Text extrahieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [strings, regex, social-media]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Social-Media-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: hashtags
hints:
  - kosten: 0
    text: |
      Extrahiere alle Hashtags aus einem Text -- ohne #.
      Hashtag = #wort, wort = Buchstaben/Ziffern/Unterstrich, mind. 1.
      "Tolles #python und #regex hier!" → ["python", "regex"].
      Bei keinem Treffer → [].
  - kosten: 10
    text: |
      re.findall(r"#(\w+)", text). Die Capture-Group greift den
      Inhalt OHNE das #-Zeichen.
tests_sichtbar:
  - input: ["Tolles #python und #regex hier!"]
    expected: ["python", "regex"]
  - input: ["keine Hashtags"]
    expected: []
  - input: [""]
    expected: []
  - input: ["#solo"]
    expected: ["solo"]
tests_versteckt:
  - input: ["#a #b #c"]
    expected: ["a", "b", "c"]
  - input: ["#hashtag mit Text und #wieder_einer"]
    expected: ["hashtag", "wieder_einer"]
  - input: ["#123 #abc123"]
    expected: ["123", "abc123"]
  - input: ["text # leerer hashtag"]
    expected: []
  - input: ["##doppelt"]
    expected: ["doppelt"]
  - input: ["mitten#im#wort"]
    expected: ["im", "wort"]
  - input: ["#a #a #a"]
    expected: ["a", "a", "a"]
starter_code: |
  import re

  def hashtags(text: str) -> list[str]:
      # Deine Lösung hier -- Hashtags ohne #
      pass
---

# Hashtags aus Text extrahieren

Schreibe `hashtags(text)`, die alle Hashtags aus einem Text liefert
-- **ohne das `#`-Zeichen**, Reihenfolge wie im Text.

Ein Hashtag ist `#` gefolgt von einem oder mehreren **Wort-Zeichen**
(Buchstaben, Ziffern, Unterstrich).

## Beispiele

| Eingabe                                | Hashtags                       |
|----------------------------------------|--------------------------------|
| `"Tolles #python und #regex hier!"`    | `["python", "regex"]`          |
| `"#a #b #c"`                           | `["a", "b", "c"]`              |
| `"#solo"`                              | `["solo"]`                     |
| `"keine Hashtags"`                     | `[]`                           |
| `"text # leerer"`                      | `[]` (Leerzeichen nach #)      |
| `"##doppelt"`                          | `["doppelt"]`                  |
| `"mitten#im#wort"`                     | `["im", "wort"]`               |

## Idee -- Capture-Group

```python
import re

def hashtags(text):
    return re.findall(r"#(\w+)", text)
```

Die Klammern `(\w+)` sind eine **Capture-Group**: `re.findall`
liefert nur den Inhalt der Gruppe, also den Wort-Teil **ohne** das `#`.

## Erweiterungen

- **Mit Umlauten**: `r"#(\w+)"` matcht in Python standardmaessig
  Unicode-Wort-Zeichen, also auch `#München` -- in den Tests aber
  nicht berücksichtigt.
- **Nur am Wort-Anfang** (Twitter-Stil): `r"(?:^|\s)#(\w+)"` --
  `#` mitten im Wort wird nicht gematcht.

## Anwendung

Hashtags scannen ist Standard für Social-Media-Tools, Tag-Clouds,
Trend-Analysen oder Content-Moderation.
