---
schema_version: 1
id: s076-cumsum-bestellungen
revision: 1
titel: "Shop: Kumulative Bestellzahl pro Tag"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [window-function, sum-over, cumsum]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: shop
schema_hinweis: |
  kategorien(id, name)
  produkte(id, name, kategorie_id, preis, lager, marke)
  kunden(id, name, ort, plz, alter_jahre)
  bestellungen(id, kunde_id, bestellt_am, status)
  bestellpositionen(bestellung_id, produkt_id, menge, einzelpreis)
erwartete_spalten: ["bestellt_am", "tag", "kumulativ"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03-10", 1, 1]
  - ["2025-03-25", 1, 2]
  - ["2025-03-30", 1, 3]
  - ["2025-04-01", 1, 4]
  - ["2025-04-02", 1, 5]
  - ["2025-04-05", 1, 6]
  - ["2025-04-08", 1, 7]
  - ["2025-04-10", 1, 8]
  - ["2025-04-12", 1, 9]
  - ["2025-04-14", 1, 10]
  - ["2025-04-15", 1, 11]
  - ["2025-04-18", 1, 12]
  - ["2025-04-19", 1, 13]
  - ["2025-04-20", 1, 14]
  - ["2025-04-21", 1, 15]
  - ["2025-04-22", 1, 16]
hints:
  - kosten: 0
    text: |
      `SUM(...) OVER (ORDER BY ...)` ergibt fortlaufende Summe. Kombiniert mit GROUP BY.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kumulative Bestellzahl

Pro Tag: Tagsumme und kumulative Summe seit Anfang.
