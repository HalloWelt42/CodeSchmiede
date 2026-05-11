---
schema_version: 1
id: 260-ip-zu-zahlen
revision: 1
titel: IPv4-String in vier Zahlen zerlegen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [strings, parsing, netzwerk]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Netzwerk-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ip_zerlegen
hints:
  - kosten: 0
    text: |
      Zerlege "a.b.c.d" in [a, b, c, d] (4 Ints, je 0..255).
      Bei UNGUELTIGER Eingabe (zu wenig/viel Teile, Wert > 255,
      nicht-numerisch, leer) → [].
  - kosten: 15
    text: |
      teile = s.split("."); prüfen len == 4 und alle 0..255.
      try/except ValueError für int().
tests_sichtbar:
  - input: ["192.168.1.1"]
    expected: [192, 168, 1, 1]
  - input: ["0.0.0.0"]
    expected: [0, 0, 0, 0]
  - input: ["255.255.255.255"]
    expected: [255, 255, 255, 255]
  - input: [""]
    expected: []
tests_versteckt:
  - input: ["10.20.30.40"]
    expected: [10, 20, 30, 40]
  - input: ["256.0.0.0"]
    expected: []
  - input: ["1.2.3"]
    expected: []
  - input: ["1.2.3.4.5"]
    expected: []
  - input: ["abc.def.ghi.jkl"]
    expected: []
  - input: ["-1.0.0.0"]
    expected: []
  - input: ["8.8.8.8"]
    expected: [8, 8, 8, 8]
starter_code: |
  def ip_zerlegen(s: str) -> list[int]:
      # Deine Lösung hier -- ungueltig → []
      pass
---

# IPv4-String in vier Zahlen zerlegen

Schreibe `ip_zerlegen(s)`, die einen IPv4-String (`"a.b.c.d"`) in
eine Liste `[a, b, c, d]` mit vier Integern (jeweils 0..255)
zerlegt.

Bei ungültiger Eingabe → `[]`.

Ungültig sind:
- nicht 4 Teile
- nicht-numerische Werte
- Werte außerhalb 0..255
- leerer String, fuehrende Vorzeichen

## Beispiele

| Eingabe              | Ergebnis              |
|----------------------|-----------------------|
| `"192.168.1.1"`      | `[192, 168, 1, 1]`    |
| `"0.0.0.0"`          | `[0, 0, 0, 0]`        |
| `"255.255.255.255"`  | `[255, 255, 255, 255]`|
| `"8.8.8.8"`          | `[8, 8, 8, 8]`        |
| `"256.0.0.0"`        | `[]` (256 zu hoch)    |
| `"1.2.3"`            | `[]` (zu wenig Teile) |
| `"1.2.3.4.5"`        | `[]` (zu viele)       |
| `"abc.def.ghi.jkl"`  | `[]`                  |

## Idee

```python
def ip_zerlegen(s):
    teile = s.split(".")
    if len(teile) != 4:
        return []
    out = []
    for t in teile:
        if not t or t.startswith(("-", "+")) or not t.isdigit():
            return []
        n = int(t)
        if not 0 <= n <= 255:
            return []
        out.append(n)
    return out
```

`isdigit` schließt auch fuehrende Nullen wie `"007"` als gültig ein.
Wer das verbieten will, kann zusaetzlich prüfen:

```python
if len(t) > 1 and t[0] == "0":
    return []
```

## Pendant

Aufgabe **261-zahlen-zu-ip** macht den Weg zurück.
Aufgabe **128-ipv4-validierung** liefert nur True/False.

## Hintergrund

IPv4 hat **32 Bit** = 4 Bytes a 8 Bit = 4 Zahlen 0..255.
Insgesamt $2^{32} \approx 4{,}3$ Milliarden Adressen -- bei 8 Mrd
Menschen plus IoT-Geräten klar zu wenig. Darum **IPv6** (128 Bit).
