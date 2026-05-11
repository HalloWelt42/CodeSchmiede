---
schema_version: 1
id: 185-text-justify
revision: 1
titel: Text auf feste Breite ausrichten (links, rechts, Block)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [strings, formatierung, slicing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Format-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ausrichten
hints:
  - kosten: 0
    text: |
      Richte "text" auf "breite" Zeichen aus -- mit Modus
      "links", "rechts" oder "zentriert". Mit Leerzeichen aufgefüllt.
      Wenn text laenger als breite -> text unverändert zurückgeben.
  - kosten: 10
    text: |
      str.ljust/rjust/center machen das fertig. Aber Achtung:
      bei text laenger als breite müssen alle drei das Original liefern.
tests_sichtbar:
  - input: ["Hi", 5, "links"]
    expected: "Hi   "
  - input: ["Hi", 5, "rechts"]
    expected: "   Hi"
  - input: ["Hi", 5, "zentriert"]
    expected: "  Hi "
  - input: ["Hallo", 3, "links"]
    expected: "Hallo"
tests_versteckt:
  - input: ["a", 7, "zentriert"]
    expected: "   a   "
  - input: ["", 4, "links"]
    expected: "    "
  - input: ["", 4, "rechts"]
    expected: "    "
  - input: ["", 4, "zentriert"]
    expected: "    "
  - input: ["Wort", 4, "links"]
    expected: "Wort"
  - input: ["Wort", 10, "rechts"]
    expected: "      Wort"
starter_code: |
  def ausrichten(text: str, breite: int, modus: str) -> str:
      # Deine Lösung hier -- "links" / "rechts" / "zentriert"
      pass
---

# Text auf feste Breite ausrichten

Schreibe `ausrichten(text, breite, modus)`, die einen Text mit
Leerzeichen auf eine feste Breite **bringt**:

- `"links"`: Text steht links, Leerzeichen rechts.
- `"rechts"`: Leerzeichen links, Text rechts.
- `"zentriert"`: Leerzeichen je halb links und rechts.

Wenn `text` laenger als `breite` ist → unverändert zurückgeben.

## Beispiele

| Text   | Breite | Modus       | Ergebnis    |
|--------|--------|-------------|-------------|
| `Hi`   | `5`    | `links`     | `"Hi   "`   |
| `Hi`   | `5`    | `rechts`    | `"   Hi"`   |
| `Hi`   | `5`    | `zentriert` | `"  Hi "`   |
| `a`    | `7`    | `zentriert` | `"   a   "` |
| `Hallo`| `3`    | `links`     | `"Hallo"`   |

Bei zentriert: wenn die Anzahl freier Stellen ungerade ist, ist
**links ein Zeichen mehr** (Pythons `str.center`-Konvention).

## Idee

`ljust`/`rjust`/`center` liefern den Originaltext unverändert
zurück, wenn er bereits `>= breite` ist -- genau wie gewuenscht.

## Anwendung

Ausrichten braucht man in **Tabellen-Druck** (CLI-Tools wie `top`,
`htop`), **Form-Builder**-Tools (Email-Newsletter) und beim
**Code-Pretty-Printing**.
