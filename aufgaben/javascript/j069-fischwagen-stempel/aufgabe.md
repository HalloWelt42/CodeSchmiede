---
schema_version: 1
id: j069-fischwagen-stempel
revision: 1
titel: 'Fischwagen: Treuestempel'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- projekt
- wahrheit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Nimm deinen Code aus Kapitel 5 und hänge zwei Zeilen an.
- kosten: 2
  text: '`console.log("Treuestempel:", summe >= 10);` und `broetchen >= 3 && limonaden === 0`.'
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Treuestempel: true

    Gratis-Limonade: false

    '
tests_versteckt:
- input:
  - Ole
  - '4'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Ole

    4 x Heringsbrötchen: 10.00 Euro

    0 x Limonade: 0.00 Euro

    ==============================

    Summe: 10.00 Euro

    Treuestempel: true

    Gratis-Limonade: true

    '
- input:
  - Ida
  - '1'
  - '1'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Ida

    1 x Heringsbrötchen: 2.50 Euro

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 4.25 Euro

    Treuestempel: false

    Gratis-Limonade: false

    '
- input:
  - Bo
  - '2'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Bo

    2 x Heringsbrötchen: 5.00 Euro

    0 x Limonade: 0.00 Euro

    ==============================

    Summe: 5.00 Euro

    Treuestempel: false

    Gratis-Limonade: false

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 6.** Pit verteilt Treuestempel ab 10 Euro Einkauf, und wer mindestens 3 Brötchen und keine Limonade nimmt, bekommt eine Limonade gratis. Schreib beides als true oder false unter den Bon. Bei den Eingaben `Pia`, `3` und `2`:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Brötchen? Limonaden? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Treuestempel: true
Gratis-Limonade: false
```
