---
schema_version: 1
id: j138-vereinsliste
revision: 1
titel: Die Vereinsliste
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- map
- set
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`(sportarten.get(sport) || 0) + 1` zählt auch beim ersten Mal richtig, weil undefined als falsch gilt.'
- kosten: 2
  text: Vor dem add prüfen, ob der Name schon im Set ist.
tests_sichtbar:
- input:
  - Pia Schwimmen
  - Ole Rodeln
  - Pia Rodeln
  - Ida Schwimmen
  expected: 'Anmeldung? Anmeldung? Anmeldung? Anmeldung? Anmeldung? Schwimmen: 2

    Rodeln: 2

    Mitglieder: 3

    Mehrfach dabei: Pia

    '
tests_versteckt:
- input: []
  expected: 'Anmeldung? Mitglieder: 0

    '
- input:
  - A X
  - A X
  - A Y
  - B X
  - B Z
  expected: 'Anmeldung? Anmeldung? Anmeldung? Anmeldung? Anmeldung? Anmeldung? X: 3

    Y: 1

    Z: 1

    Mitglieder: 2

    Mehrfach dabei: A, B

    '
starter_code: ''
---

Lies Anmeldungen wie `Pia Schwimmen`, bis eine leere Antwort oder keine mehr kommt. Zähl in einer Map, wie viele sich je Sportart angemeldet haben, und merk dir die Namen in einem Set. Wer sich mehrfach anmeldet, zählt nur einmal als Mitglied und erscheint unter `Mehrfach dabei` (in der Reihenfolge, in der es auffiel; die Zeile fehlt, wenn es niemand ist). Bei den Eingaben `Pia Schwimmen`, `Ole Rodeln`, `Pia Rodeln` und `Ida Schwimmen`:

```
Anmeldung? Anmeldung? Anmeldung? Anmeldung? Anmeldung? Schwimmen: 2
Rodeln: 2
Mitglieder: 3
Mehrfach dabei: Pia
```
