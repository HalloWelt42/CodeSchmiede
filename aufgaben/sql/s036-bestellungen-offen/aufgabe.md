---
schema_version: 1
id: s036-bestellungen-offen
revision: 1
titel: "Shop: offene Bestellungen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, string]
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
  - [16, 12, "2025-04-19"]
  - [4, 2, "2025-04-20"]
  - [12, 8, "2025-04-21"]
hints:
  - kosten: 0
    text: |
      `WHERE status = 'offen'`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Shop: offene Bestellungen

ID + Kunde + Datum aller noch offenen Bestellungen.
