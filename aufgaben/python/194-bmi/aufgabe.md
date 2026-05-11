---
schema_version: 1
id: 194-bmi
revision: 1
titel: Body-Mass-Index (BMI) und Kategorie
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [mathematik, gesundheit, runden, klassifikation]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Gesundheits-Formel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bmi_klasse
hints:
  - kosten: 0
    text: |
      Berechne BMI = gewicht_kg / groesse_m^2 und klassifiziere:
      <18.5 → "untergewicht"
      18.5-24.9 → "normal"
      25.0-29.9 → "uebergewicht"
      >=30 → "adipositas"
      Bei groesse <= 0 oder gewicht <= 0 → "ungueltig".
  - kosten: 10
    text: |
      Schwellen sauber pruefen. round(bmi, 1) erst danach.
      Reihenfolge der Vergleiche so, dass sie schluessig ist.
tests_sichtbar:
  - input: [70, 1.75]
    expected: "normal"
  - input: [50, 1.75]
    expected: "untergewicht"
  - input: [85, 1.75]
    expected: "uebergewicht"
  - input: [100, 1.75]
    expected: "adipositas"
tests_versteckt:
  - input: [56, 1.7]
    expected: "normal"
  - input: [70, 1.6]
    expected: "uebergewicht"
  - input: [120, 1.8]
    expected: "adipositas"
  - input: [40, 1.7]
    expected: "untergewicht"
  - input: [70, 0]
    expected: "ungueltig"
  - input: [-50, 1.7]
    expected: "ungueltig"
  - input: [60, 1.5]
    expected: "uebergewicht"
  - input: [76.5, 1.8]
    expected: "normal"
starter_code: |
  def bmi_klasse(gewicht_kg: float, groesse_m: float) -> str:
      # Deine Lösung hier
      pass
---

# Body-Mass-Index (BMI) und Kategorie

Schreibe `bmi_klasse(gewicht_kg, groesse_m)`, die den Body-Mass-Index
berechnet und einer Kategorie zuordnet.

## Formel

$$BMI = \frac{Gewicht_\text{kg}}{Groesse_\text{m}^2}$$

## Klassen (WHO-Schema)

| BMI            | Kategorie         |
|----------------|-------------------|
| < 18.5         | `"untergewicht"`  |
| 18.5 – 24.99   | `"normal"`        |
| 25.0 – 29.99   | `"uebergewicht"`  |
| ≥ 30           | `"adipositas"`    |

Bei ungueltigen Eingaben (`groesse_m <= 0` oder `gewicht_kg <= 0`)
→ `"ungueltig"`.

## Beispiele

| Gewicht | Groesse | BMI   | Klasse           |
|---------|---------|-------|------------------|
| `70`    | `1.75`  | `22.9`| `"normal"`       |
| `50`    | `1.75`  | `16.3`| `"untergewicht"` |
| `85`    | `1.75`  | `27.8`| `"uebergewicht"` |
| `100`   | `1.75`  | `32.7`| `"adipositas"`   |

## Idee

```python
def bmi_klasse(gewicht_kg, groesse_m):
    if gewicht_kg <= 0 or groesse_m <= 0:
        return "ungueltig"
    bmi = gewicht_kg / (groesse_m ** 2)
    if bmi < 18.5:
        return "untergewicht"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "uebergewicht"
    return "adipositas"
```

## Hintergrund

Die BMI-Formel wurde **1832** vom belgischen Mathematiker Adolphe
Quetelet als statistisches Mass entwickelt -- nicht als medizinische
Diagnose. Sie ignoriert **Muskel-Anteil** (Bodybuilder kommen oft
"adipoes" raus) und **Fettverteilung**. Trotzdem ist BMI als
**Bevoelkerungs-Indikator** weiterhin nuetzlich.
