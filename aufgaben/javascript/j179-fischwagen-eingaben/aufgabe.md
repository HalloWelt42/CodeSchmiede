---
schema_version: 1
id: j179-fischwagen-eingaben
revision: 1
titel: 'Fischwagen: robuste Eingaben'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- try
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Prüfungen gehören in liesAnzahl, das Wiederholen in anzahlenAbfragen.
- kosten: 2
  text: 'In anzahlenAbfragen je Ware: `while (true)` mit try (liesAnzahl, break) und catch (melden; bei null 0 setzen und
    break).'
tests_sichtbar:
- input:
  - Pia
  - drei
  - '3'
  - '2'
  - '0'
  - Ole
  - '6'
  - '-1'
  - '0'
  - ''
  - '4'
  - Pia
  - '1'
  - '1'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Ungültig: "drei" ist keine Zahl

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 1 für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Ungültig: -1 ist weniger als nichts

    Limonade? Fischsuppe? Ungültig: "" ist keine Zahl

    Fischsuppe? Kassenbon Nr. 2 für Ole

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
- input:
  - Ida
  - '4'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Ungültig: keine Eingabe

    Kassenbon Nr. 1 für Ida

    4 x Heringsbrötchen: 10.00 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 10.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Ida: 1 Besuch

    Heringsbrötchen: 4 verkauft

    Nicht verkauft: Limonade, Fischsuppe

    Rangliste: Ida 10.00

    Tagesumsatz: 10.00 Euro

    '
- input:
  - Bo
  - '2.5'
  - '2'
  - x
  - '1'
  - '1'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Ungültig: "2.5" ist keine Zahl

    Heringsbrötchen? Limonade? Ungültig: "x" ist keine Zahl

    Limonade? Fischsuppe? Kassenbon Nr. 1 für Bo

    2 x Heringsbrötchen: 5.00 Euro

    1 x Limonade: 1.75 Euro

    1 x Fischsuppe: 4.50 Euro

    ==============================

    Summe: 11.25 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Bo: 1 Besuch

    Heringsbrötchen: 2 verkauft

    Limonade: 1 verkauft

    Fischsuppe: 1 verkauft

    Rangliste: Bo 11.25

    Tagesumsatz: 11.25 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 17.** Bisher hat ein Tippfehler die Kasse durcheinandergebracht. Schreib `liesAnzahl(text)`: bei null wirft sie `keine Eingabe`, bei leerem Text oder einer nicht ganzen Zahl `"text" ist keine Zahl`, bei negativen Zahlen einen RangeError `n ist weniger als nichts`. Die Abfrage meldet `Ungültig: ...` und fragt dieselbe Ware erneut; kommt gar keine Eingabe mehr, zählt die Ware als 0. Bei den Eingaben `Pia`, `drei`, `3`, `2`, `0`, `Ole`, `6`, `-1`, `0`, ``, `4`, `Pia`, `1`, `1`, `0` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Heringsbrötchen? Ungültig: "drei" ist keine Zahl
Heringsbrötchen? Limonade? Fischsuppe? Kassenbon Nr. 1 für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Heringsbrötchen? Limonade? Ungültig: -1 ist weniger als nichts
Limonade? Fischsuppe? Ungültig: "" ist keine Zahl
Fischsuppe? Kassenbon Nr. 2 für Ole
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
