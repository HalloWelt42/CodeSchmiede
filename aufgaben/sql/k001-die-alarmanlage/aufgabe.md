---
schema_version: 1
id: k001-die-alarmanlage
revision: 1
titel: Die Alarmanlage
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Filtere nach ort und art, und grenze die Zeit auf den Abend des 14. März ein, etwa mit BETWEEN."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 1
  frage: "Wann wurde die Vitrine am Abend des 14. März geöffnet? Gesucht ist der Zeitpunkt aus der Tabelle ereignisse."
  antwort: "2026-03-14 21:47"
  antwort_gegen: "2026-03-14 21:53"
  notiz: "Vitrine geöffnet: 14. März, 21:47"
  versuche: 1
---

Samstagmorgen, Vereinsheim des Turnvereins Altstadt. Die Vitrine im ersten Stock ist leer, der silberne Pokal der Stadtmeisterschaft ist weg. Aufgebrochen wurde nichts.

Die Alarmanlage schreibt jedes Öffnen und Schließen mit, auch die Vitrine hat einen Kontakt. Morgens öffnet der Putzdienst sie zum Abstauben, und am Vorabend hat jemand den Pokal poliert.
