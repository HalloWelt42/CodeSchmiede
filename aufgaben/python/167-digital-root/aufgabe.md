---
schema_version: 1
id: 167-digital-root
revision: 1
titel: Digitale Wurzel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [zahlen, modulo, mathematik, ziffer]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Quersummen-Spiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: digitale_wurzel
hints:
  - kosten: 0
    text: |
      Bilde wiederholt die Quersumme einer nicht-negativen Zahl,
      bis nur noch eine Ziffer (0-9) übrig ist.
      9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.
  - kosten: 10
    text: |
      Klassisch: while n > 9: n = sum(int(z) for z in str(n)).
      Trick: digitale_wurzel(n) == 0 if n == 0 else 1 + (n - 1) % 9.
tests_sichtbar:
  - input: [0]
    expected: 0
  - input: [9]
    expected: 9
  - input: [16]
    expected: 7
  - input: [9875]
    expected: 2
tests_versteckt:
  - input: [1]
    expected: 1
  - input: [10]
    expected: 1
  - input: [99]
    expected: 9
  - input: [12345]
    expected: 6
  - input: [123456789]
    expected: 9
  - input: [999999999]
    expected: 9
  - input: [100000]
    expected: 1
starter_code: |
  def digitale_wurzel(n: int) -> int:
      # Deine Lösung hier -- 0-9
      pass
---

# Digitale Wurzel

Die **digitale Wurzel** einer nicht-negativen Zahl ist das Ergebnis,
das man erhaelt, wenn man die Quersumme so lange wiederholt, bis nur
noch eine **einzelne Ziffer** (0-9) übrig bleibt.

## Beispiele

| Zahl    | Schritte                | Wurzel |
|---------|--------------------------|--------|
| `9`     | `9`                      | `9`    |
| `16`    | `1+6 = 7`                | `7`    |
| `99`    | `9+9 = 18`, `1+8 = 9`    | `9`    |
| `9875`  | `29 → 11 → 2`            | `2`    |
| `12345` | `15 → 6`                 | `6`    |

## Lösung 2 -- Modulo-Trick

Eine Zahl ist genau dann durch 9 teilbar, wenn ihre Quersumme es ist.
Daraus folgt:

$$dr(n) = \begin{cases} 0 & n = 0 \\ 1 + ((n-1) \bmod 9) & n > 0 \end{cases}$$

Eine einzige Operation -- unabhängig von der Anzahl der Stellen.

## Hintergrund

Die digitale Wurzel ist die Grundlage der **Neuner-Probe** -- einem
historischen Verfahren zur Prüfung von Rechnungen. Wenn `a + b = c`
gilt, dann muss auch `dr(a) + dr(b) ≡ dr(c) (mod 9)` gelten.
Schüler haben das jahrzehntelang als Plausibilitaets-Check benutzt.
