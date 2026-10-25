---
schema_version: 1
id: r002-um-die-ecke
revision: 1
titel: Um die Ecke
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 6
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    ######
    #>..##
    ###.##
    ###Z##
    ######
  versteckt: []
  sterne: {schritte: 5, zeichen: 42}
---

# Um die Ecke

Diesmal liegt das Ziel um die Ecke. `rechts()` und `links()` drehen den Roboter auf der Stelle.
