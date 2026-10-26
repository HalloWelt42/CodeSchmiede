---
schema_version: 1
id: j169-fischwagen-bonnummern
revision: 1
titel: 'Fischwagen: Bonnummern'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- projekt
- sichtbarkeit
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Der Geber aus der Einführung passt fast genau: `const bonNummer = nummernGeber(1);`'
- kosten: 2
  text: 'In bonDrucken: `` `Kassenbon Nr. ${bonNummer()} für ${kunde}` ``.'
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  - '0'
  - Ole
  - '6'
  - '0'
  - '4'
  - Pia
  - '1'
  - '1'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 1 für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 2 für Ole

    6 x Heringsbrötchen: 15.00 Euro

    4 x Fischsuppe: 18.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt 10 %: -3.30 Euro

    Summe: 29.70 Euro

    Stempel: [*][*][ ][ ][ ]

    Kunde? Willkommen zurück, Pia!

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 3 für Pia

    1 x Heringsbrötchen: 2.50 Euro

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 4.25 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 3

    Verschiedene Kunden: 2

    Pia: 2 Besuche

    Ole: 1 Besuch

    Heringsbrötchen: 10 verkauft

    Limonade: 3 verkauft

    Fischsuppe: 4 verkauft

    Rangliste: Ole 29.70, Pia 15.25

    Tagesumsatz: 44.95 Euro

    '
tests_versteckt:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Besuche heute: 0

    Verschiedene Kunden: 0

    Nicht verkauft: Heringsbrötchen, Limonade, Fischsuppe

    Tagesumsatz: 0.00 Euro

    '
- input:
  - Ida
  - '4'
  - '0'
  - '1'
  - Bo
  - '10'
  - '2'
  - '3'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 1 für Ida

    4 x Heringsbrötchen: 10.00 Euro

    1 x Fischsuppe: 4.50 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 14.50 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 2 für Bo

    10 x Heringsbrötchen: 25.00 Euro

    2 x Limonade: 3.50 Euro

    3 x Fischsuppe: 13.50 Euro

    ==============================

    Rabatt 15 %: -6.30 Euro

    Summe: 35.70 Euro

    Stempel: [*][*][*][ ][ ]

    Kunde? Besuche heute: 2

    Verschiedene Kunden: 2

    Ida: 1 Besuch

    Bo: 1 Besuch

    Heringsbrötchen: 14 verkauft

    Limonade: 2 verkauft

    Fischsuppe: 4 verkauft

    Rangliste: Bo 35.70, Ida 14.50

    Tagesumsatz: 50.20 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 16.** Jeder Bon bekommt eine fortlaufende Nummer. Bau dafür mit einer Closure einen `nummernGeber(start)` und lass `bonDrucken` ihn aufrufen, ohne dass irgendwer außer dem Geber die Nummer ändern kann. Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `6`, `0`, `4`, `Pia`, `1`, `1`, `0` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 1 für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 2 für Ole
6 x Heringsbrötchen: 15.00 Euro
4 x Fischsuppe: 18.00 Euro
1 x Limonade: gratis
==============================
Rabatt 10 %: -3.30 Euro
Summe: 29.70 Euro
Stempel: [*][*][ ][ ][ ]
Kunde? Willkommen zurück, Pia!
Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 3 für Pia
1 x Heringsbrötchen: 2.50 Euro
1 x Limonade: 1.75 Euro
==============================
Summe: 4.25 Euro
Stempel: [ ][ ][ ][ ][ ]
Kunde? Besuche heute: 3
Verschiedene Kunden: 2
Pia: 2 Besuche
Ole: 1 Besuch
Heringsbrötchen: 10 verkauft
Limonade: 3 verkauft
Fischsuppe: 4 verkauft
Rangliste: Ole 29.70, Pia 15.25
Tagesumsatz: 44.95 Euro
```
