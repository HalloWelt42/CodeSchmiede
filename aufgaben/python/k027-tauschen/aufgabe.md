---
schema_version: 1
id: k027-tauschen
revision: 1
titel: Plätze tauschen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- variablen
- knobeln
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Wenn du links sofort überschreibst, ist Paul verloren. Merke ihn dir vorher.
- kosten: 3
  text: 'Drei Zeilen: `merker = links`, `links = rechts`, `rechts = merker`.'
tests_sichtbar:
- input: []
  expected: 'Pia Paul

    '
starter_code: 'links = "Paul"

  rechts = "Pia"


  print(links, rechts)

  '
---

Zwei Pinguine stehen falsch herum: `links` hat `Paul`, `rechts` hat `Pia`. Tausche die Werte, sodass danach `links` den Wert `Pia` hat und `rechts` den Wert `Paul`. Die letzte Zeile gibt beide aus:

```
Pia Paul
```

Kleine Knobelei: du darfst einen dritten Namen als Zwischenablage benutzen.
