---
schema_version: 1
id: j079-fischwagen-rabatt
revision: 1
titel: 'Fischwagen: Rabatt und Gratis-Limonade'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- projekt
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Nimm deinen Code aus Kapitel 6. Die Gratis-Zeile kommt vor den Strich, der Rabatt danach.
- kosten: 2
  text: 'Im if für den Rabatt: ausrechnen, ausgeben, mit `summe -= rabatt;` abziehen.'
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

    Treuestempel: ja

    '
- input:
  - Ole
  - '8'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Ole

    8 x Heringsbrötchen: 20.00 Euro

    0 x Limonade: 0.00 Euro

    1 x Limonade: gratis

    ==============================

    Rabatt: -2.00 Euro

    Summe: 18.00 Euro

    Treuestempel: ja

    '
tests_versteckt:
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

    '
- input:
  - Bo
  - '6'
  - '4'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Bo

    6 x Heringsbrötchen: 15.00 Euro

    4 x Limonade: 7.00 Euro

    ==============================

    Rabatt: -2.20 Euro

    Summe: 19.80 Euro

    Treuestempel: ja

    '
- input:
  - Kim
  - '3'
  - '0'
  expected: '*** ZUM FROSTIGEN HERING ***

    Kunde? Brötchen? Limonaden? Kassenbon für Kim

    3 x Heringsbrötchen: 7.50 Euro

    0 x Limonade: 0.00 Euro

    1 x Limonade: gratis

    ==============================

    Summe: 7.50 Euro

    Treuestempel: nein

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 7.** Jetzt wird entschieden. Wer 3 oder mehr Brötchen und keine Limonade nimmt, bekommt eine Zeile `1 x Limonade: gratis`. Ab 20 Euro gibt es 10 Prozent Rabatt, als eigene Zeile vor der Summe; die Summe ist dann schon ermäßigt. Der Treuestempel ab 10 Euro (nach Rabatt) heißt jetzt `ja` oder `nein`. Bei den Eingaben `Pia`, `3` und `2`:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Brötchen? Limonaden? Kassenbon für Pia
3 x Heringsbrötchen: 7.50 Euro
2 x Limonade: 3.50 Euro
==============================
Summe: 11.00 Euro
Treuestempel: ja
```

Und bei `Ole`, `8` und `0`:

```
*** ZUM FROSTIGEN HERING ***
Kunde? Brötchen? Limonaden? Kassenbon für Ole
8 x Heringsbrötchen: 20.00 Euro
0 x Limonade: 0.00 Euro
1 x Limonade: gratis
==============================
Rabatt: -2.00 Euro
Summe: 18.00 Euro
Treuestempel: ja
```
