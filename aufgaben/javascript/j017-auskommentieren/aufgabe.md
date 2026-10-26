---
schema_version: 1
id: j017-auskommentieren
revision: 1
titel: Geheimes Angebot
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- ausgabe
- kommentar
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Schrägstriche `//` am Anfang einer Zeile machen sie zum Kommentar.
tests_sichtbar:
- input: []
  expected: 'Heute im Angebot:

    Heringsbrötchen

    '
starter_code: 'console.log("Heute im Angebot:");

  console.log("Alles umsonst für den Lehrling!");

  console.log("Heringsbrötchen");

  '
---

Der Lehrling hat ein Angebot in die Ansage geschmuggelt. Mach die Zeile mit dem Angebot zu einem **Kommentar**, ohne sie zu löschen, damit nur noch das hier erscheint:

```
Heute im Angebot:
Heringsbrötchen
```
