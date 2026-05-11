---
schema_version: 1
id: 070-bug-summe
revision: 1
titel: Bug -- Summe einer Liste
sprache: python
task_type: bug_finden
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [bug-finden, listen, off-by-one]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Off-by-One-Bug
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: summe
hints:
  - kosten: 0
    text: Schau dir die Schleifenbedingung genau an.
  - kosten: 10
    text: |
      `range(len(zahlen) - 1)` lässt das letzte Element aus. Korrekt
      wäre `range(len(zahlen))`.
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: 6
  - input: [[10, 20, 30, 40]]
    expected: 100
  - input: [[]]
    expected: 0
  - input: [[5]]
    expected: 5
tests_versteckt:
  - input: [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    expected: 10
  - input: [[100, -50]]
    expected: 50
  - input: [[42]]
    expected: 42
starter_code: |
  def summe(zahlen):
      ergebnis = 0
      for i in range(len(zahlen) - 1):
          ergebnis += zahlen[i]
      return ergebnis
---

# Bug -- Summe einer Liste

Diese Funktion soll die Summe aller Zahlen in der Liste zurückgeben.
Sie laesst aber **immer das letzte Element weg**. Finde den Fehler!

## Was schief geht

```
summe([1, 2, 3])  # liefert 3 (= 1+2), sollte 6 sein
summe([10])       # liefert 0, sollte 10 sein
```

## Der Bug

Schau die Schleifen-Bedingung an. Wo wird das Problem entstehen?

## Hintergrund

**Off-by-One-Fehler** sind in der Welt der Software-Bugs der Klassiker
schlechthin. Falsch verwendete Range-Grenzen, vergessenes
"+1"/"-1", `<` statt `<=`. Ganze Sicherheitslücken sind genau so
entstanden.
