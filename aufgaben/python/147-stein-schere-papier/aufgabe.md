---
schema_version: 1
id: 147-stein-schere-papier
revision: 1
titel: Stein, Schere, Papier
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [logik, dicts, vergleich, spiele]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Spiel-Beispiel für Vergleichs-Logik
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gewinner
hints:
  - kosten: 0
    text: |
      Bestimme den Gewinner zwischen zwei Zuegen:
      "stein", "schere", "papier". Liefere "spieler1", "spieler2"
      oder "unentschieden". Bei ungültiger Eingabe → "ungültig".
  - kosten: 10
    text: |
      Dictionary "schlaegt" abbilden: stein→schere, schere→papier,
      papier→stein. Prüfen ob z2 == schlaegt[z1] → spieler1 gewinnt.
tests_sichtbar:
  - input: ["stein", "schere"]
    expected: "spieler1"
  - input: ["schere", "stein"]
    expected: "spieler2"
  - input: ["stein", "stein"]
    expected: "unentschieden"
  - input: ["papier", "stein"]
    expected: "spieler1"
tests_versteckt:
  - input: ["schere", "papier"]
    expected: "spieler1"
  - input: ["papier", "schere"]
    expected: "spieler2"
  - input: ["stein", "papier"]
    expected: "spieler2"
  - input: ["schere", "schere"]
    expected: "unentschieden"
  - input: ["papier", "papier"]
    expected: "unentschieden"
  - input: ["stein", "feuer"]
    expected: "ungueltig"
  - input: ["", "stein"]
    expected: "ungueltig"
starter_code: |
  def gewinner(zug1: str, zug2: str) -> str:
      # Deine Lösung hier -- "spieler1"/"spieler2"/"unentschieden"/"ungueltig"
      pass
---

# Stein, Schere, Papier

Schreibe eine Funktion `gewinner(zug1, zug2)`, die den Sieger im
klassischen Spiel **Stein, Schere, Papier** bestimmt.

## Regeln

```
stein  schlaegt schere
schere schlaegt papier
papier schlaegt stein
```

Gleiche Zuege → `"unentschieden"`.
Unbekannte Zuege → `"ungültig"`.

## Beispiele

| Zug 1     | Zug 2     | Ergebnis          |
|-----------|-----------|-------------------|
| `stein`   | `schere`  | `"spieler1"`      |
| `schere`  | `stein`   | `"spieler2"`      |
| `stein`   | `stein`   | `"unentschieden"` |
| `papier`  | `stein`   | `"spieler1"`      |
| `stein`   | `feuer`   | `"ungültig"`     |

## Idee -- Schlag-Tabelle als Dict

```python
SCHLAEGT = {"stein": "schere", "schere": "papier", "papier": "stein"}

def gewinner(zug1, zug2):
    if zug1 not in SCHLAEGT or zug2 not in SCHLAEGT:
        return "ungültig"
    if zug1 == zug2:
        return "unentschieden"
    return "spieler1" if SCHLAEGT[zug1] == zug2 else "spieler2"
```

## Erweiterung -- Stein-Schere-Papier-Echse-Spock

Sheldon Coopers Lieblings-Variante hat 5 Zuege und 10 Schlag-Beziehungen.
Mit dem gleichen Dict-Pattern bleibt der Code trotzdem überschaubar.
