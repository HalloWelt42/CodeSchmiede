---
schema_version: 1
id: r001-geradeaus
revision: 1
titel: Geradeaus
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 5
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #######
    #>...Z#
    #######
  versteckt: []
  sterne: {schritte: 4, zeichen: 34}
---

# Geradeaus

Bring den Roboter ins grüne Feld. Er schaut nach rechts; `gehe()` bewegt ihn ein Feld nach vorn.
