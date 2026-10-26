---
schema_version: 1
id: j205-tiefe-kopie
revision: 1
titel: Eine echte Kopie
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- json
- spread
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`JSON.parse(JSON.stringify(kunde))`'
tests_sichtbar:
- input: []
  expected: 'Original: Hering

    Kopie: Hering, Aal

    '
starter_code: 'const kunde = { name: "Pia", lieblinge: ["Hering"] };

  const kopie = { ...kunde };

  kopie.lieblinge.push("Aal");

  console.log(`Original: ${kunde.lieblinge.join(", ")}`);

  console.log(`Kopie: ${kopie.lieblinge.join(", ")}`);

  '
---

Mit `{ ...kunde }` teilen sich Original und Kopie das Array `lieblinge`. Mach stattdessen eine tiefe Kopie über JSON, damit das Original unverändert bleibt:

```
Original: Hering
Kopie: Hering, Aal
```
