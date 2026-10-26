---
schema_version: 1
id: j215-angebrannt
revision: 1
titel: Angebrannt
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- async
- try
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein abgelehntes Promise wirft beim await einen Fehler, den try und catch fangen.
tests_sichtbar:
- input:
  - Suppe
  - Eis
  - Brötchen
  expected: 'Gericht? Suppe ist fertig

    Gericht? Oh nein: Eis kocht man nicht

    Gericht? Brötchen ist fertig

    Gericht? Feierabend

    '
tests_versteckt:
- input: []
  expected: 'Gericht? Feierabend

    '
- input:
  - Eis
  - Eis
  - ''
  expected: 'Gericht? Oh nein: Eis kocht man nicht

    Gericht? Oh nein: Eis kocht man nicht

    Gericht? Feierabend

    '
starter_code: "function kochen(gericht) {\n  return new Promise((erfuellen, ablehnen) => {\n    setTimeout(() => {\n     \
  \ if (gericht === \"Eis\") {\n        ablehnen(new Error(\"Eis kocht man nicht\"));\n      } else {\n        erfuellen(`${gericht}\
  \ ist fertig`);\n      }\n    }, 5);\n  });\n}\n"
---

`kochen(gericht)` lehnt bei `Eis` ab. Lies Gerichte, bis eine leere Antwort oder keine mehr kommt, koch jedes mit await und fang Fehler mit try und catch ab. Bei den Eingaben `Suppe`, `Eis` und `Brötchen`:

```
Gericht? Suppe ist fertig
Gericht? Oh nein: Eis kocht man nicht
Gericht? Brötchen ist fertig
Gericht? Feierabend
```
