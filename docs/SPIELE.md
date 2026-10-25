# Spiele und Spielmechanik

Konzept zu Schritt 6 (Plan): vier Lernspiele in einem eigenen Bereich und eine Spielmechanik, die über die ganze App
wirkt. Die Entwürfe dazu liegen in `mockups/` (Übersicht `mockups/index.html`, Abschnitt Spiele). Gebaut wird erst
nach Freigabe.

Leitlinien:

- Lernen vor Belohnung: jede Mechanik belohnt etwas, das beim Lernen hilft (üben, wiederholen, sauber und knapp
  lösen), nie bloßes Klicken.
- Eine Wahrheit: es gibt eine Währung, die Punkte. Stufe, Ränge und Sterne leiten sich aus gespeicherten Ergebnissen ab
  und werden nie getrennt gezählt.
- Freundlich statt strafend: Serien mit Schutzschild, keine Bestenliste gegen andere (ein Nutzer), dafür eigene
  Bestwerte. Verlieren kostet nie Punkte.
- Fair: Levels prüft der Server wie Aufgaben, mit sichtbaren und versteckten Fällen (beim Roboter versteckte Welten),
  damit nichts auswendig gelernt werden kann.

## Die vier Spiele

Jedes Spiel ist ein Aufgabentyp mit eigenem Prüfer; Levels sind Aufgabendateien wie alle anderen (eigener Ordner je
Spiel unter `aufgaben/spiele/`), gehören zu Pfaden, zählen in Punkte, Serie und Wiederholung. Jedes Level vergibt bis
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
- **Ablauf**: Runden mit zehn kurzen Schnipseln gegen die Uhr (Vorgabe 90 Sekunden). Antwort wählen oder tippen;
  richtige Antworten in Folge geben eine Kette, die die Punkte der Runde erhöht. Am Ende der Runde die Auswertung: jede
  falsche Antwort mit der richtigen und einer kurzen Erklärung, warum.
- **Prüfung**: wie die Ausgabe-Quizze, die richtige Antwort bleibt auf dem Server. Die Runde stellt der Server aus dem
  Bestand zusammen (Sprache und Stufe wählbar).
- **Sterne**: je Runde nach Trefferzahl (6, 8, 10 von 10). Gut fürs Telefon.

### Muster-Jagd

- **Lehrt**: reguläre Ausdrücke, von Zeichenklassen bis zu Gruppen und Ankern.
- **Ablauf**: Zwei Listen: Treffer (müssen passen) und Nieten (dürfen nicht passen). Beim Tippen markiert jede Zeile
  sofort, ob sie stimmt; kürzere Muster geben mehr Sterne.
- **Prüfung**: In der Sandbox (JavaScript, mit Zeitgrenze gegen zu gierige Muster) gegen die sichtbaren und weitere
  versteckte Zeilen. Die Vorschau im Browser nutzt dieselbe Ausdrucksart (JavaScript), damit Vorschau und Prüfung
  übereinstimmen.
- **Sterne**: Bestehen; höchstens so lang wie die Musterlösung plus Spielraum; so kurz wie die Musterlösung.

## Spielmechanik in der ganzen App

| Mechanik | Was sie belohnt | Wo sie erscheint |
|---|---|---|
| Stufe | gesammelte Punkte; Stufe k ab 25 · k² Punkten, alle fünf Stufen ein Titel (Lehrling, Geselle, Schmied, Meister, Großmeister) | Ring im Kopf, Startseite |
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

- **Deckung**: Anteil der Bildpunkte, die mit dem Ziel innerhalb einer kleinen Farbtoleranz übereinstimmen, gemessen
  auf der Bühne von 600 × 400. Der Ring zeigt sie in Prozent; das Abweichungsbild färbt "zu viel" und "zu wenig"
  verschieden.
- **Punkte in zwei Teilen**: bis 60 % der Punkte für die Deckung (linear ab 80 % Deckung), die übrigen 40 % als
  Kürzebonus, aber nur ab 99 % Deckung, gemessen an der Zeichenzahl der Musterlösung (ohne Leerraum).
- **Sterne**: Bestehen ab 95 %; 99 %; 99 % und höchstens so kurz wie die Musterlösung.
- **Messung**: verbindlich beim Prüfen, beim Tippen als Schätzung. Wo gerechnet wird (im Browser oder als Dienst am
  Mac), entscheidet der Bau; der Pi rendert keine Bilder.

## Offen für die Freigabe

- Namen und Schwellen der Stufen und Ränge
- Länge einer Sprint-Runde und Zahl der Schutzschilde
- ob der Tagesauftrag mitzählt, wenn man nur Spiele spielt
