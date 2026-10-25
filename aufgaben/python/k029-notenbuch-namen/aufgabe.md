---
schema_version: 1
id: k029-notenbuch-namen
revision: 1
titel: 'Notenbuch: Namen für die Teile'
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- projekt
- variablen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Die Gleichheitszeichen gehören in den Text: `print("===", titel, "===")`.'
tests_sichtbar:
- input: []
  expected: '=== Mein Notenbuch ===

    Fächer: Mathe, Deutsch, Musik

    '
starter_code: ''
---

**Kapitelprojekt Notenbuch, Stück 2.** Dein Notenbuch merkt sich jetzt seine Teile: lege `titel` mit `Mein Notenbuch` und `faecher` mit `Mathe, Deutsch, Musik` an und gib damit aus:

```
=== Mein Notenbuch ===
Fächer: Mathe, Deutsch, Musik
```
