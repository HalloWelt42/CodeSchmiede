---
schema_version: 1
id: j219-fischwagen-kueche
revision: 1
titel: 'Fischwagen: die Küche'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 12
tags:
- kurs
- projekt
- async
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine statische Methode `kochen(ware, ms)` liefert ein Promise, das nach ms meldet und erfüllt.
- kosten: 1
  text: '`async kueche(nummer, anzahlen)` sammelt die Versprechen und wartet mit `await Promise.all(...)`.'
- kosten: 3
  text: Das Hauptprogramm wird eine async-Funktion, die `await kasse.bedienen(kunde)` aufruft.
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

    fertig: Limonade

    fertig: Heringsbrötchen

    Bestellung Nr. 1 abholbereit

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 2 für Ole

    6 x Heringsbrötchen: 15.00 Euro

    4 x Fischsuppe: 18.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt 10 %: -3.30 Euro

    Summe: 29.70 Euro

    Stempel: [*][*][ ][ ][ ]

    fertig: Heringsbrötchen

    fertig: Fischsuppe

    Bestellung Nr. 2 abholbereit

    Kunde? Willkommen zurück, Pia!

    Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Gutschein unbekannt

    Kassenbon Nr. 3 für Pia

    1 x Heringsbrötchen: 2.50 Euro

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 4.25 Euro

    Stempel: [ ][ ][ ][ ][ ]

    fertig: Limonade

    fertig: Heringsbrötchen

    Bestellung Nr. 3 abholbereit

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
  - ''
  - Ida
  - '0'
  - '0'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kassenbuch von gestern? Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Ida

    ==============================

    Summe: 0.00 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Bestellung Nr. 1 abholbereit

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Ida: 1 Besuch

    Nicht verkauft: Heringsbrötchen, Limonade, Fischsuppe

    Rangliste: Ida 0.00

    Tagesumsatz: 0.00 Euro

    Bons heute: 1

    Kassenbuch: {"umsatz":0,"bons":1,"kunden":["Ida"]}

    '
- input:
  - kaputt
  - Bo
  - '8'
  - '1'
  - '1'
  - HERING2
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kassenbuch von gestern? Kassenbuch unlesbar

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Bo

    8 x Heringsbrötchen: 20.00 Euro

    1 x Limonade: 1.75 Euro

    1 x Fischsuppe: 4.50 Euro

    ==============================

    Rabatt 10 %: -2.63 Euro

    Gutschein: -2.00 Euro

    Summe: 21.63 Euro

    Stempel: [*][*][ ][ ][ ]

    fertig: Limonade

    fertig: Heringsbrötchen

    fertig: Fischsuppe

    Bestellung Nr. 1 abholbereit

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

**Kapitelprojekt Fischwagen, Stück 21, das letzte.** Die Kasse bekommt eine Küche. Nach jedem Bon kocht sie alle bestellten Waren zugleich (Limonade 5, Heringsbrötchen 20, Fischsuppe 40 Millisekunden), meldet jede mit `fertig: ...`, sobald sie fertig ist, und danach `Bestellung Nr. n abholbereit`. Erst dann kommt der nächste Kunde dran: `bedienen` wird async und das Hauptprogramm wartet mit await. Bei den Eingaben `{"umsatz":49.05,"bons":3,"kunden":["Pia","Ole"]}`, `Pia`, `3`, `2`, `0`, `FISCH5`, `Ole`, `6`, `0`, `4`, ``, `Pia`, `1`, `1`, `0`, `LACHS9` und einem leeren Namen:

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
fertig: Limonade
fertig: Heringsbrötchen
Bestellung Nr. 1 abholbereit
Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 2 für Ole
6 x Heringsbrötchen: 15.00 Euro
4 x Fischsuppe: 18.00 Euro
1 x Limonade: gratis
==============================
Rabatt 10 %: -3.30 Euro
Summe: 29.70 Euro
Stempel: [*][*][ ][ ][ ]
fertig: Heringsbrötchen
fertig: Fischsuppe
Bestellung Nr. 2 abholbereit
Kunde? Willkommen zurück, Pia!
Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Gutschein unbekannt
Kassenbon Nr. 3 für Pia
1 x Heringsbrötchen: 2.50 Euro
1 x Limonade: 1.75 Euro
==============================
Summe: 4.25 Euro
Stempel: [ ][ ][ ][ ][ ]
fertig: Limonade
fertig: Heringsbrötchen
Bestellung Nr. 3 abholbereit
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

Glückwunsch: Aus zwei Zeilen Kopf ist eine ganze Kasse geworden.
