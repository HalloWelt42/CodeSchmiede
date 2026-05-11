---
schema_version: 1
id: 103-bier-lied
revision: 1
titel: Bier-Lied generieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 8
tags: [strings, schleifen, format, gesang]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (beer-song), eigene Formulierung mit deutschem Text
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bier_strophe
hints:
  - kosten: 0
    text: |
      Eine Strophe besteht aus 2 Zeilen, getrennt durch \n. Beispiel
      für n=99: "99 Flaschen Bier auf der Wand, 99 Flaschen Bier.\nNimm eine runter, gib sie rum, 98 Flaschen Bier auf der Wand."
  - kosten: 8
    text: |
      Sonderfaelle:
      - n = 1: "1 Flasche..." (Singular), nächste = 0 → "keine mehr Flaschen"
      - n = 0: "Keine Flaschen Bier auf der Wand, keine Flaschen Bier.\nGeh in den Laden, kauf neues, 99 Flaschen Bier auf der Wand."
tests_sichtbar:
  - input: [99]
    expected: "99 Flaschen Bier auf der Wand, 99 Flaschen Bier.\nNimm eine runter, gib sie rum, 98 Flaschen Bier auf der Wand."
  - input: [3]
    expected: "3 Flaschen Bier auf der Wand, 3 Flaschen Bier.\nNimm eine runter, gib sie rum, 2 Flaschen Bier auf der Wand."
  - input: [2]
    expected: "2 Flaschen Bier auf der Wand, 2 Flaschen Bier.\nNimm eine runter, gib sie rum, 1 Flasche Bier auf der Wand."
  - input: [1]
    expected: "1 Flasche Bier auf der Wand, 1 Flasche Bier.\nNimm sie runter, gib sie rum, keine Flaschen Bier auf der Wand."
tests_versteckt:
  - input: [0]
    expected: "Keine Flaschen Bier auf der Wand, keine Flaschen Bier.\nGeh in den Laden, kauf neues, 99 Flaschen Bier auf der Wand."
  - input: [50]
    expected: "50 Flaschen Bier auf der Wand, 50 Flaschen Bier.\nNimm eine runter, gib sie rum, 49 Flaschen Bier auf der Wand."
  - input: [10]
    expected: "10 Flaschen Bier auf der Wand, 10 Flaschen Bier.\nNimm eine runter, gib sie rum, 9 Flaschen Bier auf der Wand."
starter_code: |
  def bier_strophe(n: int) -> str:
      # Deine Lösung hier -- 2 Zeilen, getrennt durch \n.
      # Singular bei 1, Sonderfaelle bei 0 und 1.
      pass
---

# Bier-Lied generieren

Schreibe eine Funktion `bier_strophe(n)`, die eine **einzelne Strophe**
des Bier-Lieds liefert. Strophe = zwei Zeilen, getrennt durch `\n`.

## Format

Für n ≥ 2:
```
N Flaschen Bier auf der Wand, N Flaschen Bier.
Nimm eine runter, gib sie rum, N-1 Flaschen Bier auf der Wand.
```

Für n = 2 (nächste = 1, Singular):
```
2 Flaschen Bier auf der Wand, 2 Flaschen Bier.
Nimm eine runter, gib sie rum, 1 Flasche Bier auf der Wand.
```

Für n = 1 (Singular + "sie" + "keine"):
```
1 Flasche Bier auf der Wand, 1 Flasche Bier.
Nimm sie runter, gib sie rum, keine Flaschen Bier auf der Wand.
```

Für n = 0 (Reset):
```
Keine Flaschen Bier auf der Wand, keine Flaschen Bier.
Geh in den Laden, kauf neues, 99 Flaschen Bier auf der Wand.
```

## Hintergrund

"99 Bottles of Beer" ist ein Standard-Test für Sprach-Vergleiche
(siehe [99-bottles-of-beer.net](https://www.99-bottles-of-beer.net/))
-- über 1500 Sprach-Implementierungen sind dort gesammelt.
