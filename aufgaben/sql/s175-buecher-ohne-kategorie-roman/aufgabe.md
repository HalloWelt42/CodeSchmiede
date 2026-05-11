---
schema_version: 1
id: s175-buecher-ohne-kategorie-roman
revision: 1
titel: "Bücher: alle außer Roman"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [where, not-equal]
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
erwartete_spalten: ["titel", "kategorie"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die Welt von Gestern", "Biographie"]
  - ["Die Verwandlung", "Erzählung"]
  - ["Schachnovelle", "Erzählung"]
  - ["Erdsee", "Fantasy"]
  - ["Drachenreiter", "Kinderbuch"]
  - ["Karlsson vom Dach", "Kinderbuch"]
  - ["Pippi Langstrumpf", "Kinderbuch"]
  - ["Tintenherz", "Kinderbuch"]
  - ["Die linke Hand der Dunkelheit", "Sci-Fi"]
hints:
  - kosten: 0
    text: |
      WHERE kategorie != 'Roman'.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher außer Romane

Titel + Kategorie aller Nicht-Roman-Bücher.
