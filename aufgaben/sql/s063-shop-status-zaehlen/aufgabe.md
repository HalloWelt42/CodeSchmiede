---
schema_version: 1
id: s063-shop-status-zaehlen
revision: 1
titel: "Shop: Bestellungen nach Status"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [group-by, count]
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
erwartete_spalten: ["status", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["geliefert", 9]
  - ["offen", 3]
  - ["storniert", 1]
  - ["versandt", 3]
hints:
  - kosten: 0
    text: |
      GROUP BY status, COUNT.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bestellungen nach Status

Wieviele Bestellungen pro Status, alphabetisch.
