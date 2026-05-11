---
schema_version: 1
id: s139-ausleihen-pro-leser-und-kategorie
revision: 1
titel: "Ausleihen pro Leser und Kategorie"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [join, group-by-multi]
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
erwartete_spalten: ["name", "kategorie", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt", "Roman", 2]
  - ["Bernd Mueller", "Roman", 2]
  - ["Clara Weber", "Kinderbuch", 3]
  - ["David Fischer", "Roman", 1]
  - ["Eva Schulz", "Biographie", 1]
  - ["Eva Schulz", "Erzählung", 1]
  - ["Eva Schulz", "Roman", 1]
  - ["Felix Bauer", "Roman", 1]
  - ["Greta Hoffmann", "Kinderbuch", 2]
  - ["Hans Wagner", "Roman", 2]
  - ["Ines Becker", "Roman", 2]
  - ["Jonas Schaefer", "Fantasy", 1]
  - ["Jonas Schaefer", "Sci-Fi", 1]
  - ["Karin Koehler", "Roman", 1]
  - ["Lukas Richter", "Erzählung", 1]
  - ["Lukas Richter", "Roman", 1]
  - ["Maria Klein", "Roman", 2]
  - ["Niklas Wolf", "Roman", 1]
  - ["Olivia Krueger", "Roman", 1]
hints:
  - kosten: 0
    text: |
      GROUP BY Leser + Kategorie.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Ausleihen pro Leser-Kategorie

Leser, Kategorie, Anzahl -- pro Leser dann meiste Ausleihen.
