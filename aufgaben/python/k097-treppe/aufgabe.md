---
schema_version: 1
id: k097-treppe
revision: 1
titel: Die Treppe
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- for
- range
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Text mal Zahl wiederholt den Text.
tests_sichtbar:
- input:
  - '4'
  expected: '#

    ##

    ###

    ####

    '
tests_versteckt:
- input:
  - '2'
  expected: '#

    ##

    '
- input:
  - '6'
  expected: '#

    ##

    ###

    ####

    #####

    ######

    '
starter_code: ''
---

Lies eine Zahl n ein und zeichne eine Treppe aus `#`: in Zeile i stehen i Zeichen. Bei `4`:

```
#
##
###
####
```
