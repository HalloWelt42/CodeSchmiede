---
schema_version: 1
id: j039-fischwagen-summe
revision: 1
titel: 'Fischwagen: die Summe'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- projekt
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Je Ware zwei Konstanten: Preis und Anzahl. Die Zeile auf dem Bon rechnet Anzahl mal Preis.'
- kosten: 2
  text: '`summe += broetchen * preisBroetchen;` sammelt den Betrag ein.'
tests_sichtbar:
- input: []
  expected: '*** Fischwagen Zum frostigen Hering ***

    Kassenbon für Pia

    3 x Heringsbrötchen: 7.5

    2 x Limonade: 3.5

    Summe: 11

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 3.** Jetzt rechnet die Kasse. Pia kauft 3 Heringsbrötchen zu je `2.5` und 2 Limonaden zu je `1.75`. Nimm deinen Code aus Kapitel 2 und ergänze Preise, Anzahlen und die Rechnung:

```
*** Fischwagen Zum frostigen Hering ***
Kassenbon für Pia
3 x Heringsbrötchen: 7.5
2 x Limonade: 3.5
Summe: 11
```
