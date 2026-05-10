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

```bash
# Sandbox-Image bauen (einmalig)
./scripts/build-sandbox.sh

# Backend starten
cd backend && uv pip install -e . && python -m codeschmiede.main

# Frontend starten (in zweitem Terminal)
cd frontend && npm install && npm run dev
```

Browser auf `http://localhost:5173`.

## Verzeichnisse

- `backend/` -- FastAPI-Server
- `frontend/` -- Svelte 5 + Vite
- `aufgaben/` -- Aufgaben-Dateien (Markdown + Musterlösungen) und
  Pfad-Definitionen
- `aufgaben/sandbox/` -- Dockerfile für die Python-Sandbox
- `data/` -- lokale SQLite-Datenbank (gitignored)
- `scripts/` -- Setup, Versionierung, Hilfs-Tools
- `docs/` -- Aufgaben-Format-Dokumentation, Architektur-Notizen

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
