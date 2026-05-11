---
schema_version: 1
id: 295-csv-zeile
revision: 1
titel: CSV-Zeile mit Quoting parsen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [strings, csv, parsing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische CSV-Aufgabe (vereinfacht)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: csv_zeile
hints:
  - kosten: 0
    text: |
      Parse eine CSV-Zeile (Komma-getrennt) zu Liste von Strings.
      Felder in DOPPELTEN ANFUEHRUNGSZEICHEN duerfen Kommas enthalten.
      Quotes selbst werden NICHT in Felder uebernommen.
      Bsp: '1,"Hallo, Welt",3' → ["1", "Hallo, Welt", "3"].
  - kosten: 25
    text: |
      Modul csv.reader([s]) macht das exakt nach RFC 4180.
      Liefer-Form: list(csv.reader([s]))[0].
tests_sichtbar:
  - input: ["a,b,c"]
    expected: ["a", "b", "c"]
  - input: ['1,"Hallo, Welt",3']
    expected: ["1", "Hallo, Welt", "3"]
  - input: [""]
    expected: []
  - input: ['"einzeln"']
    expected: ["einzeln"]
tests_versteckt:
  - input: ['a,"b,c",d']
    expected: ["a", "b,c", "d"]
  - input: ["1,2,3,4,5"]
    expected: ["1", "2", "3", "4", "5"]
  - input: ['"a","b","c"']
    expected: ["a", "b", "c"]
  - input: ["solo"]
    expected: ["solo"]
  - input: ['"mit, drei, kommas"']
    expected: ["mit, drei, kommas"]
  - input: ["a,,b"]
    expected: ["a", "", "b"]
  - input: [",,"]
    expected: ["", "", ""]
starter_code: |
  import csv

  def csv_zeile(s: str) -> list[str]:
      # Tipp: csv.reader([s]) macht das exakt nach Standard
      pass
---

# CSV-Zeile mit Quoting parsen

Schreibe `csv_zeile(s)`, die eine CSV-Zeile (Komma-getrennt) in eine
Liste von Strings umwandelt.

Quoting-Regel:
- Felder in **doppelten Anfuehrungszeichen** duerfen Kommas enthalten.
- Die Quotes selbst werden **nicht** in die Felder uebernommen.
- Leere Felder (zwischen zwei Kommas) → `""`.
- Leerer Eingabe-String → `[]`.

## Beispiele

| Eingabe                       | Ergebnis                          |
|-------------------------------|------------------------------------|
| `"a,b,c"`                     | `["a", "b", "c"]`                 |
| `'1,"Hallo, Welt",3'`         | `["1", "Hallo, Welt", "3"]`       |
| `'a,"b,c",d'`                 | `["a", "b,c", "d"]`               |
| `'"a","b","c"'`               | `["a", "b", "c"]`                 |
| `"a,,b"`                      | `["a", "", "b"]`                  |
| `"solo"`                      | `["solo"]`                        |
| `""`                          | `[]`                              |

## Idee mit `csv`-Modul

```python
import csv

def csv_zeile(s):
    if not s:
        return []
    return list(csv.reader([s]))[0]
```

Pythons `csv.reader` macht alles richtig -- inklusive
**escaped Quotes** (`""` innerhalb Quotes wird zu `"`),
Whitespace-Tolerieren etc.

`csv.reader` erwartet einen **Iterable von Zeilen** (z.B. eine
Datei). Wir geben `[s]` (Liste mit einer Zeile) und nehmen das
erste Ergebnis.

## Idee per Hand (lehrreich)

```python
def csv_zeile(s):
    if not s:
        return []
    out = []
    aktuell = ""
    in_quotes = False
    for c in s:
        if c == '"':
            in_quotes = not in_quotes
        elif c == "," and not in_quotes:
            out.append(aktuell)
            aktuell = ""
        else:
            aktuell += c
    out.append(aktuell)
    return out
```

Klassischer **State-Machine**-Parser. Pruefe `in_quotes`-Flag bevor
das Komma als Trenner gilt.

## Anwendung

Echte CSV-Files haben mehrere Zeilen + Header + Encoding-
Spielereien. Das `csv`-Modul kann all das. Manche Tools nutzen
`;` statt `,` (Excel mit deutscher Locale), das geht ueber
`csv.reader([s], delimiter=";")`.
