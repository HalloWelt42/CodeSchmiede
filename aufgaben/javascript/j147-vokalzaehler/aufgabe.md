---
schema_version: 1
id: j147-vokalzaehler
revision: 1
titel: Der Vokalzähler
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Zählschleife wandert in die Funktion, die das Ergebnis mit return liefert.
- kosten: 2
  text: Das bisher beste Wort merken und mit `vokale(...)` vergleichen.
tests_sichtbar:
- input:
  - Hering
  - Aal
  - Fischsuppe
  expected: 'Wort? Hering: 2

    Wort? Aal: 2

    Wort? Fischsuppe: 3

    Wort? Die meisten: Fischsuppe

    '
tests_versteckt:
- input:
  - Oase
  - Eis
  - ''
  expected: 'Wort? Oase: 3

    Wort? Eis: 2

    Wort? Die meisten: Oase

    '
- input:
  - ab
  - ba
  expected: 'Wort? ab: 1

    Wort? ba: 1

    Wort? Die meisten: ab

    '
starter_code: ''
---

Schreib `vokale(wort)`, die die Vokale eines Wortes zählt (groß und klein, mit Umlauten). Lies Wörter, bis eine leere Antwort oder keine mehr kommt, und gib zu jedem die Zahl aus. Am Ende das Wort mit den meisten Vokalen (bei Gleichstand das erste). Bei den Eingaben `Hering`, `Aal` und `Fischsuppe`:

```
Wort? Hering: 2
Wort? Aal: 2
Wort? Fischsuppe: 3
Wort? Die meisten: Fischsuppe
```
