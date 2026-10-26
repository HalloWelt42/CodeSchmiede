---
schema_version: 1
id: j198-aquarium
revision: 1
titel: Das Aquarium
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 8
tags:
- kurs
- klasse
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: ausZeile packt mit `const [name, art, gramm] = zeile.split(" ")` aus und baut mit new.
- kosten: 2
  text: Die beiden get-Eigenschaften rechnen mit reduce über `this.fische`.
tests_sichtbar:
- input:
  - Nemo Clownfisch 120
  - Dori Doktorfisch 340
  - Bubbles Gelbschwanz 90
  expected: 'Fisch? Fisch? Fisch? Fisch? Nemo der Clownfisch (120 g)

    Dori der Doktorfisch (340 g)

    Bubbles der Gelbschwanz (90 g)

    Schwerster: Dori

    Gesamt: 0.6 kg

    Fische im Becken: 3

    '
tests_versteckt:
- input: []
  expected: 'Fisch? Fische im Becken: 0

    '
- input:
  - Wanda Hering 250
  - Otto Hering 250
  - ''
  expected: 'Fisch? Fisch? Fisch? Wanda der Hering (250 g)

    Otto der Hering (250 g)

    Schwerster: Wanda

    Gesamt: 0.5 kg

    Fische im Becken: 2

    '
starter_code: ''
---

Schreib eine Klasse `Fisch` (Name, Art, Gewicht in Gramm, Methode `beschreibung()`) und eine Klasse `Aquarium` mit einem Array, einer Methode `einsetzen(fisch)`, den berechneten Eigenschaften `schwerster` und `gesamtKilo` (mit `get`) und einer statischen Methode `ausZeile(zeile)`, die aus `Nemo Clownfisch 120` einen Fisch baut. Lies Zeilen, bis eine leere Antwort oder keine mehr kommt. Bei den Eingaben `Nemo Clownfisch 120`, `Dori Doktorfisch 340` und `Bubbles Gelbschwanz 90`:

```
Fisch? Fisch? Fisch? Fisch? Nemo der Clownfisch (120 g)
Dori der Doktorfisch (340 g)
Bubbles der Gelbschwanz (90 g)
Schwerster: Dori
Gesamt: 0.6 kg
Fische im Becken: 3
```

Ohne Fische fehlen die Zeilen zum schwersten und zum Gesamtgewicht.
