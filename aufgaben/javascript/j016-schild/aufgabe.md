---
schema_version: 1
id: j016-schild
revision: 1
titel: Das Schild am Fischwagen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- ausgabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Striche und Pluszeichen sind ganz normaler Text.
- kosten: 1
  text: Die leere Zeile kommt von `console.log()` ohne etwas in den Klammern.
tests_sichtbar:
- input: []
  expected: '+------------+

    | Fischwagen |

    +------------+


    Täglich ab 6 Uhr

    '
starter_code: ''
---

Der Fischwagen braucht ein Schild. Gib es genau so aus, mit einer leeren Zeile vor den Öffnungszeiten:

```
+------------+
| Fischwagen |
+------------+

Täglich ab 6 Uhr
```
