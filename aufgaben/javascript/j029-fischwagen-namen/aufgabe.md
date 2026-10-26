---
schema_version: 1
id: j029-fischwagen-namen
revision: 1
titel: 'Fischwagen: Wagen und Kunde'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- projekt
- variablen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`console.log("*** Fischwagen", wagen, "***");` setzt die Leerzeichen selbst.'
tests_sichtbar:
- input: []
  expected: '*** Fischwagen Zum frostigen Hering ***

    Kassenbon für Pia

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 2.** Der Kassenbon soll für jeden Kunden passen. Lege den Namen des Wagens als Konstante `wagen` an (`"Zum frostigen Hering"`) und den Kunden als `let kunde` (`"Pia"`). Gib damit aus:

```
*** Fischwagen Zum frostigen Hering ***
Kassenbon für Pia
```

Die Sternchen bleiben Text, Wagen und Kunde kommen aus den Namen.
