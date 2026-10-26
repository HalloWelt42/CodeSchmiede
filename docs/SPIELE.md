# Spiele und Spielmechanik

Konzept zu Schritt 6 (Plan): vier Lernspiele in einem eigenen Bereich und eine Spielmechanik, die über die ganze App
wirkt. Die Entwürfe dazu liegen in `mockups/` (Übersicht `mockups/index.html`, Abschnitt Spiele). Gebaut wird erst
nach Freigabe.

Leitlinien:

- Aufbauend: Aufgaben und Levels bauen aufeinander auf; im einfachen Modus geht es ein Ziel nach dem anderen, und erst
  wenn eines klappt, kommt der nächste Teilschritt (Nutzer 25.10.2026).
- Lernen vor Belohnung: jede Mechanik belohnt etwas, das beim Lernen hilft (üben, wiederholen, sauber und knapp
  lösen), nie bloßes Klicken.
- Eine Wahrheit: es gibt eine Währung, die Punkte. Stufe, Ränge und Sterne leiten sich aus gespeicherten Ergebnissen ab
  und werden nie getrennt gezählt.
- Freundlich statt strafend: Serien mit Schutzschild, keine Bestenliste gegen andere (ein Nutzer), dafür eigene
  Bestwerte. Verlieren kostet nie Punkte.
- Fair: Levels prüft der Server wie Aufgaben, mit sichtbaren und versteckten Fällen (beim Roboter versteckte Welten),
  damit nichts auswendig gelernt werden kann.

## Die vier Spiele

Jedes Spiel ist ein Aufgabentyp mit eigenem Prüfer; Levels sind Aufgabendateien wie alle anderen. Sie liegen wie jede
Aufgabe im Ordner ihrer Sprache, mit eigenem Kürzel vor der Nummer (Muster-Jagd `m001-...` unter `aufgaben/javascript/`),
die Reihenfolge gibt ein Pfad vor, und `aufgaben/_konfig.yml` führt das Spiel unter `spiele` mit Titel, Symbol,
Aufgabentyp und Pfaden. Levels zählen in Punkte, Serie und Wiederholung. Jedes Level vergibt bis
zu drei Sterne: ein Stern fürs Bestehen, zwei und drei für Güte nach Schwellen aus der Level-Datei. Die Punkte eines
Levels sind Grundpunkte mal Sterne durch drei; es zählt der beste Versuch.

### SQL-Krimi

