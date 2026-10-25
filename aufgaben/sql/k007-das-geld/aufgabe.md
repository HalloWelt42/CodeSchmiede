---
schema_version: 1
id: k007-das-geld
revision: 1
titel: Das Geld
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 11
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 3, text: "Die id von Mira Kessler holst du mit einer Unterabfrage; der Name des Absenders kommt über von_id aus personen."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 7
  frage: "Wer überwies Mira Kessler in der Woche nach der Tat (15. bis 21. März) mehr als 500 Euro? Gesucht ist der Name."
  antwort: "Holger Brandt"
  antwort_gegen: "Sabine Lorenz"
  notiz: "Holger Brandt überwies am 17. März 1.500 Euro"
  versuche: 1
---

Mira Kessler ist Kassiererin im Turnverein. Sie gibt zu, Lars Pohl zu kennen, "aus der Schulzeit". Mehr sagt sie nicht.

Die Bank hat die Überweisungen der Woche herausgegeben. Kleine Beträge sind Mitgliedsbeiträge und Feiern; interessant ist, wer nach der Tat viel Geld geschickt hat.
