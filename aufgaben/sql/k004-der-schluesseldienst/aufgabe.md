---
schema_version: 1
id: k004-der-schluesseldienst
revision: 1
titel: Der Schlüsseldienst
sprache: sql
task_type: sql_krimi
runner_type: docker_sqlite
schwierigkeit: mittel
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [sql-krimi, sql]
voraussetzungen: []
quelle:
  url: null
  notiz: SQL-Krimi, Fall 1, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Drei Tabellen hängen zusammen: firmen, fahrzeuge (firma_id) und durchfahrten (kennzeichen)."}
  - {kosten: 2, text: "Mehrere Durchfahrten derselben Firma? DISTINCT macht aus vielen Zeilen eine."}
krimi:
  dataset: krimi_pokal
  gegenprobe: krimi_pokal_gegen
  kapitel: 4
  frage: "Welcher Schlüsseldienst fuhr am 14. März zwischen 21:00 und 22:30 Uhr mit einem blauen Wagen durch die Stadt? Gesucht ist der Name der Firma."
  antwort: "Schlüssel Sommer"
  antwort_gegen: "Rapid Schloss"
  notiz: "Schlüssel Sommer, blauer Lieferwagen LK-447-B um 21:22"
  versuche: 1
---

Die Vitrine war abgeschlossen, und aufgebrochen wurde sie nicht. Wer sie geöffnet hat, brauchte einen Schlüssel oder jemanden, der einen machen kann.

"Ein blauer Lieferwagen", hat Erika Brenner gesagt. Die Stadt führt ein Register der Firmen, und jede Fahrt durch das Altstadt-Tor steht in der Tabelle der Durchfahrten.
