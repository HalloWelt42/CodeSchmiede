---
schema_version: 1
id: j188-kundendatei
revision: 1
titel: Die Kundendatei
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- destrukturierung
- spread
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Beim Objekt reicht `{ name, alter: Number(alter), lieblinge }`: gleiche Namen muss man nicht doppelt schreiben.'
- kosten: 2
  text: '`[...set]` macht aus einem Set wieder ein Array, das join kennt.'
tests_sichtbar:
- input:
  - Pia;5;Hering;Aal
  - Ole;7
  - Ida;4;Aal;Butt
  expected: 'Zeile? Zeile? Zeile? Zeile? Pia (5) mag Hering, Aal

    Ole (7) mag nichts Besonderes

    Ida (4) mag Aal, Butt

    Ältester: 7

    Alle Lieblinge: Hering, Aal, Butt

    '
tests_versteckt:
- input:
  - Kim;9;Lachs;Lachs
  - Bo;3
  expected: 'Zeile? Zeile? Zeile? Kim (9) mag Lachs, Lachs

    Bo (3) mag nichts Besonderes

    Ältester: 9

    Alle Lieblinge: Lachs

    '
- input:
  - Bo;3
  expected: 'Zeile? Zeile? Bo (3) mag nichts Besonderes

    Ältester: 3

    Alle Lieblinge: keine

    '
starter_code: ''
---

Lies Zeilen wie `Pia;5;Hering;Aal` (Name, Alter, dann beliebig viele Lieblingsfische), bis eine leere Antwort oder keine mehr kommt. Pack jede Zeile mit `[name, alter, ...lieblinge]` aus und leg ein Objekt an. Gib jeden Kunden aus (ohne Lieblinge `nichts Besonderes`), dann das höchste Alter mit `Math.max(...)` und alle Lieblingsfische ohne Doppelte in der Reihenfolge ihres ersten Auftretens (über ein Set). Bei den Eingaben `Pia;5;Hering;Aal`, `Ole;7` und `Ida;4;Aal;Butt`:

```
Zeile? Zeile? Zeile? Zeile? Pia (5) mag Hering, Aal
Ole (7) mag nichts Besonderes
Ida (4) mag Aal, Butt
Ältester: 7
Alle Lieblinge: Hering, Aal, Butt
```
