# Aufgaben-Format für Codeschmiede

Vollständige, autarke Spezifikation einer Codeschmiede-Aufgabe.
Wer dieses Dokument liest, hat alle Informationen, um eine neue
Aufgabe zu erstellen, ohne den Quellcode der App kennen zu müssen.

Wenn du dieses Dokument einer Sprachmodell-Instanz übergibst, mit dem
Auftrag "schreibe mir Aufgabe X für Codeschmiede", soll sie genau das
Format einhalten, das hier beschrieben ist.

---

## 1. Was Codeschmiede ist (Kurz)

Codeschmiede ist ein lokal gehosteter, gamifizierter Programmier-
Trainer. Aufgaben sind Markdown-Dateien mit YAML-Frontmatter und
liegen im Verzeichnis `aufgaben/`. Beim Backend-Start werden sie
indiziert.

Wenn ein Nutzer eine Aufgabe öffnet, sieht er die Markdown-Beschreibung
links, schreibt seine Lösung im CodeMirror-Editor mittig und schickt
sie an das Backend. Dort läuft der Code in einer dockerisierten
Sandbox (`python:3.11-slim`), wird gegen sichtbare und versteckte
Tests geprüft und das Ergebnis kommt mit Performance-Metriken zurück.

Aktuelle Sprache: **Python 3.11**. Andere Sprachen kommen später.

---

## 2. Verzeichnis-Layout

Eine Aufgabe besteht aus mehreren Dateien in **einem** Unterverzeichnis:

```
aufgaben/
  python/
    NNN-id/
      aufgabe.md             Pflicht (Frontmatter + Beschreibung)
      solution_naive.py      Pflicht (eine erste, einfache Lösung)
      solution_idiomatic.py  Pflicht (idiomatische, "schöne" Lösung)
      solution_optimal.py    Optional (algorithmisch optimiert)
      tests.py               Optional (pytest-Datei für komplexe Tests)
```

**Konventionen:**

- `NNN` ist eine fortlaufende dreistellige Nummer (`004`, `005`, ...)
- Der Verzeichnisname **muss** identisch zum `id`-Feld im Frontmatter sein
- Die Aufgabe muss in einem Sprach-Unterverzeichnis liegen
  (aktuell nur `python/`)

---

## 3. Frontmatter -- vollständige Spezifikation

Das Frontmatter ist YAML, eingerahmt von `---` am Anfang und am Ende.
Direkt danach folgt die Markdown-Beschreibung.

### Pflichtfelder

| Feld                  | Typ           | Beispiel                               | Beschreibung |
|-----------------------|---------------|----------------------------------------|--------------|
| `schema_version`      | int           | `1`                                    | Immer `1` |
| `id`                  | string        | `004-summe`                            | Identisch zum Verzeichnisnamen |
| `titel`               | string        | `Summe einer Liste`                    | Anzeigename |
| `sprache`             | string        | `python`                               | Aktuell nur `python` |
| `schwierigkeit`       | enum          | `anfaenger`                            | siehe unten |
| `schwierigkeit_score` | int (1-100)   | `15`                                   | siehe unten |
| `schaetz_minuten`     | int (>= 1)    | `8`                                    | Realistische Bearbeitungsdauer |
| `funktion`            | string        | `summe`                                | Name der zu implementierenden Funktion |
| `tests_sichtbar`      | Liste         | siehe unten                            | Mindestens ein Test |

### Optionalfelder (mit Default)

