# Plan: Codeschmiede härten, verbessern und auf den Pi bringen

Geklärt am 24.10.2026 (Analyse plus Frage-für-Frage-Klärung). Entwürfe der Oberfläche liegen unter `mockups/`
(Übersicht `mockups/index.html`).

## Entscheidungen

| Thema | Wahl |
|---|---|
| Betriebsort | Dauerhaft auf dem Pi |
| Sandbox | Auf dem Pi, eigener kleiner Sandbox-Dienst startet die Container; das Backend bekommt keinen Docker-Zugang mehr |
| Zugang | Kellerwolke-Konto über die Anmeldung des Unterbaus (Appkern); eigene Optik bleibt |
| Lernende | Nur ein Konto, ein Fortschritt wie heute |
| Lösungsschutz | Server erzwingt: Musterlösungen erst nach Bestehen oder Aufgeben (Punkte verfallen), Quiz-Antworten und Erwartungen nie an den Browser, Vergleich außerhalb des Nutzercodes; JavaScript läuft in der Sandbox auf dem Pi (Node-Container) mit allen Tests |
| Verratene Tests (134 Aufgaben) | Versteckte Tests bekommen neue, gleichwertige Werte; Beispiele im Text bleiben; Prüfung beim Einlesen warnt künftig |
| Pfad-Zugehörigkeit | Die Pfad-Datei (`aufgaben/pfade/*.yml`) ist die einzige Wahrheit; Feld `pfade` im Aufgabenkopf entfällt |
| Spiele | SQL-Krimi, Roboter-Parcours, Ausgabe-Sprint, Muster-Jagd |
| Spiele-Ort | Eigener Bereich Spiele (auch am Telefon); je Spiel ein Aufgabentyp mit eigenem Prüfer, Level als Aufgabendateien, zählen in Punkte, Serie und Wiederholung |
| Neue Aufgaben | JavaScript ausbauen, Python fortgeschritten, Stufe Experte, SQL vertiefen |
| Quellen für neue Aufgaben | Ideen aus bekannten Aufgabensammlungen sind willkommen, werden aber vollständig neu formuliert: eigener Text, eigene Werte, eigener Name, Fokus auf den Lernwert. Übernommen wird nur die Idee (Problem, Algorithmus), nie fremder Text oder fremde Testdaten (Nutzer 24.10.2026) |
| Erstellung | Neue Aufgaben und Testwerte entstehen nicht durch die lokale KI (die ist nur Nachschlagewerk), sondern werden direkt geschrieben nach `docs/AUFGABEN-FORMAT.md`; jede Aufgabe wird automatisch geprüft (Musterlösung besteht, falsche Lösung scheitert, kein versteckter Test im Text, Umlaute korrekt) |
| Abhängigkeiten | Alles auf neu (Sicherheitsstand und große Sprünge), Docker-Image installiert fest nach Sperrdatei |
| Aufgabendateien auf dem Pi | Repo ist die Wahrheit; Pi nur lesend, Bearbeiten in der Verwaltung nur am Mac, danach Commit und Ausrollen |
| Repo | Vorhandenes öffentliches Repo `HalloWelt42/CodeSchmiede` |
| PHP-Lücke (CVE-2026-109618/-109619, -115560) | Betrifft die Codeschmiede nicht (kein PHP) |
| Gamifizierung | Alles gamifizieren, in bester Qualität (Nutzer 24.10.2026); Ausgestaltung mit Entwürfen vor dem Bau, zusammen mit den Spielen |
| Lokale KI | Nur als Hilfe im Lernhelfer (Nachschlagewerk mit Wissenspool), gerechnet auf dem Mac über die Leitstelle; Wissenspool und Einzelheiten vor dem Bau klären |
| Lernhelfer | Die lokale KI ist nur Hilfe: Assistent und Nachschlagewerk, das man nach Befehlen und Anweisungen fragt und das dafür in einem Wissenspool sucht (Nutzer 24.10.2026). Schwebendes, verschiebbares Hilfefenster mit diesem Lernhelfer (über die Leitstelle, Anwendung "Codeschmiede" ist angemeldet): löst nie die Aufgabe, gibt Rückfragen, kleine korrekte Bausteine (einzelne Befehle mit neutralem Mini-Beispiel), erklärt Fehler, schlägt den nächsten kleinen Schritt vor; minimalistisch. Der Server gibt ihm nur Aufgabentext, eigenen Code und letztes Ergebnis, nie Musterlösung oder versteckte Tests (Nutzer 24.10.2026). Einzelheiten vor dem Bau klären |
| Aufbaukurs | Ein idiotensicherer Aufbaukurs von null an, in kleinsten Schritten mit einer neuen Sache je Aufgabe, als eigener zweiter Lauf in Schritt 7 (Nutzer 25.10.2026). Bisher gibt es nur Themenpfade (Python-Grundlagen hat 3 Aufgaben). Ideen und Reihenfolge der Themen kommen von einer großen bekannten Lernseite für Webtechnik und Programmierung; übernommen wird nur, was sinnvoll ist, und alles wird neu geschrieben: eigene Erklärungen, eigene Beispiele, eigene Werte und Namen, kein Text und kein Beispielcode im Wortlaut. Geklärt am 25.10.2026, siehe "Klärung Aufbaukurs und Lehreinführungen" |
| Lehreinführungen | Zu jedem Thema ein richtiger, vollständiger Einführungskurs mit sinnvoller Logik, durch den man sich durcharbeitet; erst danach folgt das Üben mit den Aufgaben. Die Einführungen sind absolut vollständig und anschaulich (Nutzer 25.10.2026). Gehört zum Aufbaukurs (Schritt 7); geklärt am 25.10.2026, siehe "Klärung Aufbaukurs und Lehreinführungen" |
| Editor | Hervorhebung im klassischen dunklen Farbschema einer bekannten Entwicklungsumgebung (die ältere Fassung); Vervollständigung nur für einzelne Befehle, keine mehrzeiligen Bausteine; Syntaxfehler sofort beim Tippen sichtbar (Nutzer 25.10.2026). Gebaut direkt nach Schritt 6, vor dem Ausrollen |
| Debugger | Haltepunkte im Editor und ein Ausgabemodus wie bei einem echten Debugger, aber nur auf Ebene des eigenen Codes, kein Tiefendebugger; alle Speicherzustände Schritt für Schritt lesbar (Nutzer 25.10.2026). Umsetzung als Aufzeichnung: die Sandbox schreibt je ausgeführter Zeile des eigenen Codes die Variablen mit (Python über die Ablaufverfolgung, mit Grenze für Schritte und Größe), die Oberfläche spult vor und zurück, springt zum nächsten Haltepunkt, markiert die Zeile und zeigt den Speicher. Python zuerst, JavaScript danach; nur am Rechner, das Telefon muss nicht alles können (Nutzer 25.10.2026); Entwurf vorab. Die Aufzeichnung entsteht vor dem Aufbaukurs (der Kurs zeichnet damit Speicherbilder und Abläufe), die Debugger-Oberfläche direkt nach dem Python-Kurs |
| Bildkarten | Lernfelder und Bereiche bekommen anschauliche Karten mit Bild und Beschreibung; freigestellte Bilder begleiten die Software. Erzeugt später lokal mit Flux2 über die Leitstelle, nur wenn dort alles entladen ist und Platz ist. Farblich dürfen die Inhalte (Bilder, Karten, Spielflächen) vom Mintgrün abweichen, damit sie in sich harmonisch sind (Nutzer 25.10.2026). Ein Zeichenstil für Bildkarten und Kurs, je Sprache eine Farbfamilie, keine Schrift im Bild; vor jeder Bildserie nimmt der Nutzer selbst ab (Nutzer 25.10.2026, Einzelheiten unter "Klärung Aufbaukurs und Lehreinführungen") |
| Aufgabenvarianten (später) | Je Aufgabe mehr Vielfalt: Werte vorab erzeugen und nachrechnen, bei Auswahlaufgaben die Reihenfolge der Antworten zufällig mischen, immer nachweislich korrekt; dazu eine Lösungserklärung, die das Verständnis stärkt. Als Plan aufgehoben, weil es aufwendig ist (Nutzer 25.10.2026) |
| Literaturhinweise | Passende Stellen aus den eigenen Büchern als Literaturhinweise (zur Aufgabe und im Lernhelfer), gefunden über den Wissenspool. Nur für die eigene Installation: öffentlich hat kaum jemand diese Bücher (Nutzer 25.10.2026). Darum abschaltbar und ab Werk aus; Titel, Fundstellen und Zugang liegen nicht im öffentlichen Repo, sondern kommen zur Laufzeit aus dem privaten Wissenspool. Einzelheiten vor dem Bau klären |
| Steuerungsspiele | Größere Spiele, bei denen eine Steuerung programmiert wird: Ampeln vom Fußgängerüberweg mit Ampelsteuerung über Umschaltautomatik und verschiedene Fälle bis zur großen Kreuzung mit vier Seiten und Sonderfällen, in Draufsicht von oben mit sichtbaren Ampeln; nur wenn die Ampeln richtig schalten, gibt es keine Unfälle, geprüft mit echten Abläufen. Dasselbe mit Aufzügen, später weitere Regelungen. Der Rahmen ist vorgefertigt, geschrieben werden nur Ablauf und Inhalte. Gern ein wenig lustig: roter Matschfleck für überfahrene Fußgänger, verbeulte Autos bei Unfällen; Ton spielt eine Rolle, die Klänge kommen aus dem vorhandenen Bestand (Medienpool). Vorher Entwürfe (Nutzer 25.10.2026); Konzept in `docs/SPIELE.md` |
| Aufbau in Teilschritten | Wichtig bei allen Aufgaben: sie bauen aufeinander auf. Im einfachen Modus programmiert man erst auf ein Ziel hin; funktioniert das, kommt der nächste Teilschritt, der Code bleibt und wächst mit (Nutzer 25.10.2026). Gilt für die Steuerungsspiele von Anfang an und als Richtschnur für neue Aufgaben und den Aufbaukurs (Schritt 7) |
| CSS-Bewertung | Nach dem Bild, nicht nach Eigenschaften: Deckung mit dem Ziel in Prozent und Kürze des Codes entscheiden; die Deckung wird grafisch gezeigt (Überblenden, eingefärbte Abweichung), das ist spannender als eine Liste (Nutzer 24.10.2026) |
| CSS-Ansicht | Beim Lösen stehen Ziel und eigenes Ergebnis untereinander in der rechten Spalte, Zoom mit dem Mausrad auf beiden zugleich, gedämpft für Trackpad und Mac-Maus (Stärke nach Scrollweite, ein Schritt je Bildschirmbild, höchstens 8 %); Ergebnis und Verlauf wandern aus der rechten Spalte in die Reiter links (Entwurf `mockups/rechner-css.html`) |
| CSS-Vielfalt | Sehr große Vielfalt an CSS-Aufgaben; Ideensammlung aus einer Recherche in `docs/CSS-IDEEN.md` (229 Ideen in 28 Kategorien, eigene Worte, keine fremden Aufgaben übernommen) |
| Bausteine aus eigenen Projekten | Neben den CSS-Spielereien werden Knöpfe, Karten, Leisten und andere Bausteine aus den eigenen Projekten zu Herausforderungen, etwa die Gestaltung von Orbit. Fair bleiben: komplexe Grafik (Pixelgrafik, Bilder) wird als Bild mitgegeben, dazu eine halbfertige Vorlage, ergänzt wird der fachliche Rest. Ziel ist Lernen und Besserwerden, der Lernende soll nicht frustriert werden (Nutzer 25.10.2026); Regeln in `docs/CSS-IDEEN.md` |

