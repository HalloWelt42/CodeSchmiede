# Kursformat: Einführungen, Kurse, Begriffe

Der Aufbaukurs liegt als Dateien im Repo unter `kurs/`. Die Codeschmiede liest ihn beim Start (und mit jedem
Neueinlesen) und prüft ihn; Befunde stehen in der Verwaltung neben denen der Aufgaben. Auf dem Pi ist der Ordner nur
lesend eingebunden, bearbeitet wird am Mac. Entscheidungen dazu in `PLAN.md` unter "Klärung Aufbaukurs und
Lehreinführungen".

## Ordner

```
kurs/
  python.yml                                    Kurs je Sprache: Blöcke, Kapitel, Übungen
  begriffe/python.yml                           Begriffskatalog je Sprache
  einfuehrungen/<sprache>/<thema>/
    einfuehrung.md                              Kopf und Abschnitte
    kurztest.yml                                Fragen und eine Übung zum Überspringen
    zeichnungen/<name>.svg                      eigene Zeichnungen
  diagramme/<prüfsumme>.svg                     aus den Mermaid-Blöcken gebaut (tools/diagramme.py)
  bilder/kurs/<schlüssel>.webp                  Export des Medienpools, nur für Karten
  stilprobe.yml                                 Bildaufträge der Stilprobe
```

## Einführung

Kopf in YAML zwischen `---`-Zeilen:

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `id` | ja | Kennung, klein mit Bindestrichen (`py-schleifen-for`) |
| `sprache` | ja | `python`, `sql`, `javascript`, `css`, `digital`; muss zum Ordner passen |
| `titel` | ja | Titel des Kapitels |
| `kurz` | ja | ein Satz für die Kursübersicht |
| `fuehrt_ein` | nein | Begriffe aus dem Katalog, die diese Einführung erklärt |
| `lernziele` | ja | Sätze für "Danach kannst du" und "Kann ich jetzt" |
| `karte` | ja | kurzer Satz auf der Sammelkarte |
| `bilder` | nein | Bildaufträge an den Medienpool (vorerst nur `sammelkarte` und `bereich`) |
| `datensatz` | bei SQL | Datensatz aus `aufgaben/sql/datasets/`, auf dem die Beispiele laufen (nur und immer bei SQL) |

Ein Bildauftrag hat `schluessel` (a-z, 0-9, _), `art`, `sprache` (Farbfamilie), `motiv` (deutsch, ohne Schrift im
Bild) und `groesse` (`4 x 3`). Prompt, Stil und Auswahl gehören dem Medienpool; `tools/bildschluessel.py --abgleich`
gleicht die Aufträge ab.

Darunter folgen Abschnitte, jeder beginnt mit `## Titel`. Ein Abschnitt besteht aus Markdown und Blöcken in
Zaunzeilen (die schließende Zeile ist genau drei Backticks). Je Abschnitt genau eine neue Sache.

| Block | Inhalt (YAML) | Zweck |
|---|---|---|
| ` ```alltag ` | `text`, `zeichnung` (optional, Name ohne Endung) | Konkretes aus dem Leben vor dem Code |
| ` ```zeichnung ` | `datei`, `unterschrift` | eigene Zeichnung aus `zeichnungen/` |
| ` ```merke ` | `text` | Merksatz; erscheint auch auf dem Merkblatt |
| ` ```falle ` | `titel`, `text` | typischer Fehler; erscheint auch auf dem Merkblatt |
| ` ```augenzwinkern ` | `text` | ein lockerer Satz zum Schluss |
| ` ```beispiel ` | `id`, `code`, `vorhersage` (optional), `ablauf` (Vorgabe ja), bei CSS `html` (Pflicht) | Beispiel zum Ausführen, mit Ablauf und Speicherbild |
| ` ```kv ` | `id`, `eingaenge` (2 bis 4), `werte` (je Belegung 0, 1 oder x), `formeln` (Liste aus `titel` und `formel` wie in der KV-Werkstatt, etwa `C + A B`), `start` (`raster` oder `wuerfel`), `regler`, `plan` | Digitaltechnik: Funktion in der Werkbank als Würfel (nur drei Eingänge, mit `regler` zum Raster aufklappbar) oder KV-Raster; jede Formel muss beim Einlesen zur Funktion passen |
| ` ```frage ` | siehe unten | Verständnisfrage |
| ` ```mermaid ` | Mermaid-Code (kein YAML) | Diagramm, als SVG gebaut |

### Vorhersage

```yaml
vorhersage:
  art: auswahl            # oder eintippen
  optionen:               # bei auswahl: 2 bis 6, genau eine richtig
    - {text: "Hallo", richtig: true, erklaerung: "Genau."}
    - {text: "print(Hallo)", erklaerung: "Ausgegeben wird nur der Text."}
  erklaerung: ...         # bei eintippen: nach dem Vergleich mit dem echten Ergebnis
  frage: ...              # optional: eigene Frage statt "Was gibt das Beispiel aus?"
  vergleich: zeilen       # optional: zeilen oder anfang statt der ganzen Ausgabe (Vorgabe: ausgabe)
