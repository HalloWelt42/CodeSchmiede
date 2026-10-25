---
schema_version: 1
id: k002-die-zeugin
revision: 1
titel: Die Zeugin
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Zwei Bedingungen zugleich: Straße und Hausnummer, verbunden mit AND."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 2
  frage: "Wer wohnt in der Marktgasse 14? Gesucht ist der Name."
  antwort: "Erika Brenner"
  antwort_gegen: "Hanna Vogt"
  notiz: "Zeugin: Erika Brenner, Marktgasse 14"
  versuche: 1
---

Gegenüber dem Vereinsheim, in der Marktgasse 14, sitzt jeden Abend jemand am Fenster. "Die sieht alles", sagt der Hausmeister. Den Namen weiß er nicht.

Im Einwohnerverzeichnis stehen alle mit Straße und Hausnummer. Aber Vorsicht: Am Marktplatz gibt es auch eine 14, und in der Marktgasse eine 4 und eine 41.
