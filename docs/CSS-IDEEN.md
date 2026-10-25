# CSS-Aufgaben für die Codeschmiede: Ideensammlung

Grundlage für Aufgaben, bei denen ein Zielbild mit HTML und CSS nachgebaut wird. Bewertet wird die Deckung des gerenderten Ergebnisses mit dem Ziel (Pixelvergleich in Prozent) und die Kürze des Codes. Alle Ideen sind eigene Formulierungen; es wurden keine Aufgabentexte, Bilder oder Lösungen übernommen.

## Legende

- **Stufe**: Anfänger, Mittel, Fortgeschritten, Experte
- **Wenig Code**: Wie gut sich die Aufgabe für eine Kürzewertung eignet
  - *sehr gut*: viele Lösungswege, Kürzen ist ein eigenes Rätsel
  - *gut*: Kürzen lohnt sich, die Lösungswege liegen aber nah beieinander
  - *mäßig*: Länge streut wenig oder Kürzen geht auf Kosten der Lesbarkeit
  - *kaum*: Lernziel ist sauberer Aufbau, Kürze sollte nicht gewertet werden
- **Festes HTML**: Bei manchen Aufgaben ist das HTML vorgegeben und nur das CSS zählt (sonst sind Selektor- und Zustandsaufgaben sinnlos).

## Übersicht

| Kategorie | Ideen |
|---|---|
| 1. Grundformen und Geometrie | 9 |
| 2. Muster mit Verläufen | 12 |
| 3. Typografie und Textgestaltung | 10 |
| 4. Layout mit Flexbox | 8 |
| 5. Layout mit Grid | 9 |
| 6. Schatten, Licht und Tiefe | 8 |
| 7. Pseudo-Elemente | 7 |
| 8. Clip-Path und Masken | 9 |
| 9. Transformationen in 2D und 3D | 8 |
| 10. Animationen mit Standbild-Ziel | 9 |
| 11. Farbfunktionen, Filter und Mischmodi | 9 |
| 12. Container-Queries und Mehrbreiten-Ziele | 6 |
| 13. :has und andere neue Selektoren | 8 |
| 14. Zähler und Zählstile | 7 |
| 15. Rahmenkunst | 8 |
| 16. Fantasie-Logos aus einfachen Formen | 7 |
| 17. Icons | 9 |
| 18. Pixel-Art | 6 |
| 19. Ladeanzeigen als Standbild | 8 |
| 20. UI-Bausteine | 11 |
| 21. Optische Täuschungen | 8 |
| 22. Kniffe mit wenig Code | 9 |
| 23. Szenen und Illustrationen | 7 |
| 24. Alltags- und Spielgegenstände | 9 |
| 25. Diagramme und Datenanzeigen | 8 |
| 26. Kunststile nachempfinden | 7 |
| 27. Moderne Layout-Werkzeuge | 7 |
| 28. Zustände als Standbild | 6 |
| **Summe** | **229** |

---

## 1. Grundformen und Geometrie

Der Einstieg: wenige Farben, scharfe Kanten, gut messbar. Ideal für die ersten Pixelvergleiche.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 1 | Mittelpunkt finden | Ein einzelnes Quadrat exakt in der Mitte einer einfarbigen Fläche | Box-Modell, Standardrand von `body`, `margin:auto`, `place-items` | Anfänger | sehr gut |
| 2 | Drei Kreise im Dreieck | Drei gleich große Kreise, die sich gegenseitig berühren | `border-radius:50%`, absolute Positionierung, Rechnen mit `calc()` und `sqrt()` | Mittel | gut |
| 3 | Sichel | Mondsichel, entstanden aus einem Kreis, den ein versetzter Kreis in Hintergrundfarbe überdeckt | Überdeckung, `box-shadow` mit Versatz statt zweitem Element | Anfänger | sehr gut |
| 4 | Pfeilspitze aus Rändern | Ein Dreieck, das nach rechts zeigt | Transparente Ränder, Rahmenbreiten als Geometrie | Anfänger | sehr gut |
| 5 | Ei | Eiform mit oben schmalerer Rundung | `border-radius` mit acht Werten und Schrägstrich-Schreibweise | Mittel | sehr gut |
| 6 | Windrad aus Viertelkreisen | Vier Viertelkreise in vier Farben, um einen Punkt gedreht | Einseitiger Eckenradius, `transform-origin`, `rotate` | Mittel | gut |
| 7 | Offener Ring | Kreisring mit einer Lücke, wie ein liegendes C | Rand mit einer transparenten Seite, Drehung | Anfänger | sehr gut |
| 8 | Regelmäßiges Sechseck | Sechseck mit exakt gleichen Seiten | `aspect-ratio`, `clip-path: polygon()`, `cos()` für das Seitenverhältnis | Mittel | gut |
| 9 | Tropfen | Wassertropfen mit einer spitzen Ecke | Drei runde Ecken und eine spitze, Drehung um 45 Grad | Anfänger | sehr gut |

## 2. Muster mit Verläufen

Verläufe mit harten Farbstopps sind das wichtigste Werkzeug für kurzen Code. Kachelgröße und Ebenenreihenfolge sind die Kernlektionen.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 10 | Schachbrett | 8 x 8 Felder in zwei Farben | `repeating-conic-gradient`, `background-size` | Mittel | sehr gut |
| 11 | Warnstreifen | Schräge gelb-schwarze Bänder über die ganze Fläche | `repeating-linear-gradient`, harte Farbstopps | Anfänger | sehr gut |
| 12 | Versetzte Tupfen | Punkteraster, jede zweite Reihe um einen halben Abstand verschoben | `radial-gradient`, zwei Ebenen, `background-position` | Mittel | sehr gut |
| 13 | Zickzackband | Waagerechtes Zickzack in zwei Farben | `conic-gradient` mit `from`-Winkel, Kachelseitenverhältnis | Fortgeschritten | gut |
| 14 | Schottenkaro | Sich kreuzende Streifen in drei Breiten und Mischtönen an den Kreuzungen | Halbtransparente Streifenebenen, Mischen durch Überlagern | Mittel | gut |
| 15 | Wellenlinie | Durchgehende Welle aus abwechselnd oben und unten offenen Halbkreisen | Kreisausschnitte als Kacheln, zwei versetzte `radial-gradient` | Fortgeschritten | mäßig |
| 16 | Rautengitter | Rauten in zwei Farben, Kante an Kante | `conic-gradient` in einer Kachel, Seitenverhältnis der Kachel | Fortgeschritten | gut |
| 17 | Ziegelmauer | Ziegelreihen mit Fugen, jede zweite Reihe versetzt | Mehrere `linear-gradient`-Ebenen mit unterschiedlicher Position | Mittel | gut |
| 18 | Zielscheibe | Konzentrische Ringe in zwei Farben | `repeating-radial-gradient`, Abstände in px und Prozent | Anfänger | sehr gut |
| 19 | Sonnenstrahlen | Fächer aus abwechselnd gefärbten Strahlen aus der Mitte | `repeating-conic-gradient`, Winkel in `deg` und `turn` | Anfänger | sehr gut |
| 20 | Millimeterpapier | Feines und grobes Linienraster übereinander | Vier Ebenen, 1-px-Linien, Ebenenreihenfolge | Mittel | gut |
| 21 | Kariertes Tischtuch | Zwei halbtransparente Streifenrichtungen ergeben drei Farbtöne | Deckkraft in Verläufen, Überlagerung | Mittel | sehr gut |

## 3. Typografie und Textgestaltung

