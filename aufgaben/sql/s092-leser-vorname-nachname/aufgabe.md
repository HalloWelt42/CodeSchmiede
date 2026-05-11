---
schema_version: 1
id: s092-leser-vorname-nachname
revision: 1
titel: "Vorname und Nachname trennen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [string, substr, instr]
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
erwartete_spalten: ["name", "vorname", "nachname"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Felix Bauer", "Felix", "Bauer"]
  - ["Ines Becker", "Ines", "Becker"]
  - ["David Fischer", "David", "Fischer"]
  - ["Greta Hoffmann", "Greta", "Hoffmann"]
  - ["Maria Klein", "Maria", "Klein"]
  - ["Karin Koehler", "Karin", "Koehler"]
  - ["Olivia Krueger", "Olivia", "Krueger"]
  - ["Bernd Mueller", "Bernd", "Mueller"]
  - ["Lukas Richter", "Lukas", "Richter"]
  - ["Jonas Schaefer", "Jonas", "Schaefer"]
  - ["Anna Schmidt", "Anna", "Schmidt"]
  - ["Eva Schulz", "Eva", "Schulz"]
  - ["Hans Wagner", "Hans", "Wagner"]
  - ["Clara Weber", "Clara", "Weber"]
  - ["Niklas Wolf", "Niklas", "Wolf"]
hints:
  - kosten: 0
    text: |
      `INSTR(s, ' ')` liefert die 1-basierte Position des Leerzeichens.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Vor- und Nachname

Fuer jeden Leser: name + vorname + nachname als drei Spalten, sortiert nach Nachname.
