---
schema_version: 1
id: s130-shop-tagesreport
revision: 1
titel: "Shop: Tagesreport (Bestellungen + Umsatz)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [join, group-by, count-distinct, sum]
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
erwartete_spalten: ["tag", "bestellungen", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03-10", 1, 9.78]
  - ["2025-03-25", 1, 12.76]
  - ["2025-03-30", 1, 9.47]
  - ["2025-04-01", 1, 8.07]
  - ["2025-04-02", 1, 12.66]
  - ["2025-04-05", 1, 7.97]
  - ["2025-04-08", 1, 7.88]
  - ["2025-04-10", 1, 3.69]
  - ["2025-04-12", 1, 6.94]
  - ["2025-04-14", 1, 12.47]
  - ["2025-04-15", 1, 7.77]
  - ["2025-04-18", 1, 4.87]
  - ["2025-04-19", 1, 3.28]
  - ["2025-04-20", 1, 3.87]
  - ["2025-04-21", 1, 6.56]
  - ["2025-04-22", 1, 2.2]
hints:
  - kosten: 0
    text: |
      GROUP BY auf Bestelldatum, COUNT DISTINCT auf Bestellung-ID.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Tagesreport

Pro Tag: Datum, Anzahl Bestellungen, Gesamtumsatz, chronologisch.
