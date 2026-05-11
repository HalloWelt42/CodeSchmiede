---
schema_version: 1
id: 289-tier-laute
revision: 1
titel: Tier-Hierarchie mit Vererbung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 35
schaetz_minuten: 15
tags: [oop, vererbung, polymorphismus, klassen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Vererbungs-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: tier_konzert
hints:
  - kosten: 0
    text: |
      Tiere mit Lauten: Hund -> "Wuff", Katze -> "Miau",
      Kuh -> "Muh", Hahn -> "Kikeriki".
      Liste von Tier-Strings (z.B. ["Hund", "Katze", "Kuh"]) →
      Liste der Laute (["Wuff", "Miau", "Muh"]).
      Unbekannte Tiere → "?".
  - kosten: 20
    text: |
      Basis-Klasse Tier mit Methode laut() (default "?").
      Subklassen Hund/Katze/Kuh/Hahn ueberschreiben laut().
      Dispatch via Dict {"Hund": Hund, ...}.
tests_sichtbar:
  - input: [["Hund", "Katze", "Kuh"]]
    expected: ["Wuff", "Miau", "Muh"]
  - input: [[]]
    expected: []
  - input: [["Hahn"]]
    expected: ["Kikeriki"]
  - input: [["Drachen"]]
    expected: ["?"]
tests_versteckt:
  - input: [["Hund", "Hund", "Hund"]]
    expected: ["Wuff", "Wuff", "Wuff"]
  - input: [["Katze", "Drachen", "Hahn"]]
    expected: ["Miau", "?", "Kikeriki"]
  - input: [["Hahn", "Hund", "Katze", "Kuh"]]
    expected: ["Kikeriki", "Wuff", "Miau", "Muh"]
  - input: [["Maus"]]
    expected: ["?"]
  - input: [["Kuh", "Kuh", "Kuh"]]
    expected: ["Muh", "Muh", "Muh"]
starter_code: |
  def tier_konzert(tiere: list[str]) -> list[str]:
      # Tipp: Basis-Klasse Tier, Subklassen Hund/Katze/Kuh/Hahn
      pass
---

# Tier-Hierarchie mit Vererbung

Implementiere `tier_konzert(tiere)` -- eine Liste von Tier-Strings
wird in eine Liste der **Laute** umgewandelt.

| Tier        | Laut       |
|-------------|------------|
| `"Hund"`    | `"Wuff"`   |
| `"Katze"`   | `"Miau"`   |
| `"Kuh"`     | `"Muh"`    |
| `"Hahn"`    | `"Kikeriki"` |
| sonst       | `"?"`      |

## Beispiele

| Eingabe                       | Ausgabe                              |
|-------------------------------|--------------------------------------|
| `["Hund","Katze","Kuh"]`      | `["Wuff","Miau","Muh"]`              |
| `["Hahn"]`                    | `["Kikeriki"]`                       |
| `["Katze","Drachen","Hahn"]`  | `["Miau","?","Kikeriki"]`            |
| `[]`                          | `[]`                                 |

## Idee -- Vererbung mit Polymorphismus

```python
class Tier:
    def laut(self):
        return "?"


class Hund(Tier):
    def laut(self):
        return "Wuff"


class Katze(Tier):
    def laut(self):
        return "Miau"


class Kuh(Tier):
    def laut(self):
        return "Muh"


class Hahn(Tier):
    def laut(self):
        return "Kikeriki"


KLASSEN = {"Hund": Hund, "Katze": Katze, "Kuh": Kuh, "Hahn": Hahn}


def tier_konzert(tiere):
    return [KLASSEN.get(name, Tier)().laut() for name in tiere]
```

## Konzepte hier

1. **Vererbung**: Hund ist ein Tier. `class Hund(Tier)` bedeutet
   "Hund erbt alles von Tier".
2. **Methoden ueberschreiben**: jede Subklasse hat eigenes `laut()`.
3. **Polymorphismus**: `tier.laut()` ruft die Methode der **realen
   Klasse**, egal welche Variable du hast.
4. **Default-Verhalten**: `Tier.laut()` liefert "?" -- praktischer
   Fallback fuer unbekannte Subklassen.

## Vergleich -- Dict ohne Klassen

```python
LAUTE = {"Hund": "Wuff", "Katze": "Miau", "Kuh": "Muh", "Hahn": "Kikeriki"}

def tier_konzert(tiere):
    return [LAUTE.get(t, "?") for t in tiere]
```

Funktioniert genauso. Der Punkt der OOP-Variante ist die
**Erweiterbarkeit**: wenn ein Tier zusaetzlich `groesse()`,
`alter()`, `frisst(was)` koennen soll, profitiert man von der
Hierarchie.

## Anwendung

Klassen-Hierarchien tauchen ueberall auf, wo Dinge **gleichartig
aber unterschiedlich** sind: UI-Widgets (Button/Input/Slider sind
alle Widgets), Spielfiguren, Geometrie-Formen (siehe Aufgabe 290).
