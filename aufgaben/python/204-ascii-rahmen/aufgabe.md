---
schema_version: 1
id: 204-ascii-rahmen
revision: 1
titel: ASCII-Rahmen um Text
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [strings, formatierung, ascii-art]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische CLI-UI-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rahmen
hints:
  - kosten: 0
    text: |
      Umgib einen Text mit einem Rahmen aus + und - und |.
      Mehrere Zeilen werden auf die laengste gepolstert.
      Beispiel:
      "Hi" -> ["+----+", "| Hi |", "+----+"].
      Eingabe ist eine Liste von Zeilen.
  - kosten: 15
    text: |
      breite = max(len(z) for z in zeilen).
      Top/Bottom: "+" + "-" * (breite + 2) + "+".
      Pro Zeile: f"| {z.ljust(breite)} |".
tests_sichtbar:
  - input: [["Hi"]]
    expected: ["+----+", "| Hi |", "+----+"]
  - input: [["Hallo", "Welt"]]
    expected: ["+-------+", "| Hallo |", "| Welt  |", "+-------+"]
  - input: [[]]
    expected: ["++", "++"]
  - input: [[""]]
    expected: ["++", "||", "++"]
tests_versteckt:
  - input: [["A"]]
    expected: ["+---+", "| A |", "+---+"]
  - input: [["a", "bb", "ccc"]]
    expected: ["+-----+", "| a   |", "| bb  |", "| ccc |", "+-----+"]
  - input: [["Lorem", "ipsum", "dolor"]]
    expected: ["+-------+", "| Lorem |", "| ipsum |", "| dolor |", "+-------+"]
  - input: [["x"]]
    expected: ["+---+", "| x |", "+---+"]
  - input: [["123"]]
    expected: ["+-----+", "| 123 |", "+-----+"]
starter_code: |
  def rahmen(zeilen: list[str]) -> list[str]:
      # Deine Lösung hier -- Liste von Strings, jede Zeile ein Element
      pass
---

# ASCII-Rahmen um Text

Schreibe `rahmen(zeilen)`, die einen Text mit einem **Rahmen aus
+, - und |** umgibt. Eingabe und Ausgabe sind Listen von Strings
(je ein String pro Zeile).

## Beispiele

```
["Hi"]                ["Hallo", "Welt"]
+----+                +-------+
| Hi |                | Hallo |
+----+                | Welt  |
                      +-------+
```

Bei `[]` liefere `["++", "++"]` (leerer Rahmen).
Bei `[""]` liefere `["++", "||", "++"]`.

## Idee

```python
def rahmen(zeilen):
    if not zeilen:
        return ["++", "++"]
    breite = max(len(z) for z in zeilen)
    rand = "+" + "-" * (breite + 2) + "+" if breite > 0 else "++"
    out = [rand]
    for z in zeilen:
        if breite == 0:
            out.append("||")
        else:
            out.append(f"| {z.ljust(breite)} |")
    out.append(rand)
    return out
```

## Stolperstein -- alle Zeilen gleich lang

Damit der rechte Rand sauber bleibt, müssen kürzere Zeilen mit
Leerzeichen aufgefüllt werden. `str.ljust(breite)` macht das in
einer Zeile.

## Hintergrund

ASCII-Rahmen tauchen in CLI-Tools (Banner-Text), Code-Reviews
(Diff-Boxen), Drucker-Ausgaben und Retro-Spielen auf. Die
**Box-Drawing-Characters** in Unicode (`╔═╗║╚╝`) bieten schickere
Linien -- aber nicht jedes Terminal stellt sie korrekt dar.
