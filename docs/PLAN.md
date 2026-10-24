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
| CSS-Bewertung | Nach dem Bild, nicht nach Eigenschaften: Deckung mit dem Ziel in Prozent und Kürze des Codes entscheiden; die Deckung wird grafisch gezeigt (Überblenden, eingefärbte Abweichung), das ist spannender als eine Liste (Nutzer 24.10.2026) |
| CSS-Ansicht | Beim Lösen stehen Ziel und eigenes Ergebnis untereinander in der rechten Spalte, Zoom mit dem Mausrad auf beiden zugleich, gedämpft für Trackpad und Mac-Maus (Stärke nach Scrollweite, ein Schritt je Bildschirmbild, höchstens 8 %); Ergebnis und Verlauf wandern aus der rechten Spalte in die Reiter links (Entwurf `mockups/rechner-css.html`) |
| CSS-Vielfalt | Sehr große Vielfalt an CSS-Aufgaben; Ideensammlung aus einer Recherche in `docs/CSS-IDEEN.md` (229 Ideen in 28 Kategorien, eigene Worte, keine fremden Aufgaben übernommen) |

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
3. **Aufgabenbestand**
   - Pfad-Datei als einzige Wahrheit
   - neue versteckte Tests für die 134 verratenen Aufgaben
   - Umlaute und einfache Bindestriche in Texten und Titeln (IDs bleiben ASCII)
   - Warnung beim Einlesen
4. **Oberfläche** nach den Entwürfen: feste Köpfe, Rollfelder, Telefonschale (Freigabe der Entwürfe vorher einholen).
5. **Anmeldung und Ausrollen auf den Pi**
   - Kellerwolke-Konto
   - Daten unter `/mnt/data`
   - Verwaltung nur lesend
   - Sicherung, Handbuchseite, Einrichtungsskript
6. **Spiele und Gamifizierung**: erst Entwürfe (Spiele, Spielmechanik über die ganze App, neue CSS-Bewertung nach Deckung und Kürze), nach Freigabe Bau.
7. **Neue Aufgaben** in den vier Bereichen und viele neue CSS-Nachbauten, mit automatischer Prüfung.

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

## Offen

- Freigabe der Entwürfe in `mockups/` (vor Schritt 4).
- Entwürfe der Spiele (Schritt 6).
- Port und Adresse auf dem Pi werden beim Ausrollen nach den Regeln des Unterbaus vergeben.
- Startreserve der Sandbox auf dem Pi messen (am Mac braucht Docker Desktop gerade 6 bis 13 s je Container).
- Bis zur Anmeldung (Schritt 5) ist die Verwaltung samt Musterlösungen ohne Schutz erreichbar.