## Reihenfolge des Baus

Jeder Schritt einzeln committet und gepusht.

1. **Sicherheit und Fehler** (erledigt mit 0.72.0)
   - Sandbox-Dienst mit gehärteten Containern: `--cap-drop=ALL`, `no-new-privileges`, `--user`, `--memory-swap`, begrenzte Ausgabe, Container per Name beenden bei Zeitüberschreitung
   - SQL-Prüfung mit Zeitabbruch und ohne `ATTACH`
   - CORS fest auf die eigene Herkunft, Mermaid nicht mehr `loose`
   - Kennungsmuster für CSS- und SQL-IDs
   - kaputte Verweise mit Umlaut-IDs, Reindex robust je Datei
   - Probelauf-Rückgabe, Typfehler, toter Code
   - doppelte Logik zusammenführen, Migrationen atomar
   - Backend-Tests aufbauen
2. **Abhängigkeiten** auf den neuesten Stand, Image nach Sperrdatei. (erledigt mit 0.73.0)
3. **Aufgabenbestand** (erledigt mit 0.74.0)
   - Pfad-Datei als einzige Wahrheit
   - neue versteckte Tests für die 134 verratenen Aufgaben
   - Umlaute und einfache Bindestriche in Texten und Titeln (IDs bleiben ASCII)
   - Warnung beim Einlesen
