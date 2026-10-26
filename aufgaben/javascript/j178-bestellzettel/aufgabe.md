---
schema_version: 1
id: j178-bestellzettel
revision: 1
titel: Der Bestellzettel
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- throw
- try
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine Funktion `pruefen(zeile)` mit drei throw; sie liefert ein Objekt mit Anzahl und Ware.
- kosten: 2
  text: 'In der Schleife: try mit pruefen und Ausgabe, catch zählt und meldet.'
tests_sichtbar:
- input:
  - 3 Hering
  - zwei Suppe
  - 1 Lachs
  - Limonade
  - 2 Suppe
  expected: 'Zeile? 3 x Hering: 7.50 Euro

    Zeile? Übersprungen: "zwei" ist keine gültige Anzahl

    Zeile? Übersprungen: Lachs gibt es nicht

    Zeile? Übersprungen: Format ist: Anzahl Ware

    Zeile? 2 x Suppe: 9.00 Euro

    Zeile? Summe: 16.50 Euro

    Fehlerhafte Zeilen: 3

    '
tests_versteckt:
- input: []
  expected: 'Zeile? Summe: 0.00 Euro

    Fehlerhafte Zeilen: 0

    '
- input:
  - 0 Hering
  - 1.5 Suppe
  - 4 Limonade
  - 1 Hering extra
  expected: 'Zeile? Übersprungen: "0" ist keine gültige Anzahl

    Zeile? Übersprungen: "1.5" ist keine gültige Anzahl

    Zeile? 4 x Limonade: 7.00 Euro

    Zeile? Übersprungen: Format ist: Anzahl Ware

    Zeile? Summe: 7.00 Euro

    Fehlerhafte Zeilen: 3

    '
starter_code: ''
---

Lies Zeilen wie `3 Hering`, bis eine leere Antwort oder keine mehr kommt. Eine Funktion prüft jede Zeile und wirft einen Fehler, wenn sie nicht genau zwei Teile hat (`Format ist: Anzahl Ware`), die Anzahl keine ganze Zahl über 0 ist (`"x" ist keine gültige Anzahl`) oder es die Ware nicht gibt (`Lachs gibt es nicht`). Gültige Zeilen kommen auf den Zettel, fehlerhafte werden mit `Übersprungen: ...` gemeldet und gezählt. Preise: Hering 2.5, Limonade 1.75, Suppe 4.5. Bei den Eingaben `3 Hering`, `zwei Suppe`, `1 Lachs`, `Limonade` und `2 Suppe`:

```
Zeile? 3 x Hering: 7.50 Euro
Zeile? Übersprungen: "zwei" ist keine gültige Anzahl
Zeile? Übersprungen: Lachs gibt es nicht
Zeile? Übersprungen: Format ist: Anzahl Ware
Zeile? 2 x Suppe: 9.00 Euro
Zeile? Summe: 16.50 Euro
Fehlerhafte Zeilen: 3
```
