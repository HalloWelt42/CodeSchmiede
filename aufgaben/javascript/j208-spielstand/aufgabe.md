---
schema_version: 1
id: j208-spielstand
revision: 1
titel: Der Spielstand
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- json
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Alles, was beim Lesen schiefgehen kann, in ein try; im catch das neue Spiel anlegen.
- kosten: 2
  text: Ein Array ist auch ein object, darum zusätzlich `Array.isArray(stand)` prüfen.
tests_sichtbar:
- input:
  - '{"name":"Pia","punkte":5,"fische":["Aal"]}'
  - punkte 3
  - fisch Butt
  expected: 'Spielstand? Befehl? Befehl? Befehl? Pia hat 8 Punkte und 2 Fische

    {"name":"Pia","punkte":8,"fische":["Aal","Butt"]}

    '
tests_versteckt:
- input:
  - kaputt
  - fisch Hering
  - tanzen
  expected: 'Spielstand? Neues Spiel

    Befehl? Befehl? Unbekannt: tanzen

    Befehl? Pit hat 0 Punkte und 1 Fische

    {"name":"Pit","punkte":0,"fische":["Hering"]}

    '
- input:
  - ''
  expected: 'Spielstand? Neues Spiel

    Befehl? Pit hat 0 Punkte und 0 Fische

    {"name":"Pit","punkte":0,"fische":[]}

    '
- input:
  - '[1]'
  - punkte 2
  - ''
  expected: 'Spielstand? Neues Spiel

    Befehl? Befehl? Pit hat 2 Punkte und 0 Fische

    {"name":"Pit","punkte":2,"fische":[]}

    '
starter_code: ''
---

Lies einen Spielstand als JSON. Ist er unlesbar, leer oder kein Objekt, beginnt ein neues Spiel (`Neues Spiel`) mit `{"name":"Pit","punkte":0,"fische":[]}`. Dann Befehle, bis eine leere Antwort oder keine mehr kommt: `punkte n` zählt Punkte dazu, `fisch Name` legt einen Fisch dazu, alles andere ist `Unbekannt: ...`. Am Ende eine Zusammenfassung und der neue Spielstand als kompakter JSON-Text. Bei den Eingaben `{"name":"Pia","punkte":5,"fische":["Aal"]}`, `punkte 3` und `fisch Butt`:

```
Spielstand? Befehl? Befehl? Befehl? Pia hat 8 Punkte und 2 Fische
{"name":"Pia","punkte":8,"fische":["Aal","Butt"]}
```
