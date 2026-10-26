---
schema_version: 1
id: j049-fischwagen-vorlagen
revision: 1
titel: 'Fischwagen: Bon mit Vorlagen'
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- projekt
- text
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Nimm den Code aus Kapitel 3 und ersetze die Ausgaben durch Vorlagen.
- kosten: 2
  text: '`${wagen.toUpperCase()}` in der Vorlage, der Strich mit `"=".repeat(30)`.'
tests_sichtbar:
- input: []
  expected: '*** ZUM FROSTIGEN HERING ***

    Kassenbon für Pia

    3 x Heringsbrötchen: 7.5 Euro

    2 x Limonade: 3.5 Euro

    ==============================

    Summe: 11 Euro

    '
starter_code: ''
---

**Kapitelprojekt Fischwagen, Stück 4.** Der Bon bekommt Ordnung. Schreib alle Zeilen mit Vorlagen, den Namen des Wagens in Großbuchstaben, Euro hinter die Beträge und vor die Summe einen Strich aus 30 `=`:

```
*** ZUM FROSTIGEN HERING ***
Kassenbon für Pia
3 x Heringsbrötchen: 7.5 Euro
2 x Limonade: 3.5 Euro
==============================
Summe: 11 Euro
```
