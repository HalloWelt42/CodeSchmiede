---
schema_version: 1
id: j148-wechselgeld
revision: 1
titel: Das Wechselgeld
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- funktion
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Arrays, Münzwerte in Cent und ihre Namen, mit demselben Index.
- kosten: 2
  text: 'Für jede Münze: `Math.floor(cent / wert)` Stück, den Rest weiterreichen.'
tests_sichtbar:
- input:
  - '7.30'
  - '10'
  expected: 'Preis? Bezahlt? Rückgeld: 2.70 Euro

    1 x 2 Euro, 1 x 50 Cent, 1 x 20 Cent

    '
tests_versteckt:
- input:
  - '4.5'
  - '4.5'
  expected: 'Preis? Bezahlt? Rückgeld: 0.00 Euro

    passt genau

    '
- input:
  - '12.99'
  - '10'
  expected: 'Preis? Bezahlt? Es fehlen noch 2.99 Euro

    '
- input:
  - '0.01'
  - '5'
  expected: 'Preis? Bezahlt? Rückgeld: 4.99 Euro

    2 x 2 Euro, 1 x 50 Cent, 2 x 20 Cent, 1 x 5 Cent, 2 x 2 Cent

    '
starter_code: ''
---

Lies Preis und bezahlten Betrag ein. Rechne in Cent (`Math.round(betrag * 100)`), damit keine Kommazahlen krümeln. Reicht das Geld nicht, sag, wie viel fehlt. Sonst gib das Rückgeld aus und zerlege es in einer Funktion `zerlegen(cent)` in möglichst wenige Münzen (2 Euro, 1 Euro, 50, 20, 10, 5, 2, 1 Cent), die einen Text liefert. Bei den Eingaben `7.30` und `10`:

```
Preis? Bezahlt? Rückgeld: 2.70 Euro
1 x 2 Euro, 1 x 50 Cent, 1 x 20 Cent
```

Passt es genau, heißt die zweite Zeile `passt genau`.
