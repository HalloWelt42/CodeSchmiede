---
schema_version: 1
id: j149-fischwagen-funktionen
revision: 1
titel: 'Fischwagen: aufgeräumt in Funktionen'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 12
tags:
- kurs
- projekt
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
  text: Fang mit `euro` an und ersetze alle `.toFixed(2)} Euro` durch Aufrufe.
- kosten: 1
  text: '`rabattSatz` liefert 15, 10 oder 0; der Rabatt ist `summe * satz / 100`.'
- kosten: 3
  text: bonDrucken bekommt Kunde und Anzahlen und liefert mit return die Summe nach Rabatt.
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

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ole

    6 x Heringsbrötchen: 15.00 Euro

    4 x Fischsuppe: 18.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt 10 %: -3.30 Euro

    Summe: 29.70 Euro

    Stempel: [*][*][ ][ ][ ]

    Kunde? Willkommen zurück, Pia!

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia

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

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ida

    4 x Heringsbrötchen: 10.00 Euro

    1 x Fischsuppe: 4.50 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 14.50 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Bo

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

    Tagesumsatz: 50.20 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 14.** Die Kasse ist lang geworden. Räum sie in Funktionen auf: `euro(betrag)`, `rabattSatz(summe)`, `stempelkarte(summe)`, `anzahlenAbfragen()`, `bonDrucken(kunde, anzahlen)` (liefert die Summe) und `tagesabschluss(...)`. Neu dabei: Ab 40 Euro gibt es 15 Prozent Rabatt, ab 20 Euro weiter 10, und die Rabattzeile nennt den Satz. Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `6`, `0`, `4`, `Pia`, `1`, `1`, `0` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Stempel: [*][ ][ ][ ][ ]
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ole
6 x Heringsbrötchen: 15.00 Euro
4 x Fischsuppe: 18.00 Euro
1 x Limonade: gratis
==============================
Rabatt 10 %: -3.30 Euro
Summe: 29.70 Euro
Stempel: [*][*][ ][ ][ ]
Kunde? Willkommen zurück, Pia!
Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia
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
Tagesumsatz: 44.95 Euro
```
