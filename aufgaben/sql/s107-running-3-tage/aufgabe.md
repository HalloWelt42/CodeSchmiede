---
schema_version: 1
id: s107-running-3-tage
revision: 1
titel: "Bestellungen: laufende 3er-Summe"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 12
tags: [window-function, rows-between, moving-sum]
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
erwartete_spalten: ["bestellt_am", "tag", "letzte3"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03-10", 1, 1]
  - ["2025-03-25", 1, 2]
  - ["2025-03-30", 1, 3]
  - ["2025-04-01", 1, 3]
  - ["2025-04-02", 1, 3]
  - ["2025-04-05", 1, 3]
  - ["2025-04-08", 1, 3]
  - ["2025-04-10", 1, 3]
  - ["2025-04-12", 1, 3]
  - ["2025-04-14", 1, 3]
  - ["2025-04-15", 1, 3]
  - ["2025-04-18", 1, 3]
  - ["2025-04-19", 1, 3]
  - ["2025-04-20", 1, 3]
  - ["2025-04-21", 1, 3]
  - ["2025-04-22", 1, 3]
hints:
  - kosten: 0
    text: |
      `SUM(...) OVER (ORDER BY ... ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Laufende 3-Tage-Summe

Pro Tag: Anzahl Bestellungen + Summe der letzten 3 Tage (inkl. heute).
