---
schema_version: 1
id: 072-js-quadrat
revision: 1
titel: JavaScript -- Quadrat
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags: [javascript, einsteiger, arithmetik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Erste JS-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: quadrat
hints:
  - kosten: 0
    text: Multipliziere die Zahl mit sich selbst.
tests_sichtbar:
  - input: [3]
    expected: 9
  - input: [0]
    expected: 0
  - input: [-4]
    expected: 16
  - input: [1.5]
    expected: 2.25
tests_versteckt: []
starter_code: |
  function quadrat(n) {
      // Deine Loesung hier
  }
---

# JavaScript -- Quadrat

Schreibe eine Funktion `quadrat(n)`, die das Quadrat einer Zahl
zurueckgibt.

## Beispiele

| Eingabe | Ergebnis |
|---------|----------|
| `3`     | `9`      |
| `0`     | `0`      |
| `-4`    | `16`     |
| `1.5`   | `2.25`   |

## Hintergrund

Diese Aufgabe laeuft **clientseitig im WebWorker** -- kein Docker, kein
Backend-Sandbox-Run. Damit ist sie blitzschnell, hat aber eine
eingebaute Einschraenkung: **versteckte Tests gibt es nicht**, weil
der Client den Test-Code immer sehen kann. Anti-Hardcoding-Schutz wie
bei Python-Aufgaben funktioniert hier nicht.
