---
schema_version: 1
id: j119-fischwagen-stammkunden
revision: 1
titel: 'Fischwagen: Stammkunden'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- arraymethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Vor dem push mit `namen.includes(kunde)` nachsehen, ob der Name schon da ist.
- kosten: 1
  text: Ein Array `verkauft` mit einer 0 je Ware zählt mit, `verkauft[i] += anzahlen[i];`.
- kosten: 3
  text: 'Alphabetisch ohne das Original zu ändern: `namen.slice().sort()`.'
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

    Kunden: Ole, Pia

    Verkauft: 6 x Heringsbrötchen, 3 x Limonade, 4 x Fischsuppe

    Tagesumsatz: 38.25 Euro

    '
tests_versteckt:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Besuche heute: 0

    Verkauft: 0 x Heringsbrötchen, 0 x Limonade, 0 x Fischsuppe

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

    Kunden: Bo, Ida

    Verkauft: 4 x Heringsbrötchen, 1 x Limonade, 3 x Fischsuppe

    Tagesumsatz: 25.25 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 11.** Die Kasse erkennt Stammkunden: Kommt ein Name zum zweiten Mal, begrüßt sie ihn mit `Willkommen zurück, Name!`, und in der Namensliste steht jeder nur einmal. Am Ende zählt sie die Besuche, nennt die Kunden alphabetisch und wie viel von jeder Ware verkauft wurde. Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `2`, `0`, `3`, `Pia`, `1`, `1`, `1` und einem leeren Namen:

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
Kunden: Ole, Pia
Verkauft: 6 x Heringsbrötchen, 3 x Limonade, 4 x Fischsuppe
Tagesumsatz: 38.25 Euro
```
