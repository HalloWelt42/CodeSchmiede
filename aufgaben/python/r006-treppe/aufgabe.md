---
schema_version: 1
id: r006-treppe
revision: 1
titel: Treppe
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 10
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #######
    #####Z#
    ####..#
    ###..##
    ##..###
    #>.####
    #######
  versteckt:
    - |
      #####
      ###Z#
      ##..#
      #>.##
      #####
    - |
      #########
      #######Z#
      ######..#
      #####..##
      ####..###
      ###..####
      ##..#####
      #>.######
      #########
  sterne: {schritte: 16, zeichen: 55}
---

# Treppe

Eine Treppe nach rechts oben, in den versteckten Welten mit weniger und mit mehr Stufen. Jede Stufe ist dasselbe Muster aus vier Befehlen.
