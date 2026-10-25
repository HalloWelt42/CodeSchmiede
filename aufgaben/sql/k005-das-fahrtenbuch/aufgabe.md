---
schema_version: 1
id: k005-das-fahrtenbuch
revision: 1
titel: Das Fahrtenbuch
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: mittel
schwierigkeit_score: 15
schaetz_minuten: 9
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 3, text: "Vom Fahrtenbuch über fahrzeuge zu firmen, und für den Namen zu personen: vier Tabellen."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 5
  frage: "Wer fuhr am 14. März den blauen Wagen von Schlüssel Sommer? Gesucht ist der Name."
  antwort: "Lars Pohl"
  antwort_gegen: "Timo Kraus"
  notiz: "Fahrer am Tatabend: Lars Pohl"
  versuche: 1
---

Jonas Sommer, der Inhaber von Schlüssel Sommer, war am Samstag auf einer Hochzeit, zwanzig Gäste bestätigen das. Aber die Firma hat zwei Wagen und mehrere Leute, die damit fahren.

Wer an welchem Tag welchen Wagen fuhr, steht im Fahrtenbuch.
