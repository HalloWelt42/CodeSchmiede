---
schema_version: 1
id: 058-schaltjahr
revision: 1
titel: Schaltjahr prüfen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [zahlen, if-else, modulo, datum]
pfade: [python_datum]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Schaltjahr
  notiz: Klassischer Test für if/else-Verschachtelung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_schaltjahr
hints:
  - kosten: 0
    text: |
      Regel im Gregorianischen Kalender:
      - durch 4 teilbar: ja, außer
      - durch 100 teilbar: nein, außer
      - durch 400 teilbar: ja
  - kosten: 10
    text: |
      Kompakt: `(jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0`.
tests_sichtbar:
  - input: [2024]
    expected: true
  - input: [2023]
    expected: false
  - input: [2000]
    expected: true
  - input: [1900]
    expected: false
tests_versteckt:
  - input: [1]
    expected: false
  - input: [4]
    expected: true
  - input: [100]
    expected: false
  - input: [400]
    expected: true
  - input: [2400]
    expected: true
  - input: [2100]
    expected: false
starter_code: |
  def ist_schaltjahr(jahr: int) -> bool:
      # Deine Lösung hier -- Gregorianischer Kalender.
      pass
---

# Schaltjahr prüfen

Schreibe eine Funktion `ist_schaltjahr(jahr)`, die prüft, ob ein Jahr
ein **Schaltjahr** im Gregorianischen Kalender ist.

## Regel

Ein Jahr ist Schaltjahr, wenn:

1. es durch **4** teilbar ist
2. **aber nicht** durch **100** teilbar ist,
3. **es sei denn**, es ist auch durch **400** teilbar

In Code:

```
(jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0
```

## Beispiele

| Jahr  | Schaltjahr? | Wegen                       |
|-------|-------------|-----------------------------|
| 2024  | `True`      | durch 4, nicht durch 100    |
| 2023  | `False`     | nicht durch 4               |
| 2000  | `True`      | durch 400                   |
| 1900  | `False`     | durch 100, nicht durch 400  |
| 2100  | `False`     | wie 1900                    |
| 2400  | `True`      | wie 2000                    |

## Hintergrund

Diese Regel kompensiert, dass ein Sonnenjahr ungefaehr 365.2422 Tage
hat -- nicht ganz 365.25. Die 400-Jahr-Ausnahme korrigiert den
Überschuss, der entstehen würde, wenn man jedes durch 4 teilbare
Jahr als Schaltjahr nehmen würde.

Die Regel wurde 1582 von **Papst Gregor XIII.** eingefuehrt, als der
julianische Kalender über die Jahrhunderte aus dem Tritt geraten war.
