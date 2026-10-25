---
schema_version: 1
id: r004-ein-kristall
revision: 1
titel: Ein Kristall unterwegs
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 8
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    ##########
    #>..K...Z#
    ##########
  versteckt:
    - |
      #############
      #>......K..Z#
      #############
    - |
      #######
      #>.K.Z#
      #######
  sterne: {schritte: 8, zeichen: 53}
---

# Ein Kristall unterwegs

Auf dem Weg liegt ein Kristall. Nimm ihn mit `nimm()` auf, bevor du ins Ziel gehst; `kristall()` sagt, ob auf deinem Feld einer liegt. In den versteckten Welten liegt er woanders.
