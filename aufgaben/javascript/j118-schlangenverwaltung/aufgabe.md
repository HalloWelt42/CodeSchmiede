---
schema_version: 1
id: j118-schlangenverwaltung
revision: 1
titel: Die Schlangenverwaltung
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- arraymethoden
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`befehl.split(" ")` trennt Befehl und Namen: `teile[0]` und `teile[1]`.'
- kosten: 2
  text: Ein switch über `teile[0]`, je Fall eine Array-Methode.
tests_sichtbar:
- input:
  - an Pia
  - an Ole
  - vor Bo
  - weiter
  - weg Ole
  expected: 'Befehl? Befehl? Befehl? Befehl? Bedient: Bo

    Befehl? Befehl? Schlange: [ ''Pia'' ]

    '
tests_versteckt:
- input:
  - weiter
  - weg Ida
  - tanzen
  expected: 'Befehl? Niemand da

    Befehl? Ida steht nicht an

    Befehl? Unbekannt

    Befehl? Schlange: []

    '
- input:
  - an A
  - an B
  - an C
  - weiter
  - weiter
  - vor D
  - ''
  expected: 'Befehl? Befehl? Befehl? Befehl? Bedient: A

    Befehl? Bedient: B

    Befehl? Befehl? Schlange: [ ''D'', ''C'' ]

    '
starter_code: ''
---

Lies Befehle, bis eine leere Antwort oder keine mehr kommt: `an Name` stellt hinten an, `vor Name` stellt vorne an, `weiter` bedient den Ersten (`Bedient: Name`, bei leerer Schlange `Niemand da`), `weg Name` streicht ihn (oder meldet `Name steht nicht an`). Alles andere heißt `Unbekannt`. Am Ende steht die Schlange. Bei den Eingaben `an Pia`, `an Ole`, `vor Bo`, `weiter` und `weg Ole`:

```
Befehl? Befehl? Befehl? Befehl? Bedient: Bo
Befehl? Befehl? Schlange: [ 'Pia' ]
```
