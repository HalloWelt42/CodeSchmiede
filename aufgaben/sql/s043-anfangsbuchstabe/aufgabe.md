---
schema_version: 1
id: s043-anfangsbuchstabe
revision: 1
titel: "Anfangsbuchstabe der Autorennamen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [string, substr]
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
erwartete_spalten: ["name", "initial"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Astrid Lindgren", "A"]
  - ["Cornelia Funke", "C"]
  - ["Franz Kafka", "F"]
  - ["George Orwell", "G"]
  - ["Haruki Murakami", "H"]
  - ["Hermann Hesse", "H"]
  - ["Jane Austen", "J"]
  - ["Stefan Zweig", "S"]
  - ["Thomas Mann", "T"]
  - ["Ursula K. Le Guin", "U"]
hints:
  - kosten: 0
    text: |
      `SUBSTR(name, 1, 1)` -- ab Position 1, Laenge 1 (1-basiert).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Anfangsbuchstabe der Autorennamen

Name + erstes Zeichen, alphabetisch nach Name.
