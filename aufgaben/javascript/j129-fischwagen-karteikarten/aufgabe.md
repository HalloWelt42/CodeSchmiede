---
schema_version: 1
id: j129-fischwagen-karteikarten
revision: 1
titel: 'Fischwagen: Karte und Zählwerk'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- objekt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`{ name: "Heringsbrötchen", preis: 2.5 }` je Ware; `karte[i].preis` statt `preise[i]`.'
- kosten: 1
  text: '`kunde in besuche` erkennt Stammkunden; neue bekommen 1, bekannte ++.'
- kosten: 3
  text: '`verkauft` mit 0 je Warenname anlegen, beim Abfragen hochzählen, am Ende mit for ... in ausgeben.'
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
  - Pia
  - '1'
  - '1'
  - '1'
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

    Kunde? Willkommen zurück, Pia!

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia

    1 x Heringsbrötchen: 2.50 Euro

    1 x Limonade: 1.75 Euro

    1 x Fischsuppe: 4.50 Euro

    ==============================

    Summe: 8.75 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 3

    Pia: 2 Besuche

    Ole: 1 Besuch

    Heringsbrötchen: 6 verkauft

    Limonade: 3 verkauft

    Fischsuppe: 4 verkauft

    Tagesumsatz: 38.25 Euro

    '
tests_versteckt:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Besuche heute: 0

    Heringsbrötchen: 0 verkauft

    Limonade: 0 verkauft

    Fischsuppe: 0 verkauft

    Tagesumsatz: 0.00 Euro

    '
- input:
  - Ida
  - '4'
  - '0'
  - '1'
  - Bo
  - '0'
  - '0'
  - '2'
  - Ida
  - '0'
  - '1'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ida

    4 x Heringsbrötchen: 10.00 Euro

    1 x Fischsuppe: 4.50 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 14.50 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Bo

    2 x Fischsuppe: 9.00 Euro

    ==============================

    Summe: 9.00 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Willkommen zurück, Ida!

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ida

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 1.75 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 3

    Ida: 2 Besuche

    Bo: 1 Besuch

    Heringsbrötchen: 4 verkauft

    Limonade: 1 verkauft

    Fischsuppe: 3 verkauft

    Tagesumsatz: 25.25 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 12.** Die Speisekarte wird ein Array aus Objekten mit `name` und `preis`, und zwei Objekte zählen mit: `besuche` je Kunde und `verkauft` je Ware. Am Ende stehen alle Besuche zusammen, je Kunde seine Besuche (`1 Besuch`, sonst `Besuche`) und je Ware die verkaufte Menge. Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `2`, `0`, `3`, `Pia`, `1`, `1`, `1` und einem leeren Namen:

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
Kunde? Willkommen zurück, Pia!
Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Pia
1 x Heringsbrötchen: 2.50 Euro
1 x Limonade: 1.75 Euro
1 x Fischsuppe: 4.50 Euro
==============================
Summe: 8.75 Euro
Stempel: [ ][ ][ ][ ][ ]
Kunde? Besuche heute: 3
Pia: 2 Besuche
Ole: 1 Besuch
Heringsbrötchen: 6 verkauft
Limonade: 3 verkauft
Fischsuppe: 4 verkauft
Tagesumsatz: 38.25 Euro
```
