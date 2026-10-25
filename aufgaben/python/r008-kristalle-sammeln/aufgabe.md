---
schema_version: 1
id: r008-kristalle-sammeln
revision: 1
titel: Kristalle sammeln
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 12
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #########
    #>..K.#Z#
    #####.#.#
    #.K...#K#
    #.#####.#
    #.......#
    #########
  versteckt:
    - |
      #######
      #>.K#Z#
      ###.#.#
      #...#K#
      #K###.#
      #.....#
      #######
    - |
      #######
      #ZK...#
      #####K#
      #>..K.#
      #######
  sterne: {schritte: 36, zeichen: 105}
---

# Kristalle sammeln

Derselbe Kurvengang, diesmal liegen mehrere Kristalle darin, auch auf dem Startfeld. Sammle alle ein.
