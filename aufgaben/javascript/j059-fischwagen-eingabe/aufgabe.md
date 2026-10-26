---
schema_version: 1
id: j059-fischwagen-eingabe
revision: 1
titel: 'Fischwagen: die Kasse fragt'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- projekt
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Nimm deinen Code aus Kapitel 4: Kunde und Anzahlen kommen jetzt aus prompt, die Anzahlen mit Number.'
- kosten: 2
  text: Jeder Betrag bekommt `.toFixed(2)`, um Rechnungen herum mit Klammern.
tests_sichtbar:
- input:
  - Pia
  - '3'
  - '2'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Pia

    3 x Heringsbrötchen: 7.50 Euro

    2 x Limonade: 3.50 Euro

    ==============================

    Summe: 11.00 Euro

    '
tests_versteckt:
- input:
  - Ole
  - '1'
  - '5'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Ole

    1 x Heringsbrötchen: 2.50 Euro

    5 x Limonade: 8.75 Euro

    ==============================

    Summe: 11.25 Euro

    '
- input:
  - Ida
  - '0'
  - '1'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Ida

    0 x Heringsbrötchen: 0.00 Euro

    1 x Limonade: 1.75 Euro

    ==============================

    Summe: 1.75 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 5.** Jetzt fragt die Kasse selbst: zuerst den Namen (`Kunde? `), dann die Zahl der Brötchen (`Brötchen? `) und der Limonaden (`Limonaden? `). Alle Beträge erscheinen mit zwei Stellen. Bei den Eingaben `Pia`, `3` und `2`:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Brötchen? Limonaden? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
```

Die Kopfzeile steht vor den Fragen, darum hängen die Fragen an ihr dran.
