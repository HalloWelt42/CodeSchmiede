---
schema_version: 1
id: s182-leser-mit-roman-historie
revision: 1
titel: "Leser, die mind. einen Roman ausgeliehen haben"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [join, where, distinct]
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
  - ["Bernd Mueller"]
  - ["David Fischer"]
  - ["Eva Schulz"]
  - ["Felix Bauer"]
  - ["Hans Wagner"]
  - ["Ines Becker"]
  - ["Karin Koehler"]
  - ["Lukas Richter"]
  - ["Maria Klein"]
  - ["Niklas Wolf"]
  - ["Olivia Krueger"]
hints:
  - kosten: 0
    text: |
      JOINs + WHERE kategorie='Roman' + DISTINCT.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Roman-Leser

Leser, die irgendwann einen Roman ausgeliehen haben.
