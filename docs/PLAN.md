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
| Erstellung | Lokale KI (80B) entwirft nach `docs/AUFGABEN-FORMAT.md`; jede Aufgabe wird automatisch geprüft (Musterlösung besteht, falsche Lösung scheitert, kein versteckter Test im Text, Umlaute korrekt) |
| Abhängigkeiten | Alles auf neu (Sicherheitsstand und große Sprünge), Docker-Image installiert fest nach Sperrdatei |
| Aufgabendateien auf dem Pi | Repo ist die Wahrheit; Pi nur lesend, Bearbeiten in der Verwaltung nur am Mac, danach Commit und Ausrollen |
| Repo | Vorhandenes öffentliches Repo `HalloWelt42/CodeSchmiede` |
| PHP-Lücke (CVE-2026-109618/-109619, -115560) | Betrifft die Codeschmiede nicht (kein PHP) |

## Reihenfolge des Baus

Jeder Schritt einzeln committet und gepusht.

1. **Sicherheit und Fehler**
   - Sandbox-Dienst mit gehärteten Containern: `--cap-drop=ALL`, `no-new-privileges`, `--user`, `--memory-swap`, begrenzte Ausgabe, Container per Name beenden bei Zeitüberschreitung
   - SQL-Prüfung mit Zeitabbruch und ohne `ATTACH`
   - CORS fest auf die eigene Herkunft, Mermaid nicht mehr `loose`
   - Kennungsmuster für CSS- und SQL-IDs
   - kaputte Verweise mit Umlaut-IDs, Reindex robust je Datei
   - Probelauf-Rückgabe, Typfehler, toter Code
   - doppelte Logik zusammenführen, Migrationen atomar
   - Backend-Tests aufbauen
2. **Abhängigkeiten** auf den neuesten Stand, Image nach Sperrdatei.
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
6. **Spiele**: erst Entwürfe, nach Freigabe Bau der vier Spiele.
7. **Neue Aufgaben** in den vier Bereichen mit automatischer Prüfung.

## Offen

- Freigabe der Entwürfe in `mockups/` (vor Schritt 4).
- Entwürfe der Spiele (Schritt 6).
- Port und Adresse auf dem Pi werden beim Ausrollen nach den Regeln des Unterbaus vergeben.