- **Lehrt**: Abfragen in einer echten, unordentlichen Datenbank: Filter, Joins, Gruppierung, Unterabfragen, Datum.
- **Ablauf**: Ein Fall in Kapiteln. Jedes Kapitel erzählt ein Stück und stellt eine Frage ("Welches Auto stand zur
  Tatzeit vor dem Lager?"). Die Antwort steckt in einem Abfrageergebnis. Gefundene Hinweise landen auf der Pinnwand
  der Akte und bleiben sichtbar.
- **Prüfung**: Die Abfrage läuft in der Sandbox auf der Tatort-Datenbank des Falls und auf einer zweiten, anders
  befüllten Datenbank (wie die Gegenprobe der SQL-Aufgaben): das Ergebnis muss die gesuchte Antwort enthalten, egal wie
  die Abfrage geschrieben ist.
- **Sterne**: Bestehen; ohne Hinweis; mit höchstens so vielen Abfragen wie die Musterlösung braucht.

### Roboter-Parcours

- **Lehrt**: Schleifen, Bedingungen, eigene Funktionen, Zerlegen von Problemen; in Python.
- **Ablauf**: Ein Roboter auf einem Raster mit Wänden, Ziel und Kristallen. Gesteuert wird mit `gehe()`,
  `links()`, `rechts()`, `wand_vorne()`, `am_ziel()`, `kristall()`, `nimm()`. Der Lauf wird als Folge von Schritten
  animiert (abspielen, einzeln, Tempo), die Spur bleibt sichtbar; ein Fehler (gegen die Wand) zeigt die Stelle.
- **Prüfung**: Der Code läuft in der Sandbox gegen die sichtbare Welt und gegen versteckte Welten mit gleicher Aufgabe
  und anderer Gestalt (längerer Gang, Kristalle woanders). Wer nur die eine Welt abläuft, scheitert; wer eine Schleife
  schreibt, besteht.
- **Sterne**: Bestehen; höchstens so viele Schritte wie die Musterlösung; höchstens so viele Zeichen.

### Ausgabe-Sprint

- **Lehrt**: Code lesen und im Kopf ausführen: Reihenfolge, Gültigkeit, Grenzfälle, Gleitkomma, Wahrheitswerte.
- **Ablauf**: Runden mit zehn kurzen Schnipseln gegen die Uhr (Vorgabe 90 Sekunden). Antwort wählen (Klick oder Tasten
  1 bis 4); richtige Antworten in Folge bilden eine Kette, die als eigener Bestwert zählt, nicht in Punkte (eine
  Währung). Am Ende der Runde die Auswertung: jede falsche Antwort mit der richtigen und einer kurzen Erklärung, warum.
- **Prüfung**: Je Sprache und Stufe ein Sprint-Level mit eigenem Vorrat an Schnipseln. Die Runde stellt der Server
  zusammen und mischt die Antworten; die richtige erfährt der Browser erst nach seiner Wahl, gewählt wird der Reihe nach
  und nur bis zur Frist. Der Bestandstest lässt jeden Schnipsel in der Sandbox laufen und vergleicht mit der richtigen
  Antwort.
- **Sterne**: je Runde nach Trefferzahl (6, 8, 10 von 10). Gut fürs Telefon.

### Muster-Jagd

- **Lehrt**: reguläre Ausdrücke, von Zeichenklassen bis zu Gruppen und Ankern.
- **Ablauf**: Zwei Listen: Treffer (müssen passen) und Nieten (dürfen nicht passen). Beim Tippen markiert jede Zeile
  sofort, ob sie stimmt; kürzere Muster geben mehr Sterne.
- **Prüfung**: In der Sandbox (JavaScript, mit Zeitgrenze gegen zu gierige Muster) gegen die sichtbaren und weitere
  versteckte Zeilen. Die Vorschau im Browser nutzt dieselbe Ausdrucksart (JavaScript), damit Vorschau und Prüfung
  übereinstimmen.
- **Sterne**: Bestehen; höchstens so lang wie die Musterlösung plus Spielraum; so kurz wie die Musterlösung.

## Steuerungsspiele

Größere Spiele, bei denen eine Steuerung programmiert wird und echte Abläufe zeigen, ob sie stimmt (Nutzer
25.10.2026). Der Rahmen ist vorgefertigt: Welt, Verkehr, Zeichnung, Abläufe. Geschrieben wird nur der Ablauf, eine
Funktion `takt(lage)`, die jede Sekunde die Sensoren bekommt und die Stellung der Signale oder den Fahrbefehl
zurückgibt. Wie beim Roboter kommt aus der Sandbox nur diese Folge; Verkehr, Unfälle, Regelverstöße und Wartezeiten
rechnet das Backend selbst nach, die Abläufe laufen deterministisch.

- **Aufbau in Teilschritten** (`backend/src/codeschmiede/steuerung/teilschritte.py`): Jedes Level ist eine Folge
  kleiner Ziele mit eigenen Regeln, jedes schließt die vorigen ein. Der erste Teilschritt gilt im ersten sichtbaren
  Ablauf, spätere nehmen weitere Abläufe beim Namen dazu, der letzte nimmt "alle", auch die versteckten. Geprüft wird
  immer alles; "Schritt für Schritt" zeigt die Ziele bis zum ersten offenen, "Alles auf einmal" alle. Einen getrennt
  gespeicherten Stand gibt es nicht: der Code selbst sagt, wie weit er ist. Auch die Levels bauen aufeinander auf:
  gibt es noch kein eigenes Programm, beginnt ein Level mit dem bestandenen Programm des Levels davor
  (`aufbauend_auf`).
- **Spaß und Ton**: roter Matschfleck für überfahrene Fußgänger, verbeultes Blech mit Rauch; Klänge für Taster,
  Ticken bei Grün für Fußgänger, Anfahren, Blechschaden und Matsch aus dem Bestand des Medienpools (CC0, Quellen in
  `docs/KLAENGE.md`). Ton ist aus, bis man ihn einschaltet; die Wahl merkt sich der Browser.
- **Prüfung**: sichtbare und versteckte Abläufe (andere Ankünfte, Stoßzeiten, langsame Lkw, Sonderfälle).
  Sicherheitsregeln sind harte Tests: ein Unfall oder Verstoß, und das Level gilt nicht. Ein misslungener versteckter
  Ablauf lässt sich ab kurz vor der ersten Stelle abspielen.
- **Sterne**: einer, wenn alle Teilschritte in allen Abläufen erfüllt sind; zwei, wenn dazu im ersten sichtbaren
  Ablauf die Fußgänger höchstens so lange und die Fahrzeuge im Mittel höchstens so lange warten; drei, wenn dazu der
  Code höchstens so viele Zeichen hat.
- **Ansicht**: links Aufgabe, Teilschritte, Sensoren, Signale und Sterne; Mitte das Programm mit "Ablauf" (die
  sichtbaren Abläufe) und "Prüfen"; rechts die Anlage mit Abspielen, Ton und Tempo, darunter der Signalplan (Klick
  springt zur Sekunde), Kennzahlen und die Abläufe. Am Telefon dieselben drei Teile als Schritte.

### Ampelschule (gebaut, 0.89.0)

Draufsicht von oben, die Ampeln am Straßenrand; Autos halten bei Rot und bei Gelb, wenn sie noch halten können
(ein Lkw hat den längeren Bremsweg), Fußgänger drücken den Taster und gehen bei Grün. Gebaut im Paket
`backend/src/codeschmiede/steuerung/`:

- **Welt** (`ampel_welt.py`): reines Python, dieselbe Quelle läuft in der Sandbox (für die Sensoren des Programms)
  und im Backend (für das Urteil). Wege sind Linienzüge mit Gruppe, Haltlinie und Kontaktschleife; Konfliktzonen
  entstehen aus der Geometrie (Wege fremder Gruppen, die sich kreuzen oder zusammenlaufen) und sagen auch, welche
  Gruppen einander feind sind. Warten heißt: vor der Haltlinie stehen.
- **Anlagen** (`ampel_anlage.py`): Vorlagen Überweg und Kreuzung (bis vier Zufahrten, je ein oder zwei Spuren mit
  Bewegungen und Gruppe, Überwege je Zufahrt, Kontaktschleifen, Vorfahrt für das gelbe Blinken). Kreuzen sich Wege
  einer Gruppe, meldet das die Bestandsprüfung.
- **Abläufe** (`ampel_ablauf.py`): Verkehr als feste Zeiten, Takt oder Zufall je Sekunde mit festem Startwert, für
  einen Weg, eine Zufahrt oder einen Überweg; dazu Nachtzeiten, eine gestörte Kontaktschleife und
  Einsatzfahrzeuge, die sich zwölf Sekunden vorher anmelden.
- **Sensoren** in `lage`: `sekunde`, `taster[g]`, `schleife[g]`, `wartend[g]`, `frei[g]` (niemand Fremdes auf den
  Flächen, die g kreuzt), `einsatz`, `nacht`, `stoerung`. `taster` und `schleife` sind als Wahrheitswert "irgendwo".
- **Regeln** (`ampel_regeln.py`): feindlich, gelb, rotgelb, raeumzeit, mindestgruen, ruhe, reagiert, nur_bei_bedarf,
  bedient, kein_unfall, nacht, einsatz; jede mit ihren Werten in der Level-Datei.

Die acht Levels (`aufgaben/python/v001` bis `v008`, Pfad `ampelschule`):

1. Fußgängerampel im festen Takt
2. Fußgänger auf Knopfdruck (Mindestgrün, Gelb, Räumzeit, langsamer Lkw im Lieferverkehr)
3. Zwei Straßen, ein Umlauf
4. Kontaktschleifen: Grün nur bei Bedarf
5. Kreuzung mit Fußgängern ringsum
6. Linksabbieger mit eigener Phase
7. Die große Kreuzung: vier Zufahrten, zweispurig, Abbieger, Fußgänger in eigener Phase
8. Sonderfälle: Blaulicht, Nacht mit gelbem Blinklicht, gestörte Kontaktschleife (je ein sichtbarer Ablauf)

Jede Musterlösung besteht mit drei Sternen, jeder Startcode scheitert am ersten Teilschritt, und wer `frei` nicht
fragt, baut im versteckten Lieferverkehr einen Unfall (Tests in `backend/tests/test_ampel.py`).

### Aufzugsteuerung (gebaut, 0.90.0)

Schnitt durchs Haus von der Seite: Schächte mit Seilen, Kabinen mit gleitenden Türen, Anzeigen über den Türen,
Rufknöpfe und Wartende, darunter das Fahrdiagramm (Etage über Zeit je Kabine, Rufe als Punkte, Verstöße als Marken).
Gebaut im Paket `backend/src/codeschmiede/steuerung/` auf demselben Unterbau wie die Ampelschule (Sandbox-Lauf,
Teilschritte, gemeinsame Ansicht `SteuerungsView`):

- **Welt** (`aufzug_welt.py`): jede Kabine fragt `takt(lage)`, sobald sie mit ihrem Befehl fertig ist, und bekommt
  "hoch", "runter" (eine Etage, zwei Sekunden), "auf", "zu" (je eine Sekunde) oder "warten". Bei offener Tür steigen
  erst alle aus, dann ein, einer nach dem anderen und ohne Lücke (Lichtschranke). Wer an der Etage wartet, steigt ein,
  solange Platz ist; wo die Kabine hält, entscheidet das Programm. Überladen wird zwei Sekunden verhandelt, dann steigt
  der Letzte wieder aus und ruft erst, wenn die Kabine weiterfährt. Bei Feueralarm steigt niemand mehr ein, im EG
  alle aus. Was gegen die Regeln geht, führt die Welt nicht aus und vermerkt es als Verstoß.
- **Vorgaben** (`aufzug_ablauf.py`): Haus (Etagen, Kabinen, Plätze, Höchstlast) und Fahrgäste als feste Zeiten,
  Takt oder Zufall mit festem Startwert, Start und Ziel als Etage, Liste oder Zufall; Feueralarm je Ablauf.
- **Sensoren**: `etage`, `tuer`, `rufe[1]`, `rufe[-1]`, `ziele`, `richtung`, `sekunde`, dazu je Level `wartend`,
  `lichtschranke`, `voll` und `drin`, `ueberlast`, `feuer`, `aufzuege` (alle Kabinen) und `aufzug`.
- **Regeln** (`aufzug_regeln.py`): tuer_sicher, kein_einklemmen, ueberlast, bedient, mitnehmen (wer in
  Fahrtrichtung wartet, wird mitgenommen), umkehren (erst wenden, wenn in der Richtung nichts mehr liegt, was schon
  vor der Ankunft bestand), zuegig, feuer, parken.

Die sieben Levels (`aufgaben/python/e001` bis `e007`, Pfad `aufzugsteuerung`):

1. Zwei Etagen: rufen, fahren, Tür auf und zu, Lichtschranke
2. Rufe sammeln: unterwegs mitnehmen, erst umkehren, wenn alles erledigt ist
3. Volle Kabine: Gruppen, vier Plätze
4. Bürohaus: zehn Etagen, im EG parken
5. Zwei Aufzüge: wer fährt?
6. Stoßzeit am Morgen
7. Sonderfälle: Überlast (ein Klavier) und Feueralarm, je ein sichtbarer Ablauf

"Tür und Lichtschranke" aus dem Entwurf steckt schon im ersten Level, weil die Tür von Anfang an dem Programm gehört;
an seiner Stelle kam die volle Kabine dazu. Jede Musterlösung besteht mit drei Sternen, jeder Startcode scheitert am
ersten Teilschritt, und das Programm des Levels davor reicht nicht (Tests in `backend/tests/test_aufzug.py`).

### Weitere Regelungen (Ideen)

Bahnübergang mit Schranke, Schleuse mit Wasserstand, Heizungsregler mit Schaltpause, Parkhaus mit Belegung und
Schranken, Förderband mit Weiche, Garagentor mit Sicherheitsleiste.

## Turingmaschine und digitale Schaltungen (Entwürfe freigegeben 26.10.2026)

Vorschlag des Nutzers (25.10.2026): eine Turingmaschine programmieren, extrem anschaulich, mit mehreren Aufgaben, und
digitale Schaltungen bis zur 7-Segment-Anzeige, Halb- und Volladdierer; einfache und etwas komplexere Aufgaben,
Verdrahtungsaufgaben mal mit, mal ohne fertige Anordnung.

- **Gemeinsam**: abgegeben wird kein Code, sondern Daten (Übergangstabelle, Schaltplan als Liste von Bausteinen und
  Leitungen). Der Server rechnet sie vollständig nach, ganz ohne Sandbox; das ist billig und sicher auf dem Pi.
  Aufbau in Teilschritten wie überall.
- **Schaltungen**: Bausteine UND, ODER, NICHT, XOR, NAND; Leitungen leuchten bei 1, Lämpchen und 7-Segment-Anzeige
  zeigen das Ergebnis. Stufen: einzelne Gatter, Halbaddierer, Volladdierer, 4-Bit-Addierer, Multiplexer, Dekoder,
  7-Segment-Dekoder, später Flipflop und Zähler. Zwei Arten: "Verdrahten" (Bausteine stehen, nur Leitungen ziehen) und
  "Frei" (Bausteine selbst setzen). Prüfung über die ganze Wahrheitstabelle; Sterne nach Zahl der Bausteine und Tiefe
  (Laufzeit).
- **Turingmaschine**: Band mit Kopf, Zustandsdiagramm und Übergangstabelle, Schritt für Schritt abspielbar. Aufgaben:
  Binärzahl um eins erhöhen, Einsen zählen, Kopieren, Palindrom, Klammern prüfen, unäre Addition. Prüfung auf sichtbaren
  und versteckten Bändern mit Schrittgrenze; Sterne nach Zahl der Zustände und Schritte. Passt zur Ampel: beides sind
  Zustandsautomaten.

Entwürfe: `mockups/rechner-turing.html` und `mockups/rechner-schaltung.html`. Beide Spiele liegen unter der Sprache
"Maschinen" (`aufgaben/maschine/`), weil sie keinen Code schreiben.

### Turingmaschine (gebaut, 0.91.0)

- **Tabelle als Text** (`backend/src/codeschmiede/steuerung/turing.py`): eine Regel je Zeile, `Zustand liest ->
  schreibt geht danach`, Kommentare mit `#`, `_` ist leer. Der Text ist die eine Wahrheit; die Oberfläche zeigt ihn
  als Tabelle (Zustände als Eingaben, Zeichen und Richtung als Auswahl) oder als Text, Kommentare bleiben stehen.
- **Prüfung** (`pruefung/turing_pruefer.py`) im Backend ohne Sandbox: jedes Band läuft bis zu einem Endzustand,
  ohne passende Regel oder bis zur Grenze an Schritten. Ein Band stimmt, wenn die Maschine hält und das Band
  stimmt, bei Entscheidern der Endzustand (ja, nein). Teilschritte nennen Bänder beim Namen.
- **Sterne**: alle Bänder; höchstens so viele Zustände (ohne Endzustände); dazu höchstens so viele Zeilen.
- **Ansicht** `TuringView` in der gemeinsamen Ansicht: Tabelle mit Zustandsdiagramm (Zustände im Kreis, Regeln als
  beschriftete Pfeile, Zustand und Regel des Schritts leuchten), rechts das Band mit Kopf und Zustand und die Spur
  aller Schritte (Klick springt).
- **Levels** (`t001` bis `t007`, Pfad `turingmaschine`): Bits tauschen, Plus eins, Gerade Anzahl (erster
  Entscheider), Unär addieren, Klammern prüfen, Palindrom, Kopieren. Jede Musterlösung besteht mit drei Sternen,
  jeder Startcode scheitert am ersten Teilschritt (Tests in `backend/tests/test_turing.py`).

## Weitere Spielideen: Codes knacken und Flaggenjagd (Idee, vor dem Bau Entwürfe)

Vorschlag des Nutzers (25.10.2026): geheime Codes knacken und Hacking-Aufgaben, bei denen man eine versteckte Flagge
findet.

- **Codes knacken**: man schreibt einen Knacker statt zu raten. Stufen: Verschiebung (Cäsar), Ersetzung mit
  Häufigkeitsanalyse, Schlüsselwort (Vigenère), XOR mit kurzem Schlüssel, Kodierungen (Base64, Hex) als Schichten,
  kleine Schlüsselräume durchprobieren (vierstellige PIN gegen einen Prüfwert). Geprüft wird auf versteckten
  Geheimtexten mit anderen Schlüsseln, ein eingetippter Klartext zählt also nicht. Sterne nach Laufzeit und Kürze.
- **Flaggenjagd**: kleine, absichtlich verwundbare Systeme, die nur in der Sandbox leben: Anmeldung mit SQL-Einschleusung,
  Dateiausgabe mit Pfadausbruch, vorhersagbare Zugangsmarke, Rechenfehler im Warenkorb (negative Menge), Seite mit
  eingeschleustem Skript. Die Flagge wird je Spieler und Lauf zufällig erzeugt und lässt sich nicht weitergeben.
  Aufbau in Teilschritten: erst die Flagge finden, dann im zweiten Teilschritt die Lücke im Code schließen; die
  Prüfung greift dann erneut an und darf die Flagge nicht mehr finden. So lernt man Angriff und Abwehr zusammen.
- **Grenze**: nie gegen echte Systeme, kein Netz; alle Ziele sind eigene Übungssysteme in der Sandbox.

## Spielmechanik in der ganzen App

| Mechanik | Was sie belohnt | Wo sie erscheint |
|---|---|---|
| Stufe | gesammelte Punkte; Stufe k ab 25 * k * k Punkten, alle fünf Stufen ein Titel (Lehrling, Geselle, Schmied, Meister, Großmeister) | Ring im Kopf, Startseite |
| Meisterschaft | Anteil der erreichbaren Punkte je Sprache und je Spiel (Rang Bronze ab 25 %, Silber ab 50 %, Gold ab 80 %) | Startseite, Kopf der Aufgabenliste |
| Serie | Tage am Stück mit mindestens einer bestandenen Aufgabe oder einem Level; je sieben Tage ein Schutzschild (höchstens drei), der einen verpassten Tag auffängt | Startseite, Kopf |
| Tagesauftrag | drei kleine Ziele je Tag (eine Wiederholung oder neue Aufgabe, ein Spiel-Level, eine Aufgabe ohne Hinweis); alle drei geben 10 Punkte | Startseite |
| Erfolge | Meilensteine in drei Stufen (Bronze, Silber, Gold), Technik-Erfolge (CSS mit voller Deckung, Roboter in drei Zeilen), Spiel-Erfolge (Fall gelöst) | Startseite, eigene Seite |
| Eigene Bestwerte | kürzerer Code, schnellerer Lauf, mehr Sterne als beim letzten Mal | Ergebnis, Verlauf |
| Belohnungsmoment | nach dem Bestehen: Punkte, Fortschritt der Stufe, neue Erfolge, Bestwert, Stand des Tagesauftrags in einem Band | Ergebnisspalte, am Telefon im Schritt Ergebnis |
| Pfade als Strecken | Stationen mit Fortschritt, Abschluss eines Pfads ist ein Erfolg | Pfade |

Abgelehnt, weil es beim Lernen nicht hilft oder zu einem Nutzer nicht passt: Bestenlisten gegen andere, Duelle,
Punktabzug fürs Scheitern, Zeitdruck bei normalen Aufgaben.

## CSS-Bewertung nach Bild

- **Deckung**: gemessen auf der Bühne von 600 × 400 (`frontend/src/lib/css/buehne.ts`, für Anzeige und Messung
  dieselbe). Grund ist die häufigste Randfarbe des Zielbilds; Motiv sind alle Bildpunkte, die bei Ziel oder eigenem
  Bild nicht Grund sind. Die Deckung ist der Anteil des Motivs, der mit dem Ziel übereinstimmt (höchstens 6 Stufen je
  Farbkanal daneben). So deckt ein leeres Blatt nichts, auch wenn das Ziel nur ein kleiner Kreis ist; eine Deckung
  über die ganze Bühne hätte ihm 98 % gegeben. Der Ring zeigt sie in Prozent, das Abweichungsbild gleiche Punkte
  gedämpft, fehlende blau, zu viel oder falsche Farbe rot.
- **Punkte in zwei Teilen**: bis 60 % der Punkte für die Deckung (linear ab 80 % Deckung), die übrigen 40 % als
  Kürzebonus, aber nur ab 99 % Deckung, gemessen an der Zeichenzahl der Musterlösung (ohne Leerraum).
- **Sterne**: Bestehen ab 95 %; 99 %; 99 % und höchstens so kurz wie die Musterlösung.
- **Messung**: im Browser (`frontend/src/lib/css/deckung.ts`): beide Bilder werden über SVG-foreignObject gerastert,
  das keine Skripte ausführt und nichts nachlädt; beide Seiten laufen durch denselben Weg, Schrift und Kantenglättung
  stimmen also überein. Gemessen wird schon beim Tippen, Prüfen schickt die Messung ab. Bestehen, Sterne und Punkte
  leitet der Server daraus ab (`css_klon_pruefer.werte`), die Zeichen misst er selbst. Der Pi rendert keine Bilder.
- **Bestand**: alle 111 Musterlösungen decken ihr Ziel voll, kein Startcode besteht (gemessen beim Bau, 25.10.2026).

## Offen für die Freigabe

- Namen und Schwellen der Stufen und Ränge
- Länge einer Sprint-Runde und Zahl der Schutzschilde
- ob der Tagesauftrag mitzählt, wenn man nur Spiele spielt