Achtung Bewertung: nur mit einer gebündelten, fest ausgelieferten Schrift und einheitlicher Kantenglättung (siehe Fallstricke). Text immer mit etwas Toleranz an den Glyphenkanten bewerten.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 22 | Initial | Absatz mit großem Anfangsbuchstaben über drei Zeilen | `::first-letter`, `initial-letter`, `float` | Mittel | mäßig |
| 23 | Umrissschrift | Großes Wort, nur als Kontur gezeichnet | `text-stroke` (mit Herstellerpräfix), transparente Füllung | Anfänger | gut |
| 24 | Verlaufsschrift | Überschrift, deren Buchstaben einen Farbverlauf zeigen | `background-clip: text`, transparente Textfarbe | Anfänger | gut |
| 25 | Stempel | Schräg gestelltes Wort in Großbuchstaben mit doppeltem Rahmen | `rotate`, `letter-spacing`, `text-transform`, `border-style: double` | Mittel | gut |
| 26 | Buchrücken | Senkrecht laufender Titel auf einem schmalen Streifen | `writing-mode: vertical-rl`, `text-orientation` | Mittel | gut |
| 27 | Ausgewogene Überschrift | Dreizeilige Überschrift mit gleich langen Zeilen | `text-wrap: balance`, `max-width` in `ch` | Mittel | mäßig |
| 28 | Zahlenkolonne | Rechtsbündige Beträge, Ziffern exakt untereinander | `font-variant-numeric: tabular-nums`, `text-align: end` | Mittel | mäßig |
| 29 | Bündige Textkante | Text, dessen Großbuchstaben exakt an einer Linie oben und unten anliegen | `text-box-trim`, `text-box-edge`, `line-height` | Fortgeschritten | mäßig |
| 30 | Leuchtschrift | Wort mit farbigem Glühen in mehreren Stufen | Mehrfacher `text-shadow` mit wachsender Unschärfe | Anfänger | gut |
| 31 | Ausgestanzter Text | Großes Wort, durch das ein Streifenmuster sichtbar wird | `mix-blend-mode: screen` oder `multiply`, alternativ `background-clip` | Fortgeschritten | gut |

## 4. Layout mit Flexbox

Hier lohnt oft festes HTML, damit das Layoutverständnis im Mittelpunkt steht.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 32 | Drei gleiche Säulen | Drei gleich breite Blöcke mit gleichen Abständen | `flex:1`, `gap` | Anfänger | gut |
| 33 | Kopfleiste | Zeichen links, drei Verweise rechts, alles mittig in der Höhe | `margin-left:auto`, `justify-content`, `align-items` | Anfänger | gut |
| 34 | Würfelseiten | Alle sechs Würfelseiten nebeneinander | `justify-content`, `align-self`, `flex-direction: column`, Umbruch | Mittel | mäßig |
| 35 | Knopf bleibt unten | Drei Karten mit verschieden langem Text, die Knöpfe auf gleicher Höhe | Spaltenrichtung, `margin-top:auto` | Anfänger | mäßig |
| 36 | Schlagwort-Wolke | Viele kleine Etiketten, die in mehrere Zeilen umbrechen | `flex-wrap`, `gap`, `inline-flex` | Anfänger | mäßig |
| 37 | Gespiegelte Reihenfolge | Elemente erscheinen in umgekehrter Reihenfolge, HTML unverändert | `order`, `row-reverse` (festes HTML) | Anfänger | gut |
| 38 | Dreispalter | Kopf, drei Spalten im Verhältnis 1:3:1, Fuß | `flex-basis`, `flex-grow`, Verschachtelung | Mittel | mäßig |
| 39 | Wachstumsrechnung | Balken mit exakt vorgegebenen Breiten, nur über Wachstumsfaktoren erreichbar | Verteilung von Restplatz durch `flex-grow` und `flex-shrink` | Fortgeschritten | gut |

## 5. Layout mit Grid

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 40 | Komposition mit Fugen | Asymmetrische Rechteckflächen in Rot, Blau, Gelb und Weiß mit schwarzen Fugen | `grid-template-areas`, `gap` als Fuge mit Hintergrundfarbe | Mittel | gut |
| 41 | Fotowand | Kacheln in drei Größen, lückenlos gefüllt | `span`, `grid-auto-flow: dense` | Mittel | mäßig |
| 42 | Kalenderblatt | Monat mit sieben Spalten, Monatserster versetzt, Wochenende eingefärbt | `grid-column-start`, `:nth-child` | Mittel | mäßig |
| 43 | Rechnertastatur | Tastenfeld mit doppelt breiter Null und doppelt hoher Gleich-Taste | `span` in beide Richtungen, feste Spuren | Mittel | mäßig |
| 44 | Gestapelt im selben Feld | Text liegt mittig auf einer Fläche, ohne absolute Positionierung | Mehrere Kinder in `grid-area: 1/1` | Mittel | gut |
| 45 | Selbstfüllende Kacheln | Bei fester Breite genau vier Spalten, Rest umbrechend | `repeat(auto-fill, minmax())` | Mittel | mäßig |
| 46 | Drei gewinnt | 3 x 3 Feld mit Linien nur zwischen den Feldern | `gap` mit Hintergrund als Linie | Anfänger | gut |
| 47 | Zeitungsseite | Dreispaltiger Fließtext, Überschrift über alle Spalten, Trennlinien | `columns`, `column-rule`, `column-span: all` | Mittel | mäßig |
| 48 | Diagonale Treppe | Quadrate entlang der Diagonalen eines 6 x 6 Rasters | Platzierung über `:nth-child`-Formeln | Mittel | gut |

## 6. Schatten, Licht und Tiefe

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 49 | Schwebende Karte | Karte mit weichem, natürlich wirkendem Schatten | Geschichtete `box-shadow` mit wachsender Unschärfe | Mittel | mäßig |
| 50 | Eingedrückte Taste | Taste, die in die Fläche gedrückt wirkt | `box-shadow: inset`, Licht oben links | Anfänger | gut |
| 51 | Weiche Kunststoffoptik | Erhabener Knopf in Hintergrundfarbe mit hellem und dunklem Schatten | Zwei Schatten in Nachbarfarben des Hintergrunds | Mittel | gut |
| 52 | Langer Schatten | Symbol mit flachem Diagonalschatten bis zum Rand | Viele gestaffelte Schatten oder ein gedrehter Verlauf | Fortgeschritten | mäßig |
| 53 | Papierstapel | Drei leicht versetzte Blätter hintereinander | Mehrere `box-shadow` mit Spread, abwechselnd Rand- und Papierfarbe | Mittel | sehr gut |
| 54 | Glänzende Kugel | Kugel mit Glanzpunkt oben links | `radial-gradient` mit verschobenem Mittelpunkt | Anfänger | sehr gut |
| 55 | Schatten folgt der Form | Ausgeschnittener Stern mit Schatten, der der Sternform folgt | `filter: drop-shadow()` im Unterschied zu `box-shadow` | Mittel | gut |
| 56 | Bodenschatten | Schwebende Kugel mit unscharfer Ellipse darunter | `filter: blur()` oder weicher `radial-gradient` | Anfänger | gut |

## 7. Pseudo-Elemente

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 57 | Sprechblase | Rundliche Blase mit Zipfel unten links | `::after` als Dreieck, Positionierung | Anfänger | gut |
| 58 | Zitat | Zitatblock mit übergroßem Anführungszeichen im Hintergrund | `content`, Schriftgröße, Positionierung | Anfänger | mäßig |
| 59 | Drei aus einem | Ampel mit drei Lichtern aus genau einem Element | `::before`, `::after`, gemeinsame Maße | Mittel | sehr gut |
| 60 | Textmarker | Wort mit schrägem Farbbalken hinter der unteren Hälfte | `::before` mit `z-index:-1`, `isolation` | Mittel | gut |
| 61 | Eckband | Schräges Band über der oberen rechten Ecke einer Karte | Gedrehtes Pseudo-Element, `overflow: hidden` | Mittel | gut |
| 62 | Trennlinie mit Wort | Waagerechte Linie, in der Mitte unterbrochen von einem Wort | `::before`, `::after`, Flex-Wachstum | Anfänger | gut |
| 63 | Beschriftung aus Attribut | Kästchen, deren Beschriftungen aus Attributwerten stammen (festes HTML) | `content: attr()` | Fortgeschritten | gut |

## 8. Clip-Path und Masken

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 64 | Fünfzackiger Stern | Gleichmäßiger Stern mit fünf Zacken | `clip-path: polygon()` mit zehn Punkten | Mittel | mäßig |
| 65 | Schräger Abschnitt | Farbiger Kopfbereich mit diagonaler Unterkante | Viereckiges `polygon()` | Anfänger | gut |
| 66 | Herz | Symmetrisches Herz | `path()` oder `shape()`, alternativ zwei Kreise und ein gedrehtes Quadrat | Mittel | gut |
| 67 | Lochblech | Fläche mit runden Löchern im Raster, Hintergrund scheint durch | `mask` mit gekacheltem `radial-gradient` | Fortgeschritten | gut |
| 68 | Briefmarke | Rechteck mit gezacktem Perforationsrand | `mask` mit `radial-gradient` an den Kanten | Fortgeschritten | mäßig |
| 69 | Segmentring | Ring aus acht Segmenten mit Lücken | Zwei Maskenebenen, `mask-composite` | Experte | gut |
| 70 | Tortenstück | Kreis mit fehlendem Viertel | `conic-gradient` oder `clip-path` | Anfänger | sehr gut |
| 71 | Eintrittskarte | Karte mit halbrunden Einkerbungen links und rechts | `mask` mit zwei `radial-gradient` | Mittel | gut |
| 72 | Wellenkante | Fläche, deren Unterkante als Welle ausläuft | `mask` aus wiederholten Kreisausschnitten | Fortgeschritten | mäßig |

