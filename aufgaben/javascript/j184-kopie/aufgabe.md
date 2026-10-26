---
schema_version: 1
id: j184-kopie
revision: 1
titel: Die Angebotskarte
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- spread
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`{ ...g, preis: g.preis * 0.8 }` ist eine geänderte Kopie eines Gerichts.'
- kosten: 2
  text: 'Gibt eine Pfeilfunktion ein Objekt direkt zurück, braucht es runde Klammern darum: `g => ({ ... })`.'
tests_sichtbar:
- input: []
  expected: 'Angebot: Hering 2.00, Suppe 3.60, Matjes 3.00

    Original: Hering 2.50, Suppe 4.50

    '
starter_code: 'const karte = [{ name: "Hering", preis: 2.5 }, { name: "Suppe", preis: 4.5 }];

  const zeigen = (liste) => liste.map((g) => `${g.name} ${g.preis.toFixed(2)}`).join(", ");

  '
---

Mach mit `...` eine Kopie der Karte, in der jedes Gericht 20 Prozent billiger ist (mit map und einer Objektkopie je Gericht), und hänge in der Kopie noch `{ name: "Matjes", preis: 3 }` an. Das Original darf sich nicht ändern:

```
Angebot: Hering 2.00, Suppe 3.60, Matjes 3.00
Original: Hering 2.50, Suppe 4.50
```
