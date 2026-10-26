---
schema_version: 1
id: j218-kueche
revision: 1
titel: Die Küche
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- async
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Erst alles einlesen, dann zugleich kochen: `Promise.all(bestellung.map(kochen))`.'
- kosten: 2
  text: '`Math.max(0, ...zahlen)` liefert auch bei einer leeren Liste 0.'
tests_sichtbar:
- input:
  - Suppe
  - Eis
  - Limonade
  - Brötchen
  expected: 'Gericht? Gericht? Eis gibt es nicht

    Gericht? Gericht? Gericht? fertig: Limonade

    fertig: Brötchen

    fertig: Suppe

    Tablett: Suppe, Limonade, Brötchen

    Wartezeit: 30 ms

    '
tests_versteckt:
- input: []
  expected: 'Gericht? Tablett: leer

    Wartezeit: 0 ms

    '
- input:
  - Matjes
  - Suppe
  - Matjes
  - ''
  expected: 'Gericht? Gericht? Gericht? Gericht? fertig: Matjes

    fertig: Matjes

    fertig: Suppe

    Tablett: Matjes, Suppe, Matjes

    Wartezeit: 30 ms

    '
starter_code: ''
---

Lies Gerichte, bis eine leere Antwort oder keine mehr kommt; unbekannte meldest du mit `... gibt es nicht`. Die Kochzeiten stehen in einer Map: Suppe 30, Brötchen 10, Limonade 5, Matjes 15 Millisekunden. Dann kochen alle zugleich mit `Promise.all`, jedes meldet `fertig: ...`, sobald es fertig ist. Zum Schluss das Tablett in Bestellreihenfolge (oder `leer`) und die Wartezeit, also die längste Kochzeit. Bei den Eingaben `Suppe`, `Eis`, `Limonade` und `Brötchen`:

```
Gericht? Gericht? Eis gibt es nicht
Gericht? Gericht? Gericht? fertig: Limonade
fertig: Brötchen
fertig: Suppe
Tablett: Suppe, Limonade, Brötchen
Wartezeit: 30 ms
```
