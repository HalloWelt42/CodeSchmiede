---
schema_version: 1
id: j159-fischwagen-rangliste
revision: 1
titel: 'Fischwagen: die Rangliste'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- pfeilfunktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Eine Map `jeKunde`: `jeKunde.set(kunde, (jeKunde.get(kunde) || 0) + summe)`.'
- kosten: 2
  text: 'Am Ende: Objekte `{ name, betrag }` in ein Array, dann `sort((a, b) => b.betrag - a.betrag)`.'
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
  - Ida
  - '1'
  - '0'
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

    10 x Heringsbrötchen: 25.00 Euro

    2 x Limonade: 3.50 Euro

    3 x Fischsuppe: 13.50 Euro

    ==============================

    Rabatt 15 %: -6.30 Euro

    Summe: 35.70 Euro

    Stempel: [*][*][*][ ][ ]

    Kunde? Willkommen zurück, Ida!

    Heringsbrötchen? Limonade? Fischsuppe? Kassenbon für Ida

    1 x Heringsbrötchen: 2.50 Euro

    ==============================

    Summe: 2.50 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 3

    Verschiedene Kunden: 2

    Ida: 2 Besuche

    Bo: 1 Besuch

    Heringsbrötchen: 15 verkauft

    Limonade: 2 verkauft

    Fischsuppe: 4 verkauft

    Rangliste: Bo 35.70, Ida 17.00

    Tagesumsatz: 52.70 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 15.** Pit möchte wissen, wer heute am meisten ausgegeben hat. Merk dir je Kunde die Summe aller Bons (in einer Map), bau daraus am Ende ein Array aus Objekten, sortiere es absteigend mit einer Vergleichsfunktion und gib es mit map und join als Rangliste vor dem Tagesumsatz aus (nur wenn es Kunden gab). Bei den Eingaben `Pia`, `3`, `2`, `0`, `Ole`, `6`, `0`, `4`, `Pia`, `1`, `1`, `0` und einem leeren Namen:

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
Rangliste: Ole 29.70, Pia 15.25
Tagesumsatz: 44.95 Euro
```