## 9. Transformationen in 2D und 3D

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 73 | Kartenfächer | Fünf Karten, aus einer gemeinsamen Ecke aufgefächert | `rotate` mit `transform-origin` unten Mitte | Mittel | mäßig |
| 74 | Schräger Knopf | Parallelogramm-Knopf mit gerade stehendem Text | `skew` am Rahmen, Gegen-`skew` am Inhalt | Mittel | gut |
| 75 | Würfel in Schrägansicht | Würfel mit drei sichtbaren Flächen in drei Helligkeiten | `preserve-3d`, `rotateX`, `rotateY`, alternativ 2D mit `skew` | Fortgeschritten | mäßig |
| 76 | Spiegelung | Form mit nach unten ausblendendem Spiegelbild | `scaleY(-1)`, Maske mit Verlauf | Mittel | mäßig |
| 77 | Zehn nach zehn | Uhr mit zwei Zeigern auf 10:10 | Drehen um den Endpunkt, Winkelrechnung | Anfänger | gut |
| 78 | Fluchtende Fliesen | Gitterboden, der zum Horizont hin kleiner wird | `perspective`, `rotateX`, Fluchtpunkt | Fortgeschritten | gut |
| 79 | Stundenstriche | Ziffernblatt mit zwölf Strichen | Drehung in 30-Grad-Schritten oder `repeating-conic-gradient` | Mittel | gut |
| 80 | Aufgeklappte Karte | Halb geöffnete Faltkarte in Perspektive | `rotateY`, `perspective-origin`, Rückseiten | Experte | mäßig |

## 10. Animationen mit Standbild-Ziel

Bewertet wird ein festgelegter Zeitpunkt oder ein Filmstreifen aus mehreren Zeitpunkten (Deckung gemittelt). Der Bewerter setzt alle Animationen auf diese Zeitpunkte, bevor er das Bild aufnimmt.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 81 | Ball am Scheitelpunkt | Springender Ball, aufgenommen genau am höchsten Punkt | `@keyframes`, Prozentangaben, negative `animation-delay` | Mittel | gut |
| 82 | Pendel in drei Bildern | Filmstreifen: Pendel links, Mitte, rechts | `ease-in-out`, `alternate`, Mehrbild-Ziel | Fortgeschritten | mäßig |
| 83 | Springender Zeiger | Zeiger, der in Sprüngen läuft; Bild nach 2,5 Sekunden | `steps()`, Zeitrechnung | Fortgeschritten | gut |
| 84 | Gestaffelte Balken | Fünf Balken mit versetzter Phase, Momentbild zeigt eine Treppe | Verzögerung je Index über Variablen oder `sibling-index()` | Fortgeschritten | gut |
| 85 | Farbreise | Fläche durchläuft Farben; Momentbild zeigt einen Zwischenton | Farbinterpolation, `in oklch` | Fortgeschritten | gut |
| 86 | Drehender Verlauf | Rand mit umlaufendem Verlauf, Momentbild bei 90 Grad | `@property` registriert einen Winkel, damit er animierbar ist | Experte | mäßig |
| 87 | Schreibmaschine | Text halb getippt mit Schreibmarke | Breite in `ch`, `steps()`, `overflow: hidden` | Mittel | gut |
| 88 | Umlaufbahn | Planet auf Kreisbahn, Momentbild bei einem Achtel | `rotate`, `translate`, Rückdrehung | Fortgeschritten | gut |
| 89 | Weg entlang der Kurve | Punkt auf einer geschwungenen Bahn, drei Momentbilder | `offset-path`, `offset-distance` | Experte | mäßig |

## 11. Farbfunktionen, Filter und Mischmodi

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 90 | Farbtreppe | Sieben Felder von hell bis dunkel aus einer Grundfarbe | `color-mix()` mit Weiß und Schwarz in Prozentstufen | Mittel | gut |
| 91 | Gegenfarbe | Zwei Felder, das zweite in der Komplementärfarbe | Relative Farbsyntax: `oklch(from ... l c calc(h + 180))` | Fortgeschritten | gut |
| 92 | Farbkreis | Vollständiger Farbkreis | `conic-gradient` mit `in hsl longer hue` | Mittel | sehr gut |
| 93 | Mengendiagramm | Drei überlappende Kreise, Schnittflächen in Mischfarben | `mix-blend-mode: multiply` | Mittel | gut |
| 94 | Verlauf ohne graue Mitte | Zwei Verläufe derselben Farben, einer mit trüber, einer mit klarer Mitte | Interpolationsfarbraum `in srgb` gegenüber `in oklab` | Fortgeschritten | sehr gut |
| 95 | Gealtertes Muster | Buntes Muster in Sepia mit erhöhtem Kontrast | `filter`-Ketten, Reihenfolge der Filter | Mittel | gut |
| 96 | Verschmelzende Tropfen | Zwei Kreise, die an der Berührung weich zusammenfließen | `blur` plus `contrast` am Elternelement | Experte | mäßig |
| 97 | Umkehrstreifen | Text, der über einem Balken seine Farbe umkehrt | `mix-blend-mode: difference` | Mittel | gut |
| 98 | Hell und Dunkel | Dieselbe Karte zweimal: links helles, rechts dunkles Farbschema | `light-dark()`, `color-scheme` je Container | Fortgeschritten | mäßig |

## 12. Container-Queries und Mehrbreiten-Ziele

Das Zielbild zeigt dieselbe Komponente in mehreren fest vorgegebenen Breiten, oder der Bewerter rendert die Lösung in mehreren Fenstergrößen und mittelt die Deckung.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 99 | Eine Karte, drei Breiten | Dieselbe Karte schmal gestapelt, mittel nebeneinander, breit mit Zusatzspalte | `container-type`, `@container` | Mittel | mäßig |
| 100 | Mitwachsende Überschrift | Überschrift, deren Größe mit dem Container wächst, mit Ober- und Untergrenze | `cqi`, `clamp()` | Mittel | gut |
| 101 | Hervorhebung per Stilabfrage | Zwei Karten, nur eine mit Rahmen und Band, gesteuert über eine Variable | `@container style(--variante: ...)` | Fortgeschritten | mäßig |
| 102 | Bereich statt Fenster | Seitenleiste und Hauptbereich; nur der Hauptbereich bricht sein Raster um | Abfrage auf den Bereich statt auf das Fenster | Fortgeschritten | mäßig |
| 103 | Hoch oder quer | Kachel ordnet Bild und Text je nach Seitenverhältnis des Containers um | `orientation` in `@container` | Fortgeschritten | mäßig |
| 104 | Ohne Medienabfragen | Lösung wird in drei Fensterbreiten gerendert, alle müssen passen | `clamp()`, `min()`, `max()` | Fortgeschritten | gut |

## 13. :has und andere neue Selektoren

Nur mit festem HTML sinnvoll; das CSS zählt.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 105 | Karte mit Bild | Zwei Karten: die mit Bild zweispaltig, die ohne einspaltig | `:has(img)` | Mittel | gut |
| 106 | Anzahl bestimmt das Raster | Drei Listen mit 3, 4 und 6 Einträgen, jede mit eigener Spaltenzahl | Mengenabfragen mit `:has(:nth-child(n+5))` | Fortgeschritten | gut |
| 107 | Vorgänger einfärben | In einer Reihe ist das Element vor dem markierten hervorgehoben | `:has(+ .aktiv)` | Mittel | sehr gut |
| 108 | Angehakter Bereich | Formularabschnitte, deren Hintergrund sich bei angehaktem Kästchen färbt | `:has(:checked)` | Mittel | gut |
| 109 | Jedes dritte einer Sorte | Gemischte Liste, nur jedes dritte Element einer Klasse markiert | `:nth-child(3n of .klasse)` | Fortgeschritten | sehr gut |
| 110 | Selektoren eindampfen | Sechs Elemente mit vier Gestaltungen; Ziel ist die kürzeste Selektorliste | `:is()`, `:where()`, `:not()` | Mittel | sehr gut |
| 111 | Leere sichtbar machen | Raster, in dem leere Felder gestrichelt und Einzelkinder zentriert sind | `:empty`, `:only-child` | Anfänger | gut |
| 112 | Gegen den Grundstil | Vorgegebenes, unveränderliches CSS plus Zielbild; die eigene Regel muss sich durchsetzen | Spezifität, `@layer` | Fortgeschritten | mäßig |

