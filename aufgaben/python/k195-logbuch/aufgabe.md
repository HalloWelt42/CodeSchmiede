---
schema_version: 1
id: k195-logbuch
revision: 1
titel: Das Logbuch
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- datei
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: In der Funktion mit `"a"` öffnen, beim Anlegen mit `"w"`.
tests_sichtbar:
- input:
  - Fisch gefangen
  - Eis gegessen
  - ende
  expected: 'Logbuch

    Fisch gefangen

    Eis gegessen

    '
tests_versteckt:
- input:
  - ende
  expected: 'Logbuch

    '
starter_code: ''
---

Schreibe eine Funktion `eintragen(text)`, die eine Zeile an `logbuch.txt` anhängt. Lege das Logbuch zuerst mit der Überschrift `Logbuch` neu an, trage dann jede Eingabe ein, bis `ende` kommt, und gib zum Schluss die ganze Datei aus. Bei `Fisch gefangen`, `Eis gegessen`, `ende`:

```
Logbuch
Fisch gefangen
Eis gegessen
```
