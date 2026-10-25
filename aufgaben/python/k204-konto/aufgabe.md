---
schema_version: 1
id: k204-konto
revision: 1
titel: Das Konto
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- klasse
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`konto.einzahlen(betrag)` und `konto.abheben(-betrag)`.'
tests_sichtbar:
- input:
  - '50'
  - '-20'
  - '-100'
  - ende
  expected: 'Zu wenig Geld

    Pia hat 30

    '
tests_versteckt:
- input:
  - ende
  expected: 'Pia hat 0

    '
- input:
  - '10'
  - '-10'
  - ende
  expected: 'Pia hat 0

    '
starter_code: "class Konto:\n    def __init__(self, inhaber):\n        self.inhaber = inhaber\n        self.stand = 0\n\n\
  \    def einzahlen(self, betrag):\n        self.stand += betrag\n\n    def abheben(self, betrag):\n        if betrag > self.stand:\n\
  \            print(\"Zu wenig Geld\")\n        else:\n            self.stand -= betrag\n\n\nkonto = Konto(\"Pia\")\n"
---

Die Klasse `Konto` steht schon da. Lies Buchungen ein, bis `ende` kommt: eine positive Zahl wird eingezahlt, eine negative abgehoben (ohne Minus). Gib zum Schluss Inhaber und Stand aus. Bei `50`, `-20`, `-100`, `ende`:

```
Zu wenig Geld
Pia hat 30
```
