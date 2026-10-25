---
schema_version: 1
id: k228-fangprotokoll
revision: 1
titel: Das Fangprotokoll
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- regex
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 22
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ein Muster mit zwei Gruppen: Name und Zahl.'
- kosten: 3
  text: '`re.fullmatch(r"([A-ZÄÖÜ]\w*) fing (\d+) \w+", zeile)`.'
tests_sichtbar:
- input:
  - Pia fing 3 Heringe
  - Pit hat Hunger
  - Pia fing 2 Lachse
  - Pit fing 5 Welse
  - ende
  expected: 'Unlesbar: Pit hat Hunger

    Pia: 5

    Pit: 5

    '
tests_versteckt:
- input:
  - ende
  expected: ''
- input:
  - pia fing 3 Heringe
  - Paul fing 10 Wale
  - Paul fing viele Wale
  - ende
  expected: 'Unlesbar: pia fing 3 Heringe

    Unlesbar: Paul fing viele Wale

    Paul: 10

    '
starter_code: ''
---

Lies Zeilen eines Fangprotokolls ein, bis `ende` kommt. Gültig sind Zeilen der Form `Pia fing 3 Heringe`: ein Name mit großem Anfangsbuchstaben, `fing`, eine Zahl, ein Wort. Andere Zeilen werden mit `Unlesbar:` gemeldet. Zum Schluss steht je Name die Summe der Fänge, in der Reihenfolge des ersten Auftretens. Bei `Pia fing 3 Heringe`, `Pit hat Hunger`, `Pia fing 2 Lachse`, `Pit fing 5 Welse`, `ende`:

```
Unlesbar: Pit hat Hunger
Pia: 5
Pit: 5
```
