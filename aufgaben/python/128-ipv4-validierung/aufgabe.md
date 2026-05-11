---
schema_version: 1
id: 128-ipv4-validierung
revision: 1
titel: IPv4-Adresse validieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, parsing, netzwerk, validierung]
pfade: [python_codes]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/IPv4
  notiz: Klassische Netzwerk-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_ipv4
hints:
  - kosten: 0
    text: |
      4 Zahlen, durch Punkte getrennt, jede zwischen 0 und 255.
      Keine fuehrenden Nullen ("01" ist invalid). Kein Whitespace.
  - kosten: 8
    text: |
      `text.split('.')` muss exakt 4 Teile geben. Pro Teil:
      isdigit, > "0" → keine fuehrende Null (außer bei 1 Stelle),
      0 <= int(t) <= 255.
tests_sichtbar:
  - input: ["192.168.1.1"]
    expected: true
  - input: ["0.0.0.0"]
    expected: true
  - input: ["255.255.255.255"]
    expected: true
  - input: ["256.1.1.1"]
    expected: false
tests_versteckt:
  - input: ["192.168.1"]
    expected: false
  - input: ["192.168.1.1.1"]
    expected: false
  - input: [""]
    expected: false
  - input: ["192.168.01.1"]
    expected: false
  - input: ["192.168.-1.1"]
    expected: false
  - input: ["a.b.c.d"]
    expected: false
  - input: [" 192.168.1.1 "]
    expected: false
  - input: ["192.168.1.1\n"]
    expected: false
starter_code: |
  def ist_ipv4(text: str) -> bool:
      # Deine Lösung hier -- 4 Zahlen 0-255, keine fuehrenden Nullen.
      pass
---

# IPv4-Adresse validieren

Schreibe eine Funktion `ist_ipv4(text)`, die prüft, ob ein String eine
**gültige IPv4-Adresse** ist.

## Regeln

- Genau **4 Zahlen**, getrennt durch Punkte
- Jede Zahl zwischen **0 und 255** (inklusiv)
- **Keine führenden Nullen**: `"01"` ist ungültig, `"0"` ist ok
- **Keine Vorzeichen, kein Whitespace, kein Newline**

## Beispiele

| Eingabe              | Gültig? |
|----------------------|---------|
| `"192.168.1.1"`      | `True`  |
| `"0.0.0.0"`          | `True`  |
| `"255.255.255.255"`  | `True`  |
| `"256.1.1.1"`        | `False` |
| `"192.168.1"`        | `False` |
| `"192.168.01.1"`     | `False` |
| `" 192.168.1.1 "`    | `False` |
| `"a.b.c.d"`          | `False` |

## Hintergrund

IPv4-Adressen sind seit den 1980ern Standard und werden langsam von
IPv6 abgelöst. Die strikte Validierung mit den Regeln oben gilt für
"dotted-decimal notation" (RFC 791).
