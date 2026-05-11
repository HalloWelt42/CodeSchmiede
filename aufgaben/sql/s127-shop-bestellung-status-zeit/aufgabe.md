---
schema_version: 1
id: s127-shop-bestellung-status-zeit
revision: 1
titel: "Shop: Bestellungen nach Status und Monat"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 7
tags: [group-by-multi, date]
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
erwartete_spalten: ["monat", "status", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2025-03", "geliefert", 3]
  - ["2025-04", "geliefert", 6]
  - ["2025-04", "offen", 3]
  - ["2025-04", "storniert", 1]
  - ["2025-04", "versandt", 3]
hints:
  - kosten: 0
    text: |
      GROUP BY auf Monat + Status.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen pro Monat und Status

Monat + Status + Anzahl, chronologisch dann alphabetisch.
