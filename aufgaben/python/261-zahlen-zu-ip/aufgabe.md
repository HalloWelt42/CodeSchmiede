---
schema_version: 1
id: 261-zahlen-zu-ip
revision: 1
titel: Vier Zahlen zur IPv4 zusammensetzen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, listen, netzwerk, formatierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 260
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ip_zusammen
hints:
  - kosten: 0
    text: |
      Setze [a, b, c, d] zu "a.b.c.d" zusammen.
      Bei UNGUELTIGEN Werten (nicht 4 Teile, nicht 0..255) → "".
  - kosten: 10
    text: |
      Prüfe len == 4 und alle Werte 0..255.
      ".".join(str(x) for x in zahlen).
tests_sichtbar:
  - input: [[192, 168, 1, 1]]
    expected: "192.168.1.1"
  - input: [[0, 0, 0, 0]]
    expected: "0.0.0.0"
  - input: [[255, 255, 255, 255]]
    expected: "255.255.255.255"
  - input: [[]]
    expected: ""
tests_versteckt:
  - input: [[8, 8, 8, 8]]
    expected: "8.8.8.8"
  - input: [[10, 20, 30, 40]]
    expected: "10.20.30.40"
  - input: [[256, 0, 0, 0]]
    expected: ""
  - input: [[1, 2, 3]]
    expected: ""
  - input: [[1, 2, 3, 4, 5]]
    expected: ""
  - input: [[-1, 0, 0, 0]]
    expected: ""
  - input: [[127, 0, 0, 1]]
    expected: "127.0.0.1"
starter_code: |
  def ip_zusammen(zahlen: list[int]) -> str:
      # Deine Lösung hier -- ungueltig → ""
      pass
---

# Vier Zahlen zur IPv4 zusammensetzen

Schreibe `ip_zusammen(zahlen)`, die `[a, b, c, d]` mit vier Zahlen
(jeweils 0..255) zu einem IPv4-String `"a.b.c.d"` zusammensetzt.

Bei ungültiger Eingabe → `""`.

## Beispiele

| Eingabe                   | Ergebnis              |
|---------------------------|-----------------------|
| `[192, 168, 1, 1]`        | `"192.168.1.1"`       |
| `[0, 0, 0, 0]`            | `"0.0.0.0"`           |
| `[255, 255, 255, 255]`    | `"255.255.255.255"`   |
| `[127, 0, 0, 1]`          | `"127.0.0.1"`         |
| `[256, 0, 0, 0]`          | `""` (256 zu hoch)    |
| `[1, 2, 3]`               | `""` (zu wenig)       |
| `[]`                      | `""`                  |

## Idee

```python
def ip_zusammen(zahlen):
    if len(zahlen) != 4:
        return ""
    if not all(0 <= x <= 255 for x in zahlen):
        return ""
    return ".".join(str(x) for x in zahlen)
```

Drei Schritte: Laenge prüfen, Werte prüfen, joinen.

## Pendant

Aufgabe **260-ip-zu-zahlen** macht den Weg hin (String → Liste).
Zusammen ist es ein **Round-Trip**:

```python
ip_zusammen(ip_zerlegen("8.8.8.8")) == "8.8.8.8"
```

## Loopback und 0.0.0.0

- `127.0.0.1` ist die **Loopback-IP** -- der eigene Rechner.
- `0.0.0.0` ist "alle Interfaces" beim Listen-Server,
  aber "ungültig" als Quell-Adresse.
- `255.255.255.255` ist die **Broadcast-Adresse**.
