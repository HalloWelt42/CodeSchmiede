---
schema_version: 1
id: j189-fischwagen-gutscheine
revision: 1
titel: 'Fischwagen: Gutscheine'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags:
- kurs
- projekt
- destrukturierung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`gutscheine.get(code) ?? 0` ist 0, wenn es den Code nicht gibt.'
- kosten: 2
  text: 'Im Bon nach dem Rabatt: `Math.min(abzug, summe)` abziehen, damit nichts unter 0 fällt.'
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

    '
tests_versteckt:
- input:
  - Ida
  - '1'
  - '0'
  - '0'
  - FISCH5
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Heringsbrötchen? Limonade? Fischsuppe? Gutschein? Kassenbon Nr. 1 für Ida

    1 x Heringsbrötchen: 2.50 Euro

    ==============================

    Gutschein: -2.50 Euro

    Summe: 0.00 Euro

    Stempel: [ ][ ][ ][ ][ ]

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Ida: 1 Besuch

    Heringsbrötchen: 1 verkauft

    Nicht verkauft: Limonade, Fischsuppe

    Rangliste: Ida 0.00

    Tagesumsatz: 0.00 Euro

    '
- input:
  - Bo
  - '8'
  - '1'
  - '1'
  - HERING2
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

    Kunde? Besuche heute: 1

    Verschiedene Kunden: 1

    Bo: 1 Besuch

    Heringsbrötchen: 8 verkauft

    Limonade: 1 verkauft

    Fischsuppe: 1 verkauft

    Rangliste: Bo 21.63

    Tagesumsatz: 21.63 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 18.** Nach den Waren fragt die Kasse jetzt `Gutschein? `. Gültige Codes stehen in einer Map (`FISCH5` ist 5 Euro wert, `HERING2` 2 Euro); unbekannte Codes melden `Gutschein unbekannt`, eine leere Antwort heißt kein Gutschein. Der Gutschein wird nach dem Rabatt abgezogen, höchstens bis 0. `bonDrucken` bekommt jetzt ein Objekt und packt es aus: `bonDrucken({ kunde, anzahlen, abzug })`; und die Rangliste packt die Paare der Map mit `[name, betrag]` aus. Bei den Eingaben `Pia`, `3`, `2`, `0`, `FISCH5`, `Ole`, `6`, `0`, `4`, ``, `Pia`, `1`, `1`, `0`, `LACHS9` und einem leeren Namen:

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
```
