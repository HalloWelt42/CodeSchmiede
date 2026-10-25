---
schema_version: 1
id: r007-kurvenreich
revision: 1
titel: Kurvenreich
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 11
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #########
    #>....#Z#
    #####.#.#
    #.....#.#
    #.#####.#
    #.......#
    #########
  versteckt:
    - |
      #######
      #>..#Z#
      ###.#.#
      #...#.#
      #.###.#
      #.....#
      #######
    - |
      #######
      #Z....#
      #####.#
      #>....#
      #######
  sterne: {schritte: 33, zeichen: 86}
---

# Kurvenreich

Ein Gang mit vielen Kurven, mal nach rechts, mal nach links, ohne Abzweigungen. Steht eine Wand vor dir, probier eine Richtung; ist dort auch Wand, geht es in die andere.
