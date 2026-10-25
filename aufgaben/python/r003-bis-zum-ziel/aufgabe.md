---
schema_version: 1
id: r003-bis-zum-ziel
revision: 1
titel: Bis zum Ziel
sprache: python
task_type: roboter
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 7
tags: [roboter, schleifen]
voraussetzungen: []
quelle:
  url: null
  notiz: Roboter-Parcours, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints: []
starter_code: "# gehe(), links(), rechts(), nimm()\n# wand_vorne(), kristall(), am_ziel()\n"
roboter:
  welt: |
    #########
    #>.....Z#
    #########
  versteckt:
    - |
      ######
      #>..Z#
      ######
    - |
      ##############
      #>..........Z#
      ##############
  sterne: {schritte: 6, zeichen: 34}
---

# Bis zum Ziel

Geradeaus bis ins Ziel. Geprüft wird auch in versteckten Welten mit kürzeren und längeren Gängen: zähl nicht die Felder, sondern frag mit `am_ziel()`, ob du schon da bist.
