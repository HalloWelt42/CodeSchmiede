---
schema_version: 1
id: 160-zinseszins
revision: 1
titel: Zinseszins-Berechnung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [mathematik, finanzen, runden]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Finanz-Mathematik
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zinseszins
hints:
  - kosten: 0
    text: |
      Berechne den Endwert eines Kapitals nach n Jahren bei jaehrlicher
      Verzinsung. zinssatz_prozent ist eine Zahl wie 5 für 5%.
      Liefere auf 2 Nachkommastellen gerundet.
  - kosten: 10
    text: |
      Formel: K_n = K_0 * (1 + p/100)^n.
      Mit pow() oder ** ist beides moeglich.
      round(..., 2) am Ende.
tests_sichtbar:
  - input: [1000.0, 5.0, 1]
    expected: 1050.0
  - input: [1000.0, 5.0, 2]
    expected: 1102.5
  - input: [1000.0, 5.0, 0]
    expected: 1000.0
  - input: [0.0, 5.0, 10]
    expected: 0.0
tests_versteckt:
  - input: [1000.0, 0.0, 10]
    expected: 1000.0
  - input: [100.0, 10.0, 5]
    expected: 161.05
  - input: [10000.0, 3.0, 10]
    expected: 13439.16
  - input: [1.0, 100.0, 10]
    expected: 1024.0
  - input: [500.0, 2.5, 7]
    expected: 594.34
  - input: [1000.0, -5.0, 2]
    expected: 902.5
starter_code: |
  def zinseszins(kapital: float, zinssatz_prozent: float, jahre: int) -> float:
      # Deine Lösung hier -- auf 2 Nachkommastellen runden
      pass
---

# Zinseszins-Berechnung

Schreibe eine Funktion `zinseszins(kapital, zinssatz_prozent, jahre)`,
die den **Endwert** eines Kapitals nach `jahre` Jahren jaehrlicher
Verzinsung berechnet. Liefere auf **2 Nachkommastellen gerundet**.

## Formel

$$K_n = K_0 \cdot \left(1 + \frac{p}{100}\right)^n$$

mit `K_0` = Anfangskapital, `p` = Zinssatz in Prozent, `n` = Jahre.

## Beispiele

| Kapital | Zins | Jahre | Endwert    |
|---------|------|-------|------------|
| `1000`  | `5%` | `1`   | `1050.00`  |
| `1000`  | `5%` | `2`   | `1102.50`  |
| `100`   | `10%`| `5`   | `161.05`   |
| `10000` | `3%` | `10`  | `13439.16` |
| `1`     | `100%`|`10`  | `1024.00`  |

## Idee

```python
def zinseszins(kapital, zinssatz_prozent, jahre):
    return round(kapital * (1 + zinssatz_prozent / 100) ** jahre, 2)
```

## Beobachtung -- Verdopplungs-Faustregel

Bei einem Zinssatz `p` verdoppelt sich Kapital nach etwa `72/p` Jahren
(genauer: `ln(2)/ln(1 + p/100)`). Bei 5% also ca. 14,4 Jahre.

## Hintergrund

Zinseszins war historisch eine **moralisch umstrittene** Erfindung --
der Glaube verbot Zinseszins (Wucher). Heute ist er die Grundlage
nahezu aller langfristigen Geldanlagen, von Sparbüchern bis zu
Investmentfonds.
