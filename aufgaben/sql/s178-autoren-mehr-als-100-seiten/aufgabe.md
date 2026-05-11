---
schema_version: 1
id: s178-autoren-mehr-als-100-seiten
revision: 1
titel: "Autoren mit Durchschnitt > 200 Seiten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, having, avg]
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
erwartete_spalten: ["name", "schnitt"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Thomas Mann", 875.5]
  - ["Cornelia Funke", 504.0]
  - ["Haruki Murakami", 460.0]
  - ["Jane Austen", 453.0]
  - ["Stefan Zweig", 312.0]
  - ["Ursula K. Le Guin", 264.0]
  - ["Hermann Hesse", 220.5]
  - ["George Orwell", 219.0]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY + HAVING AVG(seiten) > 200.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Schreib-mächtige Autoren

Autoren mit Durchschnittsbuch > 200 Seiten.
