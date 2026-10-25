---
schema_version: 1
id: r010-schatz-im-labyrinth
revision: 1
titel: Schatz im Labyrinth
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 14
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 10
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #########
    #>.K#...#
    #.#.#K#.#
    #.#...#.#
    #.#####K#
    #...#..Z#
    #########
  versteckt:
    - |
      #########
      #>..#..Z#
      ###.#.###
      #.K.#...#
      #.#####.#
      #....K..#
      #########
    - |
      #######
      #>#.K.#
      #.#.#.#
      #K..#Z#
      #######
  sterne: {schritte: 80, zeichen: 86}
---

# Schatz im Labyrinth

Das Labyrinth vom letzten Level, jetzt mit Kristallen an der Wand entlang. Sammle alle ein, bevor du ins Ziel gehst.
