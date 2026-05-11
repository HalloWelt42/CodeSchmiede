---
schema_version: 1
id: s098-shop-vip-kunden
revision: 1
titel: "Shop: VIP-Kunden (über 30 EUR Umsatz)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [join, group-by, having]
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
erwartete_spalten: ["name", "umsatz"]
sortierung_egal: false
erwartetes_ergebnis:
  []
hints:
  - kosten: 0
    text: |
      JOINs + HAVING auf Aggregat-Summe.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# VIP-Kunden

Kunden mit Gesamtumsatz > 30 EUR -- Name + Umsatz, hoechste zuerst.