| Feld                  | Typ      | Default            | Beschreibung |
|-----------------------|----------|--------------------|--------------|
| `revision`            | int      | `1`                | Hochzählen bei jeder inhaltlichen Änderung |
| `task_type`           | string   | `code_schreiben`   | aktuell nur `code_schreiben` |
| `runner_type`         | string   | `docker_python`    | aktuell nur `docker_python` |
| `tags`                | string[] | `[]`               | Frei wählbare Schlagworte (Kleinbuchstaben, kebab-case) |
| `pfade`               | string[] | `[]`               | IDs von Lernpfaden, denen die Aufgabe angehört |
| `voraussetzungen`     | string[] | `[]`               | IDs anderer Aufgaben, die vorher Sinn ergeben |
| `quelle.url`          | string   | `null`             | Optionaler Link zur Inspirationsquelle |
| `quelle.notiz`        | string   | `null`             | Bemerkung zur Quelle (z.B. "eigene Reformulierung") |
| `lizenz`              | enum     | `eigen`            | `eigen`, `PD`, `CC-BY-4.0`, `BSD-3`, `MIT` |
| `autor`               | string   | `null`             | Frei (z.B. `HalloWelt42`) |
| `erstellt_am`         | date     | `null`             | ISO-Format `YYYY-MM-DD` |
| `zeitlimit_sekunden`  | int 1-60 | `5`                | Wallclock-Timeout pro Sandbox-Lauf |
| `hints`               | Liste    | `[]`               | siehe unten |
| `tests_versteckt`     | Liste    | `[]`               | Stark empfohlen, siehe unten |
| `starter_code`        | string   | `""`               | Multi-Line, Pipe-Notation in YAML |

### Schwierigkeit -- vier Stufen

| Wert               | Charakter                                              | Score-Bereich |
|--------------------|--------------------------------------------------------|---------------|
| `anfaenger`        | Erste Berührung mit einem Konzept                      | 1-25          |
| `mittel`           | Konzept ist bekannt, Aufgabe verlangt Kombination      | 26-50         |
| `fortgeschritten`  | Mehrere Konzepte, Algorithmus-Überlegung nötig         | 51-75         |
| `experte`          | Studiumsaufgabe, Datenstrukturen + Performance-Tuning  | 76-100        |

`schwierigkeit_score` ist eine feinere Gradierung innerhalb der Stufe
(zwei Anfänger-Aufgaben mit Scores 5 und 22 unterscheiden sich
deutlich, beide bleiben aber "anfaenger").

### Tests -- Format

Sowohl `tests_sichtbar` als auch `tests_versteckt` sind Listen aus
Objekten mit zwei Feldern:

```yaml
tests_sichtbar:
  - input: [3, 5]        # positionale Argumente, immer als Liste
    expected: 8          # erwartetes Ergebnis (beliebiger JSON-Wert)
  - input: ["abc"]
    expected: "ABC"
```

**Aufruf:** `funktion(*test.input)` muss `test.expected` zurückgeben.
Vergleich erfolgt mit Python-`==`. Erlaubte Typen für `expected`:
`str`, `int`, `float`, `bool`, `null`, `list`, `dict`.

**Sichtbar vs. versteckt:**

- `tests_sichtbar` werden dem Nutzer im UI angezeigt (mit Eingabe und
  erwartetem Ergebnis)
- `tests_versteckt` laufen serverseitig, nur Anzahl pass/fail wird
  zurückgemeldet -- **wichtig gegen Hardcoding** (Nutzer könnte sonst
  die sichtbaren Inputs in einem Dict abbilden)
- **Faustregel:** mindestens 4-6 versteckte Tests, davon einige
  Edge-Cases (leere Eingabe, sehr große Werte, Grenzfälle)

### Hints -- gestaffelt mit Kosten

```yaml
hints:
  - kosten: 0     # erster Hint kostet meist nichts
    text: Markdown-Text mit Code-Blöcken erlaubt.
  - kosten: 10    # mittlerer Hint
    text: Konkretere Richtung, aber noch keine Lösung.
  - kosten: 25    # letzter Hint -- zeigt das Gerüst
    text: |
      ```
      def funktion(x):
          return ...
      ```
```

`text` darf Markdown enthalten, also auch Inline-Code (`` `x` ``) und
Codeblöcke. `kosten` ist die Punkte-Strafe, die ein Nutzer in Kauf
nimmt, um den Hint zu sehen.

### starter_code -- Boilerplate für den Editor

```yaml
starter_code: |
  def summe(zahlen):
      # Deine Loesung hier
      pass
```

