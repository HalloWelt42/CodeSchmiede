# Codeschmiede

Lokaler, gamifizierter Programmier-Trainer. Eigene Aufgaben in Markdown,
sichere Sandbox-Ausführung in Docker, mehrere Musterlösungen mit
Performance-Vergleich. Inhalte über didaktische Pfade strukturiert.

Vorbild im Stil: Codewars, Codecademy, LeetCode, HackerRank, CodinGame --
aber tutorialmäßig und für den Eigengebrauch.

## Stand

Frühe Phase. Repo-Skelett, Sandbox-Image für Python, drei Beispielaufgaben
(FizzBuzz, Palindrom, Fibonacci). Backend und Frontend in Aufbau.

## Sprachen im MVP

- **Python 3.11+** (Sandbox läuft im Docker-Container)

Geplant nach MVP: JavaScript (Web-Worker), HTML/CSS (sandboxed iframe),
SQL (In-Memory-SQLite).

## Stack

- Backend: Python 3.11+, FastAPI, Pydantic, SQLite
- Frontend: Svelte 5 (Runes), TypeScript strict, Vite, CodeMirror 6
- Sandbox: Docker (`python:3.11-slim`, isoliert ohne Netz)
- Aufgaben: Markdown mit YAML-Frontmatter, eine Datei pro Aufgabe

## Schnellstart

### Variante 1 -- Native (Mac, Linux, Pi)

```bash
./scripts/setup.sh
```

Das Skript prüft Docker, Python 3.11 und npm, baut das Sandbox-Image,
legt das Backend-venv an und installiert die Frontend-Pakete.

Danach in zwei Terminals:

```bash
# Backend
cd backend && .venv/bin/python -m codeschmiede.main

# Frontend
cd frontend && npm run dev
```

Browser: <http://localhost:5184>.

### Variante 2 -- Docker Compose (für Pi-Deploys)

```bash
./scripts/build-sandbox.sh    # einmalig: Sandbox-Image bauen
docker compose up -d
```

Browser: <http://localhost:8201>. Backend liegt auf 8200.

## Hilfs-Skripte

- `scripts/build-sandbox.sh` -- Sandbox-Image bauen (idempotent)
- `scripts/setup.sh` -- Plattform-Setup (Voraussetzungen + Pakete)
- `scripts/inspect-db.sh` -- Tabellen-Counts, Submissions, Streak
- `scripts/reset-db.sh` -- Datenbank löschen (Vorsicht-Modus)
- `scripts/bump.sh [patch|minor|major]` -- Version anheben

## Verzeichnisse

- `backend/` -- FastAPI-Server
- `frontend/` -- Svelte 5 + Vite
- `aufgaben/` -- Aufgaben-Dateien (Markdown + Musterlösungen) und
  Pfad-Definitionen
- `aufgaben/sandbox/` -- Dockerfile für die Python-Sandbox
- `data/` -- lokale SQLite-Datenbank (gitignored)
- `scripts/` -- Setup, Versionierung, Hilfs-Tools
- `docs/` -- Aufgaben-Format-Dokumentation, Architektur-Notizen

## Neue Aufgaben anlegen

Eine vollständige, autarke Spezifikation des Aufgaben-Formats steht in
[`docs/AUFGABEN-FORMAT.md`](docs/AUFGABEN-FORMAT.md). Das Dokument ist
so geschrieben, dass es als Prompt einer Sprachmodell-Instanz übergeben
werden kann -- die kann daraus eigenständig neue Aufgaben generieren,
ohne den Quellcode der App zu kennen.

Manuell: ein Verzeichnis unter `aufgaben/<sprache>/NNN-id/` anlegen,
mindestens `aufgabe.md` (Markdown mit YAML-Frontmatter),
`solution_naive.py` und `solution_idiomatic.py`. Beim nächsten
Backend-Start wird die Aufgabe automatisch indiziert.

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