```

Bei `vergleich: zeilen` steht in der richtigen Option die Zahl als erste Zahl im Text ("4 Zeilen"); beim Eintippen
wird die Zahl getippt. Bei `vergleich: anfang` ist die richtige Option der Anfang der Ausgabe, eine oder mehrere ganze
Zeilen (passend zu Fragen wie "Wer steht ganz oben?"). Verglichen wird an einer Stelle (`vorhersage_stimmt`), für
Antworten wie für die Prüfung des Bestands. Die Ausgabe einer SQL-Abfrage ist als Text je Ergebniszeile die Werte mit ` | ` getrennt, ohne
Kopfzeile, NULL als `NULL`.

### Ablauf

Python: Zeile für Zeile aus der Aufzeichnung in der Sandbox, mit Speicherbild. JavaScript genauso, aufgezeichnet über
den Inspector von Node wie mit einem Debugger (`aufzeichnung/aufzeichner.js`): Arrays erscheinen als Liste, Map als Wörterbuch,
Set als Menge, Objekte mit ihren Eigenschaften, `null` und `undefined` als nichts; Rückrufe aus Zeitgebern und
Versprechen laufen mit. Zeitgeber laufen dabei, wie in den Programm-Aufgaben, auf einer eigenen Uhr
(`pruefung/zeitgeber.js`): Sie warten nicht echt, sondern kommen in der Reihenfolge ihrer Wartezeiten dran. Eingaben eines Beispiels (`eingabe`) liest `prompt()`. SQL: das Ergebnis und je Klausel die
Zwischentabelle in der Reihenfolge der Abarbeitung (FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY,
LIMIT); der SQL-Parser zerlegt die Abfrage in Teilabfragen, die in der Sandbox auf dem Datensatz laufen. Zerlegt wird
eine einzelne SELECT-Abfrage ohne WITH und UNION, sonst gibt es nur das Ergebnis.

CSS: `code` ist das CSS, `html` das Markup, auf das es wirkt. Es gibt keine Textausgabe, darum gehen Vorhersagen nur
als Auswahl, und die richtige Option beschreibt das Bild ("Wie sieht es auf der Bühne aus?"). Der Lauf braucht keine
Sandbox: der Browser rendert Markup und CSS auf derselben Bühne wie bei den CSS-Aufgaben (`frontend/src/lib/css/buehne.ts`).
Die Werkbank zeigt das CSS Zeile für Zeile mit einem Schalter je Angabe und einem Abspieler (Angabe für Angabe
zuschalten), die Bühne folgt jeder Änderung im Editor sofort, und das Kastenmodell eines Elements (das erste, das unter
dem Zeiger oder das angetippte) erscheint als farbige Ringe mit der Rechnung "Rand zu Rand". In Fragen erkennt die
Oberfläche Markup am ersten Zeichen `<`.

Ausführen geht erst nach der Vorhersage (der Server erzwingt es). Bei `eintippen` vergleicht der Server mit der
Ausgabe des echten Laufs.

### Fragen

Jede Frage hat `frageart`, `id` (eindeutig in der Einführung) und `text`.

| frageart | Felder |
|---|---|
| `auswahl` | `optionen` (je `text`, `richtig`, `erklaerung`), `code` (optional), `als_code` (Optionen in fester Breite) |
| `luecke` | `code` mit `___` je Lücke, `antworten` (je Lücke eine Liste angenommener Antworten), `erklaerung`, `hinweis` |
| `ordnen` | `zeilen` in richtiger Reihenfolge (gezeigt in fester Mischung), `erklaerung`, `hinweis` |
| `fehlerstelle` | `code`, `zeile` (1-basiert), `erklaerung`, `hinweise` (je falscher Zeile, optional), `hinweis` |

Antworten und Erklärungen verlassen den Server nie; die Oberfläche bekommt sie erst mit dem Urteil. Ein Abschnitt ist
fertig, wenn alle seine Fragen richtig beantwortet sind.

## Kurztest

`kurztest.yml` neben der Einführung: `fragen` (mindestens zwei, eigene, nicht die der Einführung) und `uebung` (eine
Aufgabe, die alle Teile des Kapitels braucht). Bestanden, wenn jede Frage zuletzt richtig beantwortet und die Übung
gelöst ist; das Kapitel gilt dann als übersprungen.

## Kurs

```yaml
sprache: python
titel: Python
bloecke:
  - titel: Erste Schritte
    kapitel:
      - einfuehrung: py-ausgabe
        uebungen: [k-py-001-hallo, ...]     # verblassende Beispiele zuerst, dann je Übung eine neue Sache
        projekt: [k-py-p01-notenbuch]       # Stück des Kapitelprojekts