## 14. Zähler und Zählstile

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 113 | Kapitelnummern | Verschachtelte Gliederung 1, 1.1, 1.2, 2 | `counter-reset`, `counters()` | Mittel | mäßig |
| 114 | Eigene Aufzählungszeichen | Liste mit wiederkehrender Folge aus drei Symbolen | `@counter-style` mit `system: cyclic` | Mittel | gut |
| 115 | Nummern im Kreis | Schrittliste mit Zahlen in farbigen Kreisen | `::before`, `counter()` | Anfänger | gut |
| 116 | Rückwärts | Countdown-Liste von 10 bis 1 | Startwert und negativer `counter-increment`, `reversed` | Mittel | gut |
| 117 | Führende Nullen | Nummern 01 bis 12 | `@counter-style` mit `pad` | Fortgeschritten | gut |
| 118 | Zählt die Haken | Anzeige, wie viele Kästchen angehakt sind (festes HTML) | `counter-increment` nur bei `:checked` | Fortgeschritten | gut |
| 119 | Römische Gliederung | Liste mit römischen Ziffern und gestalteten Markern | `list-style-type: upper-roman`, `::marker` | Anfänger | gut |

## 15. Rahmenkunst

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 120 | Doppelrahmen | Box mit zwei Rahmen und Abstand dazwischen | `outline`, `outline-offset`, `border` | Anfänger | sehr gut |
| 121 | Runder Verlaufsrahmen | Abgerundete Karte mit Rahmen im Farbverlauf | Zwei Hintergrundebenen, `background-clip` für Innenfläche und Rand | Mittel | gut |
| 122 | Eigene Strichelung | Gestrichelter Rahmen mit langen Strichen und kurzen Lücken | Verläufe an den vier Kanten statt `dashed` | Fortgeschritten | mäßig |
| 123 | Eckwinkel | Nur die vier Ecken einer Box sind markiert, wie ein Sucher | Acht kleine Verlaufsebenen oder Maske | Fortgeschritten | gut |
| 124 | Gekachelter Bilderrahmen | Rahmen mit wiederholtem Muster und gefüllter Mitte | `border-image` mit Verlauf, `slice`, `fill` | Experte | mäßig |
| 125 | Fasen und Kehlen | Karte mit abgeschrägten und nach innen gewölbten Ecken | `corner-shape` (sehr neu), alternativ `clip-path` | Fortgeschritten | sehr gut |
| 126 | Klecks | Organische, weiche Form | `border-radius` mit acht unterschiedlichen Werten | Mittel | sehr gut |
| 127 | Vierfarbring | Ring in vier Farben, je Viertel eine | Vier Randfarben bei rundem Element | Anfänger | sehr gut |

## 16. Fantasie-Logos aus einfachen Formen

Nur erfundene Zeichen verwenden, keine echten Marken nachbauen.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 128 | Bergsonne | Sonne hinter zwei Bergdreiecken, alles in einem Kreis | `overflow: hidden` mit Rundung, Überlagerung | Mittel | gut |
| 129 | Monogramm | Zwei Buchstaben aus Balken gebaut, ohne Text | Rechtecke, Drehung, Raster | Mittel | gut |
| 130 | Verschränkte Ringe | Zwei Ringe, die sich gegenseitig durchdringen | Halbringe auf verschiedenen Ebenen, `z-index` | Experte | mäßig |
| 131 | Blatt | Blatt mit Mittelrippe | Zwei gegenüberliegende runde Ecken, gedrehte Linie | Anfänger | sehr gut |
| 132 | Wabenwürfel | Sechseckiger Würfel aus drei Rauten in drei Tönen | `conic-gradient` oder drei verzerrte Flächen | Fortgeschritten | gut |
| 133 | Wortmarke mit Bogen | Kurzes Wort mit Bogen darunter | Halber Ring, Textausrichtung | Mittel | mäßig |
| 134 | Vierfeld-Kreuz | Vier farbige Quadrate mit Fugen, um 45 Grad gedreht | `conic-gradient` mit Fugen, `rotate` | Mittel | sehr gut |

## 17. Icons

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 135 | Lupe | Ring mit schrägem Griff | `::after`, Drehung, Rand | Anfänger | sehr gut |
| 136 | Menü und Schließen | Drei Balken und daneben ein Kreuz | Drei Balken aus einem Verlauf oder Schatten, zwei gedrehte Balken | Anfänger | sehr gut |
| 137 | Abspieltasten | Abspielen, Pause, Stopp nebeneinander | Dreieck aus Rändern, zwei Balken aus einem Verlauf | Anfänger | sehr gut |
| 138 | Haken im Kreis | Bestätigungshaken in einem Kreis | Winkel aus zwei Rändern, gedreht | Anfänger | sehr gut |
| 139 | Funkbögen | Punkt mit drei Viertelbögen darüber | `repeating-radial-gradient` auf ein Viertel beschnitten | Mittel | gut |
| 140 | Batterie mit Füllstand | Batterie zu 60 % gefüllt, mit Pol-Kappe | Rand, `::after`, Verlauf mit Variable für den Füllstand | Mittel | gut |
| 141 | Briefumschlag | Umschlag mit Klappe | Diagonale Verläufe zu den Ecken | Mittel | gut |
| 142 | Zahnrad | Zahnrad mit acht Zähnen und Loch | `repeating-conic-gradient` für Zähne, Maske für das Loch | Experte | gut |
| 143 | Glocke mit Zähler | Glocke mit rotem Zahlpunkt oben rechts | Positionierung, Rand in Hintergrundfarbe als Aussparung | Mittel | mäßig |

## 18. Pixel-Art

Spannend für die Kürzewertung: die naheliegende Lösung mit einem Schatten je Pixel ist lang, Zeilen- und Blockverläufe sind deutlich kürzer.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 144 | Pixelherz | Herz aus etwa 9 x 8 groben Pixeln | `box-shadow`-Liste ohne Unschärfe | Mittel | mäßig |
| 145 | Eigene Spielfigur | Kleine Fantasiefigur in vier Farben | Zusammenfassen gleichfarbiger Flächen zu Rechtecken | Fortgeschritten | gut |
| 146 | Zeilen statt Punkte | Dasselbe Motiv wie eine Schattenlösung, aber zeilenweise mit Verläufen | `linear-gradient` mit harten Stopps je Zeile | Fortgeschritten | gut |
| 147 | Siebensegmentanzeige | Die Ziffern 2 und 8 in Segmentoptik | Segmente als Verlaufsebenen | Mittel | gut |
| 148 | Pixelgröße als Variable | Motiv in vierfacher Größe | Variable für Pixelmaß, `scale` oder `zoom` | Mittel | gut |
| 149 | Raster aus Elementen | 8 x 8 Elemente, Färbung nur über Formeln | `:nth-child`-Formeln im Grid | Anfänger | mäßig |

## 19. Ladeanzeigen als Standbild

Viele Ladeanzeigen kommen mit einem Element und einem Verlauf aus. Als Standbild bewertet, als Bonus auch im Filmstreifen.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 150 | Drei Punkte | Drei Punkte, der mittlere größer | Wiederholter `radial-gradient` oder `box-shadow` | Anfänger | sehr gut |
| 151 | Kreisel | Ring mit einem farbigen Viertel | Unterschiedliche Randfarben | Anfänger | sehr gut |
| 152 | Speichenrad | Zwölf Speichen mit abnehmender Deckkraft | `conic-gradient` plus Maske | Fortgeschritten | gut |
| 153 | Streifenbalken | Balken zu 65 % gefüllt mit schrägen Streifen | Zwei Ebenen, Hintergrundgröße | Mittel | gut |
| 154 | Ring mit Prozentzahl | Ring zu 72 % gefüllt, Zahl in der Mitte | `conic-gradient`, Maske für das Loch, Text zentriert | Mittel | gut |
| 155 | Pegelbalken | Fünf Balken unterschiedlicher Höhe aus einem Element | Mehrere Verläufe mit eigener Größe und Position | Mittel | gut |
| 156 | Platzhalterkarte | Graue Blöcke für Bild, Titel und Zeilen mit hellem Schimmer | Ein Element, viele Hintergrundebenen | Fortgeschritten | gut |
| 157 | Sanduhr | Zwei Dreiecke Spitze an Spitze, oben weniger Sand als unten | Ränder oder `clip-path`, Teilfüllung | Mittel | gut |

