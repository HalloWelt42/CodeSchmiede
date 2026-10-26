---
schema_version: 1
id: j165-konto
revision: 1
titel: Das Konto
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- sichtbarkeit
- closure
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ein Objekt mit Funktionen als Werte: `{ einzahlen: (betrag) => { ... }, stand: () => guthaben }`.'
tests_sichtbar:
- input:
  - '5'
  - '2.5'
  - '10'
  expected: 'Betrag? Betrag? Betrag? Betrag? Kontostand: 37.50 Euro

    '
tests_versteckt:
- input: []
  expected: 'Betrag? Kontostand: 20.00 Euro

    '
- input:
  - '0.1'
  - '0.2'
  - ''
  expected: 'Betrag? Betrag? Betrag? Kontostand: 20.30 Euro

    '
starter_code: ''
---

Schreib `kontoEroeffnen(start)`, die ein Objekt mit zwei Funktionen liefert: `einzahlen(betrag)` und `stand()`. Den Kontostand selbst soll niemand von außen ändern können, er lebt nur in der Closure. Lies Einzahlungen ein, bis eine leere Antwort oder keine mehr kommt. Bei den Eingaben `5`, `2.5` und `10`, bei Start 20:

```
Betrag? Betrag? Betrag? Betrag? Kontostand: 37.50 Euro
```
