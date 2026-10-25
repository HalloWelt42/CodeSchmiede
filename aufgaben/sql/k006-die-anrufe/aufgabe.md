---
schema_version: 1
id: k006-die-anrufe
revision: 1
titel: Die Anrufe
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 3, text: "Zähle mit GROUP BY und COUNT(*), sortiere absteigend und nimm mit LIMIT 1 nur die erste Zeile."}
  - {kosten: 2, text: "Die Nummer von Lars Pohl findest du mit einer Unterabfrage auf personen."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 6
  frage: "Wen rief Lars Pohl am 14. März am häufigsten an? Gesucht ist der Name."
  antwort: "Mira Kessler"
  antwort_gegen: "Ole Hansen"
  notiz: "Pohl rief am Tatabend viermal Mira Kessler an"
  versuche: 1
---

Lars Pohl sagt, er sei nur kurz in der Stadt gewesen, um Werkzeug zu holen. Sein Telefon erzählt etwas anderes: Am Tatabend hat er immer wieder dieselbe Nummer gewählt.

In der Tabelle anrufe stehen nur Nummern. Wem welche Nummer gehört, steht bei den Personen. Seine Mutter ruft er übrigens jeden Mittag an, aber nicht am Samstag.
