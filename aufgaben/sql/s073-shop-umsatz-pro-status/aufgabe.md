---
schema_version: 1
id: s073-shop-umsatz-pro-status
revision: 1
titel: "Shop: Umsatz pro Bestellstatus"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, sum]
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
erwartete_spalten: ["status", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["geliefert", 76.21]
  - ["versandt", 28.12]
  - ["offen", 13.71]
  - ["storniert", 2.2]
hints:
  - kosten: 0
    text: |
      JOIN bestellpositionen <-> bestellungen, dann GROUP BY status.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Umsatz pro Bestellstatus

Status + Gesamtumsatz, hoechster zuerst.