## 20. UI-Bausteine

Hier geht es eher um sauberen Aufbau; Kürze nur bewerten, wenn ausdrücklich ein Kurzmodus gewählt ist.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 158 | Kippschalter | Zwei Schalter, einer aus, einer an | `appearance: none`, `::before` als Knopf, `:checked` | Mittel | mäßig |
| 159 | Profilkarte | Runder Bildplatzhalter, Name, Rolle, zwei Knöpfe | Flex, Abstände, Hierarchie | Anfänger | kaum |
| 160 | Preistabelle | Drei Tarife, der mittlere größer und mit Band | Grid, Hervorhebung, Ausrichtung | Mittel | kaum |
| 161 | Schwebende Beschriftung | Eingabefeld, dessen Beschriftung im oberen Rand sitzt | `:placeholder-shown`, `:focus-within`, Positionierung | Fortgeschritten | kaum |
| 162 | Schieberegler | Gestalteter Regler mit Spur und rundem Griff | `accent-color` als Kurzweg, herstellerpräfixierte Pseudo-Elemente | Fortgeschritten | mäßig |
| 163 | Reiter | Aktiver Reiter verschmilzt mit dem Inhaltsbereich | Negativer Rand, fehlende Unterkante | Mittel | mäßig |
| 164 | Pfadleiste | Brotkrumen als ineinandergreifende Pfeilformen | `clip-path`, negative Abstände | Mittel | gut |
| 165 | Hinweisleiste | Meldung mit Farbstreifen links, Symbol und Schließkreuz | Flex, Rand nur links | Anfänger | mäßig |
| 166 | Sternbewertung | 3,5 von 5 Sternen | Sterne als Maske, Füllung per Verlauf bis 70 % | Fortgeschritten | gut |
| 167 | Eigene Kästchen | Kontrollkästchen und Optionsfelder in eigener Optik | `appearance: none`, Haken per Verlauf oder `clip-path` | Mittel | mäßig |
| 168 | Dialog | Zentrierter Dialog über abgedunkeltem Hintergrund | `dialog`, `::backdrop`, Schatten | Mittel | mäßig |

## 21. Optische Täuschungen

Lehrreich und überraschend: kleine Codes mit großer Wirkung, dazu ein Gesprächsanlass über Wahrnehmung.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 169 | Gleiche Grautöne | Zwei identische graue Quadrate auf hellem und dunklem Grund | Simultankontrast, harte Verlaufsstopps | Anfänger | sehr gut |
| 170 | Pfeilenden (Müller-Lyer) | Zwei gleich lange Linien mit nach innen und nach außen zeigenden Enden | Pseudo-Elemente, gedrehte Ränder | Mittel | gut |
| 171 | Umgebung täuscht (Ebbinghaus) | Zwei gleich große Kreise, einer von großen, einer von kleinen Kreisen umringt | Viele `radial-gradient` an berechneten Positionen | Fortgeschritten | gut |
| 172 | Versetzte Fliesen (Café-Wand) | Schwarz-weiße Reihen mit halbem Versatz und grauen Fugen | Mehrere Streifenebenen | Mittel | gut |
| 173 | Scheinkontur (Kanizsa) | Drei angeschnittene Kreise lassen ein weißes Dreieck erscheinen | `conic-gradient`-Ausschnitte | Mittel | gut |
| 174 | Unmögliches Dreieck | Drei schattierte Balken, scheinbar räumlich verschränkt | `clip-path`, Drehungen, Ebenen | Experte | mäßig |
| 175 | Graue Punkte (Hermann-Gitter) | Schwarze Quadrate mit weißen Straßen | Ein einziger Verlauf als Gitter | Anfänger | sehr gut |
| 176 | Scheinbewegung | Ruhendes Muster aus Ringen, das zu kreisen scheint | `repeating-conic-gradient` mit Helligkeitssägezahn | Fortgeschritten | gut |

## 22. Kniffe mit wenig Code

Aufgaben, deren Lernziel ausdrücklich die Kürze ist. Gut als eigene Spielklasse.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 177 | Null Elemente | Zielbild nur aus Hintergründen von `html` und `body` | Wurzelelemente gestalten | Mittel | sehr gut |
| 178 | Rahmen statt Element | Rechteck im Rechteck | Rand von `body` plus Standardabstand | Anfänger | sehr gut |
| 179 | Schatten als Kopie | Fünf gleiche Kreise in einer Reihe aus einem Element | `box-shadow` als Vervielfältiger | Anfänger | sehr gut |
| 180 | Kürzeste Einheit | Ziel mit Maßen, die in `vw`, `vh` oder `em` kürzer sind | Einheiten umrechnen | Mittel | sehr gut |
| 181 | Kürzeste Farbe | Ziel mit Farben, die als Name oder dreistelliger Hexwert kürzer sind | Farbschreibweisen | Anfänger | sehr gut |
| 182 | Nützliche Vorgaben | Formen, die Standardelemente schon mitbringen (Linie, Rahmen, Abstand) | Browser-Standardstile kennen und nutzen | Fortgeschritten | sehr gut |
| 183 | Ein Hintergrund, viele Formen | Vier Rechtecke in verschiedenen Farben | Eine `background`-Angabe mit Größe und Position je Ebene | Fortgeschritten | sehr gut |
| 184 | Eine Farbe für alles | Rand, Schatten und Verlauf in derselben Farbe | `currentColor`, Erbung | Mittel | sehr gut |
| 185 | Kurzschreibweisen | Mehrere absolut platzierte Flächen | `inset`, `place-items`, Kurzformen von `margin` | Anfänger | sehr gut |

## 23. Szenen und Illustrationen

Größere Motive, gut als Wochenaufgabe oder Abschluss einer Staffel.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 186 | Sonnenuntergang am Meer | Verlaufshimmel, halbe Sonne am Horizont, Wellenlinien | Verläufe, Überdeckung, Muster | Mittel | gut |
| 187 | Nachthimmel | Mondsichel und viele kleine Sterne | Punktmuster mit Schatten oder Verläufen | Mittel | gut |
| 188 | Stadtsilhouette | Hochhäuser verschiedener Höhe mit Fensterrastern | Ein Verlauf je Haus, Fenster als Muster | Fortgeschritten | gut |
| 189 | Dampfende Tasse | Tasse mit Henkel, Untertasse, drei Dampfbögen | Ring als Henkel, Ellipsen, gebogene Ränder | Mittel | mäßig |
| 190 | Kaktus im Topf | Kaktus mit zwei Armen in trapezförmigem Topf | Abgerundete Rechtecke, Trapez per `clip-path` | Mittel | gut |
| 191 | Leuchtturm | Gestreifter Turm mit Lichtkegel in der Nacht | Trapez, Streifen, `conic-gradient` mit Transparenz | Fortgeschritten | gut |
| 192 | Regen am Fenster | Fensterkreuz, dahinter schräger Strichregen | `repeating-linear-gradient`, Ebenen | Mittel | gut |

## 24. Alltags- und Spielgegenstände

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 193 | Spielkarte | Herz-Ass mit Eckzeichen oben links und kopfstehend unten rechts | `rotate(180deg)`, Pseudo-Elemente | Mittel | mäßig |
| 194 | Würfel mit fünf Augen | Würfelseite mit fünf Augen | Fünf Punkte in einem Hintergrund | Mittel | sehr gut |
| 195 | Dominostein | Zwei Hälften mit Trennstrich, links drei, rechts vier Augen | Verlaufsebenen, Spiegelung | Mittel | gut |
| 196 | Grüne Ampel | Gehäuse mit drei Lichtern, nur Grün leuchtet | Glühen per Schatten, gedämpfte Farben | Anfänger | sehr gut |
| 197 | Bahnhofsuhr | 60 Minutenstriche, kräftige Stundenstriche, drei Zeiger | Zwei `repeating-conic-gradient`, Maske | Fortgeschritten | gut |
| 198 | Klaviertasten | Eine Oktave weißer und schwarzer Tasten | Schwarze Tasten im Muster 2 und 3 per Verlauf | Fortgeschritten | gut |
| 199 | Strichcode | Unregelmäßige Balken verschiedener Breite | Ein Verlauf mit vielen harten Stopps | Mittel | mäßig |
| 200 | Drehwürfelseite | 3 x 3 farbige Felder mit schwarzen Fugen | Grid oder Verläufe, `gap` als Fuge | Anfänger | gut |
| 201 | Kassette | Gehäuse, Fenster, zwei Spulen | Ringe, Rundungen, Verschachtelung | Fortgeschritten | mäßig |

