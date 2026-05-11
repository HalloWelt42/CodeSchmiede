---
schema_version: 1
id: s134-buecher-jahrhundert
revision: 1
titel: "Buecher pro Jahrhundert"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, math]
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
erwartete_spalten: ["jahrhundert", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - [19, 2]
  - [20, 16]
  - [21, 2]
hints:
  - kosten: 0
    text: |
      Jahrhundert = ((jahr - 1) / 100) + 1 (1815 -> 19. Jh.).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buecher pro Jahrhundert

Jahrhundert + Anzahl Buecher, chronologisch.
