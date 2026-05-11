---
schema_version: 1
id: s151-buecher-seitensummen-autor
revision: 1
titel: "Seiten-Summe pro Autor"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, sum, group-by]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: bibliothek
schema_hinweis: |
  autoren(id, name, geburtsjahr, land)
  buecher(id, titel, autor_id, jahr, seiten, kategorie, exemplare)
  leser(id, name, ort, alter_jahre, mitglied_seit)
  ausleihen(id, leser_id, buch_id, ausgeliehen_am, zurueck_am)
erwartete_spalten: ["name", "gesamt"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Thomas Mann", 1751]
  - ["Cornelia Funke", 1008]
  - ["Haruki Murakami", 920]
  - ["Jane Austen", 906]
  - ["Stefan Zweig", 624]
  - ["Ursula K. Le Guin", 528]
  - ["Hermann Hesse", 441]
  - ["George Orwell", 438]
  - ["Franz Kafka", 386]
  - ["Astrid Lindgren", 292]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY autor + SUM(seiten).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Seitensumme pro Autor

Autor + Gesamtseiten aller seiner Bücher, dickste zuerst.
