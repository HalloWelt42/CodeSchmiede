---
schema_version: 1
id: j078-eintritt
revision: 1
titel: Eintritt ins Pinguinkino
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- verzweigung
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst den Preis nach dem Alter mit if und else if bestimmen, dann für Mitglieder halbieren.
- kosten: 2
  text: 'Für die Ausgabe passt die Kurzform: `preis === 0 ? "frei" : ...`'
tests_sichtbar:
- input:
  - '15'
  - ja
  expected: 'Alter? Mitglied? Eintritt: 2.00 Euro

    '
tests_versteckt:
- input:
  - '4'
  - nein
  expected: 'Alter? Mitglied? Eintritt: frei

    '
- input:
  - '30'
  - nein
  expected: 'Alter? Mitglied? Eintritt: 8.00 Euro

    '
- input:
  - '70'
  - ja
  expected: 'Alter? Mitglied? Eintritt: 2.50 Euro

    '
- input:
  - '18'
  - nein
  expected: 'Alter? Mitglied? Eintritt: 8.00 Euro

    '
starter_code: ''
---

Der Eintritt richtet sich nach dem Alter: unter 6 frei, unter 18 4 Euro, ab 65 5 Euro, sonst 8 Euro. Mitglieder (Antwort `ja`) zahlen die Hälfte. Gib `frei` aus oder den Preis mit zwei Stellen. Bei den Eingaben `15` und `ja`:

```
Alter? Mitglied? Eintritt: 2.00 Euro
```
