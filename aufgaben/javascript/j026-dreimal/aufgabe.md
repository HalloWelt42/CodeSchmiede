---
schema_version: 1
id: j026-dreimal
revision: 1
titel: Einmal ändern, überall neu
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- variablen
- const
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mit Kommas setzt `console.log` die Leerzeichen zwischen Text und Namen selbst.
- kosten: 2
  text: '`console.log("Frischer", fisch);` und so weiter.'
tests_sichtbar:
- input: []
  expected: 'Frischer Hering

    Gebratener Hering

    Hering im Brötchen

    '
starter_code: ''
---

Der Fisch kommt dreimal in der Ansage vor. Schreibe das Programm so, dass der Fisch nur **einmal** im Code steht, in einer Konstante `fisch`, und dreimal ausgegeben wird:

```
Frischer Hering
Gebratener Hering
Hering im Brötchen
```

Wer morgen Makrele verkauft, ändert dann nur eine Stelle.