## 25. Diagramme und Datenanzeigen

Datenwerte als Variablen im HTML vorgeben, das CSS rechnet die Darstellung aus.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 202 | Kreisdiagramm | Vier Anteile in vier Farben | `conic-gradient` mit harten Stopps | Anfänger | sehr gut |
| 203 | Ringdiagramm | Ring mit drei Anteilen und Summe in der Mitte | Maske für das Loch | Mittel | gut |
| 204 | Säulen aus Variablen | Sechs Säulen, Höhen aus `--wert` am Element | `calc()` mit Variablen | Mittel | mäßig |
| 205 | Linienzug | Liniendiagramm mit fünf Messpunkten | `clip-path: polygon()` aus Werten | Fortgeschritten | mäßig |
| 206 | Gestapelter Balken | Ein Balken, aufgeteilt in drei Anteile | `flex-grow` aus Variablen | Anfänger | gut |
| 207 | Tacho | Halbkreisskala mit Nadel bei 70 % | Halber `conic-gradient`, Nadel drehen | Mittel | gut |
| 208 | Wärmekarte | 7 x 5 Felder, Farbe nach Wert zwischen zwei Farben | `color-mix(in oklch, ...)` mit Variable | Fortgeschritten | mäßig |
| 209 | Schrittanzeige | Kreise mit Verbindungslinie, erledigte Schritte gefüllt | Zähler, Pseudo-Elemente, Zustände | Mittel | mäßig |

## 26. Kunststile nachempfinden

Stile, keine konkreten Werke: eigene Kompositionen im Geist einer Epoche.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 210 | Grundformen der Moderne | Kreis, Dreieck und Quadrat in Grundfarben auf hellem Grund | Formen kombinieren, Ebenen | Anfänger | sehr gut |
| 211 | Gewölbtes Schachbrett | Schachbrett, das in der Mitte nach vorn gewölbt wirkt | Verzerrung durch radial gesteuerte Feldgrößen | Experte | mäßig |
| 212 | Farbfelder | Zwei weich verschwommene Rechtecke auf Farbgrund | `filter: blur()`, gedämpfte Töne | Mittel | gut |
| 213 | Rautenmosaik | Mosaik aus Rauten in fünf Tönen | Mehrere `conic-gradient`-Ebenen | Fortgeschritten | gut |
| 214 | Holzschnittwellen | Mehrere Reihen stilisierter Wellen in zwei Farben | Wiederholte Kreisausschnitte, Versatz | Fortgeschritten | mäßig |
| 215 | Rasterpunkte | Halbtonraster, Punkte werden zur Seite hin größer | `radial-gradient` plus Maske mit linearem Verlauf | Experte | gut |
| 216 | Scherenschnitt | Hintereinander gestaffelte Hügel in abgestuften Tönen | Ellipsen, Ebenen, Farbabstufung | Mittel | gut |

## 27. Moderne Layout-Werkzeuge

Neuere Eigenschaften; nur stellen, wenn die Bewertungs-Engine sie beherrscht.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 217 | Hinweis am Anker | Hinweisblase mit Pfeil sitzt über einem Knopf | `anchor-name`, `position-anchor`, `position-area` | Fortgeschritten | mäßig |
| 218 | Bündige Karten | Drei Karten, Titel, Text und Knöpfe jeweils auf gleicher Höhe | `subgrid` | Fortgeschritten | mäßig |
| 219 | Beide Leserichtungen | Dieselbe Komponente einmal links-nach-rechts, einmal rechts-nach-links | Logische Eigenschaften wie `margin-inline-start` | Mittel | gut |
| 220 | Feste Seitenverhältnisse | Kacheln in 16:9, 1:1 und 4:3 ohne Höhenangaben | `aspect-ratio` | Anfänger | gut |
| 221 | Verschachtelte Regeln | Bekannte Gestaltung, aber mit Verschachtelung kürzer geschrieben | CSS-Verschachtelung mit `&` | Mittel | gut |
| 222 | Ebenen ordnen | Zielbild entsteht nur bei richtiger Reihenfolge vorgegebener Ebenen | `@layer`-Reihenfolge | Fortgeschritten | mäßig |
| 223 | Punkte auf dem Kreis | Acht Punkte gleichmäßig auf einem Kreis | `sin()`, `cos()`, `sibling-index()` oder Variablen | Experte | gut |

## 28. Zustände als Standbild

Der Bewerter erzwingt den Zustand (Überfahren, Fokus, Auswahl) über die Fernsteuerungsschnittstelle des Browsers, für Ziel und Lösung gleich.

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 224 | Karte beim Überfahren | Gehobene Karte mit stärkerem Schatten und Farbwechsel | `:hover`, `translate`, Schatten | Mittel | mäßig |
| 225 | Tastaturfokus | Knopf mit deutlichem Fokusring mit Abstand | `:focus-visible`, `outline-offset` | Anfänger | gut |
| 226 | Aufgeklappt | Aufklappbereich offen, Pfeil gedreht | `details`, `summary`, `[open]` | Mittel | mäßig |
| 227 | Ungültige Eingabe | Feld mit roter Kontur und Hinweistext darunter | `:user-invalid`, Hinweis per `:has()` | Fortgeschritten | mäßig |
| 228 | Markierter Text | Absatz, in dem ein Wort farbig markiert ist | `::selection` | Anfänger | gut |
| 229 | Platzhaltertext | Leeres Feld mit kursivem, gedämpftem Platzhalter | `::placeholder` | Anfänger | gut |

---

## Farben der Aufgaben

Jede Aufgabe hat ihre eigene, in sich stimmige Farbgebung, nicht immer denselben Akzent der App (Nutzer 25.10.2026).
Der Grund darf dunkel bleiben, Akzente wechseln: Bernstein, Lavendel, Lachs, Azur, Rosa, Oliv, Magenta, Gold und
mehr; Farbnamen im Text passen zum Farbwert. Die alten Aufgaben sind so umgefärbt.

## Spielerische Grundlagenübungen zu Flexbox und Grid

Vorschlag des Nutzers (25.10.2026): wie die bekannten Lernspiele im Netz, aber ganz eigen gebaut. Sie gehören zu den
CSS-Übungen und kommen vor den spielerischen Herausforderungen: erst die Grundlagen üben, dann knobeln.

- **Form**: eine kleine Welt mit Figuren und Zielfeldern (eigene Bildwelt, etwa Boote und Liegeplätze für Flexbox,
  Beete und Setzlinge für Grid). Bearbeitet werden nur die Eigenschaften des Behälters bzw. der Elemente in einem
  kleinen Feld; die Figuren rücken sofort an ihren Platz. Geschafft ist ein Level, wenn jede Figur auf ihrem Feld
  steht; das prüft die Bilddeckung wie bei den Nachbauten.
- **Aufbau**: je Level genau eine neue Eigenschaft (justify-content, align-items, flex-direction, order, flex-wrap,
  align-self, align-content; bei Grid Spalten, Zeilen, Linien, span, Bereiche, fr, repeat), dann gemischte Level.
  Aufbauend in Teilschritten wie überall.
- **Vor dem Bau**: Entwürfe; Einordnung zwischen Lehreinführung und Herausforderungen im Aufbaukurs.

## Bausteine aus eigenen Projekten

Neben den Spielereien oben werden echte Bausteine aus den eigenen Projekten nachgebaut: Knöpfe, Karten, Leisten, Anzeigen, Rohstoff- und Fortschrittsbalken, Reiter, Abzeichen. Erste Quelle ist die Gestaltung von Orbit, weitere eigene Apps folgen. Ziel ist Lernen und Besserwerden, nicht Frust. Die Ideen unten sind vorläufig und werden vor dem Bau an den echten Bausteinen abgeglichen.

### Fairnessregeln

