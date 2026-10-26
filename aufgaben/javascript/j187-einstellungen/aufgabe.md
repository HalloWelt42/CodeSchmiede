---
schema_version: 1
id: j187-einstellungen
revision: 1
titel: Einstellungen zusammenführen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- spread
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
  text: '`const [schluessel, wert] = paar.split("=");` packt ein Paar aus.'
- kosten: 2
  text: '`{ ...standard, ...wuensche }`: was später kommt, gewinnt.'
tests_sichtbar:
- input:
  - waehrung=CHF,stempel=10
  expected: 'Wünsche? waehrung: CHF

    rabatt: 10

    stempel: 10

    '
tests_versteckt:
- input:
  - ''
  expected: 'Wünsche? waehrung: Euro

    rabatt: 10

    stempel: 5

    '
- input:
  - farbe=blau
  expected: 'Wünsche? waehrung: Euro

    rabatt: 10

    stempel: 5

    farbe: blau

    '
starter_code: 'const standard = { waehrung: "Euro", rabatt: "10", stempel: "5" };

  '
---

Die Kasse hat Standardeinstellungen. Lies die Wünsche des Tages als Text wie `waehrung=CHF` ein (mehrere mit Komma), mach daraus ein Objekt und führ beides mit `...` zusammen; die Wünsche gewinnen. Gib dann jede Einstellung aus. Bei der Eingabe `waehrung=CHF,stempel=10`:

```
Wünsche? waehrung: CHF
rabatt: 10
stempel: 10
```
