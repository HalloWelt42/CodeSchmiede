---
schema_version: 1
id: j109-fischwagen-speisekarte
revision: 1
titel: 'Fischwagen: die Speisekarte'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- array
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Zwei Arrays, gleicher Index: `waren[i]` kostet `preise[i]`.'
- kosten: 1
  text: 'Die Anzahlen je Kunde: ein leeres Array, dann für jede Ware `anzahlen.push(Number(prompt(...)))`.'
- kosten: 3
  text: Beim Drucken mit `continue` die Waren mit Anzahl 0 überspringen.
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  - '0'
  - Ole
  - '2'
  - '0'
  - '3'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ole

    2 x Heringsbrötchen: 5.00 Euro

    3 x Fischsuppe: 13.50 Euro

    ==============================

    Summe: 18.50 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Kunden heute: 2

    Namen: Pia, Ole

    Tagesumsatz: 29.50 Euro

    '
tests_versteckt:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Kunden heute: 0

    Tagesumsatz: 0.00 Euro

    '
- input:
  - Ida
  - '4'
  - '0'
  - '1'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ida

    4 x Heringsbrötchen: 10.00 Euro

    1 x Fischsuppe: 4.50 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 14.50 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Kunden heute: 1

    Namen: Ida

    Tagesumsatz: 14.50 Euro

    '
- input:
  - Bo
  - '0'
  - '0'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Bo

    ==============================

    Summe: 0.00 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Kunden heute: 1

    Namen: Bo

    Tagesumsatz: 0.00 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 10.** Pit nimmt Fischsuppe (`4.5`) ins Sortiment, und die Kasse soll mit beliebig vielen Waren klarkommen. Leg Waren und Preise in zwei Arrays, frag je Kunde jede Ware ab (`Heringsbrötchen? ` und so weiter, gesammelt mit push) und druck nur Zeilen für Waren, die gekauft wurden. Die Gratis-Limonade gilt weiter für 3 oder mehr Heringsbrötchen ohne Limonade. Am Ende stehen die Zahl der Kunden, ihre Namen (nur wenn es Kunden gab) und der Umsatz. Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `2`, `0`, `3` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ole
2 x Heringsbrötchen: 5.00 Euro
3 x Fischsuppe: 13.50 Euro
==============================
Summe: 18.50 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Kunden heute: 2
Namen: Pia, Ole
Tagesumsatz: 29.50 Euro
```
