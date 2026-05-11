---
schema_version: 1
id: 247-runden-zu-vielfache
revision: 1
titel: Auf Vielfaches von k runden
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, runden, modulo]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Rundungs-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: runde_zu_vielfache
hints:
  - kosten: 0
    text: |
      Runde n auf das nächste Vielfache von k.
      Bei Gleichstand: Standard-Python-Rundung (banker's rounding).
      k <= 0 → n unverändert.
      Negative n und k werden korrekt behandelt.
  - kosten: 10
    text: |
      round(n / k) * k -- Standard-Trick.
tests_sichtbar:
  - input: [13, 5]
    expected: 15
  - input: [12, 5]
    expected: 10
  - input: [0, 5]
    expected: 0
  - input: [100, 10]
    expected: 100
tests_versteckt:
  - input: [7, 3]
    expected: 6
  - input: [-13, 5]
    expected: -15
  - input: [25, 10]
    expected: 20
  - input: [123, 25]
    expected: 125
  - input: [0, 0]
    expected: 0
  - input: [50, -10]
    expected: 50
  - input: [99, 100]
    expected: 100
starter_code: |
  def runde_zu_vielfache(n: int, k: int) -> int:
      # Deine Lösung hier
      pass
---

# Auf Vielfaches von k runden

Schreibe `runde_zu_vielfache(n, k)`, die `n` auf das **nächste
Vielfache von k** rundet.

- Bei `k <= 0` → `n` unverändert.
- Bei Gleichstand: Pythons Standard-Rundung ("banker's rounding"
  zur **geraden** Zahl).
- Funktioniert mit positiven und negativen Werten.

## Beispiele

| `n`  | `k`  | Ergebnis | Begruendung               |
|------|------|----------|---------------------------|
| 13   | 5    | 15       | naeher an 15 als an 10    |
| 12   | 5    | 10       | naeher an 10 als an 15    |
| 7    | 3    | 6        | naeher an 6 als an 9      |
| 25   | 10   | 20       | banker's: gerade Zahl     |
| 100  | 10   | 100      | schon Vielfaches          |
| 99   | 100  | 100      | nächstes Vielfaches      |
| -13  | 5    | -15      | symmetrisch               |

## Idee

```python
def runde_zu_vielfache(n, k):
    if k <= 0:
        return n
    return round(n / k) * k
```

Der Trick: durch k teilen, runden, mit k multiplizieren.

## Banker's Rounding

In Python rundet `round` bei `.5` auf die **gerade** Zahl:

```python
round(0.5)   # 0
round(1.5)   # 2
round(2.5)   # 2
round(3.5)   # 4
```

Das ist statistisch fairer als immer aufrunden -- vermeidet **Bias**
bei vielen Werten. In der Praxis gemerkenswert, wenn man "runden"
beibringt.

## Anwendung

- Preise auf 5-ct runden (Supermarkt-Kassen-Logik).
- Pixel-Snap auf Raster (UI-Layout).
- Zeit-Slots: 14:23 Uhr → nächstes 15-Min-Slot.
