---
schema_version: 1
id: j176-weiterwerfen
revision: 1
titel: Weiterwerfen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- try
- throw
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Bei null scheitert schon `ware.trim()`, das ist ein TypeError und kein Fall für unbekannte Waren.
- kosten: 2
  text: 'Im catch: ist `fehler.name` nicht RangeError, dann `throw fehler;`.'
tests_sichtbar:
- input: []
  expected: 'Hering: 2.5

    unbekannt: Lachs

    Außen gefangen: TypeError

    '
starter_code: "const preise = { Hering: 2.5, Limonade: 1.75 };\nfunction preisVon(ware) {\n  if (!(ware in preise)) {\n  \
  \  throw new RangeError(ware);\n  }\n  return preise[ware];\n}\n\n// bon(waren) hier\n\ntry {\n  bon([\"Hering\", \"Lachs\"\
  , null]);\n} catch (fehler) {\n  console.log(\"Außen gefangen:\", fehler.name);\n}\n"
---

`preisVon(ware)` wirft bei unbekannten Waren einen `RangeError`. Die Funktion `bon(waren)` soll unbekannte Waren mit `unbekannt: Name` überspringen; jeder **andere** Fehler muss mit `throw fehler;` weiterfliegen und wird außen gemeldet. Für die Waren im Startcode kommt heraus:

```
Hering: 2.5
unbekannt: Lachs
Außen gefangen: TypeError
```
