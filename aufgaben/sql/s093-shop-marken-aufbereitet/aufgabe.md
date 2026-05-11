---
schema_version: 1
id: s093-shop-marken-aufbereitet
revision: 1
titel: "Shop: Marken mit Großbuchstaben"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [string, upper, distinct]
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
erwartete_spalten: ["marke", "marke_gross"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Alpenglück", "ALPENGLüCK"]
  - ["AquaPur", "AQUAPUR"]
  - ["Bauernbäckerei", "BAUERNBäCKEREI"]
  - ["Bio-Hof Schulz", "BIO-HOF SCHULZ"]
  - ["BlubberCo", "BLUBBERCO"]
  - ["Citrus Plus", "CITRUS PLUS"]
  - ["FruchtFest", "FRUCHTFEST"]
  - ["GartenFrisch", "GARTENFRISCH"]
  - ["KakaoLuxus", "KAKAOLUXUS"]
  - ["KekseRoll", "KEKSEROLL"]
  - ["KäseHof", "KäSEHOF"]
  - ["Pariser Art", "PARISER ART"]
  - ["Tropico", "TROPICO"]
hints:
  - kosten: 0
    text: |
      DISTINCT + UPPER.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Marken klein + groß

Jede Marke mit Original-Schreibweise und UPPERCASE-Variante.