4. **Oberfläche** nach den Entwürfen: feste Köpfe, Rollfelder, Telefonschale (Entwürfe freigegeben 25.10.2026, erledigt mit 0.75.0).
5. **Anmeldung und Ausrollen auf den Pi** (erledigt mit 0.76.0)
   - Kellerwolke-Konto
   - Daten unter `/mnt/data`
   - Verwaltung nur lesend
   - Sicherung, Handbuchseite, Einrichtungsskript
6. **Spiele und Gamifizierung**: erst Entwürfe (Spiele, Spielmechanik über die ganze App, neue CSS-Bewertung nach Deckung und Kürze), nach Freigabe Bau (erledigt mit 0.77.0).
7. **Neue Aufgaben** in den vier Bereichen und viele neue CSS-Nachbauten, mit automatischer Prüfung.
   - zweiter, eigener Lauf: Aufbaukurs von null an mit Lehreinführungen (Reihenfolge unter "Klärung Aufbaukurs und
     Lehreinführungen")

## Ergebnis Schritt 1

- Sandbox-Dienst als einziger Teil mit Docker-Zugang, Code über stdin, gehärtete Container, Startreserve einstellbar
- Prüfung im Backend: nur Eingaben gehen in die Sandbox, Rückgaben typgetreu, Vergleich im Backend; JavaScript und SQL laufen ebenfalls in der Sandbox
- SQL-Gegenprobe auf ausgedünnten Datensätzen als versteckte Tests
- Musterlösungen erst nach Bestehen oder Aufgeben (Punkte verfallen), Quiz-Antwort bleibt auf dem Server
- CORS nur für erlaubte Herkünfte, ändernde Anfragen aus fremder Herkunft abgewiesen, Mermaid strikt
- Einlesen robust je Datei, Bestandsprüfung mit Befunden, IDs und Funktionsnamen geprüft, CSS- und SQL-Aufgaben speicherbar, Sprachwechsel zieht um, Musterlösungen mit Endung der Sprache
- Verwaltung auf "nur lesen" schaltbar (Compose: aus)
- Migrationen atomar, Submissions über ein Repository, doppelte Logik zusammengeführt
- Fehler im Bestand behoben: Umlaut-ID 024, drei tote Voraussetzungen, zwei falsche versteckte Tests (033, 036)
- Frontend: 18 Typfehler behoben, Probelauf zeigt die Rückgabe, echte Fehlertexte statt "nicht gefunden"
- Backend-Tests: 51, dazu die Prüfung des ganzen Bestands (590 Musterlösungen)

## Ergebnis Schritt 2

- Backend auf Python 3.14 (3.15 hat für `uvicorn[standard]` noch keine fertigen Pakete), alle Pakete neu gesperrt, `httpx2` statt `httpx`; `pip-audit`: keine Lücken
- Docker-Images installieren genau nach `uv.lock`; Sandbox-Dienst mit `docker-cli` (Debian 13 trennt Kommandozeile und Daemon)
- Sandbox-Images: Python 3.15, Node 26
- Frontend: Vite 8, Svelte-Plugin 7, Svelte 5.57, Mermaid 12, KaTeX 0.19, DOMPurify 3.4.17 und alle übrigen auf neu; TypeScript 6.0 (7 wird von der Svelte-Typprüfung noch nicht unterstützt); `npm audit`: 0 Lücken
- Mermaid wird erst geladen, wenn ein Diagramm vorkommt
- Musterlösungen und Verlauf als gemeinsame Bausteine in allen Aufgabenansichten (CSS und SQL hatten keinen Verlauf und kein Aufgeben)
- Dateibeobachter abschaltbar, im Compose aus (das Einrichten blockierte im Container das Backend minutenlang)

## Ergebnis Schritt 3

- Pfad-Dateien unter `aufgaben/pfade/` sind die einzige Wahrheit; ein `pfade`-Feld in einer Aufgabe ist ein Ladefehler
- Lecksuche in der Bestandsprüfung: ein versteckter Test gilt als verraten, wenn eine Zeile des Aufgabentexts oder eines kostenlosen Hinweises alle Eingaben samt Erwartung zeigt; bezahlte Hinweise zählen nicht, Fälle nur aus leeren Werten, `None` oder Wahrheitswerten lassen sich nicht anders formulieren und sind ausgenommen
- 537 neue versteckte Tests in 231 Aufgaben (die genauere Suche fand mehr als die anfangs 134 Aufgaben); jeder neue Wert hat dieselbe Art und dieselben Merkmale (Null, negativ, Kommazahl, leer, Großbuchstaben, Sonderzeichen ...) wie der alte, alle Musterlösungen bestehen ihn, keiner steht im Text
- Aufgaben 147, 195 und 255 umgebaut: gültige Fälle sichtbar, ungültige versteckt
- Ausgaben mit echten Umlauten in 11 Aufgaben samt Musterlösungen (etwa "ungültig", "fünfzehn", "Äpfel"), Kommentare in Vorlagen und Lösungen bereinigt (287 Zeilen), Funktions- und Parameternamen bleiben ASCII
- Revision jeder geänderten Aufgabe um eins erhöht
- Werkzeug `scripts/verratene-tests-ersetzen.py`: prüft Vorschläge aus einer Datei (Art, Merkmale, Doppelte, Sandbox-Lauf aller Musterlösungen, Lecksuche) und schreibt sie erst danach
- Bestandsprüfung: 644 Aufgaben, 0 Ladefehler, 0 Befunde

## Ergebnis Schritt 4

- Gestaltungssystem aus den Entwürfen in `frontend/src/styles/global.css` (Seite, Kopf, Rollfeld, Knöpfe, Reiter, Kennzahlen, Filter, Tabellen, Karten, Telefonbausteine); Entwurf und App nutzen dieselben Klassen und Werte
- Rechnerschale: feste Kopfleiste, Navigation breit oder nur mit Symbolen (unter 1200 px immer schmal), Fuß mit Fassung
- Übersichten mit festem Kopf und Rollfeld: Dashboard (drei Karten, Fortschritt, Aktivität, Erfolge), Aufgaben (Tabelle mit fester Kopfzeile, Filter gespeichert), Pfade (nach Sprache gruppiert, aufklappbar), Verwaltung (Kennzahlenleiste, aufklappbare Zeile mit Tests, Beschreibung, Hinweisen, Startcode, technischen Daten; Befunde der Bestandsprüfung, sobald es welche gibt)
- Aufgabenansicht: ein gemeinsames Spaltenlayout für Code, SQL, Lückentext und CSS; der Prüfen-Knopf gehört dem Layout; Ergebnis mit Trefferzahl und Testzeilen
- CSS-Aufgabe nach Entwurf: Reiter Aufgabe, Hinweise, Verlauf, Lösung; Zeichenzahl im Editorkopf; rechts Ziel über eigenem Ergebnis, Getrennt, Überblenden mit Regler, Abweichung als Farbdifferenz, gemeinsamer gedämpfter Zoom. Der Ring zeigt bis zur Bewertung nach Deckung (Schritt 6) den Anteil erfüllter Prüfpunkte, daneben Zeichen und eigener Bestwert
- Telefon als eigene Schale: Reiter unten ohne Abstand über dem Home-Balken, eigene Startseite, Aufgaben- und Pfadliste; jede Aufgabe in drei Schritten (Aufgabe, Code, Ergebnis), nach dem Prüfen direkt beim Ergebnis
- Geprüft: alle Ansichten in 1920, 1440, 1280, 1100, 900 und 390 px ohne seitliches Rollen und ohne Überlauf, Seite rollt nie als Ganzes; Prüfablauf am Telefon mit der Sandbox
- Texte bereinigt (doppelte Bindestriche, Ersatzschreibungen in Bestätigungen und im Aufgabeneditor)

## Ergebnis Schritt 5

- Anmeldung mit dem Kellerwolke-Konto über den Baustein des Appkern (Passwort oder gekoppeltes Gerät); nutzen darf das Konto, dem der App-Schlüssel gehört; alle Endpunkte außer Gesundheit, App-Angaben, Einrichtung und Anmeldung geschützt
- Erste Einrichtung im Browser (Adresse und App-Schlüssel der Kellerwolke), von anderen Geräten nur mit dem Einrichtungscode aus der Datei am Rechner; Anmelde- und Einrichtungsseite nach Entwurf `mockups/rechner-anmeldung.html`, `telefon-anmeldung.html`
- Betrieb auf dem Pi unter `/mnt/data/codeschmiede`, Port 8661: Vorschaltdienst mit Zertifikat der Hausstelle und HTTP/2, Backend mit gebauter Oberfläche, Sandbox-Dienst als einziger Teil mit Docker-Socket, Sandbox-Abbilder beim Ausrollen gebaut; Aufgaben nur lesend aus dem Repo
- Ausrollen `tools/ausrollen.sh` mit den Schritten des Appkern (Zertifikat, Stand, Bauen, Sicherung, Start) und eigenen (Tests, Sandbox-Schlüssel nur auf dem Pi, Abbilder, Fassungen); vorher Probelauf des Handbuchs in einer abgeschotteten Umgebung
- Datenbank nachts und vor jedem Ausrollen gesichert, vom Werkzeug Sicherungen auf den Mac geholt; Handbuchseite `docs/handbuch.md`, Einrichtungsskript `einrichten.sh`
- Sandbox auf dem Pi gemessen: Containerstart warm unter 1 s, kalt rund 5 s (schneller als Docker am Mac); ohne Netz bestätigt
- Speicher-cgroup ist auf dem Pi aus (`cgroup_disable=memory`): der Sandbox-Dienst erkennt das und begrenzt über die Datengrenze je Prozess
- Zwei zufällig rote Tests behoben (die gesuchte 42 stand in Laufzeiten und Laufkennungen)

## Ergebnis Schritt 6

- Spielmechanik über die ganze App, alles abgeleitet aus Abgaben: Stufen mit Titeln, Serie mit Schutzschilden,
  Tagesauftrag, Meisterschaft je Sprache und für die Spiele, Erfolge in drei Rängen, Belohnungsband nach dem Bestehen,
  eigene Bestwerte; Startseite, Kopf und eigene Seite Erfolge nach den Entwürfen
- Spielebereich mit vier Spielen, Level aus Pfaden, Sterne aus Ergebnis und Verlauf:
  Muster-Jagd (12 Level, reguläre Ausdrücke mit Live-Markierung), Ausgabe-Sprint (Runden auf dem Server mit Frist,
  Antwort erst nach der Wahl), Roboter-Parcours (10 Level, Lauf vom Server nachgerechnet und abgespielt, versteckte
  Welten), SQL-Krimi (Fall 1 mit acht Kapiteln, Gegenprobe mit anderer Befüllung, Pinnwand)
- CSS nach Bild: Deckung im Motiv im Browser gemessen, Wertung auf dem Server, Abweichungsbild, Punkte aus Deckung und
  Kürze; Eigenschafts-Prüfpunkte entfernt, alle 111 Musterlösungen decken voll, kein Startcode besteht; Aufgaben in
  abwechslungsreichen Farben
- Editor wie in einer Entwicklungsumgebung: klassisches dunkles Farbschema, fette Schlüsselwörter, keine Ligaturen,
  Vervollständigung einzelner Befehle, Syntaxprüfung beim Tippen, Suchen und Ersetzen
- Saubere Pfade statt `#` in den Adressen
- Entwürfe der Steuerungsspiele (Ampelschule, Aufzugsteuerung) mit Teilschritten und Klängen aus dem Medienpool
  liegen zur Freigabe
- Breiten 1920, 1440, 1280, 1100, 900, 430, 390 und 360 automatisch geprüft, mit Gegentest (abgeschnittene Elemente
  zählen mit); gefunden und behoben: abgeschnittener Reiter im Krimi, zu langes Schlagwort in der Aufgabenliste

## Klärung Aufbaukurs und Lehreinführungen

Frage für Frage geklärt am 25.10.2026 (Nutzer); Grundlage waren die Entscheidungen "Aufbaukurs" und
"Lehreinführungen" und die Vorschläge in `docs/DIDAKTIK.md`.

| Thema | Wahl |
|---|---|
| Kursform | Eigener Bereich Kurs neben Aufgaben, Pfade und Spiele. Je Sprache ein Kurs mit Kapiteln; jedes Kapitel hat erst die Lehreinführung, dann die Übungen |
| Einführung und Themen | Eine Einführung je Thema, überall verlinkt: jede Einführung gibt es genau einmal, der Kurs ordnet sie zu Kapiteln, Themenpfade und Aufgaben verweisen darauf ("Erst lesen") |
| Sprachen | Alle vier, Python zuerst; danach SQL, JavaScript, CSS |
| HTML | HTML-Grundlagen vorn im CSS-Kurs (Elemente, Verschachtelung, Klassen, Attribute), so weit, dass man das vorgegebene HTML lesen und Selektoren treffen kann; kein eigener HTML-Kurs |
| Aufbau einer Einführung | Kurze Abschnitte mit genau einer neuen Sache: Erklärung, Bild, Beispiel (erst vorhersagen, dann ausführen), danach eine Verständnisfrage; weiter nach der Antwort, bei falscher Antwort eine Erklärung. Am Ende die Karte "kann ich jetzt", dann die Übungen |
| Beispiele | Ausführen und verändern: kleiner Editor, Lauf in der Sandbox (CSS live auf der Bühne, SQL auf Beispieldaten), danach Herumprobieren erlaubt, ein Knopf stellt das Original wieder her |
| Vorhersage | Je Beispiel festgelegt: Auswahl aus 3 bis 4 Ausgaben (am Anfang) oder Ausgabe selbst eintippen (später); danach Vergleich mit dem echten Ergebnis |
| Fragearten | Auswahl (je falscher Antwort eine eigene Erklärung), Lücke im Code, Zeilen ordnen, Fehlerstelle zeigen |
| Anschauungsmittel | Speicherbilder, Ablauf Schritt für Schritt, Diagramme, Bilder und Zeichnungen |
| Speicherbild und Ablauf | Aus dem echten Lauf: die Sandbox zeichnet auf (dieselbe Aufzeichnung wie für den Debugger), Bilder stimmen darum auch nach einer Änderung am Beispiel |
| SQL und CSS | Abspielen als Zwischentabellen und Kästen: SQL in der Reihenfolge der Abarbeitung (FROM, JOIN, WHERE, GROUP BY, SELECT, ORDER BY) mit Zwischentabelle je Schritt; CSS Regel für Regel zugeschaltet, Außenabstand, Rand, Innenabstand und Inhalt als farbige Kästen |
| Begleitmaterial | Sinnbilder (bildsprachliche Zeichnung je Abschnitt), Alltagsbeispiele (Konkretes vor dem Code), Schemata (abstrakt, exakt, von der App gezeichnet), Merkblatt je Kapitel (auch im Hilfefenster beim Üben und zum Ausdrucken). Abstraktes, Konkretes und Bildsprachliches stützen sich gegenseitig (Nutzer 25.10.2026) |
| Bildwelt | Ein Zeichenstil für alle Kurse und die Bildkarten, festgelegt in einer Stilvorgabe, die jeder Bildauftrag erbt; je Sprache eine harmonische Farbfamilie; keine Schrift im Bild, Beschriftungen setzt die App darüber. Zeichnungen kommen aus dem Bildgenerator (Flux2 über die Leitstelle, nur wenn dort alles entladen ist) und werden freigestellt |
| Exakte Grafiken | Für Sonderfälle und alles, was exakt stimmen muss, nicht der Bildgenerator, sondern Mermaid-Diagramme als Vektorbild (Nutzer 25.10.2026): der Mermaid-Code steht in der Einführung, beim Einlesen entsteht daraus ein SVG in der Stilvorgabe der App; der Browser lädt kein Mermaid, ein kaputtes Diagramm meldet die Prüfung beim Einlesen |
| Abnahme der Zeichnungen | Bevor Hunderte Grafiken entstehen, nimmt der Nutzer selbst ab (Nutzer 25.10.2026): erst eine Stilprobe mit 12 Bildern quer durch alle Arten (`kurs/stilprobe.yml`), weiter erst nach Freigabe der Bildwelt; danach Bilder kapitelweise, erst abgenommene erscheinen im Kurs. Erzeugt, ausgewählt und freigestellt wird im Medienpool, Projekt codeschmiede, mit FLUX.2 klein (Nutzer 25.10.2026: Medienpool statt eigenem Bildbogen); die Bildaufträge gleicht `tools/bildschluessel.py` ab, die Leitstelle gibt dafür Speicher frei |
| Zeichnungen in den Einführungen | Die erzeugten Bilder aus dem Medienpool sind vorerst nur für Übersichtskarten (Kapitel-, Sammel- und Bereichskarten); die Zeichnungen in den Einführungen bleiben die eigenen (gezeichnet im Code, wie die Pinguine am Förderband) und werden nicht ersetzt. Wie es weitergeht, klären wir später (Nutzer 25.10.2026) |
| Ablage der Bilder | Im Repo: der Bildauftrag (Schlüssel, Art, Sprache, Motiv auf Deutsch, Seitenverhältnis) steht im Kopf der Einführung; Prompts, Stil und Farbfamilien gehören dem Medienpool. Sein Export legt das gewählte Bild als WebP mit Transparenz nach `kurs/bilder/<satz>/<schluessel>.webp`; das Repo bleibt die einzige Wahrheit, der Pi liest nur |
| Format | Markdown mit eigenen Blöcken: je Thema ein Ordner (etwa `einfuehrungen/python/schleifen/`) mit Kopf, Abschnitten als Überschriften, Beispielen, Fragen, Diagrammen und Bildaufträgen als Blöcke, Bilder daneben; je Sprache eine Kursdatei, die Themen zu Kapiteln ordnet und die Übungen anhängt; geprüft beim Einlesen |
| Freischalten | Geführt: die Übungen eines Kapitels öffnen sich nach der Einführung, das nächste Kapitel nach den Pflichtübungen. Wer ein Thema schon kann, überspringt es per Kurztest; die Einführung bleibt jederzeit lesbar |
| Kurztest | Eigene Testfragen je Kapitel (nicht die der Einführung) plus eine kleine Übung, die alle Teile des Kapitels braucht; bestanden nur, wenn alles stimmt |
| Übungen | Neue Kursübungen: je Übung eine neue Sache, aufeinander aufbauend in Teilschritten. Passende Bestandsaufgaben am Kapitelende als freiwillige Vertiefung, aber nur solche, die ausschließlich Eingeführtes brauchen |
| Prüfung "nichts vorausgesetzt" | Begriffskatalog je Sprache; jede Einführung sagt, was sie einführt; die Prüfung erkennt im Code der Beispiele und Übungen selbst, was benutzt wird (Python über den Syntaxbaum, SQL und CSS über ihre Parser), und meldet alles, was an der Stelle noch nicht eingeführt ist. Dieselbe Angabe wählt die Bestandsaufgaben für die Vertiefung |
| Spielmechanik | Voll eingebunden: abgeschlossene Abschnitte bringen etwas Erfahrung, ein fertiges Kapitel einen Erfolg, der Tagesauftrag kann ein Abschnitt sein, die Verständnisfragen kommen in die Wiederholung nach Abstand, der Kursstand steht auf der Startseite; falsche Antworten kosten nichts |
| Didaktik dazu | Verblassende Beispiele (gelöst, mit Lücken, leer), Kapitelprojekt, das über mehrere Kapitel wächst, Fehlermeldungen übersetzt mit Verweis auf den passenden Abschnitt (im Kurs und in allen Aufgaben), Sammelkarte mit Sinnbild je Kapitel |
| Ton | Nicht zu seriös, Humor und Spaß, lockerer Ton (Nutzer 25.10.2026): Du-Ansprache, kurze Sprüche, schräge Beispielwelten, witzige Sinnbilder, Erklärungen bei falschen Antworten mit Augenzwinkern, nie spottend. Fachliches bleibt exakt, Humor würzt, trägt aber nie die Erklärung |
| Telefon | Das Telefon ist Unterstützung, kein zweiter Arbeitsplatz (Nutzer 25.10.2026): dort bleibt, was lesend ist oder mit wenigen Klicks sinnvoll geht; komplexer Code und Werkzeuge bleiben am Rechner, komplexe Teile werden nicht noch einmal fürs Telefon gebaut. Für den Kurs: Einführungen lesen mit Bildern und Diagrammen, Vorhersagen und Fragen, Beispiele unverändert ausführen, Ablauf abspielen, Merkblatt; Beispiele verändern, Kursübungen und Kurztest-Übung nur am Rechner |
| Umfang Python | Von null bis Klassen und Dateien, rund 20 Kapitel: Ausgabe, Werte und Variablen, Rechnen, Text, Verzweigungen, Schleifen, Listen, Wörterbücher, Mengen, Funktionen, Fehlerbehandlung, Module, Dateien, Klassen. Fortgeschrittenes folgt als zweiter Teil |
| Zusatzthemen | Themen außerhalb des Kurses (etwa Datum und Zeit, reguläre Ausdrücke, Algorithmen) bekommen ihre Einführung nach dem Kurs ihrer Sprache, gleich aufgebaut; erst danach die nächste Sprache |
| Inbetriebnahme | Kapitelweise: ein Kapitel wird ausgerollt, sobald Einführung, Übungen, Kurztest und Merkblatt geprüft und seine Bilder abgenommen sind; der Kurs zeigt nur fertige Kapitel |

Folgt aus früheren Entscheidungen:

- Antworten der Verständnisfragen, Vorhersagen und Kurztests bleiben auf dem Server (Lösungsschutz); der Browser
  bekommt nach der Antwort nur Urteil und Erklärung.
- Einführungen und Übungen werden direkt geschrieben, nicht von der lokalen KI; Themenfolge angelehnt an eine große
  Lernseite, alles neu formuliert (Entscheidung "Aufbaukurs").
- Kursstand und Erfahrung werden wie die übrige Spielmechanik aus gespeicherten Antworten und Abgaben abgeleitet.
- Bilderzeugung und Auswahl im Medienpool am Mac (der Pi liest nur), danach Export ins Repo, Commit und Ausrollen.
- Lesetext in großer Schrift (Grundschrift 17 px und mehr).

Reihenfolge des Baus:

1. Entwürfe zur Freigabe: Kursübersicht, Einführung (Abschnitt, Beispiel mit Vorhersage, Fragearten, Speicherbild,
   Ablauf, SQL-Zwischentabellen, CSS-Kästen), Kurztest, Merkblatt, Sammelkarte, Telefon (freigegeben 25.10.2026).
2. Aufzeichnung in der Sandbox (Python): je ausgeführter Zeile die Variablen, mit Grenzen für Schritte und Größe.
3. Unterbau: Format und Einlesen, Begriffskatalog mit Erkennung, Mermaid zu SVG, Prüfung beim Einlesen.
4. Kursbereich in der Oberfläche (Rechner und Telefon), Spielmechanik, Verweise aus Pfaden und Aufgaben.
5. Python-Kurs Kapitel für Kapitel; Stilprobe der Zeichnungen zur Abnahme, danach Bilder je Kapitel aus dem Medienpool;
   jedes fertige Kapitel wird ausgerollt.
6. Debugger-Oberfläche auf derselben Aufzeichnung.
7. Einführungen der übrigen Python-Themenpfade, danach SQL, JavaScript und CSS (mit HTML-Grundlagen) auf demselben
   Unterbau.

Offen für den Bau:

- Eingaben mit `input()` im Kurs: die Sandbox bekommt den Code über stdin; vorbereitete Eingaben brauchen einen
  eigenen Weg in den Lauf.
- Stilvorgabe der Zeichnungen und Farbfamilien je Sprache: entstehen mit der Stilprobe.

## Ergebnis Schritt 7, Teil 1: Aufbaukurs (0.78.0)

- Unterbau: Aufzeichnung eines Python-Laufs in der Sandbox (je Zeile der Speicher danach, mit Aufrufrahmen, Rückgabe,
  Grenzen), Aufgabentyp `programm` (ganzes Programm mit Eingaben für `input()`, Vergleich der Ausgabe), Einführungen als
  Markdown mit Blöcken (`docs/KURS-FORMAT.md`), Kurse je Sprache, Begriffskatalog Python mit Erkennung über den
  Syntaxbaum und Prüfung auf Vorgriffe, Mermaid-Diagramme als SVG (`tools/diagramme.py`), Bildaufträge an den Medienpool
  (`tools/bildschluessel.py`, vorerst nur für Karten)
- Server: Stand je Kapitel aus Ereignissen und gelösten Übungen, Antworten und Erklärungen nur nach dem Urteil,
  Ausführen erst nach der Vorhersage, Abschnitt erst nach richtigen Fragen, gesperrte Kapitel nur per Kurztest,
  Merkblatt aus der Einführung; Erfahrung je fertigem Abschnitt, Kurstage zählen zur Serie, Erfolg für Kapitel
- Oberfläche: Bereich Kurs am Rechner (Übersicht, Einführung mit Werkbank, Ablauf und Speicherbild, alle Fragearten,
  Kapitelende, Kurztest, Merkblatt) und am Telefon (Kurs, Einführung lesen, Fragen, Ausführen, Ablauf); Startseiten
  führen zum aktuellen Kapitel; Programm-Aufgaben mit Ausgabevergleich und Probelauf mit Eingaben
- Python-Kurs vollständig, Kapitel 1 bis 20 in fünf Blöcken (Erste Schritte; Entscheiden und wiederholen; Sammeln
  und ordnen mit Listen, Tupeln, Wörterbüchern und Mengen; Eigene Funktionen mit Sichtbarkeit und Fehlerbehandlung;
  Größere Programme mit Modulen, Dateien und Klassen): Einführungen mit eigenen Zeichnungen und Diagrammen, je sieben
  Übungen, Kurztest mit eigener Übung und ein Stück des Kapitelprojekts Notenbuch, das am Ende eine eigene Klasse ist;
  dazu der Block Zusatzthemen, Kapitel 21 bis 24 (Datum und Zeit, Reguläre Ausdrücke, Suchen und Sortieren, Rekursion),
  gleich aufgebaut, nur ohne Kapitelprojekt; Bestandsprüfung lässt jedes Beispiel laufen
  und vergleicht die richtige Vorhersage mit dem echten Lauf
- Erzeugte Bilder ruhen (Nutzer 25.10.2026): Stilprobe im Medienpool angelegt, acht Bilder erzeugt, Erzeugung gestoppt;
  weiter erst nach Klärung

## Ergebnis Schritt 7, Teil 2: SQL-Kurs (0.82.0)

- Unterbau: Einführungen zu SQL laufen auf einem Datensatz (`datensatz` im Kopf, Datensatz pinguinzoo); Beispiele zeigen
  das Ergebnis und je Klausel die Zwischentabelle in der Reihenfolge der Abarbeitung (FROM, JOIN, WHERE, GROUP BY,
  HAVING, SELECT, DISTINCT, ORDER BY, LIMIT), zerlegt mit dem SQL-Parser sqlglot und ausgeführt in der Sandbox;
  Begriffserkennung und Vorgriffsprüfung über denselben Parser; Vorhersagen mit eigener Frage und Vergleich der
  Zeilenzahl; Vertiefung auch aus den SQL-Aufgaben des Bestands
- SQL-Kurs Kapitel 1 bis 3 (Die erste Abfrage, Rechnen und umbenennen, Zeilen filtern mit WHERE) mit eigenen
  Zeichnungen, Diagrammen, Kurztest, je sieben Übungen und dem Kapitelprojekt Pinguinsteckbrief

## Ergebnis Schritt 7, Teil 3: SQL-Kurs fertig (0.83.0)

- SQL-Kurs Kapitel 4 bis 12 in den Blöcken Genauer filtern (Mehrere Bedingungen, Texte durchsuchen, Wenn nichts
  drinsteht), Sortieren und zusammenfassen (Sortieren und kürzen, Zusammenfassen, Gruppen bilden) und Verbinden und
  entscheiden (Tabellen verbinden, Abfragen in Abfragen, Wenn, dann, sonst); je Kapitel Zeichnung, Kurztest, sieben
  Übungen und ein Stück des Pinguinsteckbriefs bis zur fertigen Tafel; Kapitel 8 und 9 bauen deren Kopfzeile
- Ablauf: nach einem JOIN tragen gleichnamige Spalten ihre Tabelle davor (p.name, k.name), LEFT JOIN ist ein eigener
  Schritt, SELECT erklärt das Zusammenfassen zu einer Zeile oder je Gruppe
- Vorhersagen vergleichen wahlweise den Anfang des Ergebnisses (`vergleich: anfang`, etwa "Wer steht ganz oben?");
  ein Ort für alle Vergleiche (`vorhersage_stimmt`)
- Übungen ohne ORDER BY nach JOIN oder GROUP BY vergleichen ohne Reihenfolge; Ranglisten verlangen eine zweite
  Sortierspalte, damit Gleichstände (auch in den Gegenproben) eindeutig sind

## Ergebnis Schritt 7, Teil 4: SQL, Daten ändern (0.84.0)

- Block Daten ändern mit Kapitel 13 bis 16 (Zeilen einfügen, Werte ändern, Zeilen löschen, Tabellen anlegen), je
  Kapitel Zeichnung, Kurztest, sieben Übungen und ein Stück des Kapitelprojekts Umzug in den Westen
- Ablauf für Skripte: Anweisung für Anweisung (zerlegt an vollständigen Anweisungen), je Schritt die betroffene
  Tabelle davor und danach über die rowid: neue Zeilen, geänderte Zellen mit durchgestrichenem alten Wert, gelöschte
  Zeilen, neue Spalten; Fehler nennen Anweisung und Zeile, die Schritte davor bleiben sichtbar
- Aufgabenart `sql_aenderung`: das Skript läuft vollständig, eine Kontrollabfrage (Pflichtfeld `kontrolle`, in der
  Ansicht sichtbar) liefert das verglichene Ergebnis; Gegenproben auf ausgedünnten Daten wie bei Abfragen; den Aufbau
  neuer Tabellen liest die Kontrolle über pragma_table_info
- Kommazahlen erscheinen auch in den Ergebnissen der SQL-Aufgaben so, wie die Datenbank sie schreibt (4.0)

## Ergebnis Schritt 7, Teil 5: JavaScript-Kurs (0.85.0)

- JavaScript-Kurs vollständig, wie der Python-Kurs in fünf Blöcken mit 21 Kapiteln: Erste Schritte (Hallo, Konsole;
  Werte mit Namen; Rechnen; Mit Text arbeiten; Eingaben und Umwandeln), Entscheiden und wiederholen (Wahr oder falsch;
  Entscheiden; Wiederholen mit while; Zählen mit for), Sammeln und ordnen (Arrays; Arrays bearbeiten; Objekte; Map
  und Set), Eigene Funktionen (Eigene Funktionen; Pfeilfunktionen und Rückrufe; Sichtbarkeit und Closures; Fehler
  abfangen), Größere Programme (Auspacken und verteilen; Klassen; JSON; Später und gleichzeitig); Beispiele und
  Übungen laufen in Node ohne Webseite, ausgegeben wird in die Konsole
- je Kapitel eigene Zeichnung, Diagramme, Kurztest mit eigener Übung, sieben Übungen und ein Stück des
  Kapitelprojekts Fischwagen: die Kasse des Fischwagens Zum frostigen Hering wächst vom Kopf des Kassenbons über
  Eingaben, Rabatte, einen ganzen Tag, Arrays, Maps, Funktionen, Closures und robuste Eingaben bis zur Klasse mit
  Kassenbuch in JSON und einer Küche, die mit Promise.all kocht; ab Kapitel 5 versteckte Fälle mit anderen Eingaben
- Unterbau: Aufzeichnung eines JavaScript-Laufs über den Inspector von Node (ein Worker hängt sich als Debugger an
  den Hauptthread, Haltepunkte an jeder Stelle des Beispiels, je Halt die Namen aller Rahmen; Rückgabewerte,
  Fehlerzeile mit den Schritten davor, Rückrufe aus Zeitgebern und Versprechen); Programm-Aufgaben in JavaScript mit
  `prompt()` als Eingabe, je Fall ein frischer Kontext; Zeitgeber laufen in Aufzeichnung und Prüfung auf einer
  eigenen Uhr (`pruefung/zeitgeber.js`), damit die Reihenfolge nie von der Last oder den Halten des Debuggers abhängt
  und niemand echt wartet; Begriffserkennung über tree-sitter mit Knotenarten, Operatoren, Aufrufen, Methoden und
  Eigenschaften

## Schritt 7, Teil 6: CSS-Kurs mit HTML-Grundlagen (Plan)

Wie die übrigen Kurse 21 Kapitel, hier in vier Blöcken; die HTML-Grundlagen stehen vorn, so weit, dass man das
vorgegebene HTML lesen und Selektoren treffen kann (Klärung vom 25.10.2026). Grundlage für Werkbank und Bühne ist der
freigegebene Entwurf `mockups/rechner-einfuehrung-css.html`.

- Gliederung: Erste Schritte (HTML lesen und die erste Regel; Klassen und ids; Selektoren kombinieren; Kaskade und
  Vererbung; Farben), Gestalten (Text und Schrift; Das Kastenmodell; Ränder und Ecken; Einheiten; Schatten und
  Verläufe), Anordnen (display; Flexbox; Flexbox ausrichten; Grid; Grid-Bereiche; Positionieren), Feinschliff
  (Pseudoklassen; Pseudoelemente; Variablen und calc; Verwandeln; Media Queries). Kapitelprojekt: die Speisekarte des
  Fischwagens Zum frostigen Hering als Webseite, Kapitel für Kapitel schöner.
- Beispiele: zusätzlich `html` (Pflicht bei CSS), `code` ist das CSS; Vorhersagen nur als Auswahl, die richtige Option
  beschreibt das Bild. Ausführen prüft wie sonst die Vorhersage und liefert einen CSS-Lauf (Markup und CSS) ohne
  Sandbox; gerendert wird im Browser auf derselben Bühne wie bei den CSS-Aufgaben (`css/buehne.ts`).
- Werkbank CSS nach dem Entwurf: das HTML, der Editor (am Rechner), das CSS Zeile für Zeile mit einem Schalter je
  Angabe und einem Abspieler (Angabe für Angabe zuschalten), darunter die Bühne live und das Kastenmodell eines
  Elements als farbige Ringe (Inhalt, padding, border, margin) mit der Rechnung "Rand zu Rand"; gezeigt wird das erste
  Element, das unter dem Zeiger oder das angeklickte. Das Merkblatt zeigt die Beispiele mit kleiner Bühne.
- Begriffe: Erkenner über tinycss2 (Selektorarten, Pseudoklassen und -elemente, at-Regeln, Eigenschaften,
  Schlüsselwörter als eigenschaft:wert, Funktionen, Einheiten) und html.parser (Elemente, Attribute); neue Felder
  `werte`, `elemente`, `attribute` in der Erkennung. Markup erkennt der Erkenner am ersten Zeichen `<`.
- Übungen: Aufgabentyp `css_klon` wie im Bestand, Kennungen `w<Kapitel><Nummer>` (w wie Web); keine Übung, die nur mit Zeiger,
  Übergang oder Animation sichtbar wird (die Bühne ist ein Standbild).
- Bestand messen: wiederholbar in der Verwaltung im Browser (Musterlösung deckt voll, Startcode besteht nicht), mit
  derselben Messung wie die Aufgaben.

## Offen

- Entwürfe der Steuerungsspiele (Ampelschule, Aufzugsteuerung) zur Freigabe; Bau danach als eigener Abschnitt.
- Weitere Spielideen (Nutzer 25.10.2026): Turingmaschine (sehr anschaulich, mehrere Aufgaben) und digitale Schaltungen
  bis zur 7-Segment-Anzeige, Halb- und Volladdierer, Verdrahtungsaufgaben mit und ohne fertige Anordnung; Skizze in
  `docs/SPIELE.md`, vor dem Bau Entwürfe.
- Weitere Spielideen (Nutzer 25.10.2026): Codes knacken (Knacker schreiben, geprüft auf versteckten Geheimtexten) und
  Flaggenjagd (verwundbare Übungssysteme nur in der Sandbox, erst Flagge finden, dann Lücke schließen); Skizze in
  `docs/SPIELE.md`, vor dem Bau Entwürfe.
- Volle Speichergrenze der Sandbox auf dem Pi: Speicher-cgroup einschalten (`cgroup_enable=memory`, Neustart des Pi), Entscheidung des Nutzers.
- Bausteine aus eigenen Projekten: Ideenliste in `docs/CSS-IDEEN.md` vor dem Bau an den echten Bausteinen aus Orbit abgleichen (Schritt 7).
- Vorschläge aus `docs/DIDAKTIK.md`, die nicht in den Kurs übernommen sind (Tagesrätsel, Fehler gegen die Uhr,
  Wochenaufgabe "kürzer als die Musterlösung", echte eigene Daten als Datensätze): später einzeln entscheiden.
- Aufbaukurs weiter: CSS mit HTML-Grundlagen (Plan oben, im Bau); Debugger auf der Aufzeichnung; Wiederholung von Fragen; Bilder der Sammelkarten nach Klärung.
- Aufbaukurs mit Lehreinführungen: geklärt am 25.10.2026; Entwürfe liegen zur Freigabe in `mockups/` (Übersicht
  `mockups/index.html`, Abschnitt Aufbaukurs): Kursübersicht, Einführung für Python, SQL und CSS, Kurztest, Merkblatt,
  Kapitelende mit Sammelkarte, Telefon; freigegeben 25.10.2026 (der Bildbogen entfällt, Bilder kommen aus dem Medienpool).
- Spielerische Grundlagenübungen zu Flexbox und Grid (Nutzer 25.10.2026): eigene Bildwelt, je Level eine neue
  Eigenschaft, Teil der CSS-Übungen vor den Herausforderungen; Skizze in `docs/CSS-IDEEN.md`, vor dem Bau Entwürfe.
- Bildkarten für Lernfelder und Bereiche: Motive und Beschreibungen festlegen, Bilder mit Flux2 über die Leitstelle
  erzeugen und freistellen, sobald dort alles entladen ist; Entwurf der Karten vorab.
- Literaturhinweise aus den eigenen Büchern: Schalter, Quelle im Wissenspool und Anzeige vor dem Bau klären.
