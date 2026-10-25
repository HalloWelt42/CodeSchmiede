---
schema_version: 1
id: r005-der-lange-gang
revision: 1
titel: Der lange Gang
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 9
schaetz_minuten: 9
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    ########
    ######Z#
    ######.#
    ###..K.#
    ###.####
    ###.####
    #>..####
    ########
  versteckt:
    - |
      ##########
      ########Z#
      ########.#
      ########.#
      ###....K.#
      ###.######
      ###.######
      #>..######
      ##########
    - |
      ########
      ####Z###
      ##...###
      ##.#####
      #>K#####
      ########
  sterne: {schritte: 14, zeichen: 167}
---

# Der lange Gang

Bring den Roboter ins grüne Feld und nimm unterwegs den Kristall mit. Der Gang knickt dreimal ab, in den versteckten Welten mit anderen Längen. Eine eigene Funktion, die bis zur Wand läuft, spart viel Tipparbeit.
