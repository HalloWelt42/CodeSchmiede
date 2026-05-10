---
schema_version: 1
id: 082-rna-transkription
revision: 1
titel: DNA zu RNA umwandeln
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [strings, dict, biologie]
pfade: [python_bio]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Transkription_(Biologie)
  notiz: Inspiration aus Exercism (rna-transcription), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: zu_rna
hints:
  - kosten: 0
    text: |
      Tausch: G→C, C→G, T→A, A→U. Andere Zeichen bleiben (oder werfen
      einen Fehler -- hier: bleiben).
  - kosten: 10
    text: |
      `str.translate(str.maketrans("GCTA", "CGAU"))` ist ein Einzeiler.
tests_sichtbar:
  - input: ["G"]
    expected: "C"
  - input: ["C"]
    expected: "G"
  - input: ["T"]
    expected: "A"
  - input: ["A"]
    expected: "U"
tests_versteckt:
  - input: ["GCTA"]
    expected: "CGAU"
  - input: ["ACGTGGTCTTAA"]
    expected: "UGCACCAGAAUU"
  - input: [""]
    expected: ""
starter_code: |
  def zu_rna(dna: str) -> str:
      # Deine Lösung hier -- G->C, C->G, T->A, A->U.
      pass
---

# DNA zu RNA umwandeln

Schreibe eine Funktion `zu_rna(dna)`, die eine DNA-Sequenz in die
**komplementäre RNA-Sequenz** umwandelt.

## Tausch-Regel

| DNA | RNA |
|-----|-----|
| G   | C   |
| C   | G   |
| T   | A   |
| A   | U   |

## Beispiele

| Eingabe          | Ergebnis        |
|------------------|-----------------|
| `"G"`            | `"C"`           |
| `"GCTA"`         | `"CGAU"`        |
| `"ACGTGGTCTTAA"` | `"UGCACCAGAAUU"` |

## Hintergrund

Bei der **Transkription** in der Zelle wird die DNA-Sequenz in
mRNA umgeschrieben. Statt **Thymin (T)** wird in der RNA **Uracil (U)**
verbaut. Bioinformatik-Tools machen genau diese Umwandlung
millionenfach pro Sekunde.
