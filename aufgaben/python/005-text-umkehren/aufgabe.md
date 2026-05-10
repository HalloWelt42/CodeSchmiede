---
schema_version: 1
id: 005-text-umkehren
revision: 1
titel: Text umkehren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [strings, slicing]
pfade: [python_strings]
voraussetzungen: []
quelle:
  url: null
  notiz: String-Slicing als Einstieg
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: text_umkehren
hints:
  - kosten: 0
    text: Python kann Strings rückwärts mit Slicing lesen.
  - kosten: 15
    text: |
      Slicing-Notation `[start:stop:schritt]`. Wenn Schritt `-1` ist,
      geht es rückwärts.
  - kosten: 25
    text: |
      Idiomatisch:

      ```
      return text[::-1]
      ```
tests_sichtbar:
  - input: ["abc"]
    expected: "cba"
  - input: [""]
    expected: ""
  - input: ["a"]
    expected: "a"
  - input: ["hallo"]
    expected: "ollah"
tests_versteckt:
  - input: ["12345"]
    expected: "54321"
  - input: ["Python"]
    expected: "nohtyP"
  - input: ["  "]
    expected: "  "
  - input: ["a b c"]
    expected: "c b a"
starter_code: |
  def text_umkehren(text: str) -> str:
      # Deine Lösung hier
      pass
---

# Text umkehren

Schreibe eine Funktion `text_umkehren(text)`, die den übergebenen
String **rückwärts** zurückgibt.

## Beispiele

| Eingabe         | Ausgabe   |
|-----------------|-----------|
| `"abc"`         | `"cba"`   |
| `"hallo"`       | `"ollah"` |
| `""`            | `""`      |
| `"a b c"`       | `"c b a"` |

## Hinweise

- Auch der leere String muss zurückgegeben werden (als leerer String).
- Leerzeichen bleiben Zeichen wie alle anderen.