- **Grafik wird mitgegeben**: Komplexe Bildteile (Pixelgrafik, Planeten, Hintergrundbilder, Kopfbilder, aufwendige Symbole) liegen der Aufgabe als Bild bei und stehen in Ziel und Vorlage gleich. Sie verfälschen die Deckung nicht, und niemand muss ein Foto aus Verläufen nachmalen.
- **Halbfertige Vorlage**: HTML-Gerüst, eingebundene Bilder, Schriften und Grundmaße sind vorgegeben. Ergänzt wird der fachliche Rest, um den es in der Aufgabe geht (Verlaufsrahmen, Leuchten, Raster, Zustände, Abstände).
- **Kürze nur für den eigenen Teil**: Gezählt werden nur die Zeichen, die der Lernende hinzufügt; die Vorlage zählt nicht mit.
- **Eingebundene Bilder nur aus der Aufgabe**: Mitgegebene Bilder stehen unter festen Namen bereit; eigene `url()` mit Daten oder Adressen bleiben in der strengen Klasse gesperrt (siehe Fallstrick 11).
- **Schriften der Vorlage**: Die Schriften des Originals werden in der Prüfumgebung mitgeliefert, sonst ist volle Deckung unmöglich.
- **In Stufen statt am Stück**: Erst ein Einzelteil (ein Knopf in einem Zustand), dann die Karte, dann der Bereich. Jede Stufe ist eine eigene Aufgabe mit eigener Bestehensgrenze.
- **Bestehensgrenze passend zur Stufe**: Bei Bausteinen mit Bildern, Schatten und Glättung eine erreichbare Grenze wählen und mit der Musterlösung messen (siehe Fallstrick 10); volle Punkte erst bei hoher Deckung.
- **Hilfen**: Das Abweichungsbild zeigt, wo es noch hakt; gestufte Hinweise nennen erst die Eigenschaft, dann den Wertebereich, nie die Lösung.

### Ideen

| # | Titel | Zielbild | Lehrt | Stufe | Wenig Code |
|---|---|---|---|---|---|
| 1 | Leuchtknopf | Ein Knopf mit Verlaufsrand und weichem Leuchten, Symbol und Schrift vorgegeben | `border-image` oder Verlauf im Hintergrund, mehrere `box-shadow` | Mittel | gut |
| 2 | Knopf in drei Zuständen | Derselbe Knopf normal, überfahren und gesperrt nebeneinander | Zustandsklassen, `opacity`, `filter`, gemeinsame Variablen | Mittel | gut |
| 3 | Rohstoffleiste | Eine Zeile mit drei Rohstoffen: Symbol (vorgegeben), Menge, Füllbalken | Flexbox, `tabular-nums`, Balken mit Verlauf und Breite in Prozent | Mittel | mäßig |
| 4 | Planetenkarte | Karte mit Planetenbild (vorgegeben), Name, Werteliste und Eckenschnitt | `clip-path` für schräge Ecken, Grid für Bild und Werte | Fortgeschritten | mäßig |
| 5 | Reiterleiste | Reiter mit aktiver Markierung und feiner Trennlinie | `::after` als Markierung, `gap`, Rahmen nur unten | Mittel | gut |
| 6 | Kopfbild mit Auslauf | Breites Kopfbild (vorgegeben), das nach unten in den Hintergrund ausläuft, Karten darüber | `mask-image` mit Verlauf, Überlappung mit negativem Rand oder Grid | Fortgeschritten | gut |
| 7 | Abzeichen und Stufenziffer | Rundes Abzeichen mit Ring, Ziffer in der Zahlenschrift | `aspect-ratio`, `outline-offset`, Schrift der Vorlage | Anfänger | sehr gut |
| 8 | Bauauftrag mit Restzeit | Zeile mit Fortschrittsbalken, Restzeit und Abbrechen-Knopf | Grid mit festen und freien Spalten, Balken als Hintergrundverlauf | Fortgeschritten | mäßig |

## Spielmechaniken aus der Recherche

### Vergleich von Ziel und Ergebnis

- **Live-Vorschau**: Das Ergebnis rendert beim Tippen neben dem Ziel. Die Deckung in Prozent erscheint sofort; lokal als Schätzung, verbindlich erst nach serverseitiger Bewertung.
- **Vorhang**: Ziel und Ergebnis liegen übereinander, eine senkrechte Trennlinie folgt der Maus. Links das eine, rechts das andere Bild. Sehr wirksam für Versätze von wenigen Pixeln.
- **Überblenden**: Ein Deckkraftregler blendet das Ergebnis über das Ziel. Zeigt Größen- und Lageunterschiede auf einen Blick.
- **Differenzbild**: Abweichende Pixel werden farbig markiert, gleiche gedämpft. Hilfreich ist eine zweite Farbe für 'zu viel' gegenüber 'zu wenig' sowie eine eigene Farbe für reine Kantenglättungsabweichungen.
- **Blinkvergleich**: Per Taste schnell zwischen Ziel und Ergebnis umschalten; das Auge erkennt Bewegung leichter als Unterschiede.
- **Farbliste und Lineal**: Die Farben des Ziels stehen als anklickbare Werte unter dem Bild; beim Überfahren werden Koordinaten angezeigt. So bleibt die Aufgabe ein Rätsel über Techniken, nicht über Farbtöne.

### Wertung

- **Erst treffen, dann kürzen**: Die Genauigkeit dominiert. Unter voller Deckung bringt Kürzen kaum etwas; erst ab einer Schwelle (etwa 99,5 % oder 100 %) zählt die Zeichenzahl stark.
- **Zweiteilige Punkte**: Beispielhaft bis zu 600 Punkte für Genauigkeit und bis zu 400 Punkte Kürzebonus, der nur oberhalb der Schwelle vergeben wird. Den Bonus relativ zur eigenen Musterlösung berechnen, damit jede Aufgabe vergleichbar bleibt.
- **Bestenliste der kürzesten Lösung**: Je Aufgabe Rang nach Zeichenzahl bei voller Deckung; bei Gleichstand gewinnt die frühere Einreichung.
- **Zwei Wertungsklassen**: Eine strenge Klasse nur mit CSS und eine offene, in der etwa eingebettete Vektorgrafik oder Sonderzeichen erlaubt sind. Nur die strenge zählt für die Gesamtwertung.
- **Lesbar oder roh zählen** (Vorschlag für die Codeschmiede): Im Lernmodus zählt die Länge nach automatischer Normalisierung (Leerraum und Kommentare zählen nicht), damit sauber formatierter Code nicht bestraft wird. Im Kurzmodus zählt der rohe Text.
- **Einreichungsverlauf**: Kurve der Zeichenzahl über alle Versuche einer Aufgabe; macht Fortschritt beim Kürzen sichtbar.

### Rhythmus und Motivation

- **Tagesaufgabe**: Eine neue Aufgabe zu fester Uhrzeit, ohne Bestenliste, nur mit persönlicher Statistik. Senkt den Wettbewerbsdruck.
- **Serie**: Zähler für Tage am Stück mit Aufgabe. Ein Schutzschild (etwa alle 100 Tage einer, höchstens drei) verhindert, dass ein einzelner verpasster Tag alles zunichtemacht.
- **Staffeln**: Zeitlich begrenzte Aufgabensätze mit eigener Bestenliste, die am Ende eingefroren wird. Die Aufgaben bleiben danach spielbar.
- **Duelle**: Zwei Personen, gleiches Ziel, gleiche Uhr. Spielstärke als Elo-artige Zahl.
- **Lernpfad**: Viele kleine Aufgaben statt langer Texte, jede führt genau eine neue Eigenschaft ein, von Abständen bis zu `:has()` und `color-mix()`.
- **Abzeichen**: Für Meilensteine (erste volle Deckung, zehn Aufgaben in Folge) und für Techniken (Lösung mit einem Element, ohne Positionierung, nur mit Verläufen).
- **Freundesansicht**: Bestenliste auf bekannte Personen gefiltert.
- **Spoilerschutz**: Fremde Lösungen erst nach eigenem Treffer sichtbar. Empfehlung, sich vor dem Nachschauen ein Zeitlimit zu setzen. Nach dem Treffer eine kommentierte Musterlösung zeigen.

### Aufgabenformate als zusätzliche Mechanik

