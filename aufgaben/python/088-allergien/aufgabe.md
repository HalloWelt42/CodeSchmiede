---
schema_version: 1
id: 088-allergien
revision: 1
titel: Allergien aus Bitfeld lesen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 9
tags: [zahlen, bitfeld, listen]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (allergies), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: allergien
hints:
  - kosten: 0
    text: |
      Jede Allergie hat einen Bit-Wert: Eier=1, Erdnuesse=2, Schalentiere=4,
      Erdbeeren=8, Tomaten=16, Schokolade=32, Pollen=64, Katzen=128.
      Bit-AND `score & wert` testet ob Allergie vorhanden.
  - kosten: 15
    text: |
      Liste der Allergien in fester Reihenfolge. Pro Eintrag testen,
      ob das entsprechende Bit gesetzt ist. Höhere Bits (>=256)
      werden ignoriert.
tests_sichtbar:
  - input: [0]
    expected: []
  - input: [1]
    expected: ["eier"]
  - input: [5]
    expected: ["eier", "schalentiere"]
  - input: [255]
    expected: ["eier", "erdnuesse", "schalentiere", "erdbeeren", "tomaten", "schokolade", "pollen", "katzen"]
tests_versteckt:
  - input: [256]
    expected: []
  - input: [257]
    expected: ["eier"]
  - input: [509]
    expected: ["eier", "schalentiere", "erdbeeren", "tomaten", "schokolade", "pollen", "katzen"]
  - input: [11]
    expected: ["eier", "erdnuesse", "erdbeeren"]
  - input: [128]
    expected: ["katzen"]
starter_code: |
  def allergien(score: int) -> list[str]:
      # Deine Lösung hier -- Bit-Felder dekodieren.
      # Reihenfolge: eier, erdnuesse, schalentiere, erdbeeren,
      # tomaten, schokolade, pollen, katzen.
      pass
---

# Allergien aus Bitfeld lesen

In einem alten medizinischen System sind Allergien eines Patienten
als **einzelne Zahl** kodiert -- ein Bitfeld. Schreibe eine Funktion
`allergien(score)`, die die Liste der Allergien zurückgibt.

## Bit-Werte

| Bit | Wert | Allergie       |
|-----|------|----------------|
| 0   | 1    | `eier`         |
| 1   | 2    | `erdnuesse`    |
| 2   | 4    | `schalentiere` |
| 3   | 8    | `erdbeeren`    |
| 4   | 16   | `tomaten`      |
| 5   | 32   | `schokolade`   |
| 6   | 64   | `pollen`       |
| 7   | 128  | `katzen`       |

Höhere Bits ($\ge 256$) werden ignoriert.

## Beispiele

| Score | Allergien                                        |
|-------|--------------------------------------------------|
| `0`   | `[]`                                             |
| `1`   | `["eier"]`                                       |
| `5`   | `["eier", "schalentiere"]` (1+4)                 |
| `255` | alle 8                                           |
| `257` | `["eier"]` (1+256, 256 wird ignoriert)           |

## Hintergrund

Bitfelder waren früher Standard für **kompakte Speicher**. Heute
nutzen wir oft Sets oder Listen, aber für Embedded-Systeme oder
Datenbank-Flags ist die Bit-Variante immer noch verbreitet.
