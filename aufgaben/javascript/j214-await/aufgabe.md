---
schema_version: 1
id: j214-await
revision: 1
titel: Schritt für Schritt warten
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- async
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: In einer Schleife darf await stehen, solange die Funktion async ist.
- kosten: 2
  text: Das Ergebnis einer async-Funktion holt ein await.
tests_sichtbar:
- input: []
  expected: 'Kaffee ist fertig

    Brötchen ist fertig

    Hering ist fertig

    Frühstück aus 3 Teilen

    '
starter_code: 'const warte = (ms) => new Promise((erfuellen) => setTimeout(erfuellen, ms));

  '
---

Schreib eine async-Funktion `fruehstueck()`, die nacheinander auf drei Dinge wartet und jedes meldet. Danach meldet das Hauptprogramm, wie viele es waren:

```
Kaffee ist fertig
Brötchen ist fertig
Hering ist fertig
Frühstück aus 3 Teilen
```
