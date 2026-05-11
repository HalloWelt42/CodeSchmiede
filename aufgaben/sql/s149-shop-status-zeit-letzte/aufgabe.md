---
schema_version: 1
id: s149-shop-status-zeit-letzte
revision: 1
titel: "Shop: zuletzt gelieferte Bestellung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, order, limit]
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
erwartete_spalten: ["id", "kunde_id", "bestellt_am"]
sortierung_egal: false
erwartetes_ergebnis:
  - [9, 5, "2025-04-18"]
hints:
  - kosten: 0
    text: |
      WHERE + ORDER DESC + LIMIT 1.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Zuletzt gelieferte Bestellung

Eine Zeile -- die jüngste gelieferte Bestellung.
