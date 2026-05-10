---
schema_version: 1
id: 077-hamming-distanz
revision: 1
titel: Hamming-Distanz
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [strings, vergleich, zip, schleifen]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Hamming-Abstand
  notiz: Inspiration aus Exercism (hamming), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: hamming_distanz
hints:
  - kosten: 0
    text: |
      Vergleiche Position für Position. Zähle, wo sich die Strings
      unterscheiden. Nur erlaubt für Strings gleicher Länge --
      sonst -1 zurückgeben.
  - kosten: 10
    text: |
      `sum(1 for a, b in zip(s1, s2) if a != b)` -- aber vorher
      Längen-Check.
tests_sichtbar:
  - input: ["GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"]
    expected: 7
  - input: ["A", "A"]
    expected: 0
  - input: ["GGACTGA", "GGACTGA"]
    expected: 0
  - input: ["", ""]
    expected: 0
tests_versteckt:
  - input: ["AT", "ATG"]
    expected: -1
  - input: ["AAAA", "TTTT"]
    expected: 4
  - input: ["A", "G"]
    expected: 1
  - input: ["GGACG", "GGTCG"]
    expected: 1
  - input: ["AAAAAAAAA", "AAAAAAAAA"]
    expected: 0
starter_code: |
  def hamming_distanz(a: str, b: str) -> int:
      # Deine Lösung hier -- Strings müssen gleich lang sein, sonst -1.
      pass
---

# Hamming-Distanz

Schreibe eine Funktion `hamming_distanz(a, b)`, die die **Hamming-Distanz**
zweier Strings zurückgibt -- die Anzahl der Positionen, an denen
sich die Strings unterscheiden.

Beide Strings müssen die **gleiche Länge** haben. Sonst gib `-1`
zurück.

## Beispiele

| String 1 | String 2 | Ergebnis |
|----------|----------|----------|
| `"GAGCCTACTAACGGGAT"` | `"CATCGTAATGACGGCCT"` | `7` |
| `"A"` | `"A"` | `0` |
| `""` | `""` | `0` |
| `"AT"` | `"ATG"` | `-1` |

## Hintergrund

Richard Hamming entwickelte das Konzept 1950 in den Bell Labs für
die Fehlererkennung in Datenübertragungen. In der **Bioinformatik**
ist es Standard, um zwei DNA- oder Protein-Sequenzen zu vergleichen.
