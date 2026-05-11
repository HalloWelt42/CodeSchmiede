---
schema_version: 1
id: s165-buecher-pro-laenge-stufe
revision: 1
titel: "Bücher: Längen-Stufe + Anzahl"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [case, group-by]
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
erwartete_spalten: ["stufe", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["< 200", 6]
  - ["200-399", 6]
  - ["400-599", 5]
  - [">= 600", 3]
hints:
  - kosten: 0
    text: |
      GROUP BY auf CASE-Ergebnis. ORDER BY MIN(seiten) damit Stufen aufsteigend kommen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher nach Längenstufe

Längen-Klasse + Anzahl, kurze zuerst.
