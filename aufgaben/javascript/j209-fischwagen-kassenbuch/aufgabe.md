---
schema_version: 1
id: j209-fischwagen-kassenbuch
revision: 1
titel: 'Fischwagen: das Kassenbuch'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- json
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Morgens: prompt, dann JSON.parse in einem try.'
- kosten: 2
  text: 'Abends: ein Objekt `{ umsatz, bons, kunden }` bauen; `Number(umsatz.toFixed(2))` rundet und bleibt eine Zahl.'
tests_sichtbar:
- input:
  - '{"umsatz":49.05,"bons":3,"kunden":["Pia","Ole"]}'
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

    Kassenbuch von gestern? Gestern: 49.05 Euro, 3 Bons

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

    Kassenbuch: {"umsatz":39.95,"bons":3,"kunden":["Pia","Ole"]}

    '
tests_versteckt:
- input:
  - kaputt
  expected: '*** ZUM FROSTIGEN HERING ***

    Kassenbuch von gestern? Kassenbuch unlesbar

    Kunde? Besuche heute: 0

    Verschiedene Kunden: 0

    Nicht verkauft: Heringsbrötchen, Limonade, Fischsuppe

    Tagesumsatz: 0.00 Euro

    Bons heute: 0

    Kassenbuch: {"umsatz":0,"bons":0,"kunden":[]}

    '
- input:
  - ''
  - Ida
  - '1'
  - '0'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kassenbuch von gestern? Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Ida

    1 x Heringsbrötchen: 2.50 Euro

    ==============================

    Summe: 2.50 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Ida: 1 Besuch

    Heringsbrötchen: 1 verkauft

    Nicht verkauft: Limonade, Fischsuppe

    Rangliste: Ida 2.50

    Tagesumsatz: 2.50 Euro

    Bons heute: 1

    Kassenbuch: {"umsatz":2.5,"bons":1,"kunden":["Ida"]}

    '
- input:
  - '{"umsatz":0,"bons":0,"kunden":[]}'
  - Bo
  - '8'
  - '1'
  - '1'
  - HERING2
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kassenbuch von gestern? Gestern: 0.00 Euro, 0 Bons

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Bo

    8 x Heringsbrötchen: 20.00 Euro

    1 x Limonade: 1.75 Euro

    1 x Fischsuppe: 4.50 Euro

    ==============================

    Rabatt 10 %: -2.63 Euro

    Gutschein: -2.00 Euro

    Summe: 21.63 Euro

    Stempel: [*][*][ ][ ][ ]

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Bo: 1 Besuch

    Heringsbrötchen: 8 verkauft

    Limonade: 1 verkauft

    Fischsuppe: 1 verkauft

    Rangliste: Bo 21.63

    Tagesumsatz: 21.63 Euro

    Bons heute: 1

    Kassenbuch: {"umsatz":21.63,"bons":1,"kunden":["Bo"]}

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 20.** Die Kasse führt ein Kassenbuch. Am Morgen fragt sie nach dem Kassenbuch von gestern (ein JSON-Text) und meldet Umsatz und Bons, bei unlesbarem Text `Kassenbuch unlesbar`, bei leerer Antwort nichts. Am Abend schreibt sie das Kassenbuch von heute als letzte Zeile: Umsatz (auf zwei Stellen gerundet, als Zahl), Bons und die Namen der Kunden. Bei den Eingaben `{"umsatz":49.05,"bons":3,"kunden":["Pia","Ole"]}`, `Pia`, `3`, `2`, `0`, `FISCH5`, `Ole`, `6`, `0`, `4`, ``, `Pia`, `1`, `1`, `0`, `LACHS9` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kassenbuch von gestern? Gestern: 49.05 Euro, 3 Bons
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
Kassenbuch: {"umsatz":39.95,"bons":3,"kunden":["Pia","Ole"]}
```
