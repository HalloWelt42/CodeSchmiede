---
schema_version: 1
id: 186-zahl-zu-bisexagesimal
revision: 1
titel: Sekunden in Stunden:Minuten:Sekunden
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, zeit, formatierung, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Zeit-Konvertierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zeit_format
hints:
  - kosten: 0
    text: |
      Konvertiere eine Anzahl Sekunden in das Format "HH:MM:SS"
      (Stunden zweistellig, kann auch > 24 sein).
      Bei n < 0 → "00:00:00".
  - kosten: 10
    text: |
      h = n // 3600, m = (n // 60) % 60, s = n % 60.
      f"{h:02}:{m:02}:{s:02}".
tests_sichtbar:
  - input: [0]
    expected: "00:00:00"
  - input: [60]
    expected: "00:01:00"
  - input: [3600]
    expected: "01:00:00"
  - input: [3661]
    expected: "01:01:01"
tests_versteckt:
  - input: [59]
    expected: "00:00:59"
  - input: [3599]
    expected: "00:59:59"
  - input: [86400]
    expected: "24:00:00"
  - input: [-5]
    expected: "00:00:00"
  - input: [359999]
    expected: "99:59:59"
  - input: [3725]
    expected: "01:02:05"
starter_code: |
  def zeit_format(sekunden: int) -> str:
      # Deine Lösung hier -- HH:MM:SS, h kann > 24 sein
      pass
---

# Sekunden in Stunden:Minuten:Sekunden

Schreibe `zeit_format(sekunden)`, die eine **Anzahl Sekunden** in
das Format `"HH:MM:SS"` umwandelt -- jeder Teil **zweistellig** mit
fuehrender Null.

Stunden können **größer als 24** sein (kein Tagesüberlauf).
Bei `sekunden < 0` → `"00:00:00"`.

## Beispiele

| Sekunden  | Format        |
|-----------|---------------|
| `0`       | `"00:00:00"`  |
| `60`      | `"00:01:00"`  |
| `3600`    | `"01:00:00"`  |
| `3661`    | `"01:01:01"`  |
| `86400`   | `"24:00:00"`  |
| `359999`  | `"99:59:59"`  |
| `-5`      | `"00:00:00"`  |

## Idee

```python
def zeit_format(sekunden):
    if sekunden < 0:
        return "00:00:00"
    h = sekunden // 3600
    m = (sekunden // 60) % 60
    s = sekunden % 60
    return f"{h:02}:{m:02}:{s:02}"
```

Der Format-Specifier `:02` fuellt mit fuehrenden Nullen auf zwei
Stellen auf.

## Sexagesimal-Zahlsystem

Unsere Zeit-Einteilung kommt aus Babylon: 60 Sekunden, 60 Minuten,
360 Grad im Vollkreis. **Sexagesimal** = "Basis 60". Vorteil: 60
hat sehr viele Teiler (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60),
was Bruchrechnungen ohne Dezimalpunkt erleichtert.

## Erweiterung

Mit `divmod` könnte man die Berechnung verdichten:

```python
m, s = divmod(sekunden, 60)
h, m = divmod(m, 60)
```

Geschmackssache -- liest sich kompakter, ist aber subtiler.
