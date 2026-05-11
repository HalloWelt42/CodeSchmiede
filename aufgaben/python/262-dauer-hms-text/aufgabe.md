---
schema_version: 1
id: 262-dauer-hms-text
revision: 1
titel: Dauer als "Xh Ym Zs" formatieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [zahlen, strings, zeit, formatierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Zeitangabe in CLI/UI
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dauer_text
hints:
  - kosten: 0
    text: |
      Formatiere Sekunden als kompakter Text:
      0 → "0s", 60 → "1m", 3600 → "1h", 3661 → "1h 1m 1s".
      Nullen WEGLASSEN.
      Sekunden < 0 → "0s".
  - kosten: 15
    text: |
      h, m, s extrahieren. teile = []; jeweils anhängen wenn > 0.
      Bei alle == 0 → "0s".
tests_sichtbar:
  - input: [0]
    expected: "0s"
  - input: [60]
    expected: "1m"
  - input: [3600]
    expected: "1h"
  - input: [3661]
    expected: "1h 1m 1s"
tests_versteckt:
  - input: [59]
    expected: "59s"
  - input: [3601]
    expected: "1h 1s"
  - input: [3660]
    expected: "1h 1m"
  - input: [86400]
    expected: "24h"
  - input: [-5]
    expected: "0s"
  - input: [125]
    expected: "2m 5s"
  - input: [3725]
    expected: "1h 2m 5s"
  - input: [359999]
    expected: "99h 59m 59s"
starter_code: |
  def dauer_text(sekunden: int) -> str:
      # Deine Lösung hier -- Nullen weglassen, "0s" wenn alles 0
      pass
---

# Dauer als "Xh Ym Zs" formatieren

Schreibe `dauer_text(sekunden)`, die eine Zeit als kompakten Text
ausgibt -- mit den Einheiten **h**, **m**, **s**, aber **Nullen
weggelassen**.

Negative Zahlen → `"0s"`.

## Beispiele

| Sekunden | Text         |
|----------|--------------|
| 0        | `"0s"`       |
| 59       | `"59s"`      |
| 60       | `"1m"`       |
| 125      | `"2m 5s"`    |
| 3600     | `"1h"`       |
| 3601     | `"1h 1s"`    |
| 3660     | `"1h 1m"`    |
| 3661     | `"1h 1m 1s"` |
| 3725     | `"1h 2m 5s"` |
| 86400    | `"24h"`      |
| -5       | `"0s"`       |

## Idee

```python
def dauer_text(sekunden):
    if sekunden <= 0:
        return "0s"
    h = sekunden // 3600
    m = (sekunden // 60) % 60
    s = sekunden % 60
    teile = []
    if h:
        teile.append(f"{h}h")
    if m:
        teile.append(f"{m}m")
    if s:
        teile.append(f"{s}s")
    return " ".join(teile)
```

## Verwandt -- Aufgabe 186 mit fester Form

Aufgabe **186-zahl-zu-bisexagesimal** liefert immer
`"HH:MM:SS"` (mit fuehrenden Nullen). Hier ist die Form **kompakt**
und überspringt Nullen -- besser für CLI-Tool-Output, schlechter
für feste Tabellen-Spalten.

## Anwendung

- Build-Zeiten in CI: "Build dauerte 1h 23m 5s".
- Video-Dauer in Listen: "1h 30m" statt "01:30:00".
- Backup-Dauer-Logs.
