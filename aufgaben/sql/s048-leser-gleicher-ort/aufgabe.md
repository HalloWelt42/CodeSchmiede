---
schema_version: 1
id: s048-leser-gleicher-ort
revision: 1
titel: "Leser-Paare aus dem selben Ort"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [self-join]
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
erwartete_spalten: ["leser_a", "leser_b", "ort"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt", "David Fischer", "Berlin"]
  - ["Anna Schmidt", "Ines Becker", "Berlin"]
  - ["Anna Schmidt", "Niklas Wolf", "Berlin"]
  - ["David Fischer", "Ines Becker", "Berlin"]
  - ["David Fischer", "Niklas Wolf", "Berlin"]
  - ["Ines Becker", "Niklas Wolf", "Berlin"]
  - ["Bernd Mueller", "Greta Hoffmann", "Hamburg"]
  - ["Bernd Mueller", "Maria Klein", "Hamburg"]
  - ["Greta Hoffmann", "Maria Klein", "Hamburg"]
  - ["Clara Weber", "Jonas Schaefer", "München"]
  - ["Clara Weber", "Olivia Krueger", "München"]
  - ["Jonas Schaefer", "Olivia Krueger", "München"]
hints:
  - kosten: 0
    text: |
      Self-Join `leser l1 JOIN leser l2` mit `l1.id < l2.id` vermeidet Doppelpaare.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser-Paare aus dem selben Ort

Paare verschiedener Leser aus derselben Stadt (jedes Paar nur einmal).
