---
schema_version: 1
id: j144-preisfunktion
revision: 1
titel: Die Preisfunktion
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- funktion
- return
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Funktionen, jede mit return.
- kosten: 2
  text: 'Aufrufe lassen sich verschachteln: `euro(preis(broetchen, 2.5))`.'
tests_sichtbar:
- input:
  - '3'
  - '2'
  expected: 'Brötchen? Suppen? Brötchen: 7.50 Euro

    Suppen: 9.00 Euro

    Zusammen: 16.50 Euro

    '
tests_versteckt:
- input:
  - '0'
  - '1'
  expected: 'Brötchen? Suppen? Brötchen: 0.00 Euro

    Suppen: 4.50 Euro

    Zusammen: 4.50 Euro

    '
starter_code: ''
---

Schreib `preis(anzahl, einzelpreis)`, die den Gesamtpreis liefert, und `euro(betrag)`, die ihn als Text mit zwei Stellen und `Euro` liefert. Lies die Zahl der Brötchen (2.5) und der Suppen (4.5) ein. Bei den Eingaben `3` und `2`:

```
Brötchen? Suppen? Brötchen: 7.50 Euro
Suppen: 9.00 Euro
Zusammen: 16.50 Euro
```
