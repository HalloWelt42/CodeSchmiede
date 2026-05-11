---
schema_version: 1
id: 277-emails-extrahieren
revision: 1
titel: Email-Adressen aus Text extrahieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, regex, parsing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Regex-Aufgabe (vereinfacht)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: emails
hints:
  - kosten: 0
    text: |
      Extrahiere alle einfachen Email-Adressen aus dem Text.
      Pattern: word@word.word -- Buchstaben, Ziffern, Punkt,
      Unterstrich, Bindestrich vor dem @, gleicher Charset nach @,
      dann ein Punkt und mind. 2 Buchstaben.
  - kosten: 15
    text: |
      re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", text).
      Achtung: das ist nur EIN sinnvolles Pattern -- echte
      Email-RFCs sind viel komplizierter.
tests_sichtbar:
  - input: ["Schreib an alice@example.com bitte"]
    expected: ["alice@example.com"]
  - input: ["keine Mail"]
    expected: []
  - input: [""]
    expected: []
  - input: ["a@b.de und c@d.com"]
    expected: ["a@b.de", "c@d.com"]
tests_versteckt:
  - input: ["test.user+tag@firma-name.co.uk"]
    expected: ["test.user+tag@firma-name.co.uk"]
  - input: ["info@codeschmiede.example"]
    expected: ["info@codeschmiede.example"]
  - input: ["ungueltig@.com"]
    expected: []
  - input: ["@nichts.de"]
    expected: []
  - input: ["nichts@.de"]
    expected: []
  - input: ["my@jobmagnetix.de"]
    expected: ["my@jobmagnetix.de"]
  - input: ["x@y.zz und a@b.cd."]
    expected: ["x@y.zz", "a@b.cd"]
starter_code: |
  import re

  def emails(text: str) -> list[str]:
      # Deine Lösung hier -- vereinfachtes Email-Pattern
      pass
---

# Email-Adressen aus Text extrahieren

Schreibe `emails(text)`, die alle (einfachen) Email-Adressen aus
einem Text liefert.

Pattern (vereinfacht):
- vor dem `@`: ein oder mehr von `\w`, `.`, `+`, `-`
- nach dem `@`: ein oder mehr von `\w`, `-`
- dann **genau ein** `.`
- am Ende: mindestens **2 Buchstaben**

## Beispiele

| Eingabe                                       | Ergebnis                                   |
|-----------------------------------------------|--------------------------------------------|
| `"Schreib an alice@example.com bitte"`        | `["alice@example.com"]`                    |
| `"a@b.de und c@d.com"`                        | `["a@b.de", "c@d.com"]`                    |
| `"test.user+tag@firma-name.co.uk"`            | `["test.user+tag@firma-name.co.uk"]`       |
| `"my@jobmagnetix.de"`                         | `["my@jobmagnetix.de"]`                    |
| `"keine Mail"`                                | `[]`                                       |
| `"@nichts.de"`                                | `[]` (kein lokaler Teil)                   |
| `"nichts@.de"`                                | `[]` (kein Domain-Body)                    |

## Idee

```python
import re

def emails(text):
    return re.findall(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}", text)
```

## Warum kein "perfektes" Email-Regex?

Die offizielle RFC-5322-Email-Spec ist mehrere hundert Zeichen lang
und matcht z.B. auch Adressen mit Klammern oder Quoting. Für 99%
aller Praxis-Anwendungen reicht ein simpleres Pattern.

**Faustregel**: Email-Validierung "perfekt" gibt es nicht. Wer
wirklich sichergehen will, schickt eine **Bestaetigungs-Email** --
die ist die einzige verlaessliche Prüfung.

## Stolperstein

Im Test `"x@y.zz und a@b.cd."` matcht das Pattern den letzten Punkt
**nicht** mit. Das `.` in `[a-zA-Z]{2,}` war kein Punkt sondern eine
Buchstaben-Bedingung -- wir liefern `"a@b.cd"` ohne den Schluss-Punkt.
