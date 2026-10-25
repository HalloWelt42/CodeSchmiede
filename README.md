# Codeschmiede

Lokaler Programmier-Trainer mit Spielelementen. Eigene Aufgaben in Markdown,
Ausführung in einer abgeschotteten Docker-Sandbox, mehrere Musterlösungen mit
Vergleich, Inhalte über didaktische Pfade geordnet. Für den Eigengebrauch.

## Stand

Rund 640 Aufgaben in Python, SQL, CSS und JavaScript, 34 Pfade.
Geprüft wird auf dem Server: Python, JavaScript und SQL laufen in der
Sandbox, CSS-Nachbauten rendert der Browser. Der weitere Ausbau steht in
[`docs/PLAN.md`](docs/PLAN.md).

## Stack

- Backend: Python 3.14, FastAPI, Pydantic, SQLite, Pakete fest nach `backend/uv.lock`
- Sandbox-Dienst: eigener Prozess, einziger Teil mit Docker-Zugang
- Frontend: Svelte 5 (Runes), TypeScript strict, Vite, CodeMirror 6
- Aufgaben: Markdown mit YAML-Frontmatter, eine Datei pro Aufgabe

## Schnellstart

### Am Mac (Entwicklung)

```bash
./scripts/setup.sh
./scripts/start.sh
```

`setup.sh` prüft Docker, uv und npm, baut die Sandbox-Images,
legt das Backend-venv an und installiert die Frontend-Pakete. `start.sh`
startet Sandbox-Dienst (8203), Backend (8200) und Frontend (5184) im
Hintergrund, `stop.sh` beendet sie.

Browser: <http://localhost:5184>.

Angemeldet wird mit dem Konto der Kellerwolke (Baustein des Appkern). Beim
ersten Start fragt die App nach Adresse und App-Schlüssel der Kellerwolke;
von einem anderen Gerät braucht die Einrichtung den Code aus
`<daten>/einrichtungscode`. Zum Entwickeln ohne Kellerwolke:
`CODESCHMIEDE_ANMELDUNG_PFLICHT=false`.

### Betrieb auf dem Pi

```bash
tools/ausrollen.sh
```

Vorne ein Vorschaltdienst mit HTTPS und HTTP/2, dahinter das Backend mit der
gebauten Oberfläche und der Sandbox-Dienst als einziger Teil mit
Docker-Zugang (`compose.pi.yml`). Ziel, Ordner und Adresse kommen aus dem
Handbuch des Verbunds; Einrichtung, Sicherung und Rückspielen stehen in
[`docs/handbuch.md`](docs/handbuch.md). Die Aufgaben sind dort nur lesbar,
bearbeitet wird am Mac.

## Tests

```bash
cd backend && .venv/bin/python -m pytest
```

Die Sandbox-Tests brauchen die gebauten Images. Die Prüfung des ganzen
Bestands (jede Musterlösung gegen ihre Tests, einige Minuten) läuft mit
`CODESCHMIEDE_BESTAND=1`.

## Hilfs-Skripte

- `scripts/build-sandbox.sh` - Sandbox-Images aller Sprachen bauen (idempotent)
- `scripts/setup.sh` - Plattform-Setup (Voraussetzungen + Pakete)
- `scripts/start.sh`, `scripts/stop.sh` - Dienste starten und beenden
- `scripts/inspect-db.sh` - Tabellen-Counts, Submissions, Tage mit Übung
- `scripts/reset-db.sh` - Datenbank löschen (Vorsicht-Modus)
- `scripts/bump.sh [patch|minor|major]` - Version anheben

## Verzeichnisse

- `backend/` - FastAPI-Server und Sandbox-Dienst
- `frontend/` - Svelte 5 + Vite
- `aufgaben/` - Aufgaben-Dateien (Markdown + Musterlösungen), Pfade, SQL-Datensätze
- `sandbox-bilder/` - Dockerfiles der Sandbox-Images je Sprache
- `mockups/` - Entwürfe der Oberfläche
- `data/` - lokale SQLite-Datenbank und Sandbox-Schlüssel (gitignored)
- `scripts/` - Setup, Versionierung, Hilfs-Tools
- `docs/` - Plan, Architektur, Aufgaben-Format

## Neue Aufgaben anlegen

Eine vollständige, autarke Spezifikation des Aufgaben-Formats steht in
[`docs/AUFGABEN-FORMAT.md`](docs/AUFGABEN-FORMAT.md). Das Dokument ist
so geschrieben, dass es als Prompt einer Sprachmodell-Instanz übergeben
werden kann; die kann daraus eigenständig neue Aufgaben erzeugen,
ohne den Quellcode der App zu kennen.

Manuell: ein Verzeichnis unter `aufgaben/<sprache>/<id>/` anlegen,
mindestens `aufgabe.md` (Markdown mit YAML-Frontmatter) und eine
Musterlösung `solution_<variante>.<endung>`. Das Backend liest neue und
geänderte Aufgaben sofort ein; Fehler stehen in der Verwaltung unter den
Befunden.

## Lizenz

**Nicht-kommerzielle Nutzung** -- Siehe [LICENSE](LICENSE)

Erlaubt: Private Nutzung, Installation, persönliche Anpassungen,
Teilen mit Quellenangabe

Verboten: Kommerzielle Nutzung, Verkauf, Einbindung in kommerzielle
Produkte

---

## Unterstützen

Codeschmiede ist ein privates Open-Source-Projekt. Kein Tracking,
keine Werbung, keine Kompromisse.

Wenn dir das Projekt gefällt, kannst du direkt hier "Danke sagen":

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/HalloWelt42)

**Crypto:**

| Coin | Adresse |
|------|---------|
| BTC  | `bc1qnd599khdkv3v3npmj9ufxzf6h4fzanny2acwqr` |
| DOGE | `DL7tuiYCqm3xQjMDXChdxeQxqUGMACn1ZV` |
| ETH  | `0x8A28fc47bFFFA03C8f685fa0836E2dBe1CA14F27` |

Copyright (c) 2025-2026 HalloWelt42
