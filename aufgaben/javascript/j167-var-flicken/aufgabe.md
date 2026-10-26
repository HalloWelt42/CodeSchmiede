---
schema_version: 1
id: j167-var-flicken
revision: 1
titel: Die undichte Kiste
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- sichtbarkeit
- var
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Mit let gilt das innere summe nur im Block des if.
tests_sichtbar:
- input: []
  expected: 'Summe der Rabatte: 3

    Summe der Preise: 9

    '
starter_code: "var preise = [2, 3, 4];\nvar rabatte = [1, 1, 1];\nvar summe = 0;\nfor (var p of preise) {\n  summe += p;\n\
  }\nif (rabatte.length > 0) {\n  var summe = 0;\n  for (var r of rabatte) {\n    summe += r;\n  }\n  console.log(\"Summe\
  \ der Rabatte:\", summe);\n}\nconsole.log(\"Summe der Preise:\", summe);\n"
---

Dieser alte Code mit `var` liefert ein falsches Ergebnis, weil das innere `summe` das äußere überschreibt. Ersetze alle `var` durch `let` oder `const`, ohne sonst etwas zu ändern:

```
Summe der Rabatte: 3
Summe der Preise: 9
```
