---
schema_version: 1
id: s044-replace-petrol
revision: 1
titel: "Marken ohne 'Hof'"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [string, replace, distinct]
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
erwartete_spalten: ["marke_kurz"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Alpenglück"]
  - ["AquaPur"]
  - ["Bauernbäckerei"]
  - ["Bio Schulz"]
  - ["BlubberCo"]
  - ["Citrus Plus"]
  - ["FruchtFest"]
  - ["GartenFrisch"]
  - ["KakaoLuxus"]
  - ["KekseRoll"]
  - ["KäseHof"]
  - ["Pariser Art"]
  - ["Tropico"]
hints:
  - kosten: 0
    text: |
      `REPLACE(s, alt, neu)` ersetzt Vorkommen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Marken ohne '-Hof'

Distinkte Marken-Namen, aus denen '-Hof' entfernt wurde, sortiert.
