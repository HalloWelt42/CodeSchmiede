---
schema_version: 1
id: k003-die-aussage
revision: 1
titel: Die Aussage
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Verbinde aussagen und personen mit JOIN über person_id und id."}
  - {kosten: 2, text: "Mit LIKE '%Lieferwagen%' findest du das Wort im Text."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 3
  frage: "Um wie viel Uhr sah Erika Brenner den Lieferwagen? Gesucht ist der Zeitpunkt ihrer Aussage."
  antwort: "2026-03-14 21:35"
  antwort_gegen: "2026-03-14 21:28"
  notiz: "21:35: blauer Lieferwagen hält vor dem Vereinsheim"
  versuche: 1
---

Erika Brenner hat am Abend einiges zu Protokoll gegeben: ein bellender Hund, ein Lieferwagen, später das Licht im Vereinsheim. Auch andere Nachbarn haben einen Lieferwagen gesehen.

Die Aussagen stehen in der Tabelle aussagen, die Namen aber nur in personen.
