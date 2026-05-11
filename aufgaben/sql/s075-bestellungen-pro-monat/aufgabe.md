---
schema_version: 1
id: s075-bestellungen-pro-monat
revision: 1
titel: "Shop: Bestellungen pro Monat"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [date, strftime, group-by]
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
erwartete_spalten: ["monat", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03", 3]
  - ["2025-04", 13]
hints:
  - kosten: 0
    text: |
      `strftime('%Y-%m', datum)` ergibt z.B. '2025-04'.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen pro Monat

Monat (YYYY-MM) + Anzahl Bestellungen, chronologisch.
