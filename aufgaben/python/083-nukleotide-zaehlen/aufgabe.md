---
schema_version: 1
id: 083-nukleotide-zaehlen
revision: 1
titel: Nukleotide zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [strings, dict, biologie, count]
pfade: [python_bio]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (nucleotide-count), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: nukleotide_zaehlen
hints:
  - kosten: 0
    text: |
      Genau 4 erlaubte Buchstaben: A, C, G, T. Andere → ValueError als
      Wert (also `None` als Wert wenn ungültig). Hier: gib leeres
      Dict zurück, wenn ungültige Zeichen vorkommen.
  - kosten: 10
    text: |
      `set(dna) <= set("ACGT")` prüft Validität. Dann pro Buchstabe
      `dna.count(x)`.
tests_sichtbar:
  - input: [""]
    expected: { "A": 0, "C": 0, "G": 0, "T": 0 }
  - input: ["A"]
    expected: { "A": 1, "C": 0, "G": 0, "T": 0 }
  - input: ["GGGGGGGG"]
    expected: { "A": 0, "C": 0, "G": 8, "T": 0 }
  - input: ["AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"]
    expected: { "A": 20, "C": 12, "G": 17, "T": 21 }
tests_versteckt:
  - input: ["X"]
    expected: {}
  - input: ["AGXX"]
    expected: {}
  - input: ["ACGT"]
    expected: { "A": 1, "C": 1, "G": 1, "T": 1 }
  - input: ["ACGTACGT"]
    expected: { "A": 2, "C": 2, "G": 2, "T": 2 }
starter_code: |
  def nukleotide_zaehlen(dna: str) -> dict[str, int]:
      # Deine Lösung hier -- ungültige Zeichen → leeres Dict.
      pass
---

# Nukleotide zählen

Schreibe eine Funktion `nukleotide_zählen(dna)`, die zählt, wie oft
die vier DNA-Nukleotide **A, C, G, T** in einem String vorkommen.

Bei **ungültigen Zeichen** (alles außer A, C, G, T) gib ein **leeres
Dict** zurück.

## Beispiele

| Eingabe   | Ergebnis                              |
|-----------|---------------------------------------|
| `""`      | `{"A":0,"C":0,"G":0,"T":0}`           |
| `"A"`     | `{"A":1,"C":0,"G":0,"T":0}`           |
| `"GGGGGGGG"` | `{"A":0,"C":0,"G":8,"T":0}`        |
| `"X"`     | `{}` (ungültig)                       |
| `"AGXX"`  | `{}` (ungültig)                       |

## Hintergrund

DNA besteht aus vier **Nukleobasen**: Adenin (A), Cytosin (C),
Guanin (G), Thymin (T). Das Zählen ist die einfachste Bioinformatik-
Operation -- z.B. für **GC-Gehalt** der Genome.
