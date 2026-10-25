---
schema_version: 1
id: r009-rechte-hand
revision: 1
titel: Rechte Hand an der Wand
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 12
schaetz_minuten: 13
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #########
    #>..#...#
    #.#.#.#.#
    #.#...#.#
    #.#####.#
    #...#..Z#
    #########
  versteckt:
    - |
      #########
      #>..#..Z#
      ###.#.###
      #...#...#
      #.#####.#
      #.......#
      #########
    - |
      #######
      #>#...#
      #.#.#.#
      #...#Z#
      #######
  sterne: {schritte: 77, zeichen: 67}
---

# Rechte Hand an der Wand

Ein Labyrinth mit Sackgassen. Ein alter Trick führt sicher hinaus: Halte die rechte Hand immer an der Wand. Vor jedem Schritt drehst du dich nach rechts und dann so lange nach links, bis vorn frei ist.
