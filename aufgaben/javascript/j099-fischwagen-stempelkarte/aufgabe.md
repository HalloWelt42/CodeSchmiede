---
schema_version: 1
id: j099-fischwagen-stempelkarte
revision: 1
titel: 'Fischwagen: die Stempelkarte'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- projekt
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`Math.min(5, Math.floor(summe / 10))` ist die Zahl der Stempel.'
- kosten: 2
  text: 'In der Schleife über die fünf Felder: `karte += i < stempel ? "[*]" : "[ ]";`'
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  - Ole
  - '8'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Brötchen? Limonaden? Kassenbon für Ole

    8 x Heringsbrötchen: 20.00 Euro

    0 x Limonade: 0.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt: -2.00 Euro

    Summe: 18.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Kunden heute: 2

    Tagesumsatz: 29.00 Euro

    '
tests_versteckt:
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

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Kunden heute: 1

    Tagesumsatz: 4.25 Euro

    '
- input:
  - Bo
  - '30'
  - '4'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Bo

    30 x Heringsbrötchen: 75.00 Euro

    4 x Limonade: 7.00 Euro

    ==============================

    Rabatt: -8.20 Euro

    Summe: 73.80 Euro

    Stempel: [*][*][*][*][*]

    Kunde? Kunden heute: 1

    Tagesumsatz: 73.80 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 9.** Statt ja oder nein gibt es jetzt eine Stempelkarte mit fünf Feldern: für je **volle** 10 Euro der Summe nach Rabatt ein Stempel `[*]`, höchstens fünf, die übrigen Felder bleiben `[ ]`. Bau die Karte mit einer for-Schleife. Bei den Eingaben `Pia`, `3`, `2`, `Ole`, `8`, `0` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Brötchen? Limonaden? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Brötchen? Limonaden? Kassenbon für Ole
8 x Heringsbrötchen: 20.00 Euro
0 x Limonade: 0.00 Euro
1 x Limonade: gratis
==============================
Rabatt: -2.00 Euro
Summe: 18.00 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Kunden heute: 2
Tagesumsatz: 29.00 Euro
```
