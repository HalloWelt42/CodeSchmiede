---
schema_version: 1
id: k008-das-lager
revision: 1
titel: Das Lager
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 12
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 3, text: "Nach der Tat heißt: später als der Zeitpunkt aus Kapitel 1. Sortiere nach der Zeit und nimm den ersten."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 8
  frage: "Welchen seiner Lagerräume betrat Holger Brandt nach der Tat als Ersten? Gesucht ist die Nummer des Raums."
  antwort: "L-07"
  antwort_gegen: "L-12"
  notiz: "Der Pokal liegt in Lager L-07, Hafenstraße 50"
  versuche: 1
---

Holger Brandt, der Vorsitzende des Vereins. Der Pokal hätte bei der Versicherung viel Geld gebracht, und die Vereinskasse ist leer.

Brandt hat mehrere Lagerräume am Hafen gemietet. Jede Tür hat ein Zahlenschloss, das jeden Zutritt speichert. Am Abend vor der Tat war er schon einmal dort.
