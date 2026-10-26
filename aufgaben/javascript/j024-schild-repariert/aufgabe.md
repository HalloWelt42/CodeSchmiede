---
schema_version: 1
id: j024-schild-repariert
revision: 1
titel: Das Schild klemmt
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
  text: Welcher Name bekommt später einen neuen Wert?
- kosten: 2
  text: Aus `const kunde` wird `let kunde`.
tests_sichtbar:
- input: []
  expected: 'Zum frostigen Hering begrüßt Pia

    Zum frostigen Hering begrüßt Paul

    '
starter_code: 'const wagen = "Zum frostigen Hering";

  const kunde = "Pia";

  console.log(wagen, "begrüßt", kunde);

  kunde = "Paul";

  console.log(wagen, "begrüßt", kunde);

  '
---

Dieses Programm bricht ab: `TypeError: Assignment to constant variable.` Der Kunde wechselt, der Wagen nicht. Ändere **ein Wort**, damit herauskommt:

```
Zum frostigen Hering begrüßt Pia
Zum frostigen Hering begrüßt Paul
```
