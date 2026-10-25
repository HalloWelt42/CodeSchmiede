---
schema_version: 1
id: k178-messwerte
revision: 1
titel: Der Messwertsammler
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- ausnahme
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'In der Schleife: `werte.append(messwert(text))` im try.'
- kosten: 3
  text: Scheitert float, löst messwert selbst `raise ValueError(text)` aus; dann passt beim Fangen immer `print("Übersprungen:",
    fehler)`.
tests_sichtbar:
- input:
  - '-3.5'
  - kalt
  - '-120'
  - '1.5'
  - ende
  expected: 'Übersprungen: kalt

    Übersprungen: unmöglich kalt

    Durchschnitt: -1.0

    '
tests_versteckt:
- input:
  - ende
  expected: 'Keine Messwerte

    '
- input:
  - x
  - ende
  expected: 'Übersprungen: x

    Keine Messwerte

    '
- input:
  - '20'
  - '21'
  - '23'
  - ende
  expected: 'Durchschnitt: 21.3

    '
starter_code: ''
---

Schreibe eine Funktion `messwert(text)`, die den Text mit `float` umwandelt und bei Werten unter -90 einen `ValueError` mit der Meldung `unmöglich kalt` auslöst. Lies Temperaturen ein, bis `ende` kommt. Ungültige Eingaben werden mit `Übersprungen: ` und dem Text gemeldet, falsche Werte mit `Übersprungen: unmöglich kalt`. Zum Schluss steht der Durchschnitt, auf eine Stelle gerundet; ohne gültige Werte steht dort `Keine Messwerte` (fange dafür den `ZeroDivisionError`). Bei `-3.5`, `kalt`, `-120`, `1.5`, `ende`:

```
Übersprungen: kalt
Übersprungen: unmöglich kalt
Durchschnitt: -1.0
```
