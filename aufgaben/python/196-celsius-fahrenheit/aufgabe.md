---
schema_version: 1
id: 196-celsius-fahrenheit
revision: 1
titel: Celsius nach Fahrenheit umrechnen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [mathematik, einheiten, runden]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Einheiten-Konvertierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: celsius_zu_fahrenheit
hints:
  - kosten: 0
    text: |
      F = C * 9/5 + 32. Auf 1 Nachkommastelle gerundet.
      Negative Werte muessen funktionieren (z.B. -40 → -40.0).
  - kosten: 10
    text: |
      round(c * 9 / 5 + 32, 1).
tests_sichtbar:
  - input: [0]
    expected: 32.0
  - input: [100]
    expected: 212.0
  - input: [-40]
    expected: -40.0
  - input: [37]
    expected: 98.6
tests_versteckt:
  - input: [-273.15]
    expected: -459.7
  - input: [25]
    expected: 77.0
  - input: [98.6]
    expected: 209.5
  - input: [-17.78]
    expected: 0.0
  - input: [50]
    expected: 122.0
  - input: [10.5]
    expected: 50.9
starter_code: |
  def celsius_zu_fahrenheit(c: float) -> float:
      # Deine Lösung hier -- 1 Nachkommastelle
      pass
---

# Celsius nach Fahrenheit umrechnen

Schreibe `celsius_zu_fahrenheit(c)`, die einen Wert in **Grad Celsius**
in **Grad Fahrenheit** umrechnet -- gerundet auf eine Nachkommastelle.

## Formel

$$F = C \cdot \frac{9}{5} + 32$$

## Beispiele

| Celsius   | Fahrenheit |
|-----------|------------|
| `0`       | `32.0`     |
| `100`     | `212.0`    |
| `-40`     | `-40.0`    |
| `37`      | `98.6`     |
| `-273.15` | `-459.7`   |
| `25`      | `77.0`     |

## Idee

```python
def celsius_zu_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)
```

## Spezialfall -40

`-40 °C = -40 °F` -- der einzige Wert, bei dem beide Skalen
identisch sind. Loesung der Gleichung
$x = x \cdot \frac{9}{5} + 32$ ergibt $x = -40$.

## Hintergrund

Daniel Gabriel Fahrenheit definierte 1724 seine Skala mit `0 °F`
als kaeltester von ihm reproduzierbarer Temperatur (Eis-Salz-Mischung)
und `96 °F` als Koerpertemperatur. Heute gilt sie nur noch in den
USA, Liberia und Myanmar offiziell.
