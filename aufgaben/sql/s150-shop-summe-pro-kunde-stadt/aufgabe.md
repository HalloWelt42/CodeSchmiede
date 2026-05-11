---
schema_version: 1
id: s150-shop-summe-pro-kunde-stadt
revision: 1
titel: "Shop: Umsatz pro Stadt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, sum, group-by]
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
erwartete_spalten: ["ort", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Berlin", 32.25]
  - ["Hamburg", 26.31]
  - ["Köln", 17.63]
  - ["München", 13.86]
  - ["Leipzig", 12.47]
  - ["Frankfurt", 7.88]
  - ["Stuttgart", 6.56]
  - ["Dresden", 3.28]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY ort + SUM.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Umsatz pro Stadt

Stadt + Gesamtumsatz, höchste zuerst.
