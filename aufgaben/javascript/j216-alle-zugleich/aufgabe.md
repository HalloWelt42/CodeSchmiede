---
schema_version: 1
id: j216-alle-zugleich
revision: 1
titel: Alle zugleich
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- promise
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Pit braucht 20, Pia 5, Paul 40 Millisekunden, und Pit bricht zuerst auf.
- kosten: 2
  text: '`await Promise.all([fischen(...), fischen(...), fischen(...)])` liefert die Ergebnisse in Aufbruchsreihenfolge.'
tests_sichtbar:
- input: []
  expected: 'zurück: Pia

    zurück: Pit

    zurück: Paul

    Fang: Pit 3, Pia 5, Paul 2

    '
starter_code: "function fischen(name, ms, fische) {\n  return new Promise((erfuellen) => {\n    setTimeout(() => {\n     \
  \ console.log(`zurück: ${name}`);\n      erfuellen(`${name} ${fische}`);\n    }, ms);\n  });\n}\n"
---

Drei Pinguine holen gleichzeitig Fisch, jeder braucht unterschiedlich lange. Warte mit `Promise.all` auf alle und gib erst aus, wer zurück ist (in der Reihenfolge der Ankunft), dann den Fang in der Reihenfolge des Aufbruchs:

```
zurück: Pia
zurück: Pit
zurück: Paul
Fang: Pit 3, Pia 5, Paul 2
```
