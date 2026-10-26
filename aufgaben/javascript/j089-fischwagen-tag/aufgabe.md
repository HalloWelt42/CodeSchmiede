---
schema_version: 1
id: j089-fischwagen-tag
revision: 1
titel: 'Fischwagen: ein ganzer Tag'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- projekt
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der Bon aus Kapitel 7 wandert in eine `while (true)`-Schleife; die Kopfzeile bleibt davor.
- kosten: 2
  text: 'Am Ende jedes Durchgangs: `kunden++;` und `umsatz += summe;`. Die Summe beginnt je Kunde wieder bei 0.'
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  - Ole
  - '8'
  - '0'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    Treuestempel: ja

    Kunde? Brötchen? Limonaden? Kassenbon für Ole

    8 x Heringsbrötchen: 20.00 Euro

    0 x Limonade: 0.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt: -2.00 Euro

    Summe: 18.00 Euro

    Treuestempel: ja

    Kunde? Kunden heute: 2

    Tagesumsatz: 29.00 Euro

    '
tests_versteckt:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Kunden heute: 0

    Tagesumsatz: 0.00 Euro

    '
- input:
  - Ida
  - '1'
  - '1'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Ida

    1 x Heringsbrötchen: 2.50 Euro

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 4.25 Euro

    Treuestempel: nein

    Kunde? Kunden heute: 1

    Tagesumsatz: 4.25 Euro

    '
- input:
  - Bo
  - '6'
  - '4'
  - Kim
  - '3'
  - '0'
  - Lu
  - '0'
  - '2'
  - ''
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Bo

    6 x Heringsbrötchen: 15.00 Euro

    4 x Limonade: 7.00 Euro

    ==============================

    Rabatt: -2.20 Euro

    Summe: 19.80 Euro

    Treuestempel: ja

    Kunde? Brötchen? Limonaden? Kassenbon für Kim

    3 x Heringsbrötchen: 7.50 Euro

    0 x Limonade: 0.00 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 7.50 Euro

    Treuestempel: nein

    Kunde? Brötchen? Limonaden? Kassenbon für Lu

    0 x Heringsbrötchen: 0.00 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 3.50 Euro

    Treuestempel: nein

    Kunde? Kunden heute: 3

    Tagesumsatz: 30.80 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 8.** Die Kasse bedient jetzt einen ganzen Tag. Die Kopfzeile kommt einmal am Anfang, dann fragt die Kasse nach Kunden, bis der Name leer bleibt oder nichts mehr kommt. Für jeden Kunden fragt sie Brötchen und Limonaden und druckt den Bon wie in Kapitel 7. Am Ende stehen die Zahl der Kunden und der Tagesumsatz. Bei den Eingaben `Pia`, `3`, `2`, `Ole`, `8`, `0` und einem leeren Namen:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Brötchen? Limonaden? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Treuestempel: ja
Kunde? Brötchen? Limonaden? Kassenbon für Ole
8 x Heringsbrötchen: 20.00 Euro
0 x Limonade: 0.00 Euro
1 x Limonade: gratis
==============================
Rabatt: -2.00 Euro
Summe: 18.00 Euro
Treuestempel: ja
Kunde? Kunden heute: 2
Tagesumsatz: 29.00 Euro
```
