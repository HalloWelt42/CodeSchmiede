---
schema_version: 1
id: j076-angebot
revision: 1
titel: Angebot des Tages
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- verzweigung
- switch
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei case direkt untereinander teilen sich denselben Code.
- kosten: 2
  text: Hinter jedem Fall ein `break`.
tests_sichtbar:
- input:
  - Freitag
  expected: 'Tag? Bratfisch

    '
tests_versteckt:
- input:
  - Montag
  expected: 'Tag? Ruhetag

    '
- input:
  - Dienstag
  expected: 'Tag? Ruhetag

    '
- input:
  - Mittwoch
  expected: 'Tag? Matjes

    '
- input:
  - Sonntag
  expected: 'Tag? Heringsbrötchen

    '
starter_code: ''
---

Lies den Wochentag und nenne mit `switch` das Angebot: Montag und Dienstag `Ruhetag`, Mittwoch `Matjes`, Freitag `Bratfisch`, an allen anderen Tagen `Heringsbrötchen`. Bei der Eingabe `Freitag`:

```
Tag? Bratfisch
```