```

Die Kapitelnummer ist die Stelle im Kurs. Übungen sind gewöhnliche Aufgaben unter `aufgaben/`; für Kapitel ohne
Funktionen gibt es den Aufgabentyp `programm` (ganzes Programm, `tests_sichtbar`/`tests_versteckt` mit `input` als
Liste der Eingabezeilen und `expected` als erwartete Ausgabe), in Python wie in JavaScript. Die Eingabezeilen liest
`input()` in Python und `prompt()` in JavaScript; beide schreiben ihre Frage ohne Zeilenumbruch in die Ausgabe, und
`prompt()` liefert `null`, wenn keine Zeile mehr da ist. Ein JavaScript-Programm ist fertig, wenn auch seine
Zeitgeber und Versprechen erledigt sind. Im CSS-Kurs sind die Übungen CSS-Nachbauten (`css_klon`, Kennungen
`w<Kapitel><Nummer>`): das HTML ist vorgegeben, geschrieben wird das CSS. Ob jede Musterlösung ihr Ziel voll deckt und
kein Startcode schon besteht, misst die Verwaltung im Browser ("CSS-Bestand messen"), mit derselben Messung wie beim
Lösen. Vertiefung aus dem Bestand sucht die Codeschmiede
selbst: Aufgaben, die nur Eingeführtes brauchen und das Neue des Kapitels üben. Der Kurs Digitaltechnik (`digital`) übt mit
Aufgaben unter `aufgaben/maschine/` (KV-Werkstatt, Schaltungen), die zugleich Levels der Spiele sind
(`AUFGABEN_SPRACHE` in `kurs/modelle.py`); seine Beispiele laufen nicht, sie sind ` ```kv `-Blöcke zum Anschauen.

## Begriffskatalog und Prüfung

`begriffe/<sprache>.yml` nennt je Begriff `id`, `titel` und `erkennung` (Python: `knoten`, `operatoren`, `aufrufe`,
`methoden`, `literale` aus dem Syntaxbaum; SQL: `knoten` als Ausdrucksarten des SQL-Parsers, dazu `LeftJoin` und
`RightJoin`, und `aufrufe` als Funktionen in Großbuchstaben; JavaScript: `knoten` und `literale` als Knotenarten von
tree-sitter, `operatoren` als Operatoren und Schlüsselwörter, wie sie im Code stehen (`===`, `let`, `of`), `aufrufe`
als Namen, auch mit Punkt (`console.log`, `Math.round`), `methoden` und `eigenschaften` hinter einem Punkt (`length`);
CSS über tinycss2: `knoten` als Selektorarten (`typ`, `klasse`, `id`, `universal`, `attribut`, `nachfahre`, `kind`,
`gruppe`, `nachbar`, `geschwister`), Pseudoklassen und -elemente mit Namen (`:first-child`, `::before`), at-Regeln
(`@media`) sowie `regel`, `kommentar` und `eigene_eigenschaft`, `eigenschaften` der Angaben, `werte` als
`eigenschaft:wert` oder `*:wert` (`display:flex`, `*:inherit`), `aufrufe` als Funktionen (`rgb`, `calc`), `literale`
als Einheiten, `hex`, `zahl` und `text`; Markup (beginnt mit `<`, auch `html` der Beispiele und `ziel_html` der
Aufgaben) über html.parser mit `elemente` und `attribute`). Für jedes Kapitel gilt als bekannt, was dieses und alle früheren
einführen. Benutzt Code in Beispielen, Fragen, Kurztest, Übungen oder Projekt einen Begriff, der dort noch nicht
eingeführt ist, meldet die Prüfung einen Vorgriff. Weitere Befunde: unbekannte Begriffe, doppelt eingeführte, fehlende
Einführungen, Aufgaben oder Zeichnungen, ungebaute Diagramme, Einführungen ohne Kurs.

## Werkzeuge

- `backend/.venv/bin/python tools/diagramme.py` baut fehlende Diagramme (einmalig vorher
  `cd tools/diagramme && PUPPETEER_SKIP_DOWNLOAD=1 npm ci`; nutzt das installierte Chrome).
- `backend/.venv/bin/python tools/bildschluessel.py --abgleich` gleicht Bildaufträge mit dem Medienpool ab.
