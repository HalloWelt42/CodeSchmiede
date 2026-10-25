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
| Aufbaukurs | Ein idiotensicherer Aufbaukurs von null an, in kleinsten Schritten mit einer neuen Sache je Aufgabe, als eigener zweiter Lauf in Schritt 7 (Nutzer 25.10.2026). Bisher gibt es nur Themenpfade (Python-Grundlagen hat 3 Aufgaben). Ideen und Reihenfolge der Themen kommen von einer großen bekannten Lernseite für Webtechnik und Programmierung; übernommen wird nur, was sinnvoll ist, und alles wird neu geschrieben: eigene Erklärungen, eigene Beispiele, eigene Werte und Namen, kein Text und kein Beispielcode im Wortlaut. Kursform und Umfang vor dem Bau klären |
| Lehreinführungen | Zu jedem Thema ein richtiger, vollständiger Einführungskurs mit sinnvoller Logik, durch den man sich durcharbeitet; erst danach folgt das Üben mit den Aufgaben. Die Einführungen sind absolut vollständig und anschaulich (Nutzer 25.10.2026). Gehört zum Aufbaukurs (Schritt 7); Form, Gliederung je Thema und Anschauungsmittel vor dem Bau klären |
| Editor | Hervorhebung im klassischen dunklen Farbschema einer bekannten Entwicklungsumgebung (die ältere Fassung); Vervollständigung nur für einzelne Befehle, keine mehrzeiligen Bausteine; Syntaxfehler sofort beim Tippen sichtbar (Nutzer 25.10.2026). Gebaut direkt nach Schritt 6, vor dem Ausrollen |
| Debugger | Haltepunkte im Editor und ein Ausgabemodus wie bei einem echten Debugger, aber nur auf Ebene des eigenen Codes, kein Tiefendebugger; alle Speicherzustände Schritt für Schritt lesbar (Nutzer 25.10.2026). Umsetzung als Aufzeichnung: die Sandbox schreibt je ausgeführter Zeile des eigenen Codes die Variablen mit (Python über die Ablaufverfolgung, mit Grenze für Schritte und Größe), die Oberfläche spult vor und zurück, springt zum nächsten Haltepunkt, markiert die Zeile und zeigt den Speicher. Python zuerst, JavaScript danach; nur am Rechner, das Telefon muss nicht alles können (Nutzer 25.10.2026); Entwurf vorab |
| Bildkarten | Lernfelder und Bereiche bekommen anschauliche Karten mit Bild und Beschreibung; freigestellte Bilder begleiten die Software. Erzeugt später lokal mit Flux2 über die Leitstelle, nur wenn dort alles entladen ist und Platz ist. Farblich dürfen die Inhalte (Bilder, Karten, Spielflächen) vom Mintgrün abweichen, damit sie in sich harmonisch sind (Nutzer 25.10.2026) |
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
6. **Spiele und Gamifizierung**: erst Entwürfe (Spiele, Spielmechanik über die ganze App, neue CSS-Bewertung nach Deckung und Kürze), nach Freigabe Bau.
7. **Neue Aufgaben** in den vier Bereichen und viele neue CSS-Nachbauten, mit automatischer Prüfung.
   - zweiter, eigener Lauf: Aufbaukurs von null an (siehe Entscheidung "Aufbaukurs")

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
- Aufbaukurs mit Lehreinführungen: Kursform (Pfad mit Lerneinheiten oder eigener Bereich), Sprachen, Gliederung je
  Thema, Anschauungsmittel und Umfang vor dem Bau klären, Entwürfe zuerst (Schritt 7).
- Spielerische Grundlagenübungen zu Flexbox und Grid (Nutzer 25.10.2026): eigene Bildwelt, je Level eine neue
  Eigenschaft, Teil der CSS-Übungen vor den Herausforderungen; Skizze in `docs/CSS-IDEEN.md`, vor dem Bau Entwürfe.
- CSS-Bestand automatisch messen: die Prüfung beim Bau (Musterlösung deckt voll, Startcode besteht nicht) lief
  einmalig im Browser; als wiederholbare Prüfung (etwa in der Verwaltung) einrichten, bevor neue CSS-Aufgaben kommen.
- Bildkarten für Lernfelder und Bereiche: Motive und Beschreibungen festlegen, Bilder mit Flux2 über die Leitstelle
  erzeugen und freistellen, sobald dort alles entladen ist; Entwurf der Karten vorab.
- Literaturhinweise aus den eigenen Büchern: Schalter, Quelle im Wissenspool und Anzeige vor dem Bau klären.
