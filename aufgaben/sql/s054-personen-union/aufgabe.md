---
schema_version: 1
id: s054-personen-union
revision: 1
titel: "Alle Personen-Namen (Autoren + Leser)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [union, set]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt"]
  - ["Astrid Lindgren"]
  - ["Bernd Mueller"]
  - ["Clara Weber"]
  - ["Cornelia Funke"]
  - ["David Fischer"]
  - ["Eva Schulz"]
  - ["Felix Bauer"]
  - ["Franz Kafka"]
  - ["George Orwell"]
  - ["Greta Hoffmann"]
  - ["Hans Wagner"]
  - ["Haruki Murakami"]
  - ["Hermann Hesse"]
  - ["Ines Becker"]
  - ["Jane Austen"]
  - ["Jonas Schaefer"]
  - ["Karin Koehler"]
  - ["Lukas Richter"]
  - ["Maria Klein"]
  - ["Niklas Wolf"]
  - ["Olivia Krueger"]
  - ["Stefan Zweig"]
  - ["Thomas Mann"]
  - ["Ursula K. Le Guin"]
hints:
  - kosten: 0
    text: |
      `UNION` kombiniert Resultate, entfernt Duplikate.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Alle Personen-Namen

Union aller Autor- und Lesernamen, alphabetisch.
