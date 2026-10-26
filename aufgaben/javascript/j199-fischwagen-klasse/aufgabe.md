---
schema_version: 1
id: j199-fischwagen-klasse
revision: 1
titel: 'Fischwagen: die Kasse als Klasse'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 12
tags:
- kurs
- projekt
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Alles, was bisher außen in Namen stand, wird `this.etwas` im constructor.
- kosten: 1
  text: Aus `function euro(...)` wird `static euro(...)`, aufgerufen als `Kasse.euro(...)`.
- kosten: 3
  text: '`get bons()` liefert `this.naechsteNummer - 1`.'
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  - '0'
  - FISCH5
  - Ole
  - '6'
  - '0'
  - '4'
  - ''
  - Pia
  - '1'
  - '1'
  - '0'
  - LACHS9
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Gutschein: -5.00 Euro

    Summe: 6.00 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 2 für Ole

    6 x Heringsbrötchen: 15.00 Euro

    4 x Fischsuppe: 18.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt 10 %: -3.30 Euro

    Summe: 29.70 Euro

    Stempel: [*][*][ ][ ][ ]

    Kunde? Willkommen zurück, Pia!

    Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Gutschein unbekannt

    Kassenbon Nr. 3 für Pia

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

    Rangliste: Ole 29.70, Pia 10.25

    Tagesumsatz: 39.95 Euro

    Bons heute: 3

    '
tests_versteckt:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Besuche heute: 0

    Verschiedene Kunden: 0

    Nicht verkauft: Heringsbrötchen, Limonade, Fischsuppe

    Tagesumsatz: 0.00 Euro

    Bons heute: 0

    '
- input:
  - Bo
  - '8'
  - '1'
  - '1'
  - HERING2
  - Bo
  - x
  - '1'
  - '0'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Bo

    8 x Heringsbrötchen: 20.00 Euro

    1 x Limonade: 1.75 Euro

    1 x Fischsuppe: 4.50 Euro

    ==============================

    Rabatt 10 %: -2.63 Euro

    Gutschein: -2.00 Euro

    Summe: 21.63 Euro

    Stempel: [*][*][ ][ ][ ]

    Kunde? Willkommen zurück, Bo!

    Heringsbrötchen? Ungültig: "x" ist keine Zahl

    Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 2 für Bo

    1 x Heringsbrötchen: 2.50 Euro

    ==============================

    Summe: 2.50 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 2

    Verschiedene Kunden: 1

    Bo: 2 Besuche

    Heringsbrötchen: 9 verkauft

    Limonade: 1 verkauft

    Fischsuppe: 1 verkauft

    Rangliste: Bo 24.13

    Tagesumsatz: 24.13 Euro

    Bons heute: 2

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 19.** Die ganze Kasse wird eine Klasse `Kasse`: Karte, Gutscheine, Besuche, Verkäufe, Umsätze und die nächste Bonnummer sind Eigenschaften, die Hilfsfunktionen (`euro`, `rabattSatz`, `stempelkarte`, `liesAnzahl`) werden statische Methoden, dazu die Methoden `bedienen(kunde)` und `tagesabschluss()` und ein `get bons()`, dessen Wert als neue letzte Zeile erscheint. Das Hauptprogramm ist nur noch ein paar Zeilen lang. Bei den Eingaben `Pia`, `3`, `2`, `0`, `FISCH5`, `Ole`, `6`, `0`, `4`, ``, `Pia`, `1`, `1`, `0`, `LACHS9` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Gutschein: -5.00 Euro
Summe: 6.00 Euro
Stempel: [ ][ ][ ][ ][ ]
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 2 für Ole
6 x Heringsbrötchen: 15.00 Euro
4 x Fischsuppe: 18.00 Euro
1 x Limonade: gratis
==============================
Rabatt 10 %: -3.30 Euro
Summe: 29.70 Euro
Stempel: [*][*][ ][ ][ ]
Kunde? Willkommen zurück, Pia!
Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Gutschein unbekannt
Kassenbon Nr. 3 für Pia
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
Rangliste: Ole 29.70, Pia 10.25
Tagesumsatz: 39.95 Euro
Bons heute: 3
```
