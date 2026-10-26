---
schema_version: 1
id: j139-fischwagen-maps
revision: 1
titel: 'Fischwagen: alles in Maps'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- map
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`karte.set("Heringsbrötchen", 2.5)` und so weiter; `for (const ware of karte.keys())` fragt alle Waren ab.'
- kosten: 1
  text: 'Besuche hochzählen: `besuche.set(kunde, besuche.get(kunde) + 1)`.'
- kosten: 3
  text: Am Ende die Waren mit 0 in einem Array sammeln und nur ausgeben, wenn es welche gibt.
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  - '0'
  - Ole
  - '2'
  - '0'
  - '0'
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

    2 x Heringsbrötchen: 5.00 Euro

    ==============================

    Summe: 5.00 Euro

    Stempel: [ ][ ][ ][ ][ ]

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

    Heringsbrötchen: 6 verkauft

    Limonade: 3 verkauft

    Nicht verkauft: Fischsuppe

    Tagesumsatz: 20.25 Euro

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
  - '0'
  - '1'
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

    1 x Limonade: 1.75 Euro

    2 x Fischsuppe: 9.00 Euro

    ==============================

    Summe: 10.75 Euro

    Stempel: [*][ ][ ][ ][ ]

    Kunde? Willkommen zurück, Ida!

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ida

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 1.75 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 3

    Verschiedene Kunden: 2

    Ida: 2 Besuche

    Bo: 1 Besuch

    Heringsbrötchen: 4 verkauft

    Limonade: 2 verkauft

    Fischsuppe: 3 verkauft

    Tagesumsatz: 27.00 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 13.** Die Kasse stellt auf Maps um: die Karte (Ware zu Preis), die Besuche je Kunde, die verkauften Mengen und je Kunde die Anzahlen. Neu am Tagesende: die Zahl der verschiedenen Kunden, nur Waren mit Verkäufen in der Liste und darunter, was gar nicht verkauft wurde (die Zeile fehlt, wenn alles lief). Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `2`, `0`, `0`, `Pia`, `1`, `1`, `0` und einem leeren Namen:

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
==============================
Summe: 5.00 Euro
Stempel: [ ][ ][ ][ ][ ]
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
Heringsbrötchen: 6 verkauft
Limonade: 3 verkauft
Nicht verkauft: Fischsuppe
Tagesumsatz: 20.25 Euro
```