Das ist der Code, der im Editor steht, sobald die Aufgabe geöffnet
wird. Üblicherweise: Funktions-Signatur + ein TODO-Kommentar + `pass`.

---

## 4. Markdown-Konventionen für die Beschreibung

Nach dem zweiten `---` folgt die Beschreibung. Folgende Markdown-
Erweiterungen werden gerendert:

### Standard-Markdown (GFM)

- Überschriften (H1 für den Titel, H2 für Abschnitte, H3 für
  Unterabschnitte)
- Aufzählungen, nummerierte Listen
- Tabellen
- `Inline-Code`, ```Code-Blöcke``` (Sprache mit ` ```python`)
- **fett**, *kursiv*, > Zitate

### Mathematik (KaTeX)

- Inline: `$x^2 + y^2 = z^2$`
- Display (zentriert, größer):
  ```
  $$F_n = F_{n-1} + F_{n-2}$$
  ```

### Diagramme (Mermaid)

```` ```mermaid
flowchart TD
    A[Start] --> B[Schritt 1]
    B --> C[Ende]
``` ````

Mermaid wird zur Laufzeit zu SVG gerendert. Themen-Farben sind auf
das Petrol-Dunkel-Theme eingestellt.

### Empfohlener Aufbau einer Beschreibung

```markdown
# Titel der Aufgabe

Schreibe eine Funktion `funktion(arg1, arg2)`, die ...

## Beispiele

| Eingabe | Ausgabe |
|---------|---------|
| ...     | ...     |

## Hintergrund

Optional: warum diese Aufgabe sinnvoll ist, mathematische Definition,
Diagramm.

## Worauf zu achten ist

- Edge-Case 1
- Edge-Case 2
- Tipp zur Performance falls relevant
```

---

## 5. Musterlösungen

Eine Aufgabe **muss** mindestens zwei Musterlösungen haben:

- `solution_naive.py` -- die erste, intuitive Lösung
  (klassisch: explizite Schleife, viel Boilerplate, leicht
  verständlich, nicht zwingend performant)
- `solution_idiomatic.py` -- die "pythonische" Lösung
  (List Comprehensions, Slicing, Built-Ins, kurz und klar)

Optional:

- `solution_optimal.py` -- die algorithmisch beste Lösung
  (Memoisierung, geschickte Datenstruktur, Komplexitätsklasse)

**Jede Musterlösung muss:**

- Die Funktion mit dem Namen aus `funktion` definieren
- Alle sichtbaren und versteckten Tests bestehen
- Mit einem dreizeiligen Doc-String beginnen, der den Ansatz erklärt
- Self-contained sein (keine relative Imports, keine externen Pakete
  ausser dem Python-Standard)

Beispiel:

```python
"""
Naive Loesung: explizite Schleife, akkumuliert in lokaler Variable.
"""


def summe(zahlen):
    ergebnis = 0
    for z in zahlen:
        ergebnis += z
    return ergebnis
```

---

## 6. Sandbox-Einschränkungen

Aufgaben-Code läuft in einem Container mit harten Limits:

| Ressource         | Limit                                    |
|-------------------|------------------------------------------|
| Image             | `python:3.11-slim` + nur `pytest` extra  |
| Memory            | 128 MB                                   |
| CPU               | 0.5 Cores                                |
| Wallclock-Timeout | 5 s default, per Aufgabe 1-60 s          |
| Netzwerk          | **kein** (`--network=none`)              |
| Filesystem        | read-only, ausser `/tmp` (16 MB tmpfs)   |
| Process-Limit     | 64                                       |
| File-Descriptors  | 64                                       |
| Verfügbare Pakete | nur Python-Standard + `pytest`           |

**Konsequenzen für Aufgaben-Design:**

- **Keine Aufgabe**, die HTTP-Requests, Sockets, oder DNS verwendet
- **Keine Aufgabe**, die Pakete wie `numpy`, `pandas`, `requests`
  benötigt -- nur Python-Standardbibliothek (`math`, `re`, `json`,
  `collections`, `itertools`, `functools`, `datetime`, `random`, ...)
- **Keine Aufgabe**, die Dateien an festen Pfaden ausserhalb `/tmp`
  schreiben oder lesen muss
- Aufgaben dürfen `pytest` nutzen, wenn `tests.py` mitgeliefert wird
  (Pfad-Konvention für komplexe Tests, nicht für die Standard-
  YAML-Tests)
- Subprocess-Aufrufe innerhalb des Containers sind technisch möglich,
  aber nicht sinnvoll für didaktische Aufgaben

---

## 7. Qualitätskriterien -- wann ist eine Aufgabe "gut"?

Eine Aufgabe gehört nur dann ins Repo, wenn sie alle Punkte erfüllt:

1. **Sinnvoll:** sie übt ein klar benanntes Konzept (z.B. Modulo,
   String-Slicing, Rekursion, Sortier-Algorithmen). Kein
   Aufgaben-Selbstzweck.
2. **Korrekt:** Beschreibung, Beispiele, sichtbare und versteckte
   Tests sind in sich konsistent. Wenn die Beschreibung sagt
   "case-sensitive", müssen die Tests das auch durchsetzen.
3. **Lösbar mit Standard-Mitteln:** keine versteckten Voraussetzungen
   (z.B. mathematische Sätze, die nirgends erklärt sind).
4. **Mindestens zwei Musterlösungen** vorhanden, beide grün gegen
   alle Tests, didaktisch unterschiedlich.
5. **Versteckte Tests** decken Edge-Cases ab, die durch ein simples
   Lookup-Dict nicht trivial zu lösen wären.
6. **Realistische Zeitschätzung** (`schaetz_minuten`).
7. **Genaue Funktions-Signatur** -- der `funktion`-Name im Frontmatter
   ist exakt der, den die Musterlösungen definieren, und auch der,
   den der Nutzer schreiben muss.

---

## 8. Sprachregeln (gilt für die gesamte Aufgabe)

Für **alle Texte** in `aufgabe.md` (Frontmatter `titel`, `notiz`,
`hints[].text`, Beschreibung, Quelle), für **Doc-Strings** in den
Musterlösungen und für **Kommentare**:

- **Deutsch mit Umlauten** (ä, ö, ü, ß) -- niemals ae, oe, ue, ss
  als Ersatz
- **Keine typografischen Sonderzeichen** -- nur gerade Anführungs-
  zeichen (`"`, `'`), gerade Bindestriche (`-`, `--`); kein Em-Dash,
  kein En-Dash, keine typografischen Quotes
- **Keine Verweise** auf Sprachmodelle, KI, Anthropic, Claude, OpenAI
  oder ähnliche Hersteller. Eine Aufgabe ist eine Aufgabe -- woher
  sie inhaltlich stammt, gehört in `quelle.notiz`, nicht in den
  Beschreibungstext.
- **Variablennamen, Funktionsnamen, Klassennamen, Tag-Namen** im
  Code bleiben **englisch / ASCII** (z.B. `summe`, `ist_palindrom`
  sind ok als deutsche Identifier ohne Umlaute, weil ASCII).

---

## 9. Vollständiges Beispiel (Vorlage)

Komplette Aufgabe `aufgaben/python/004-summe-liste/`:

### `aufgabe.md`

```markdown
---
schema_version: 1
id: 004-summe-liste
revision: 1
titel: Summe einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, schleifen, akkumulator]
pfade: [python_grundlagen]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Einsteiger-Aufgabe, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: summe
hints:
  - kosten: 0
    text: Eine Schleife mit `for` durchlaeuft alle Elemente.
  - kosten: 15
    text: |
      Du brauchst eine Variable, in der du die Zwischensumme sammelst.
      Initialisiere sie mit `0`.
  - kosten: 30
    text: |
      Idiomatische Variante:

      ```
      return sum(zahlen)
      ```
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: 6
  - input: [[]]
    expected: 0
  - input: [[10]]
    expected: 10
tests_versteckt:
  - input: [[1, -1, 1, -1]]
    expected: 0
  - input: [[100, 200, 300]]
    expected: 600
  - input: [[-5, -5, -5]]
    expected: -15
  - input: [[0, 0, 0, 0, 0]]
    expected: 0
starter_code: |
  def summe(zahlen):
      # Deine Loesung hier
      pass
---

# Summe einer Liste

Schreibe eine Funktion `summe(zahlen)`, die die Summe aller Elemente
einer Liste von ganzen Zahlen zurückgibt.

## Beispiele

| Eingabe        | Ausgabe |
|----------------|--------:|
| `[1, 2, 3]`    | `6`     |
| `[]`           | `0`     |
| `[-5, 5]`      | `0`     |

## Worauf zu achten ist

- Eine **leere Liste** soll `0` zurueckgeben (per Konvention -- die
  Summe über das leere Produkt ist das neutrale Element der Addition).
- Negative Zahlen sind erlaubt.

## Hintergrund

Eine Summe ist die einfachste Reduktion einer Liste. Mathematisch:

$$\text{summe}([a_1, a_2, \dots, a_n]) = \sum_{i=1}^{n} a_i$$
```

### `solution_naive.py`

```python
"""
Naive Loesung: explizite Schleife mit Akkumulator-Variable.
"""


def summe(zahlen):
    ergebnis = 0
    for z in zahlen:
        ergebnis += z
    return ergebnis
```

### `solution_idiomatic.py`

```python
"""
Idiomatische Loesung: Built-In `sum()`. Ein Aufruf, klar lesbar,
optimal in Python implementiert.
"""


def summe(zahlen):
    return sum(zahlen)
```

---

## 10. Output-Format (für ein Sprachmodell, das eine Aufgabe erzeugt)

Wenn du als Sprachmodell eine neue Aufgabe für Codeschmiede generierst,
liefere genau folgende Struktur in deiner Antwort:

```
### Pfad: aufgaben/python/NNN-id/aufgabe.md

<inhalt der aufgabe.md, inklusive frontmatter>

### Pfad: aufgaben/python/NNN-id/solution_naive.py

<python-code>

### Pfad: aufgaben/python/NNN-id/solution_idiomatic.py

<python-code>

### (optional) Pfad: aufgaben/python/NNN-id/solution_optimal.py

<python-code>
```

Mehr nicht. Keine Vor- oder Nachbemerkungen, keine Diskussion. Ein
Mensch kopiert deine Antwort in die genannten Dateien -- jeder Block
ist genau eine Datei.

---

## 11. Selbsttest vor dem Commit

Bevor eine Aufgabe ins Repo wandert:

1. **Datei-Layout** stimmt -- Verzeichnis heisst wie `id`, Pflicht-
   Dateien sind da.
2. **Frontmatter validiert** -- alle Pflichtfelder gesetzt, Typen
   korrekt, `id` == Verzeichnisname.
3. **Beide Musterlösungen laufen lokal** durch alle sichtbaren und
   versteckten Tests:
   ```bash
   cd aufgaben/python/NNN-id
   for sol in solution_*.py; do
     python -c "
   from $(basename $sol .py).${sol%.py} import $FUNKTION
   import json
   tests = $TESTS_JSON
   for t in tests:
       got = $FUNKTION(*t['input'])
       assert got == t['expected'], f'FAIL: {t} got={got}'
   print('OK', '$sol')
   "
   done
   ```
   (oder einfach: Backend starten, Aufgabe öffnen, beide Lösungen
   ins Editor-Feld einsetzen und "Prüfen" klicken)
4. **Sprachregeln** eingehalten (Umlaute, keine Em-Dashes, keine
   Hersteller-Verweise).
5. **Hardcoding-Probe** -- ein simples Lookup-Dict mit den sichtbaren
   Inputs als Keys darf die Aufgabe nicht bestehen.

Wenn alles passt: in den entsprechenden Pfad einchecken
(`aufgaben/<sprache>/<id>/`), Backend startet die Aufgabe beim
nächsten Lauf automatisch ein.
