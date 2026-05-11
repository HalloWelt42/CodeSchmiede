---
schema_version: 1
id: s176-leser-juenger-als-buch
revision: 1
titel: "Leser jünger als das älteste Buch"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [subquery]
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
  - ["Clara Weber"]
  - ["David Fischer"]
  - ["Eva Schulz"]
  - ["Felix Bauer"]
  - ["Greta Hoffmann"]
  - ["Hans Wagner"]
  - ["Ines Becker"]
  - ["Jonas Schaefer"]
  - ["Karin Koehler"]
  - ["Lukas Richter"]
  - ["Maria Klein"]
  - ["Niklas Wolf"]
  - ["Olivia Krueger"]
hints:
  - kosten: 0
    text: |
      Subquery liefert Alter des ältesten Buchs in 2026.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser jünger als ältestes Buch

Leser, deren Alter kleiner ist als das Alter des ältesten Buchs.
