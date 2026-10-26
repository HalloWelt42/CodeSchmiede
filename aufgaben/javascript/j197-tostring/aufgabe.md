---
schema_version: 1
id: j197-tostring
revision: 1
titel: Ein Objekt, das sich vorstellt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- klasse
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`toString() { return ...; }` in der Klasse; die Vorlage ruft es von selbst auf.'
tests_sichtbar:
- input:
  - '3'
  expected: 'Wie viele? Bestellung: 3 x Hering für 7.50 Euro

    Bestellung: 1 x Suppe für 4.50 Euro

    '
tests_versteckt:
- input:
  - '10'
  expected: 'Wie viele? Bestellung: 10 x Hering für 25.00 Euro

    Bestellung: 1 x Suppe für 4.50 Euro

    '
starter_code: ''
---

Gibt eine Klasse eine Methode `toString()` mit, benutzt JavaScript sie, wenn ein Objekt in einer Vorlage steht. Schreib `Bestellung` mit `ware`, `anzahl` und `preis` und einem toString, und gib die Bestellungen aus. Bei der Eingabe `3`:

```
Wie viele? Bestellung: 3 x Hering für 7.50 Euro
Bestellung: 1 x Suppe für 4.50 Euro
```