- **Freies HTML** (alles zählt) gegenüber **festem HTML** (nur CSS zählt; nötig für Selektoren, Zähler, Zustände).
- **Technikbeschränkung**: 'nur ein Element', 'ohne Positionierung', 'ohne Ränder'; zwingt zu neuen Lösungswegen bei bekannten Zielen.
- **Mehrbild-Ziel**: Filmstreifen für Animationen oder mehrere Breiten für Container-Queries; Deckung gemittelt.
- **Zustandsziel**: Bewertung im erzwungenen Zustand (Überfahren, Fokus, angehakt).
- **Hinweisstufen**: Gestaffelte Tipps (Technikname, dann Teilcode), jede Stufe kostet etwas Bonus.

### Befunde aus der Forschung zu Spielelementen

- Spielelemente steigern nachweislich die Übungsmenge; eine bessere Lernleistung folgt daraus nicht automatisch.
- Serienzähler lenken Verhalten stark: Als ein öffentlicher Serienzähler entfernt wurde, gaben viele ihr Serienziel auf. Serien also freundlich gestalten (Schutzschild, kein öffentlicher Pranger).
- Abzeichen verändern Verhalten eher kurzfristig.
- Bestenlisten fördern Wettbewerb, sprechen aber nicht alle an. Deshalb abschaltbar machen und persönliche Bestwerte gleichrangig zeigen.
- Kein einzelnes Element wirkt für sich; die Kombination muss zum Lernziel passen.

---

## Fallstricke der Pixelbewertung

Grundregel: Ziel und Lösung durchlaufen exakt dieselbe Render-Kette. Das Zielbild wird nie von Hand gezeichnet, sondern aus der Musterlösung in derselben Umgebung erzeugt.

### 1. Schriftglättung

- **Problem**: Subpixel-Glättung erzeugt farbige Säume, Graustufenglättung nicht. Hinting rastet Glyphen je Plattform unterschiedlich ein. Schon das ergibt tausende abweichende Kantenpixel.
- **Umgehung**: Bewertung nur serverseitig in einer fest versionierten, kopflosen Browser-Engine im Container. Subpixel-Glättung abschalten (Startschalter `--disable-lcd-text`), Hinting abschalten (`--font-render-hinting=none`). Kantenpixel tolerant bewerten (siehe 7).

### 2. Subpixel-Geometrie

- **Problem**: Bruchteile von Pixeln (33,333 %, 0,5 px, Drehungen, Rundungen) erzeugen halbdeckende Kantenpixel. Zwei mathematisch gleichwertige Lösungen können an den Kanten minimal verschieden aussehen.
- **Umgehung**: Feste Pixeldichte (Gerätepixelverhältnis 1) bei der Bewertung. Zielmaße möglichst auf ganze Pixel legen. Kantenglättungserkennung nutzen: Pixel, die nur an einer Kante zwischen zwei Flächenfarben liegen, als 'Kante' werten und nicht als Fehler zählen.

### 3. Schriften

- **Problem**: Systemschriften und Rückfallschriften unterscheiden sich je Rechner. Ist eine Webschrift beim Aufnehmen noch nicht geladen, wird eine Ersatzschrift fotografiert.
- **Umgehung**: Nur eine gebündelte Schrift lokal ausliefern, Netzzugriff sperren. Vor der Aufnahme auf `document.fonts.ready` warten und mit `document.fonts.check()` prüfen, dass die Schrift wirklich aktiv ist. Bunte Sonderzeichen (Emojis) verbieten oder nur in der offenen Wertungsklasse zulassen.

### 4. Farbtoleranz

- **Problem**: Gleiche Farben weichen um ein bis zwei Stufen ab: durch Farbprofile, durch Mischmodi, durch Rundung beim Umrechnen aus `oklch` nach sRGB und durch leichtes Rauschen (Dithering), das Engines zum Vermeiden von Streifenbildung in Verläufe mischen.
- **Umgehung**: Farbprofil fest auf sRGB setzen (`--force-color-profile=srgb`). Pixel nicht auf exakte Gleichheit prüfen, sondern über einen wahrnehmungsnahen Farbabstand (etwa im YIQ- oder OKLab-Raum) mit kleiner Schwelle. Farben außerhalb des sRGB-Raums in Zielen vermeiden, weil die Abbildung darauf uneinheitlich ist.

### 5. Größe der Zeichenfläche

- **Problem**: Ändert sich die Fläche, stimmt nichts mehr. Überlauf erzeugt Rollbalken, die Breite stehlen. Die Vorschau im Editor ist oft skaliert. Der Standardrand von `body` (8 px) und der Kompatibilitätsmodus ohne Doctype verändern Maße.
- **Umgehung**: Feste Fläche (etwa 400 x 300) und nur diesen Ausschnitt vergleichen. Rollbalken im Bewerter ausblenden (`--hide-scrollbars`), Überlauf abschneiden. Rendermodus (mit oder ohne Doctype) und Standardstile festlegen und dokumentieren. Hintergrund des Rahmens fest weiß; transparente Bereiche vor dem Vergleich auf diese Farbe abflachen. Skalierte Vorschau nie für die Wertung nutzen.

### 6. Leerfläche verfälscht den Prozentwert

- **Problem**: Besteht ein Ziel zu 85 % aus Hintergrund, erreicht schon eine leere Lösung 85 %. Die Prozentzahl wirkt dann besser als die Leistung.
- **Umgehung**: Leerwert abziehen und neu normieren: Deckung = (Treffer minus Treffer der leeren Lösung) geteilt durch (Gesamtpixel minus Treffer der leeren Lösung). Alternativ nur Pixel werten, die im Ziel oder in der Lösung vom Hintergrund abweichen.

### 7. Harte Strafe für knappe Treffer

- **Problem**: Eine 2 px breite Linie, um 1 px verschoben, ist zur Hälfte falsch; eine völlig falsch platzierte Linie kaum schlechter. Reiner Pixelvergleich unterscheidet 'knapp daneben' nicht von 'ganz daneben'.
- **Umgehung**: Zusätzlich auf verkleinerten oder leicht weichgezeichneten Fassungen vergleichen (Gauß-Unschärfe von 1 bis 2 px) und die Werte kombinieren. Ein Strukturvergleich (SSIM-artig) eignet sich als freundliche Fortschrittsanzeige. Für 100 % weiterhin Gleichheit innerhalb der Farbtoleranz verlangen, damit die Kürzewertung fair bleibt.

### 8. Zeit und Zustände

- **Problem**: Laufende Animationen, Übergänge, blinkende Schreibmarken und ein zufällig über der Fläche stehender Mauszeiger machen jede Aufnahme anders.
- **Umgehung**: Alle Animationen über die Animationsschnittstelle auf feste Zeitpunkte setzen (`document.getAnimations()`, `currentTime`), dann aufnehmen. Mauszeiger außerhalb der Fläche halten. Zustände wie Überfahren oder Fokus ausdrücklich erzwingen, für Ziel und Lösung gleich. Kein Fremd-CSS in die Lösung einschleusen, das würde das Ergebnis selbst verändern.

### 9. Engine-Updates

- **Problem**: Eine neue Browser-Version verändert die Glättung minimal; alte Ziele passen dann nicht mehr exakt.
- **Umgehung**: Engine-Version an jedes Ergebnis schreiben. Nach einem Update alle Ziele aus den Musterlösungen neu rendern und die Musterlösungen gegen sich selbst prüfen. Alte Bestwerte behalten und kennzeichnen.

### 10. Determinismus messen statt annehmen

- **Selbsttest**: Jede Musterlösung zweimal rendern und gegen das Ziel vergleichen; es muss 100 % herauskommen.
- **Gegenprobe**: Eine absichtlich um 1 px verschobene oder um eine Farbstufe veränderte Fassung muss unter 100 % landen. So zeigt sich, ob die Toleranz zu großzügig ist.

### 11. Umgehungen durch Lernende

- **Problem**: Eingebettete Bilder (`url()` mit Daten), Vektorgrafik im Hintergrund, Skripte, Nachladen von außen.
- **Umgehung**: Skripte und Netz per Inhaltsrichtlinie sperren, `url()` in der strengen Klasse verbieten. Aus dem Ziel generierte Schattenlisten bestraft die Zeichenzahl von selbst.

### 12. Zeichenzählung eindeutig festlegen

- **Problem**: Zeilenenden (CRLF oder LF), Tabulatoren, abschließender Leerraum und Umlaute (Bytes oder Zeichen) verändern die Zahl.
- **Umgehung**: Zeilenenden vor dem Zählen vereinheitlichen und Zeichen (Codepunkte) statt Bytes zählen. Die Regel sichtbar neben der Zahl erklären.
